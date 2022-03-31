#!/usr/bin/env python3

import logging
from typing import Dict, List, Union
from pathlib import Path
import requests
import os
import json
import argparse
from pprint import pprint

import nbformat
from traitlets.config import Config
from nbconvert import MarkdownExporter

from traitlets import Integer
from nbconvert.preprocessors import Preprocessor


class RdmdPreprocessor(Preprocessor):
    """ReadMe Markdown preprocessor"""

    start = Integer(0, help="first cell of notebook to be converted").tag(config=True)
    end = Integer(-1, help="last cell of notebook to be converted").tag(config=True)

    def preprocess(self, nb, resources):
        self.log.info("I'll keep only cells from %d to %d", self.start, self.end)
        nb.cells = nb.cells[self.start : self.end]

        for cell in nb.cells:
            if cell["cell_type"] == "code":
                print(cell["source"])
        # print(nb.cells)
        # print(resources)

        return nb, resources


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    EXPORT_MD_PATH = Path(args.path) / "export_md" / args.version
    README_VERSION = args.version
    README_CONFIG_FPATH = ROOT_PATH / "config" / "readme-config.yaml"
    DOCS_CONDENSED_CONFIG_FPATH = ROOT_PATH / "config" / "docs-config-condensed.yaml"
    DOCS_CONFIG_FPATH = ROOT_PATH / "config" / "docs-config.yaml"

    c = Config()
    c.MarkdownExporter.preprocessors = [RdmdPreprocessor]

    # Create our new, customized exporter that uses our custom preprocessor
    rdmd = MarkdownExporter(config=c)
    NOTEBOOK_PATHS = Path(DOCS_TEMPLATE_PATH).glob("**/**/*.ipynb")
    ## Filter checkpoints
    NOTEBOOK_GENERATE_PATHS = [
        n
        for n in NOTEBOOK_PATHS
        if ".ipynb_checkpoints" not in str(n) and "_notebooks_convert" in str(n)
    ]

    for notebook_fpath in NOTEBOOK_GENERATE_PATHS:
        print(notebook_fpath)
        notebook = nbformat.read(Path(notebook_fpath), as_version=4)
        # pprint(notebook)
        rdmd.from_notebook_node(notebook)[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"
    ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".."
    README_VERSION_FILE = f"v{open(ROOT_PATH / '__version__').read().strip()}"

    parser.add_argument("-d", "--debug", help="Run debug mode", action="store_true")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument(
        "-m",
        "--method",
        default="build",
        choices=["build"],
        help="Method",
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
