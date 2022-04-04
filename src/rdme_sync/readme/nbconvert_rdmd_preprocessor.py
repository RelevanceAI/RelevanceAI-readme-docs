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
from rdme_sync.readme.nbconvert_rdmd_exporter import RdmdExporter


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
                    snippet_code = {}
                    snippet_code["code"] = snippet
                    snippet_code["name"] = RDMD_SNIPPET_LANGUAGES[language]
                    snippet_code["language"] = language
                    snippet_codes = {"codes": [snippet_code]}

                    snippet = json.dumps(snippet_codes, indent=2)
                    snippet = snippet

                cell["source"] = snippet
                logging.debug(f"After: {snippet}")

        return nb, resources
