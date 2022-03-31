#!/usr/bin/env python3

import os
import re
import logging
import json
from pathlib import Path
from typing import List, Literal, Tuple, Union


def get_files(path: Union[Path, str], ext: Literal["md", "ipynb"]):
    return Path(path).glob(f"**/*.{ext}")


def file_find_replace(
    fname: str, find_sent_regex: str, find_str_regex: str, replace_str: str
):
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
                            logging.debug(
                                f"Found str within sentence: {find_replace_str.strip()}"
                            )

                            logging.debug(f"Replace str: {replace_str}")
                            line = line.replace(find_replace_str, replace_str)
                            logging.debug(f"Updated: {line.strip()}")

                        else:
                            logging.debug(f"Not found: {find_replace_str}")
                    else:
                        logging.debug(f"Not found: {find_sent_regex}")

                f.write(line)


def notebook_find_replace(
    fname: str, find_sent_regex: str, find_str_regex: str, replace_str: str
):
    logging.info(f"\tInput: {fname}")
    notebook_json = json.loads(open(fname).read())

    for cell in notebook_json["cells"]:
        if "data:image/png;base64" in str(cell["source"]):
            continue
        if bool(re.search(find_sent_regex, str(cell["source"]))):
            logging.debug(f"Found sentence: {str(cell['source'])}")
            logging.debug(f"Find string regex: {find_str_regex}")
            for i, cell_source in enumerate(cell["source"]):
                if bool(re.search(find_str_regex, cell_source)):
                    find_replace_str = re.search(find_str_regex, cell_source).group()
                    logging.debug(
                        f"Found str within sentence: {find_replace_str.strip()}"
                    )
                    logging.debug(f"Replace str: {replace_str}")
                    cell_source = cell_source.replace(find_replace_str, replace_str)
                    logging.debug(f"Updated: {cell_source.strip()}")
                    cell["source"][i] = cell_source

    logging.info(f"\tOutput file: {fname}")
    json.dump(notebook_json, fp=open(fname, "w"), indent=4)
