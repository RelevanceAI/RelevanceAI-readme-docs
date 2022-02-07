#!/usr/bin/env python3

from typing import Dict
import os
from pathlib import Path
import re
import subprocess
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

from utils import multiprocess

import logging
import argparse


###############################################################################
# Helper Functions
###############################################################################

README_NOTEBOOK_ERROR_FPATH = "readme_notebook_errors.txt"

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


def notebook_find_replace(fname: str, find_sent_regex: str, find_str_regex: str, replace_str: str):
    with open(fname, "r") as f:
        lines = f.readlines()

    with open(fname, "w") as f:
        for i, line in enumerate(lines):
            if bool(re.search(find_sent_regex, line)):
                find_sent = re.search(find_sent_regex, line)
                if find_sent:
                    find_sent = find_sent.group()
                    logging.debug(f"Found sentence: {find_sent}")

                    # if find_str == replace_str: continue
                    logging.debug(f"Find string regex: {find_str_regex}")
                    find_replace_str = re.search(find_str_regex, find_sent)
                    if find_replace_str:
                        find_replace_str = find_replace_str.group()
                        logging.debug(f"Found str within sentence: {find_replace_str.strip()}")

                        logging.debug(f"Replace str: {replace_str}")
                        line = line.replace(find_replace_str, replace_str)

                        logging.debug(f"Updated: {line.strip()}")
                    else:
                        logging.debug(f"Not found: {find_replace_str}")
                else:
                    logging.debug(f"Not found: {find_sent_regex}")

            f.write(line)


###############################################################################
# Update SDK version and test
###############################################################################


def execute_notebook(notebook:str, notebook_args: Dict):
    try:
        print(notebook)

        # to support the multiprocessing function
        if isinstance(notebook, list):
            notebook = notebook[0]

        # print(notebook_args['pip_install_args'])
        ## Update to latest version
        notebook_find_replace(
            notebook,
            **notebook_args['pip_install_args']
        )

        # print(notebook_args['client_instantiation_args'])
        ## Temporarily updating notebook with test creds
        notebook_find_replace(
            notebook,
            **notebook_args['client_instantiation_args']
        )

        ## Execute notebook with test creds
        with open(notebook, "r") as f:
            print(
                f"\nExecuting notebook: \n{notebook} with SDK version {notebook_args['relevanceai_sdk_version']}"
            )
            nb_in = nbformat.read(f, nbformat.NO_CONVERT)
            ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
            nb_out = ep.preprocess(nb_in)

        # print(notebook_args['client_base_args'])
        ## Replace creds with previous
        notebook_find_replace(
            notebook,
            **notebook_args['client_instantiation_base_args']
        )
        return
    except Exception as e:

        notebook_find_replace(
            notebook,
            **notebook_args['client_instantiation_base_args']
        )

        import traceback

        exception_reason = traceback.format_exc()
        print(
            f"{notebook}\n{exception_reason}\n\n",
            file=open(README_NOTEBOOK_ERROR_FPATH, "a"),
        )

        return {"notebook": notebook.__str__(), "Exception reason": exception_reason}



###############################################################################
# Main
###############################################################################


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

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
    pip_install_args={
        'find_sent_regex': PIP_INSTALL_SENT_REGEX,
        'find_str_regex': PIP_INSTALL_STR_REGEX,
        'replace_str': PIP_INSTALL_STR_REPLACE,
    }

    ## Env vars
    CLIENT_INSTANTIATION_SENT_REGEX = '"client.*Client(.*)"'
    # TEST_PROJECT = os.environ["TEST_PROJECT"]
    # TEST_API_KEY = os.environ["TEST_API_KEY"]
    TEST_ACTIVATION_TOKEN = os.environ["TEST_ACTIVATION_TOKEN"]
    CLIENT_INSTANTIATION_STR_REGEX = "\((.*?)\)"
    # CLIENT_INSTANTIATION_STR_REPLACE = (
    #     f'(project=\\"{TEST_PROJECT}\\", api_key=\\"{TEST_API_KEY}\\")'
    # )
    CLIENT_INSTANTIATION_STR_REPLACE = (
        f'(token=\\"{TEST_ACTIVATION_TOKEN}\\")'
    )
    CLIENT_INSTANTIATION_BASE = f'"client = Client()"'
    client_instantiation_args={
        'find_sent_regex': CLIENT_INSTANTIATION_SENT_REGEX,
        'find_str_regex': CLIENT_INSTANTIATION_STR_REGEX,
        'replace_str': CLIENT_INSTANTIATION_STR_REPLACE,
    }

    client_instantiation_base_args={
        'find_sent_regex': CLIENT_INSTANTIATION_SENT_REGEX,
        'find_str_regex': CLIENT_INSTANTIATION_SENT_REGEX,
        'replace_str': CLIENT_INSTANTIATION_BASE,
    }

    if args.notebooks:
        notebooks = args.notebooks
    else:
        ## All notebooks
        notebooks = [
            x[0] if isinstance(x, list) else x for x in list(Path(DOCS_PATH).glob("**/*.ipynb"))
        ]

    static_args= {
        'relevanceai_sdk_version': RELEVANCEAI_SDK_VERSION,
        'pip_install_args': pip_install_args,
        'client_instantiation_args': client_instantiation_args,
        'client_instantiation_base_args': client_instantiation_base_args,
    }

    with open(README_NOTEBOOK_ERROR_FPATH, "w") as f:
        f.write("")

    # results = multiprocess(func=execute_notebook,
    #                         iterables=notebooks,
    #                         static_args=static_args,
    #                         chunksize=1
    #                     )
    execute_notebook(notebooks[0], static_args)
    # # results = [execute_notebook(n) for n in ALL_NOTEBOOKS]
    # results = [r for r in results if r is  not None]
    # if len(results) > 0:
    #     for r in results:
    #         print(r.get("notebook"))
    #         print(r.get("Exception reason"))
    #     # raise ValueError(f"You have errored notebooks {results}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = 'RelevanceAI'
    ROOT_PATH = Path(__file__).parent.resolve() / '..'

    try:
        README_VERSION = open(ROOT_PATH/ '__version__').read()
    except FileNotFoundError as e:
        print(f'File not found: {e}')
        print(f'Loading file from latest Pip package release')

    parser.add_argument("-d", "--debug", default=False, help="Run debug mode")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument("-pn", "--package-name", default=PACKAGE_NAME, help="Package Name")
    parser.add_argument("-v", "--version", default=README_VERSION, help="Package Version")
    parser.add_argument("-n", "--notebooks", nargs="+", default=None, help="List of notebooks to execute")
    args = parser.parse_args()

    main(args)
