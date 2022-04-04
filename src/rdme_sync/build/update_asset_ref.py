#!/usr/bin/env python3

import json
from pathlib import Path
import itertools
from typing import List, Tuple, Union
from typing_extensions import Literal
import logging
import argparse

from rdme_sync.utils.files import get_files, file_find_replace, notebook_find_replace


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    README_VERSION = args.version

    ###############################################################################
    # Updating asset links
    ###############################################################################

    logging.info(f"Updating asset links to {README_VERSION} for all md and ipynb files")

    md_files = itertools.chain(
        get_files(DOCS_PATH, ext="md"), get_files(DOCS_TEMPLATE_PATH, ext="md")
    )
    notebooks = itertools.chain(
        get_files(DOCS_PATH, ext="ipynb"), get_files(DOCS_TEMPLATE_PATH, ext="ipynb")
    )
    # files = itertools.chain(md_files, notebooks)

    ASSET_SENTENCE_REGEX = ".*/RelevanceAI-readme-docs/blob/.*"
    ASSET_STR_REGEX = "/RelevanceAI-readme-docs/blob/.*?/"
    ASSET_REPLACE_STR = f"/RelevanceAI-readme-docs/blob/{README_VERSION}/"

    for f in md_files:
        logging.debug(f"\tUpdating assets links for {f} to {README_VERSION}")
        file_find_replace(f, ASSET_SENTENCE_REGEX, ASSET_STR_REGEX, ASSET_REPLACE_STR)

    for f in notebooks:
        logging.debug(f"\tUpdating assets links for {f} to {README_VERSION}")
        notebook_find_replace(
            f, ASSET_SENTENCE_REGEX, ASSET_STR_REGEX, ASSET_REPLACE_STR
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"

    ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".." / ".."
    README_VERSION_FILE = f"v{open(ROOT_PATH / '__version__').read().strip()}"

    parser.add_argument("-d", "--debug", help="Run debug mode", action="store_true")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument(
        "-pn", "--package-name", default=PACKAGE_NAME, help="Package Name"
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
