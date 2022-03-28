#!/usr/bin/env python3

from itertools import chain
import os
from pathlib import Path
import re
import json

from typing import List, Dict, Optional, Union
from typing_extensions import Literal

import argparse
import logging
import traceback

RDMD_SNIPPET_LANGUAGES = {
    "python": "Python (SDK)",
    "bash": "Bash",
    "json": "JSON",
}

###############################################################################
# Helper Functions
###############################################################################


def load_params_ref(param_str: str) -> dict:
    """
    Loads params ref dict from a param str
    eg. CENTROIDS=centroids, CLUSTERER=clusterer, DF=df
    """
    NUM_REGEX_PARAM = "(([A-Z])\w+=[0-9.])"
    VALUE_REGEX_PARAM = "([A-Z])\w+=([\s'\"?\./<>A-Za-z0-9_-]+)"
    LIST_REGEX_PARAM = "([A-Z])\w+=\[(.*?)\]"
    JSON_REGEX_PARAM = "([A-Z])\w+=(\[([\s\"'<>\{\}:?.,A-Za-z0-9_-]+\]))"
    STR_REGEX_PARAM_DOUBLE_QUOTE = '([A-Z])\w+=""'
    STR_REGEX_PARAM_SINGLE_QUOTE = "([A-Z])\w+=''"
    params_ref = dict(
        tuple(
            m.group()
            .strip()
            .replace("==", "=")
            .replace('""', "")
            .replace("''", "")
            .split("=")
        )
        for m in chain(
            re.finditer(NUM_REGEX_PARAM, param_str),
            re.finditer(VALUE_REGEX_PARAM, param_str),
            re.finditer(LIST_REGEX_PARAM, param_str),
            re.finditer(JSON_REGEX_PARAM, param_str),
            re.finditer(STR_REGEX_PARAM_DOUBLE_QUOTE, param_str),
            re.finditer(STR_REGEX_PARAM_SINGLE_QUOTE, param_str),
        )
        # print(m.group())
    )
    # params_ref = {}
    return params_ref


def load_param_in_snippet(snippet_path: Path, snippet: List, params: Dict):
    """
    Loads params in snippet
    """
    PARAM_REFS = []
    for i, line in enumerate(snippet):
        for m in re.finditer("<<([A-Z_0-9]*)>>", line):
            for k, v in params.items():
                if k in m.group():

                    if isinstance(v, list):
                        v = str(v)
                        if isinstance(v[0], dict):  ### List[dict]
                            v = json.dumps(v)
                    line = line.replace(f"<<{k}>>", v)
            PARAM_REFS.append(m.group().replace("<<", "").replace(">>", "").strip())
        snippet[i] = line

    SNIPPET_PARAM_DIFF = set(list(params.keys())) - (set(PARAM_REFS))
    if SNIPPET_PARAM_DIFF:
        raise ValueError(
            f"\nIncorrect params {SNIPPET_PARAM_DIFF} in required params {list(PARAM_REFS)}\n{snippet_path}"
        )
    return snippet


def load_snippet(
    snippet_path: str, ext: Literal["md", "ipynb"], params: Optional[Dict] = None
):
    """
    Loads given snippet from the given path in a given format
    """
    try:
        with open(snippet_path, "r") as f:
            if ext == "ipynb":
                text = f.readlines()  ## Need to keep '\n' for 'ipynb'
            elif ext == "md":
                text = f.read().strip().splitlines()
    except Exception as e:
        raise FileNotFoundError(f"File not found: {snippet_path}")

    ### Loading language and default params
    language = text[0].split(" ")[0]
    if len(text[0].split(" ")) > 1:
        default_params = load_params_ref(text[0])
        logging.debug(f"Found default params {default_params}")
    else:
        default_params = {}

    if ext == "ipynb":
        snippet = text[1:]
    elif ext == "md":
        snippet = text

    ## Loading params data
    snippet_params = {**default_params, **params} if params else default_params
    if snippet_params:
        load_param_in_snippet(snippet_path, snippet, snippet_params)

    ## Adding snippet wrapper for md
    if ext == "md":
        snippet[0] = f"```{language} {RDMD_SNIPPET_LANGUAGES[language]}"
        snippet.append("```")
        snippet.append("```" + language)
        snippet.append("```")
    return snippet


def generate_snippet(
    snippet_str: str,
    snippet_paths: List,
    snippet_params: Dict,
    ext: Literal["md", "ipynb"],
):
    """
    Load the corresponding snippet with given parameters depending on the extension type
    Loads snippets in order from root to inner folder - will overwrite the snippets with same name
    """
    logging.debug(f"\tSnippet paths: {snippet_paths}")
    snippet = []
    for snippet_path in snippet_paths:
        available_snippets = {
            f: f"{Path(root).joinpath(f)}"
            for root, _, files in os.walk(snippet_path)
            for f in files
        }
        snippet_name = snippet_str.split(",")[0].strip()

        if snippet_name in available_snippets.keys():
            logging.debug(f"\tSnippets: {list(available_snippets.keys())}")
            logging.debug(f"\tSnippet name: {snippet_name}")
            params = None

            if len(snippet_str.split(",")) > 1:
                ## Loading params
                params_ref = load_params_ref(snippet_str)
                logging.debug(f"\tParams ref: {params_ref}")

                params = {}
                for k, v in params_ref.items():

                    if snippet_params.get(params_ref[k]):
                        params[k] = snippet_params[params_ref[k]]
                    else:
                        params[k] = v
                logging.debug(f"\tParams: {params}")

            snippet_fpath = available_snippets[snippet_name]
            logging.debug(f"\tLoading snippet: {snippet_fpath}")
            if ext == "ipynb":
                snippet = load_snippet(snippet_fpath, params=params, ext="ipynb")
            elif ext == "md":
                snippet = load_snippet(snippet_fpath, params=params, ext="md")

    if not snippet:
        raise ValueError(f"{snippet_str} was not found in {snippet_paths}")

    return snippet


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
                            snippet += generate_snippet(
                                snippet_str, snippet_paths, snippet_params, ext="ipynb"
                            )
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

                    ## Removing snippet code wrapper union
                    if i != 0:
                        _snippet[0] = ""
                    if i != len(snippet_strs) - 1:
                        _snippet = _snippet[:-3]
                    snippet += _snippet
                    logging.debug("=================")
                    logging.debug("\n".join(snippet))
                    logging.debug("=================")

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
    args = parser.parse_args()

    main(args)
