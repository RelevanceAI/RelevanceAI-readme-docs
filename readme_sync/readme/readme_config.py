#!/usr/bin/env python3

import os
import re
from pathlib import Path
from typing import Dict, List, Literal, Tuple, Union
import logging
import argparse
import json
import yaml
import shutil
from pprint import pprint

from readme_api import ReadMeAPI


ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".."


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
        self.fpath = fpath
        self.version = version
        self.select_fields = select_fields
        self.readme = ReadMeAPI(self.version)
        self.api_categories = ["relevance-ai-endpoints"]
        self.sdk_categories = ["python-sdk"]
        self.config = yaml.safe_load(open(self.fpath, "r"))

        self.readme_page_slugs = self._load_readme_page_slugs()
        self.docs_categories = self._load_docs_categories()

    def _load_docs_categories(self):
        """Loads list of docs categories slugs"""
        categories = self.config["categories"]
        return [category for category, pages in categories.items()]

    def _load_readme_page_slugs(self):
        """Loads list of all readme page slugs"""
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
        """Builds readme config dict and outputs to readme-config file

        Parameters
        ----------
        fpath : Config filepath
            Overrides instance fpath if set
        condensed: bool
            If True, builds a condensed version of the readme-config file as well
        select_fields : List[str]
            select_fields: List
            Fields to include in the search results, empty array/list means all fields

        """
        if fpath:
            self.fpath = fpath
        if select_fields:
            self.select_fields = select_fields

        category_slugs = [
            c["slug"] for c in self.readme.get_categories(select_fields=["slug"])
        ]

        ## Building condensed
        condensed_config = {"version": self.version}
        category_detail = {}
        for cs in category_slugs:
            if not any([f in cs for f in self.api_categories + self.sdk_categories]):
                category_detail[cs] = {
                    ps["slug"]: [c["slug"] for c in ps["children"]]
                    for ps in self.readme.get_docs_for_category(
                        category_slug=cs, select_fields=["slug", "children"]
                    )
                }
        condensed_config["categories"] = category_detail

        if condensed:
            condensed_fpath = str(self.fpath).replace(".yaml", "-condensed.yaml")
            with open(condensed_fpath, "w") as f:
                yaml.dump(condensed_config, f, default_flow_style=False)

        config = condensed_config
        ## Building expanded config (inc children)
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

        config["categories"] = category_detail
        with open(self.fpath, "w") as f:
            yaml.dump(config, f, default_flow_style=False)
        return config

    def create(
        self,
        slug: str,
        select_fields: List[str] = None,
    ):
        """Creates new page in ReadMe if slug does not exist

        Parameters
        ----------
        fpath : Config filepath
            Overrides instance fpath if set
        slug: str
            Page slug to create
        select_fields : List[str]
            select_fields: List
            Fields to include in the search results, empty array/list means all fields

        """

        # category_detail = {}
        # for root, dirs, files in os.walk(self.fpath):
        #     category_path = "/".join(
        #             root.split('docs_template')[-1].split("/")[1:]
        #         )
        #     print(category_path)

        return NotImplementedError


