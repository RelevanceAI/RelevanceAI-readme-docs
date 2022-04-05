#!/usr/bin/env python3

import logging
from typing import Dict, List, Union
from typing_extensions import Literal
from pathlib import Path
import os
import re
import json
import argparse
from pprint import pprint

import nbformat
from traitlets.config import Config

from deepdiff import grep

import frontmatter

from datetime import datetime

from rdme_sync.config.readme_config import ReadMeConfig
from rdme_sync.readme.nbconvert_rdmd_preprocessor import (
    RdmdPreprocessor,
    RdmdSnippetPreprocessor,
)
from rdme_sync.readme.nbconvert_rdmd_exporter import RdmdExporter
from nbconvert import HTMLExporter, RSTExporter


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    README_VERSION = args.version
    README_CONFIG_FPATH = ROOT_PATH / "config" / "readme-config.yaml"
    readme_config = ReadMeConfig(version=README_VERSION, fpath=README_CONFIG_FPATH)

    c = Config()
    if args.format == "block":
        c.RdmdSnippetPreprocessor.snippet_format = "block"
        rdmd_template = "rdmd_block.md.j2"
    elif args.format == "rdmd":
        c.RdmdSnippetPreprocessor.snippet_format = "rdmd"
        rdmd_template = "rdmd.md.j2"

    c.Exporter.template_file = os.path.join(
        os.path.dirname(__file__), "templates", "rdmd", rdmd_template
    )
    c.RdmdExporter.preprocessors = [RdmdPreprocessor, RdmdSnippetPreprocessor]

    rdmd_exporter = RdmdExporter(config=c)

    # fig_c = Config()
    # rst_exporter = RSTExporter()
    # fig_c.HTMLExporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']

    NOTEBOOK_PATHS = Path(DOCS_TEMPLATE_PATH).glob("**/**/*.ipynb")
    ## Filter checkpoints
    NOTEBOOK_GENERATE_PATHS = [
        n
        for n in NOTEBOOK_PATHS
        if ".ipynb_checkpoints" not in str(n) and "_notebooks" != n.parent.name
    ]

    for notebook_fpath in NOTEBOOK_GENERATE_PATHS:
        output_fname = str(notebook_fpath).replace(".ipynb", ".md")
        if not Path(output_fname).exists():
            logging.debug(f"Converting: {notebook_fpath}")
            notebook = nbformat.read(Path(notebook_fpath), as_version=4)
            rdmd = rdmd_exporter.from_notebook_node(notebook)[0]

            # rdmd_print = "\n".join(
            #     [f for f in rdmd.split("\n") if "data:image/png;base64," not in f]
            # )
            # logging.debug(rdmd_print)

            ## Loading frontmatter
            post = frontmatter.loads(rdmd)

            logging.info(f"Building frontmatter: ")
            notebook_name = notebook_fpath.name.split(".")[0].replace("_", " ")

            page_slug = re.sub(
                r"[^a-zA-Z0-9-]", "", notebook_name.replace(" ", "-").lower()
            ).strip("-")

            post_metadata = {
                "title": notebook_name,
                "slug": page_slug,
                "hidden": True,
                "excerpt": "",
                "category": readme_config.category_slugs[notebook_fpath.parent.name],
                "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "updatedAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            }
            post.metadata = post_metadata
            logging.debug(post.metadata)

            # logging.info(f'Converting: ')
            # logging.debug(frontmatter.dumps(post))

            with open(output_fname, "w") as fout:
                fout.write(frontmatter.dumps(post))
                logging.info(f"\tOutput file: {output_fname}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"
    ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".." / ".."
    README_VERSION_FILE = open(ROOT_PATH / "__version__").read().strip()
    README_VERSION_FILE = (
        f"v{README_VERSION_FILE}"
        if README_VERSION_FILE[0] != "v"
        else README_VERSION_FILE
    )

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
