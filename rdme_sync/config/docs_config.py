#!/usr/bin/env python3

import os
import re
from pathlib import Path
import yaml
from typing import Dict, List, Literal, Optional, Tuple, Union
import logging

from rdme_sync.config.config import Config


class DocsConfig(Config):
    def __init__(
        self,
        dir_path: str = None,
        fpath: str = None,
        version: str = None,
        select_fields: Optional[List[str]] = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            fpath=fpath, version=version, select_fields=select_fields, *args, **kwargs
        )
        self.dir_path = dir_path
        self.config = yaml.safe_load(open(self.fpath, "r"))
        self.condensed_fpath = f"{str(self.fpath).replace('.yaml', '-condensed.yaml')}"
        self.condensed_config = yaml.safe_load(open(self.condensed_fpath, "r"))

        self.docs_page_slugs = self._load_page_slugs()
        self.docs_categories = self._load_docs_categories()

    def _load_docs_categories(self):
        """Loads list of docs categories slugs""" 
        return [
            category_name
            for category in self.config[self.dir_path.name]
            if category and isinstance(category, dict)
            for category_name, pages in category.items()
        ]

    def _load_page_slugs(self):
        """Loads list of all docs page slugs"""
        slugs = {}
        return slugs

    def build(
        self,
        dir_path: Path = None,
        fpath: Path = None,
        condensed: bool = True,
        select_fields: Optional[List[str]] = None,
    ):
        """Building config file from docs filetree

        Parameters
        ----------
        dir_path : Path
            Directory path
        fpath : Path
            Path to output config file
        condensed: bool
            If True, builds a condensed version of the readme-config file as well
        select_fields : List[str]
            select_fields: List
            Fields to include in the search results, empty array/list means all fields
        """
        if dir_path:
            self.dir_path = dir_path
        if fpath:
            self.fpath = fpath
        if select_fields:
            self.select_fields = select_fields

        self.config = self._dir_to_dict(self.dir_path)
        self.config["version"] = self.version

        with open(self.fpath, "w") as f:
            yaml.dump(self.config, f, default_flow_style=False, sort_keys=True)

        if condensed:
            self._build_condensed(fpath=self.condensed_fpath)

        return self.config

    def _dict_to_dir(self, data: dict, path: Path):
        """_dict_to_dir expects data to be a dictionary with one top-level key."""
        dest = Path.getcwd() / path
        if isinstance(data, dict):
            for k, v in data.items():
                Path(dest / k).mkdir(parents=True, exist_ok=True)
                self._dict_to_dir(v, Path / str(k))
        elif isinstance(data, list):
            for i in data:
                if isinstance(i, dict):
                    self._dict_to_dir(i, path)
                else:
                    with open(Path(dest) / i, "a"):
                        Path(dest / i).touch()
        if isinstance(data, dict):
            return list(data.keys())[0]

    def _dir_to_dict(self, path: Path):
        """_dir_to_dict returns a dictionary filetree given a path."""
        directory = {}
        for root, dirs, files in os.walk(path):
            dn = Path(root).name
            directory[dn] = []
            if dirs:
                for d in dirs:
                    directory[dn].append(self._dir_to_dict(path=Path(path) / d))
                for f in files:
                    directory[dn].append(f)
            else:
                directory[dn] = files

            return directory

    def _iterdict(self, d: Dict, filter_keys: List[str] = ["([_])\w+"]):
        """Iterate nested dict"""
        regex_filter = "(" + ")|(".join(filter_keys) + ")"
        for k, v in d.items():
            if not re.match(regex_filter, k):
                if isinstance(v, dict):
                    self._iterdict(v)
                elif isinstance(v, list):
                    for i, value in enumerate(v):
                        if isinstance(value, dict):
                            self._iterdict(value)
                        elif isinstance(value, str):
                            v[i] = value.replace(".md", "")
                return {k: v}

    @staticmethod
    def _clean_config(config: Dict, filter_keys: List[str] = ["([_])\w+"]):
        """Filter config with regex filter_keys
        Converts docs-config into docs-config-condensed
        """
        regex_filter = "(" + ")|(".join(filter_keys) + ")"
        clean_config = {}
        for category, pages in config.items():
            if not re.match(regex_filter, category):
                clean_config[category] = pages
                page_slugs = [p for p in pages if isinstance(p, str)]
                page_dicts = {
                    k: v
                    for p in pages
                    if isinstance(p, dict)
                    for k, v in p.items()
                    if not re.match(regex_filter, k)
                }
                logging.debug(f"Page Slugs: {page_slugs}")
                if page_dicts:
                    logging.debug(f"\tPage Dicts: {list(page_dicts.keys())}")
                page_detail = {}

                for slug in page_slugs:
                    if page_dicts.get(slug):
                        children = sorted(
                            [c for c in page_dicts.get(slug) if isinstance(c, str)]
                        )
                        page_detail[slug] = children
                    else:
                        page_detail[slug] = []
            clean_config[category] = page_detail
        return clean_config

    def _build_condensed(
        self,
        fpath: Path,
    ):
        """Update docs config if new slug in ReadMe

        Parameters
        ----------
        slug : str
            Page slug
        fpath : str, optional
            Config output filepath

        Returns
        -------
        config : Dict
            Config of new docs
        """
        category_detail = {}
        for category in self.config[self.dir_path.name]:
            if isinstance(category, dict):
                result = self._iterdict(category)
                if result:
                    for k, v in result.items():
                        category_detail[k] = v

        category_detail = self._clean_config(category_detail)
        docs_readme_config = {"categories": category_detail}
        docs_readme_config["version"] = self.version
        with open(fpath, "w") as f:
            yaml.dump(docs_readme_config, f, default_flow_style=False, sort_keys=True)
        return docs_readme_config