class DocsConfig(Config):
    def __init__(
        self,
        dir_path: str = None,
        fpath: str = None,
        version: str = None,
        select_fields: List[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            fpath=fpath, version=version, select_fields=select_fields, *args, **kwargs
        )
        self.dir_path = dir_path
        self.fpath = fpath
        self.version = version
        self.select_fields = select_fields
        print(self.fpath)
        self.config = yaml.safe_load(open(self.fpath, "r"))

        self.docs_page_slugs = self._load_docs_page_slugs()
        self.docs_categories = self._load_docs_categories()

    def _load_docs_categories(self):
        """Loads list of docs categories slugs"""
        # pprint(self.config["docs_template"])
        return [
            category_name
            for category in self.config["docs_template"]
            if category and isinstance(category, dict)
            for category_name, pages in category.items()
        ]

    def _load_docs_page_slugs(self):
        """Loads list of all docs page slugs"""
        slugs = {}
        return slugs

    def build(
        self,
        dir_path: Path = None,
        fpath: Path = None,
        condensed: bool = False,
        select_fields: List[str] = None,
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

        config = self.dir_to_dict(self.dir_path)

        ## TODO: Merge docs_config and readme_config schema

        ## For now, converting config to ReadMe config format

        # for category in config['docs_template']:
        #     if isinstance(category, dict):
        #         # config[category_name] = {}
        #         for category_name, pages in category.items():
        #             # logging.debug(f'{category_name}, {pages}')
        #             if isinstance(pages[0], dict):
        #                 logging.debug(category_name)
        #                 for page, children in pages[0].items():
        #                     logging.debug(f'{page}, {children}')

        # logging.debug(children)
        # print(config[category_name])
        # config[category_name][page] = self.readme.get_doc(
        #             page_slug=page, select_fields=self.select_fields
        #         )

        #                     for c in children:
        #                         slug = c.split('.md')[0]
        #                         config[category_name][page][slug] = self.readme.get_doc(
        #                             page_slug=c, select_fields=self.select_fields
        #                         )
        # if '_' not in page:
        #     # logging.debug(page, children)
        #     for c in children:
        # logging.debug(c)
        # config[category_name][page][c] = self.readme.get_doc(
        #     page_slug=c, select_fields=self.select_fields
        # )
        # logging.info(json.dumps(config, indent=4))
        # for k, v in category.items():
        #     print(k, v)
        # pprint(category)

        # category_detail = {}
        # for root, dirs, files in os.walk(self.fpath):
        #     root_name = root.split("/")[-1]
        #     # print(root)
        #     if root_name[0] != "_":
        #         category_path = "/".join(
        #             root.split('docs_template')[-1].split("/")[1:]
        #         )
        #         print(dirs)
        #         if category_path and '_' not in category_path:
        #             # logging.info(category_path)
        #             print(category_path.split('/')[1:])
        #             category_detail[category_path.split('/')[0]] = category_path.split('/')[1:]
        # pprint(category_detail)
        #                 # print(c)
        #                 # category_detail[c] = {}
        #             # category_detail
        #             # print(root)
        #             # print(category_path)
        return config

    def dict_to_dir(self, data: dict, path: Path):
        """dict_to_dir expects data to be a dictionary with one top-level key."""

        dest = Path.getcwd() / path
        if isinstance(data, dict):
            for k, v in data.items():
                Path(dest / k).mkdir(parents=True, exist_ok=True)
                self.dict_to_dir(v, Path / str(k))
        elif isinstance(data, list):
            for i in data:
                if isinstance(i, dict):
                    self.dict_to_dir(i, path)
                else:
                    with open(Path(dest) / i, "a"):
                        Path(dest / i).touch()
        if isinstance(data, dict):
            return list(data.keys())[0]

    def dir_to_dict(self, path: Path):
        """dir_to_dict returns a dictionary filetree given a path."""

        directory = {}
        for root, dirs, files in os.walk(path):
            dn = Path(root).name
            directory[dn] = []
            if dirs:
                for d in dirs:
                    directory[dn].append(self.dir_to_dict(path=Path(path) / d))
                for f in files:
                    directory[dn].append(f)
            else:
                directory[dn] = files
            return directory

        # category_slugs = [c['slug'] for c in self.readme.get_categories(select_fields=['slug'])]
        # category_detail = {}
        # for cs in category_slugs:
        #     if not any([f in cs for f in self.api_categories+self.sdk_categories]):
        #         category_detail[cs] = { ps['slug']: [c['slug'] for c in ps['children']]
        #                 for ps in self.readme.get_docs_for_category(category_slug=cs, select_fields=['slug', 'children'])}

        # if not condensed:
        #     for category, pages in category_detail.items():
        #         page_details = {}
        #         for page, children in pages.items():
        #             page_details[page] = self.readme.get_doc(page_slug=page, select_fields=self.select_fields)[0]
        #             for child in children:
        #                 page_details[page][child] = self.readme.get_doc(page_slug=child, select_fields=self.select_fields)
        #         category_detail[category] = page_details

        # config = {'version': self.version}
        # config['categories'] = category_detail

        # with open(self.fpath, 'w') as f:
        #     yaml.dump(config, f, default_flow_style=False)

    def update(
        self,
        slug: str,
        fpath: str = None,
        condensed: str = False,
        select_fields: List[str] = None,
    ):

        return NotImplementedError


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    EXPORT_MD_PATH = Path(args.path) / "export_md" / args.version
    README_VERSION = args.version
    README_CONFIG_FPATH = ROOT_PATH / "config" / "readme-config.yaml"
    DOCS_TEMPLATE_CONFIG_FPATH = ROOT_PATH / "config" / "docs_template.yaml"

    readme_config = ReadMeConfig(version=README_VERSION, fpath=README_CONFIG_FPATH)
    docs_config = DocsConfig(
        version=README_VERSION,
        dir_path=DOCS_TEMPLATE_PATH,
        fpath=DOCS_TEMPLATE_CONFIG_FPATH,
    )

    if args.method == "build":
        logging.info(f"Building {README_VERSION} config ...")
        docs_config.build()
        # readme_config.build()

    elif args.method == "import":
        logging.info(f"Importing {README_VERSION} doc export to {DOCS_PATH}")

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

        # for category, pages in readme_config.config["categories"].items():
        #     if category not in docs_category_slugs:
        #         Path(DOCS_TEMPLATE_PATH / category).mkdir(parents=True)

        for root, dirs, files in os.walk(EXPORT_MD_PATH):
            root_name = root.split("/")[-1]
            logging.debug(f"Root file: {root}")
            if root_name[0] != "_" and root_name != args.version:
                category_path = "/".join(
                    root.split(args.version)[-1]
                    .lower()
                    .replace(" ", "-")
                    .split("/")[1:]
                )
                category_name = root_name.lower().replace(" ", "-")
                if (
                    category_name
                    not in readme_config.api_categories + readme_config.sdk_categories
                ):

                    for d in dirs:
                        docs_dir_path = Path(DOCS_TEMPLATE_PATH / category_name / d)
                        logging.debug(f"Docs Dir Path: {docs_dir_path}")
                        docs_dir_path.mkdir(parents=True, exist_ok=True)

                    for f in files:
                        export_path = Path(root).joinpath(f)

                        docs_path = Path(DOCS_TEMPLATE_PATH).joinpath(category_path, f)
                        docs_path.parent.mkdir(parents=True, exist_ok=True)
                        if not docs_path.exists():
                            logging.info(f"Copying file: {export_path} to {docs_path}")
                            shutil.copy(export_path, docs_path)

    elif args.method == "update":
        logging.info(f"Updating {README_VERSION} docs to {DOCS_PATH}")

        # docs_config = yaml.safe

        # readme_config.update()
        # for category, pages in readme_config.config["categories"].items():
        #     if category not in docs_category_slugs:
        #         Path(DOCS_TEMPLATE_PATH / category).mkdir(parents=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"

    # ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".."
    README_VERSION_FILE = open(ROOT_PATH / "__version__").read().strip()

    parser.add_argument("-d", "--debug", help="Run debug mode", action="store_true")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument(
        "-m",
        "--method",
        default="update",
        choices=["build", "update", "import"],
        help="Method",
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
