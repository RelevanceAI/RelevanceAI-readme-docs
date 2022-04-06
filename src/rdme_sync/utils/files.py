#!/usr/bin/env python3

import os
import re
import logging
import json
from pathlib import Path
from typing import List, Tuple, Union
from typing_extensions import Literal


def get_files(path: Union[Path, str], ext: Literal["md", "ipynb"]):
    """Gets all files in a directory with a specific extension

    Parameters
    ----------
    path : Union[Path, str]
        The path to the directory containing the files.
    ext : Literal["md", "ipynb"]
        The extension of the files you want to get.

    """
    return Path(path).glob(f"**/*.{ext}")


def file_find_replace(
    fname: str, find_sent_regex: str, find_str_regex: str, replace_str: str
):
    """This function takes a file name, a find sentence regex, a find string regex, and a replace string.
    It then opens the file, finds the sentence that matches the find sentence regex, and replaces the
    string that matches the find string regex with the replace string

    Parameters
    ----------
    fname : str
        The name of the file to be modified.
    find_sent_regex : str
        A regular expression that will be used to find sentences.
    find_str_regex : str
        The regex that will be used to find the string that needs to be replaced.
    replace_str : str
        The string to replace the found string with.

    """
    if fname.is_file():
        with open(fname, "r") as f:
            lines = f.readlines()

        with open(fname, "w") as f:
            for i, line in enumerate(lines):
                if "data:image/png;base64" in str(line):
                    continue
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
    """This function finds and replaces a string in a Jupyter notebook

    Parameters
    ----------
    fname : str
        The name of the file to be searched.
    find_sent_regex : str
        A regular expression that will be used to find sentences.
    find_str_regex : str
        The regex that will be used to find the string that needs to be replaced.
    replace_str : str
        The string to replace the found string with.

    """
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
