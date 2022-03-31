#!/usr/bin/env python3

import os
from pathlib import Path
from pprint import pprint
import re
import json
import shutil

from typing import List, Dict, Optional, Union
from typing_extensions import Literal

import argparse
import logging
import traceback

from rdme_sync.build.build_snippets import generate_snippet
from rdme_sync.build.constants import RDMD_SNIPPET_LANGUAGES


## TODO: Refactor into DocBuilder class


def generate_ipynb_file(
    input_fname: Path,
    output_fname: Path,
    snippet_paths: List[Path],
    snippet_params=Dict,
):
    """
    Given a list of snippet paths, generate a notebook `output_fname` with the given `input_fname`
    """
    logging.info(f"\tInput file: {input_fname}")
    notebook_json = json.loads(open(input_fname).read())

    for i, cell in enumerate(notebook_json["cells"]):
        try:
            if bool(re.search("@@@.*@@@", str(cell["source"]))):
                for j, cell_source in enumerate(cell["source"]):
                    if "@@@" in cell_source:
                        snippet_strs = cell_source.replace("@@@", "").strip().split(";")
                        logging.debug(f"Snippet strs: {snippet_strs}")
                        snippet = []
                        for snippet_str in snippet_strs:
                            snippet_str = snippet_str.strip()
                            logging.debug(f"Snippet str {snippet_str}")
                            snippet_text = generate_snippet(
                                snippet_str, snippet_paths, snippet_params, ext="ipynb"
                            )
                            snippet += snippet_text["snippet"]
                            snippet += ["\n"]
                        cell["source"][j] = "".join(snippet)
                        logging.debug("=================")
                        logging.debug("".join(snippet))
                        logging.debug("=================")
        except Exception as e:
            logging.info(
                f"\n-------\nFile Error: {input_fname}\nLine: {i+1}\n---------\n"
            )
            raise ValueError(f"Error in cell {i} {traceback.format_exc()}")

    Path(output_fname.parent).mkdir(parents=True, exist_ok=True)
    logging.info(f"\tOutput file: {output_fname}")
    json.dump(notebook_json, fp=open(output_fname, "w"), indent=4)


def generate_md_file(
    input_fname: Path,
    output_fname: Path,
    snippet_paths: List[Path],
    snippet_params: Dict,
    snippet_format: Literal["rdmd", "block"] = "block",
):
    """
    Given a list of snippet paths, generate a file `output_fname` with the given `input_fname`
    """
    logging.info(f"\tInput file: {input_fname}")
    with open(input_fname) as f:
        md_file = f.read()

    md_lines = list()
    for i, line in enumerate(md_file.split("\n")):
        ## Concatenated snippets
        try:
            if (not bool(re.search("<!--.*", line))) and bool(
                re.search("@@@.*@@@", line)
            ):
                snippet_strs = line.replace("@@@", "").strip().split(";")
                logging.debug(f"Snippet strs: {snippet_strs}")
                snippet = []
                for i, snippet_str in enumerate(snippet_strs):
                    snippet_str = snippet_str.strip()
                    logging.debug(f"Snippet str {snippet_str}")
                    _snippet = generate_snippet(
                        snippet_str, snippet_paths, snippet_params, ext="md"
                    )
                    language = _snippet["language"]
                    snippet_text = _snippet["snippet"]

                    snippet += snippet_text

                    logging.debug("=================")
                    logging.debug("\n".join(snippet))
                    logging.debug("=================")

                # Adding snippet wrapper
                ### RDMD Format
                if snippet_format == "rdmd":
                    snippet[0] = f"```{language} {RDMD_SNIPPET_LANGUAGES[language]}"
                    snippet.append("```")
                    snippet.append("```" + language)
                    snippet.append("```")

                ### ReadMe Block Format
                elif snippet_format == "block":
                    snippet_block = ["[block:code]"]
                    snippet_code = {}
                    snippet_code["code"] = "\n".join(snippet)
                    snippet_code["name"] = RDMD_SNIPPET_LANGUAGES[language]
                    snippet_code["language"] = language
                    snippet_codes = {"codes": [snippet_code]}

                    snippet_block.append(json.dumps(snippet_codes, indent=2))
                    snippet_block.append("[/block]")
                    snippet = snippet_block

                [md_lines.append(x) for x in snippet]

            else:
                md_lines.append(line)
        except Exception as e:
            logging.info(
                f"\n-------\nFile Error: {input_fname}\nLine: {i+1}\n---------\n"
            )
            raise ValueError(f"Error in cell {i} {traceback.format_exc()}")

    Path(output_fname.parent).mkdir(parents=True, exist_ok=True)
    with open(output_fname, "w") as fout:
        for element in md_lines:
            fout.write(element + "\n")
        logging.info(f"\tOutput file: {output_fname}")


