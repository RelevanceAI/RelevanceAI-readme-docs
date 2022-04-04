#!/usr/bin/env python3

from typing import Dict, List, Union
import os
import json

from traitlets.config import Config
from nbconvert import MarkdownExporter


class RdmdExporter(MarkdownExporter):
    """Custom ReadMe Markdown Exporter

    Parameters
    ----------
    MarkdownExporter : TemplateExporter
        Extends MarkdownExporter to add ReadMe specific rendering

    """

    export_from_notebook = "ReadMe Markdown"

    # def __init__(self, readme_version: str = None):
    #     if not readme_version:
    #         raise ValueError(
    #             f"Readme version is required. Please specify a version. eg. 'v2.0.0'"
    #         )
    #     self.readme_version = readme_version

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
        return super()._template_paths() + [
            os.path.join(os.path.dirname(__file__), "templates")
        ]

    # def _template_file_default(self):
    #     """
    #     We want to use the new template we ship with our library.
    #     """
    #     return  "rdmd"

    # @property
    # def template_file(self):
    #     return os.path.join(
    #     os.path.dirname(__file__), "templates", "rdmd", "rdmd.md.j2"
    # )
