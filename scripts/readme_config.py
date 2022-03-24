#!/usr/bin/env python3

import os
import re
from pathlib import Path
import itertools
from typing import List, Literal, Tuple, Union
import logging
import argparse
import json
from pprint import pprint
import yaml
import markdown
import shutil

from readme_api import ReadMeAPI


def get_files(path: Union[Path, str], ext: Literal["md", "ipynb"]):
    return Path(path).glob(f"**/*.{ext}")


class Config:
    def __init__(
        self,
        fpath: str = None,
        version: str = None,
        select_fields: List[str] = None,
        *args,
        **kwargs,
    ):
        self.version = f"v{version}" if version[0] != "v" else version
        self.fpath = fpath
        if not select_fields:
            self.select_fields = [
                "slug",
                "title",
                "excerpt",
                "hidden",
                "createdAt",
                "updatedAt",
                "parentDoc",
                "order",
            ]


class ReadMeConfig(Config):
    def __init__(
        self,
        fpath: str = None,
        version: str = None,
        select_fields: List[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            fpath=fpath, version=version, select_fields=select_fields, *args, **kwargs
        )
        self.readme = ReadMeAPI(self.version)
        self.api_categories = ["relevance-ai-endpoints"]
        self.sdk_categories = ["python-sdk"]
        self.config = yaml.safe_load(open(self.fpath, "r"))

        self.readme_page_slugs = self._load_readme_page_slugs()
        self.docs_categories = self._load_docs_categories()

    def _load_docs_categories(self):
        categories = self.config["categories"]
        return [category for category, pages in categories.items()]

    def _load_readme_page_slugs(self):
        categories = self.config["categories"]
        slugs = []
        for category, pages in categories.items():
            slugs += [category]
            for page, children in pages.items():
                slugs += [page]
                slugs += children
        return slugs

    def build(self, fpath=None, condensed=False, select_fields: List[str] = None):
        if fpath:
            self.fpath = fpath
        if select_fields:
            self.select_fields = select_fields

        category_slugs = [
            c["slug"] for c in self.readme.get_categories(select_fields=["slug"])
        ]

        category_detail = {}
        for cs in category_slugs:
            if not any([f in cs for f in self.api_categories + self.sdk_categories]):
                category_detail[cs] = {
                    ps["slug"]: [c["slug"] for c in ps["children"]]
                    for ps in self.readme.get_docs_for_category(
                        category_slug=cs, select_fields=["slug", "children"]
                    )
                }

        if not condensed:
            for category, pages in category_detail.items():
                page_details = {}
                for page, children in pages.items():
                    page_details[page] = self.readme.get_doc(
                        page_slug=page, select_fields=self.select_fields
                    )[0]
                    for child in children:
                        page_details[page][child] = self.readme.get_doc(
                            page_slug=child, select_fields=self.select_fields
                        )
                category_detail[category] = page_details

        config = {"version": self.version}
        config["categories"] = category_detail

        with open(self.fpath, "w") as f:
            yaml.dump(config, f, default_flow_style=False)

    def update(
        self,
        slug: str,
        fpath: str = None,
        condensed: str = False,
        select_fields: List[str] = None,
    ):
        return NotImplementedError


class DocsConfig(Config):
    def __init__(
        self,
        fpath: str = None,
        version: str = None,
        select_fields: List[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            fpath=fpath, version=version, select_fields=select_fields, *args, **kwargs
        )

    # def build(self, fpath=None, condensed=False, select_fields: List[str] = None):
    #     if fpath: self.fpath = fpath
    #     if select_fields: self.select_fields = select_fields

    #     category_slugs = [c['slug'] for c in self.readme.get_categories(select_fields=['slug'])]

    #     category_detail = {}
    #     for cs in category_slugs:
    #         if not any([f in cs for f in self.api_categories+self.sdk_categories]):
    #             category_detail[cs] = { ps['slug']: [c['slug'] for c in ps['children']]
    #                     for ps in self.readme.get_docs_for_category(category_slug=cs, select_fields=['slug', 'children'])}

    #     if not condensed:
    #         for category, pages in category_detail.items():
    #             page_details = {}
    #             for page, children in pages.items():
    #                 page_details[page] = self.readme.get_doc(page_slug=page, select_fields=self.select_fields)[0]
    #                 for child in children:
    #                     page_details[page][child] = self.readme.get_doc(page_slug=child, select_fields=self.select_fields)
    #             category_detail[category] = page_details

    #     config = {'version': self.version}
    #     config['categories'] = category_detail

    #     with open(self.fpath, 'w') as f:
    #         yaml.dump(config, f, default_flow_style=False)

    # def update(self, slug: str, fpath:str=None, condensed:str=False, select_fields: List[str]=None):
    #     return NotImplementedError


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    EXPORT_MD_PATH = Path(args.path) / "export_md" / "_v0.31.0"
    README_VERSION = args.version
    README_CONFIG_FPATH = Path(__file__).parent.resolve() / ".." / "readme-config.yml"

    readme_config = ReadMeConfig(version=README_VERSION, fpath=README_CONFIG_FPATH)

    if args.method == "build":
        print(f"Building {README_VERSION} config ...")
        readme_config.build()
    elif args.method == "build-condensed":
        print(f"Building {README_VERSION} condensed config ...")
        fpath = str(README_CONFIG_FPATH).replace(
            "readme-config", "readme-config-condensed"
        )
        readme_config.build(fpath, condensed=True)

    elif args.method == "update":
        MD_FILES = Path(DOCS_TEMPLATE_PATH).glob("**/**/*.md")
        EXPORT_MD_FILES = Path(EXPORT_MD_PATH).glob("**/**/*.md")

        docs_category_slugs = []
        for file in DOCS_TEMPLATE_PATH.iterdir():
            if file.is_dir() and file.name[0] != "_":
                docs_category_slugs += [file.name]

        docs_page_slugs = []
        for md in MD_FILES:
            with open(md, "r") as f:
                text = f.read().strip().splitlines()
                docs_page_slugs += [
                    line.split('"')[1::2][0]
                    for i, line in enumerate(text)
                    if "slug: " in line
                ]

        # Making category folders
        export_path = [
            f for f in EXPORT_MD_FILES if "writing-aggregation-queries" in f.name
        ]
        print(export_path)

        for category, pages in readme_config.config["categories"].items():
            if category not in docs_category_slugs:
                Path(DOCS_TEMPLATE_PATH / category).mkdir(parents=True)
            for page, children in pages.items():
                if page not in docs_page_slugs:
                    Path(DOCS_TEMPLATE_PATH / category / page).mkdir(
                        parents=True, exist_ok=True
                    )
                    if page not in readme_config.select_fields:
                        print(page)
                        export_path = [f for f in EXPORT_MD_FILES if page in f.name]
                        print(export_path)
                        if export_path == []:
                            print(f"{page} not found in export_md")
                            Path(DOCS_TEMPLATE_PATH / category / f"{page}.md").touch()
                        else:
                            print(f"Copying {page} from export_md")
                            print(
                                str(export_path[0]),
                                DOCS_TEMPLATE_PATH / category / f"{page}.md",
                            )
                            shutil.copy(
                                str(export_path[0]),
                                DOCS_TEMPLATE_PATH / category / f"{page}.md",
                            )

                for child in children:
                    if child not in docs_page_slugs:
                        if child not in readme_config.select_fields:
                            export_path = [
                                f for f in EXPORT_MD_FILES if child in f.name
                            ]
                            # Path(DOCS_TEMPLATE_PATH / category / f'{child}.md').touch()
                            if export_path == []:
                                print(f"{child} not found in export_md")
                                Path(
                                    DOCS_TEMPLATE_PATH / category / page / f"{child}.md"
                                ).touch()
                            else:
                                print(f"Copying {child} from export_md")
                                print(
                                    str(export_path[0]),
                                    DOCS_TEMPLATE_PATH
                                    / category
                                    / page
                                    / f"{child}.md",
                                )
                                shutil.copy(
                                    str(export_path[0]),
                                    DOCS_TEMPLATE_PATH
                                    / category
                                    / page
                                    / f"{child}.md",
                                )
                    if child in readme_config.select_fields:
                        Path(
                            DOCS_TEMPLATE_PATH / category / page / f"{child}.md"
                        ).unlink(missing_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"

    ROOT_PATH = Path(__file__).parent.resolve() / ".."
    README_VERSION_FILE = open(ROOT_PATH / "__version__").read().strip()

    parser.add_argument("-d", "--debug", help="Run debug mode", action="store_true")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument(
        "-pn",
        "--method",
        default="update",
        choices=["build", "build-condensed", "update"],
        help="Method",
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
