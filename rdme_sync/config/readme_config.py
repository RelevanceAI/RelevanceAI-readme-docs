#!/usr/bin/env python3

import yaml
from typing import Dict, List, Literal, Optional, Tuple, Union
import logging

from rdme_sync.readme.rdme_api import ReadMeAPI
from rdme_sync.config.config import Config


class ReadMeConfig(Config):
    def __init__(
        self,
        fpath: str,
        version: str,
        select_fields: Optional[List[str]] = [
            "slug",
            "title",
            "excerpt",
            "hidden",
            "createdAt",
            "updatedAt",
            "parentDoc",
            "order",
            "_id",
        ],
        *args,
        **kwargs,
    ):
        super().__init__(
            fpath=fpath, version=version, select_fields=select_fields, *args, **kwargs
        )
        self.rdme = ReadMeAPI(self.version)
        self.api_categories = ["relevance-ai-endpoints"]
        self.sdk_categories = ["python-sdk"]
        self.config = yaml.safe_load(open(self.fpath, "r"))
        self.condensed_fpath = f"{str(self.fpath).replace('.yaml', '-condensed.yaml')}"
        self.condensed_config = yaml.safe_load(open(self.condensed_fpath, "r"))
        self.select_fields = select_fields

        self.category_slugs = {
            c["slug"]: c["_id"]
            for c in self.rdme.get_categories(select_fields=["slug", "_id"])
        }
        self.rdme_page_slugs = self._load_page_slugs()
        self.docs_categories = self._load_docs_categories()

    def _load_docs_categories(self):
        """Loads list of docs categories slugs"""
        categories = self.config["categories"]
        return [category for category, pages in categories.items()]

    def _load_page_slugs(self):
        """Loads list of all rdme page slugs"""
        categories = self.config["categories"]
        slugs = []
        for category, pages in categories.items():
            slugs += [category]
            for page, children in pages.items():
                slugs += [page]
                slugs += children
        return slugs

    def build(
        self, fpath: str = None, condensed: bool = True, select_fields: List[str] = None
    ):
        """Builds rdme config dict and outputs to rdme-config file

        Parameters
        ----------
        fpath : Config filepath
            Overrides instance fpath if set
        condensed: bool
            If True, builds a condensed version of the rdme-config file as well
        select_fields : List[str]
            select_fields: List
            Fields to include in the search results, empty array/list means all fields

        """
        if fpath:
            self.fpath = fpath
        if select_fields:
            self.select_fields = select_fields

        category_slugs = {
            c["slug"]: c["_id"]
            for c in self.rdme.get_categories(select_fields=["slug", "_id"])
        }

        ## Building condensed
        condensed_config = {"version": self.version}
        category_detail = {}
        for cs in category_slugs.keys():
            if not any([f in cs for f in self.api_categories + self.sdk_categories]):
                category_detail[cs] = {
                    ps["slug"]: sorted([c["slug"] for c in ps["children"]])
                    for ps in self.rdme.get_docs_for_category(
                        category_slug=cs, select_fields=["slug", "children"]
                    )
                }
        condensed_config["categories"] = category_detail

        if condensed:
            logging.debug(f"Saving config to { self.condensed_fpath}")
            with open(self.condensed_fpath, "w") as f:
                yaml.dump(condensed_config, f, default_flow_style=False, sort_keys=True)

        config = condensed_config

        ## Building expanded config (inc children)
        for category, pages in category_detail.items():
            page_details = {}
            for page, children in pages.items():
                page_detail = self.rdme.get_doc(
                    page_slug=page, select_fields=self.select_fields
                )
                page_details[page] = (
                    page_detail[0] if isinstance(page_detail, list) else page_detail
                )

                for child in children:
                    page_details[page][child] = self.rdme.get_doc(
                        page_slug=child, select_fields=self.select_fields
                    )

            category_detail[category] = page_details

        logging.debug(f"Saving config to {self.fpath} ... ")
        # logging.debug(f'Config: {json.dumps(category_detail, indent=2)}')
        config["categories"] = category_detail
        with open(self.fpath, "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=True)
        return config

    def _search_dict(self, k, d):
        if k in d:
            return d[k]
        for v in d.values():
            if isinstance(v, dict):
                return self._search_dict(k, v)
        return None

    def create(
        self,
        title: str,
        type: Union["basic", "link", "error"],
        category_slug: str,
        parent_slug: str = None,
        body: str = "",
        hidden: bool = True,
        order: int = 999,
        error_code: Dict = None,
    ):
        """Creates new page in rdme if slug does not exist

        Parameters
        ----------
        title: str
            A URL-safe representation of the doc title.
            Slugs must be all lowercase, and replace spaces with hyphens.
            For example, for the the doc "New Features", enter the slug "new-features"
        type: str
            Type of the page. The available types all show up under the /docs/ URL path of your docs project.
            Can be "basic" (most common), "error" (page desribing an API error), or "link" (page that redirects to an external link).
        category_slug: str
            A URL-safe representation of the category title.
            Slugs must be all lowercase, and replace spaces with hyphens.
            For example, for the the category "Getting Started", enter the slug "getting-started"
        parent_slug: str
            Slug of the parent doc. If you don't want to have a parent doc, leave this blank.
        body: str
            Body content of the page, formatted in rdme or GitHub flavored Markdown. Accepts long page content, for example, greater than 100k characters.
        hidden: bool
            Whether or not the doc should be hidden in rdme.
        order: int
            The position of the page in your project sidebar.
        error_code: dict
            code: str
            The error code for docs with the "error" type
        """
        category_id = self.category_slugs[category_slug]

        if category_slug!=parent_slug:
            result = self._search_dict(parent_slug, self.config)
            parent_doc_id = result["_id"]
        else:
            parent_doc_id=category_id
        

        return self.rdme.create_doc(
            title=title,
            type=type,
            category_id=category_id,
            parent_doc_id=parent_doc_id,
            body=body,
            hidden=hidden,
            order=order,
            error_code=error_code,
        )

    @staticmethod
    def get_page_orders(d: Dict, category: bool=False):
        """Returns list of page orders
        d: dict
            Config dict
        category: bool
            If true, get category order else page/children order
        """
        page_orders = []
        for k, v in d.items():
            if category:
                if v.get('order'):
                    page_orders.append(v["order"])
            if isinstance(v, list):
                if isinstance(v[0], dict):
                    page_orders.append(v[0]["order"])
        return page_orders
