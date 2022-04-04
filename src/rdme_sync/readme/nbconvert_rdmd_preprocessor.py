#!/usr/bin/env python3

import logging
from typing import Dict, List, Union
from typing_extensions import Literal
import json

from traitlets import Integer, Unicode
from nbconvert.preprocessors import Preprocessor

from rdme_sync.build.constants import RDMD_SNIPPET_LANGUAGES
import re


class RdmdPreprocessor(Preprocessor):
    """ReadMe Markdown Snippet preprocessor"""

    def preprocess(self, nb, resources):
        LOGO_REGEX = [
            "<img src=.*RelevanceAI-logo.svg.*",
            "<img src=.*https://relevance.ai/wp-content/uploads/2021/11/logo.79f303e-1.svg.*",
        ]
        LOGO_REGEX_FILTER = "(" + ")|(".join(LOGO_REGEX) + ")"

        for cell in nb.cells:
            if cell["cell_type"] == "markdown":

                ## Removing logo
                if bool(re.search(LOGO_REGEX_FILTER, cell["source"])):
                    for m in re.finditer(LOGO_REGEX_FILTER, cell["source"]):
                        logging.debug(m.group())
                        cell["source"] = cell["source"].replace(m.group(), "")
                ## Converting

        return nb, resources


class RdmdSnippetPreprocessor(Preprocessor):
    """ReadMe Markdown Snippet preprocessor"""

    # start = Integer(0, help="first cell of notebook to be converted").tag(config=True)
    # end = Integer(-1, help="last cell of notebook to be converted").tag(config=True)

    snippet_format: Literal["rdmd", "block"] = Unicode(allow_none=False).tag(
        config=True
    )

    def preprocess(self, nb, resources):
        # nb.cells = nb.cells[self.start : self.end]
        language = "python"

        for cell in nb.cells:
            if cell["cell_type"] == "code":

                snippet = cell["source"]
                logging.debug(f"Before: {snippet}")
                # if self.snippet_format == "rdmd":
                #     snippet_code[0] = f"```{language} {RDMD_SNIPPET_LANGUAGES[language]}"
                #     snippet.append("```")
                #     snippet.append("```" + language)
                #     snippet.append("```")

                ### ReadMe Block Format
                if self.snippet_format == "block":
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
