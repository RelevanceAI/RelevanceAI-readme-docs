#!/usr/bin/env python3

from typing import Dict, List, Union
import requests
import os
import json

from traitlets.config import Config
from nbconvert import MarkdownExporter

from traitlets import Integer
from nbconvert.preprocessors import Preprocessor


class ReadMeMarkdown(Preprocessor):
    """ReadMe Markdown preprocessor"""

    start = Integer(0, help="first cell of notebook to be converted").tag(config=True)
    end = Integer(-1, help="last cell of notebook to be converted").tag(config=True)

    def preprocess(self, nb, resources):
        self.log.info("I'll keep only cells from %d to %d", self.start, self.end)
        nb.cells = nb.cells[self.start : self.end]
        return nb, resources


class ReadmeMarkdownExporter(MarkdownExporter):
    """Custom ReadMe Markdown Exporter

    Parameters
    ----------
    MarkdownExporter : TemplateExporter
        Extends MarkdownExporter to add ReadMe specific rendering

    """

    export_from_notebook = "ReadMe Markdown"

    def __init__(self, readme_version: str = None):
        if not readme_version:
            raise ValueError(
                f"Readme version is required. Please specify a version. eg. 'v2.0.0'"
            )

        self.base_url = "https://dash.readme.com/api/v1/"
        self.session = requests.Session()
        self.readme_version = readme_version

        self.readme_api_key = self._check_env_var_exist("RELEVANCEAI_README_API_KEY")
        self.headers = {
            "x-readme-version": readme_version,
            "Authorization": f"Basic {self.readme_api_key}",
            "Content-Type": "application/json",
        }

    # def _file_extension_default(self):
    #     """
    #     The new file extension is ``.ipynb``
    #     """
    #     return '.ipynb'

    @property
    def template_paths(self):
        """
        We want to inherit from Markdown template, and have template under
        ``./templates/`` so append it to the search path. (see next section)

        Note: nbconvert 6.0 changed ``template_path`` to ``template_paths``
        """
        return super().template_paths + [
            os.path.join(os.path.dirname(__file__), "templates")
        ]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return "test_template"  # full
