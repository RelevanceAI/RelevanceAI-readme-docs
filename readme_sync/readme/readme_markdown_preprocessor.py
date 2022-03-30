#!/usr/bin/env python3

from typing import Dict, List, Union
from pathlib import Path
import requests
import os
import json
import argparse

import nbformat
from traitlets.config import Config
from nbconvert import MarkdownExporter

from traitlets import Integer
from nbconvert.preprocessors import Preprocessor


class ReadMeMarkdown(Preprocessor):
    """ReadMe Markdown preprocessor"""

    start = Integer(0, help="first cell of notebook to be converted").tag(config=True)
    end = Integer(-1, help="last cell of notebook to be converted").tag(config=True)

    def preprocess(self, nb, resources):
        self.log.info("I'll keep only cells from %d to %d", self.start, self.end)
        nb.cells = nb.cells[self.start : self.end]

        print(nb.cells)

        return nb, resources


def main():
    c = Config()

    c.MarkdownExporter.preprocessors = [ReadMeMarkdown]

    # Create our new, customized exporter that uses our custom preprocessor
    rdmd = MarkdownExporter(config=c)
    #     return '.ipynb'

    notebook = nbformat.read(Path("notebook.ipynb"), as_version=4)
    print(rdmd.from_notebook_node(jake_notebook)[0])


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
        default="update",
        choices=["build", "update", "import_md"],
        help="Method",
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
