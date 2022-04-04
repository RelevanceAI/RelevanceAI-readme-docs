#!/usr/bin/env python3

import logging
from typing import Dict, List, Literal, Union
from pathlib import Path
import requests
import os
import re
import json
import argparse
from pprint import pprint
import traceback

import frontmatter

import nbformat
from traitlets.config import Config
from nbconvert import MarkdownExporter

from traitlets import Integer
from nbconvert.preprocessors import Preprocessor

from rdme_sync.build.build_snippets import generate_snippet
from rdme_sync.build.constants import RDMD_SNIPPET_LANGUAGES

from rdme_sync.readme.nbconvert_rdmd_preprocessor import RdmdSnippetPreprocessor
from rdme_sync.readme.nbconvert_rdmd_exporter import RdmdExporter


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    README_VERSION = args.version

    c = Config()
    if args.format == "block":
        c.snippet_format = "block"
        rdmd_template = "rdmd_block.md.j2"
    elif args.format == "rdmd":
        c.snippet_format = "rdmd"
        rdmd_template = "rdmd.md.j2"

    c.Exporter.template_file = os.path.join(
        os.path.dirname(__file__), "templates", "rdmd", rdmd_template
    )
    c.RdmdExporter.preprocessors = [RdmdSnippetPreprocessor]

    # rdmd_exporter = MarkdownExporter(config=c)
    rdmd_exporter = RdmdExporter(config=c)

    NOTEBOOK_PATHS = Path(DOCS_TEMPLATE_PATH).glob("**/**/*.ipynb")
    ## Filter checkpoints
    NOTEBOOK_GENERATE_PATHS = [
        n
        for n in NOTEBOOK_PATHS
        if ".ipynb_checkpoints" not in str(n) and "_notebooks" != n.parent.name
    ]
    logging.info(f"Converting: {NOTEBOOK_GENERATE_PATHS}")

    for notebook_fpath in NOTEBOOK_GENERATE_PATHS:
        logging.debug(f"Converting: {notebook_fpath}")
        notebook = nbformat.read(Path(notebook_fpath), as_version=4)
        rdmd = rdmd_exporter.from_notebook_node(notebook)[0]
        rdmd_print = "\n".join(
            [f for f in rdmd.split("\n") if "data:image/png;base64," not in f]
        )

        # rdmd_frontmatter = frontmatter.load(rdmd_print)
        logging.debug(rdmd_print)
        print(c.snippet_format)

        output_fname = Path(
            str(notebook_fpath)
            .replace("docs_template", "docs")
            .replace(".ipynb", ".md")
        )
        with open(output_fname, "w") as fout:
            # for element in md_lines:
            fout.write(rdmd)
            logging.info(f"\tOutput file: {output_fname}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"
    ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".." / ".."
    README_VERSION_FILE = f"v{open(ROOT_PATH / '__version__').read().strip()}"

    parser.add_argument("-d", "--debug", help="Run debug mode", action="store_true")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument(
        "-f",
        "--format",
        default="block",
        choices=["rdmd", "block"],
        help="Conversion format",
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
