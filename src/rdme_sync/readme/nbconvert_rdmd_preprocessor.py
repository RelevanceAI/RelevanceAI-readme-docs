#!/usr/bin/env python3

import logging
from typing import Dict, List, Union
from typing_extensions import Literal
import json

from traitlets import Integer, Unicode
from nbconvert.preprocessors import Preprocessor

from rdme_sync.build.constants import RDMD_SNIPPET_LANGUAGES
import re
import base64
import io
from PIL import Image


class RdmdPreprocessor(Preprocessor):
    """ReadMe Markdown preprocessor"""

    format: Literal["rdmd", "block"] = Unicode(allow_none=False).tag(config=True)

    def preprocess(self, nb, resources):
        LOGO_REGEX = [
            "<img src=.*RelevanceAI-logo.svg.*",
            "<img src=.*https://relevance.ai/wp-content/uploads/2021/11/logo.79f303e-1.svg.*",
        ]
        LOGO_REGEX_FILTER = "(" + ")|(".join(LOGO_REGEX) + ")"
        FILE_ATTACHMENT_REGEX = [
            ".*data:image/png;base64,.*",
        ]
        FILE_ATTACHMENT_REGEX_FILTER = "(" + ")|(".join(FILE_ATTACHMENT_REGEX) + ")"

        for cell in nb.cells:
            if cell["cell_type"] == "markdown":

                ## Removing logo
                if bool(re.search(LOGO_REGEX_FILTER, cell["source"])):
                    for m in re.finditer(LOGO_REGEX_FILTER, cell["source"]):
                        logging.debug(m.group())
                        cell["source"] = cell["source"].replace(m.group(), "")
                # ## Converting attachment to markdown
                # if bool(re.search(FILE_ATTACHMENT_REGEX_FILTER, cell["source"])):
                #     for m in re.finditer(FILE_ATTACHMENT_REGEX_FILTER, cell["source"]):
                #         # logging.debug(m.group())
                #         base64_string = m.group().split("data:image/png;base64,")[-1]
                #         logging.debug(base64_string[:10])
                #         image_data = base64.b64decode(str(base64_string))
                #         image = Image.open(io.BytesIO(image_data))
                #         image.save('img.png')
        return nb, resources


class RdmdSnippetPreprocessor(Preprocessor):
    """ReadMe Markdown Snippet preprocessor"""

    snippet_format: Literal["rdmd", "block"] = Unicode(allow_none=False).tag(
        config=True
    )

    def preprocess(self, nb, resources):
        language = "python"

        for cell in nb.cells:
            if cell["cell_type"] == "code":

                snippet = cell["source"]
                if not bool(re.search("@@@.*@@@", snippet)):
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
