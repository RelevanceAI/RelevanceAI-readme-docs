
#!/usr/bin/env python3

import os
import re
from pathlib import Path
import itertools
from typing import List, Tuple, Union
import logging
import argparse
import json


def file_find_replace(fname: str, find_sent_regex: str, find_str_regex: str, replace_str: str):
    if fname.is_file():
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



def get_files(path: Union[Path, str], ext: Union['md', 'ipynb']):
	return Path(path).glob(f"**/*.{ext}")



def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    #logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    README_VERSION = args.version

    ###############################################################################
    # Updating semver ref in installation
    ###############################################################################

    logging.info(f'Updating semver ref to {README_VERSION} for all installation files')

    SEMVER_SENT = f'.*v(\d+\.\d+(?:\.\d+)?).*'
    SEMVER_STR = f"v(\d+\.\d+(?:\.\d+)?)"
    SEMVER_REPLACE_STR = f"v{README_VERSION}"

    installation_guide =  [Path(args.path) / "docs_template" / "GETTING_STARTED" / "installation.md"] + \
                            [Path(args.path) / "docs" / "GETTING_STARTED" / "installation.md"]

    for f in installation_guide:
        logging.debug(f'\tUpdating {f} to {README_VERSION}')
        file_find_replace(f, SEMVER_SENT, SEMVER_STR, SEMVER_REPLACE_STR)


    ###############################################################################
    # Updating version ref in snippet config
    ###############################################################################

    logging.info(f'Updating version ref to {README_VERSION} in snippet config')
    SNIPPET_PARAMS_FPATH = Path(DOCS_TEMPLATE_PATH) / "_snippet_params.json"
    SNIPPET_PARAMS = json.loads(open(str(SNIPPET_PARAMS_FPATH), 'r').read())

    SNIPPET_PARAMS['RELEVANCEAI_SDK_VERSION'] = args.version
    json.dump(SNIPPET_PARAMS, open(SNIPPET_PARAMS_FPATH, 'w'), separators=(',\n', ': '))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = 'RelevanceAI'

    ROOT_PATH = Path(__file__).parent.resolve() / '..'
    README_VERSION_FILE = open(ROOT_PATH / '__version__').read()

    parser.add_argument("-d", "--debug", help="Run debug mode", action='store_true')
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument("-pn", "--package-name", default=PACKAGE_NAME, help="Package Name")
    parser.add_argument("-v", "--version", default=README_VERSION_FILE, help="Package Version")
    args = parser.parse_args()

    main(args)
