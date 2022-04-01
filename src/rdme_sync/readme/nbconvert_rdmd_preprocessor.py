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


class RdmdSnippetPreprocessor(Preprocessor):
    """ReadMe Markdown Snippet preprocessor"""

    start = Integer(0, help="first cell of notebook to be converted").tag(config=True)
    end = Integer(-1, help="last cell of notebook to be converted").tag(config=True)
    snippet_format: Literal["rdmd", "block"] = "block"

    def preprocess(self, nb, resources):
        # nb.cells = nb.cells[self.start : self.end]
        language = "python"
        for cell in nb.cells:
            if cell["cell_type"] == "code":
                snippet = cell["source"]
                logging.debug(f"Before: {snippet}")
                if self.snippet_format == "rdmd":
                    snippet[0] = f"```{language} {RDMD_SNIPPET_LANGUAGES[language]}"
                    snippet.append("```")
                    snippet.append("```" + language)
                    snippet.append("```")

                ### ReadMe Block Format
                elif self.snippet_format == "block":
                    snippet_block = ["[block:code]"]
                    snippet_code = {}
                    snippet_code["code"] = "\n".join(snippet)
                    snippet_code["name"] = RDMD_SNIPPET_LANGUAGES[language]
                    snippet_code["language"] = language
                    snippet_codes = {"codes": [snippet_code]}

                    snippet_block.append(json.dumps(snippet_codes, indent=2))
                    snippet_block.append("[/block]")
                    snippet = snippet_block

                cell["source"] = snippet
                logging.debug(f"After: {snippet}")

        return nb, resources


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    README_VERSION = args.version

    c = Config()
    c.snippet_format = "block"
    # c.MarkdownExporter.preprocessors = [RdmdSnippetPreprocessor]

    # Create our new, customized exporter that uses our custom preprocessor
    rdmd_exporter = MarkdownExporter(config=c)
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
        # pprint(notebook)
        rdmd = rdmd_exporter.from_notebook_node(notebook)[0]
        # output_fname = notebook_fpath.parent.parent / f"{notebook_fpath.stem}.md"
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
    ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".."
    README_VERSION_FILE = f"v{open(ROOT_PATH / '__version__').read().strip()}"

    parser.add_argument("-d", "--debug", help="Run debug mode", action="store_true")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    # parser.add_argument(
    #     "-m",
    #     "--method",
    #     default="build",
    #     choices=["build"],
    #     help="Method",
    # )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
