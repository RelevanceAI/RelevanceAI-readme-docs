#!/usr/bin/env python3

from itertools import chain
import os
from pathlib import Path
from pprint import pprint
import re
import json

from typing import List, Dict, Optional, Union
from typing_extensions import Literal

import logging


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
    snippet_path: str,
    ext: Literal["md", "ipynb"],
    params: Optional[Dict] = None,
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

    snippet = text[1:]
    ## Loading params data
    snippet_params = {**default_params, **params} if params else default_params
    if snippet_params:
        load_param_in_snippet(snippet_path, snippet, snippet_params)

    return {"language": language, "snippet": snippet}


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
