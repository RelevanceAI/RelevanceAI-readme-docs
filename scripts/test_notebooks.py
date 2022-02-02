#!/usr/bin/env python3

import os
from pathlib import Path
import re
import subprocess
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

import logging
import argparse


###############################################################################
# Helper Functions
###############################################################################


def get_latest_version(name: str):
    latest_version = str(
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "{}==random".format(name)],
            capture_output=True,
            text=True,
        )
    )
    latest_version = latest_version[latest_version.find("(from versions:") + 15 :]
    latest_version = latest_version[: latest_version.find(")")]
    latest_version = latest_version.replace(" ", "").split(",")[-1]
    return latest_version


def check_latest_version(name: str):
    latest_version = get_latest_version(name)

    current_version = str(
        subprocess.run(
            [sys.executable, "-m", "pip", "show", "{}".format(name)],
            capture_output=True,
            text=True,
        )
    )
    current_version = current_version[current_version.find("Version:") + 8 :]
    current_version = current_version[: current_version.find("\\n")].replace(" ", "")

    if latest_version == current_version:
        return True
    else:
        return False


def notebook_find_replace(notebook: str, find_sent_regex: str, find_str_regex: str, replace_str: str):

    with open(notebook, "r") as f:
        lines = f.readlines()

    with open(notebook, "w") as f:
        for i, line in enumerate(lines):
            if bool(re.search(find_sent_regex, line)):
                find_sent = re.search(find_sent_regex, line)
                if find_sent:
                    find_sent = find_sent.group()
                    print(f"\nFound: {find_sent}\n")

                    # if find_str == replace_str: continue
                    print(f"Find string: {find_str_regex}")
                    find_replace_str = re.search(find_str_regex, find_sent)
                    if find_replace_str:
                        find_replace_str = find_replace_str.group()
                        print(f"Found: {find_replace_str}\n")

                        print(f"Replace: \n{find_replace_str}\n{replace_str}\n")
                        line = line.replace(find_replace_str, replace_str)

                        print(f"Updated:")
                        print(line.strip())
                    else:
                        print(f"Not found: {find_replace_str}\n")
                else:
                    print(f"Not found: {find_sent_regex}\n")

            f.write(line)

###############################################################################
# Update SDK version and test
###############################################################################



def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    RELEVANCEAI_SDK_VERSION = (
        args.version if args.version else get_latest_version(args.package_name)
    )
    logging.info(
        f"Executing notebook test with {args.package_name}=={RELEVANCEAI_SDK_VERSION}\n\n"
    )

    PIP_INSTALL_SENT_REGEX = f'".*pip install .* {args.package_name}.*==.*"'
    PIP_INSTALL_STR_REGEX = f"==.*[0-9]"
    PIP_INSTALL_STR_REPLACE = f"=={RELEVANCEAI_SDK_VERSION}"

    ## Env vars
    CLIENT_INSTANTIATION_SENT_REGEX = '"client.*Client(.*)"'
    TEST_PROJECT = os.getenv("TEST_PROJECT")
    TEST_API_KEY = os.getenv("TEST_API_KEY")
    CLIENT_INSTANTIATION_STR_REGEX = "\((.*?)\)"
    CLIENT_INSTANTIATION_STR_REPLACE = (
        f'(project=\\"{TEST_PROJECT}\\", api_key=\\"{TEST_API_KEY}\\")'
    )

    CLIENT_INSTANTIATION_BASE = f'"client = Client()"'

    README_NOTEBOOK_ERROR_FPATH = "readme_notebook_errors.txt"
    with open(README_NOTEBOOK_ERROR_FPATH, "w") as f:
        f.write("")

    for notebook in Path(DOCS_PATH).glob("**/*.ipynb"):
        try:
            logging.info( {notebook})
            logging.info(f'Updating pip install to latest version {RELEVANCEAI_SDK_VERSION} ...')
            notebook_find_replace(
                notebook,
                PIP_INSTALL_SENT_REGEX,
                PIP_INSTALL_STR_REGEX,
                PIP_INSTALL_STR_REPLACE,
            )

            logging.info(f'Temporarily updating notebook with test creds ...')
            notebook_find_replace(
                notebook,
                CLIENT_INSTANTIATION_SENT_REGEX,
                CLIENT_INSTANTIATION_STR_REGEX,
                CLIENT_INSTANTIATION_STR_REPLACE,
            )

            ## Execute notebook with test creds
            with open(notebook, "r") as f:
                logging.info(
                    f"Executing notebook: {notebook} with SDK version {RELEVANCEAI_SDK_VERSION}"
                )
                nb_in = nbformat.read(f, nbformat.NO_CONVERT)
                ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
                nb_out = ep.preprocess(nb_in)

            logging.info(f'Replacing client with base auth ...')
            notebook_find_replace(
                notebook,
                CLIENT_INSTANTIATION_SENT_REGEX,
                CLIENT_INSTANTIATION_SENT_REGEX,
                CLIENT_INSTANTIATION_BASE,
            )
        except Exception as e:
            ERROR_MESSAGE = f"Error in notebook: {notebook}\n{e}"

            logging.error(ERROR_MESSAGE)
            print(
                ERROR_MESSAGE,
                file=open(README_NOTEBOOK_ERROR_FPATH, "a"),
            )

            pass



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    PACKAGE_NAME = 'RelevanceAI'
    ROOT_PATH = Path(__file__).parent.resolve() / '..'
   
    try:
        README_VERSION = open(ROOT_PATH/ '__version__').read()
    except FileNotFoundError as e:
        print(f'File not found: {e}')
        print(f'Loading file from latest Pip package release')

    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument("-n", "--package-name", default=PACKAGE_NAME, help="Package Name")
    parser.add_argument("-v", "--version", default=README_VERSION, help="Package Version")
    args = parser.parse_args()

    main(args)