def load_snippet_paths(base_dir: Path, fdir: Path):
    """
    Loads all snippet paths in a `_snippets` folder between `base_dir` and `fdir` directories
    """
    GENERAL_SNIPPETS = Path(base_dir) / "_snippets"
    target_subdir = [f for f in list(fdir.parts) if f not in list(base_dir.parts)]
    target_path = "/".join([f"./{base_dir.name}"] + target_subdir + ["_snippets"])
    ## Getting all snippets in target_subdir
    snippet_paths = []
    for root, dirs, _ in os.walk(base_dir):
        root_name = root.split("/")[-1]
        if root_name[0] != "_" and dirs:
            if root_name in target_subdir:
                for subdir in dirs:
                    if subdir == "_snippets":
                        snippet_paths.append(os.path.join(root, subdir))
    if snippet_paths:
        logging.debug(f"Snippet_paths for {target_path}:\n{snippet_paths} ")

    return [GENERAL_SNIPPETS] + snippet_paths


###############################################################################
# Generating ReadMe Markdown files and notebooks with automated snippets
###############################################################################


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=logging_level)
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)

    ### For files in sections and subsections
    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"

    SNIPPET_PARAMS_FPATH = Path(DOCS_TEMPLATE_PATH) / "_snippet_params.json"
    SNIPPET_PARAMS = json.loads(open(str(SNIPPET_PARAMS_FPATH), "r").read())

    if args.files:
        MD_FILES = [f for f in args.files if f.endswith(".md")]
        NOTEBOOKS = [f for f in args.files if f.endswith(".ipynb")]
    else:
        MD_FILES = Path(DOCS_TEMPLATE_PATH).glob("**/**/*.md")
        NOTEBOOKS = Path(DOCS_TEMPLATE_PATH).glob("**/**/*.ipynb")

    if args.clear:
        shutil.rmtree(DOCS_PATH, ignore_errors=True)
    for input_fname in MD_FILES:
        input_fname = Path(input_fname)
        output_fname = Path(str(input_fname).replace("docs_template", "docs"))
        snippet_paths = load_snippet_paths(
            base_dir=DOCS_TEMPLATE_PATH, fdir=input_fname.parent
        )
        logging.debug("---")
        generate_md_file(
            input_fname=input_fname,
            output_fname=output_fname,
            snippet_paths=snippet_paths,
            snippet_params=SNIPPET_PARAMS,
        )

    for input_fname in NOTEBOOKS:
        input_fname = Path(input_fname)
        output_fname = Path(str(input_fname).replace("docs_template", "docs"))
        snippet_paths = load_snippet_paths(
            base_dir=DOCS_TEMPLATE_PATH, fdir=input_fname.parent
        )
        logging.debug("---")
        generate_ipynb_file(
            input_fname=input_fname,
            output_fname=output_fname,
            snippet_paths=snippet_paths,
            snippet_params=SNIPPET_PARAMS,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"
    ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".."
    README_VERSION_FILE = open(ROOT_PATH / "__version__").read()

    parser.add_argument("-d", "--debug", action="store_true", help="Run debug mode")
    parser.add_argument(
        "-p", "--path", default=ROOT_PATH, type=str, help="Path of root folder"
    )
    parser.add_argument(
        "-pn", "--package-name", default=PACKAGE_NAME, type=str, help="Package Name"
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    parser.add_argument(
        "-f", "--files", nargs="+", default=None, help="Files to generate"
    )
    parser.add_argument(
        "-c", "--clear", action="store_true", help="Whether to clear docs folder"
    )
    args = parser.parse_args()

    main(args)
