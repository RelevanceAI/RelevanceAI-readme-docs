#!/usr/bin/env python3

from typing import Dict, List, Union
import requests
import os
import json


class NotebookRDMDBuilder:
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
