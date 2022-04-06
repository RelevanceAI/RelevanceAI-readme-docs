#!/usr/bin/env python3

import json
from multiprocessing.sharedctypes import Value
import os
from pathlib import Path

from typing import Dict, List, Optional, Tuple, Union
from typing_extensions import Literal

import logging
import argparse

import frontmatter
from deepdiff import DeepDiff, grep
import shutil

from rdme_sync.config.readme_config import ReadMeConfig
from rdme_sync.config.docs_config import DocsConfig


ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".." / ".."


def get_diff_fpaths(
    ddiff: DeepDiff, diff_type: Literal["removed", "added"], fpath: Path
):
    """This function returns a list of file paths that have been removed or added

    Parameters
    ----------
    ddiff : DeepDiff
        DeepDiff object
    diff_type : Literal['removed', 'added']
        either 'removed' or 'added'
    fpath : Path
        Path

    """
    ddiff_fpaths = []
    ddiff_items = [i for k, v in ddiff.items() for i in ddiff[k] if diff_type in k]
    logging.debug(f"{len(ddiff_items)} items {diff_type} in this repo...")
    for d in ddiff_items:
        path = [
            i
            for i in d.path(output_format="list")
            if i not in ["categories"]
            if isinstance(i, str)
        ]

        ## Traversing tree diff
        for node in [d.t1, d.t2]:
            if isinstance(node, dict):
                fname = [f"{list(node.keys())[0]}.md"]
                break
            if isinstance(node, list):
                fname = [f"{path[-1]}.md"]
                path.pop()
                break
            if str(node) != "not present":
                fname = [f"{node}.md"]
                break
        path += fname

        if ddiff_items:
            NEW_DOC_FPATH = fpath / "/".join(path)
            logging.debug(f"\n{NEW_DOC_FPATH} ...")
            ddiff_fpaths.append(NEW_DOC_FPATH)
    return ddiff_fpaths


def get_config_diff(docs_config: Dict, readme_config: Dict, root: Path) -> List[Path]:
    """This function compares the configs in the docs and the configs in the readme

    Parameters
    ----------
    docs_config : Dict
        The configuration from the docs.
    readme_config : Dict
        The configuration read from the README.
    root : Path
        Root dir path

    """
    new_doc_fpaths = new_readme_fpaths = []

    ddiff = DeepDiff(
        docs_config,
        readme_config,
        ignore_order=True,
        report_repetition=True,
        view="tree",
    )
    if ddiff:
        logging.debug(f"---------")
        logging.debug(f"Deepdiff: \n{ddiff} ...")

        fpath = root / "docs"
        new_doc_fpaths = get_diff_fpaths(ddiff, "removed", fpath)

        fpath = root / "docs_template"
        new_readme_fpaths = get_diff_fpaths(ddiff, "added", fpath)

    return new_doc_fpaths, new_readme_fpaths


def get_frontmatter(fpath: Path) -> Dict:
    """The function takes a file path and returns a dictionary of the front matter

    Parameters
    ----------
    fpath : Path
        Path

    """
    with open(fpath, "r") as f:
        post = frontmatter.load(f)
        logging.debug(f"Loading frontmatter: {post.to_dict()}")
        # dt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        # post["createdAt"] = dt
        # post["updatedAt"] = dt
        # frontmatter.dump(post, fpath, sort_keys=False)
    return post.to_dict()


def create_readme_page(path: Path, readme_config: ReadMeConfig):
    """This function creates a readme page for the given path

    Parameters
    ----------
    path : Path
        The path to the directory that contains the readme file.
    readme_config : ReadMeConfig
        ReadMeConfig

    """
    category = str(path).split("/docs")[1].split("/")[1]
    parent = path.parent.name
    logging.debug(f"Category: {category} Parent: {parent}")

    post = get_frontmatter(path)

    ## Getting max page order
    if category == parent:
        config_dict = readme_config.config["categories"][category]
        page_orders = readme_config.get_page_orders(config_dict, category=True)
    else:
        config_dict = readme_config.config["categories"][category][parent]
        page_orders = readme_config.get_page_orders(config_dict, category=False)
    max_page_order = max(page_orders)

    ## Creating new page
    args = {
        "title": post["title"],
        "type": "basic",
        "category_slug": category,
        "parent_slug": parent,
        "hidden": post["hidden"],
        "order": max_page_order + 1,
    }
    logging.debug(f"Creating new ReadMe config page... \n\t{path}\n{json.dumps(args)}")
    readme_config.create(**args)


def create_doc_page(path: Path, readme_config: ReadMeConfig):

    doc = readme_config.get_readme_page(page_slug=path.name.replace(".md", ""))
    post_metadata = {
        "title": doc["title"],
        "slug": doc["slug"],
        "hidden": doc["hidden"],
        "excerpt": doc["excerpt"],
        "createdAt": doc["createdAt"],
        "updatedAt": doc["updatedAt"],
    }

    post = frontmatter.loads(doc["body"])
    post.metadata = post_metadata

    logging.debug(
        f"Creating new page in repo ... \n\t{path}\n{json.dumps(post_metadata)}"
    )
    with open(path, "w") as fout:
        fout.write(frontmatter.dumps(post))
        logging.info(f"\tOutput file: {path}")


def create_categories(fpath: Path, readme_config: ReadMeConfig):
    readme_categories = readme_config.config["categories"]
    doc_categories = [
        d.name for d in fpath.iterdir() if d.is_dir() if str(d.name)[0] != "_"
    ]

    for c in readme_categories:
        if c not in doc_categories:
            new_category_fpath = fpath / c
            logging.debug(f"Creating new category: {new_category_fpath}")
            Path(new_category_fpath).mkdir()


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    # DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    EXPORT_MD_PATH = Path(args.path) / "export_md" / args.version
    README_VERSION = args.version
    README_CONFIG_FPATH = ROOT_PATH / "config" / "readme-config.yaml"
    DOCS_CONDENSED_CONFIG_FPATH = (
        ROOT_PATH / "config" / "docs-template-config-condensed.yaml"
    )
    DOCS_CONFIG_FPATH = ROOT_PATH / "config" / "docs-template-config.yaml"

    readme_config = ReadMeConfig(version=README_VERSION, fpath=README_CONFIG_FPATH)
    docs_config = DocsConfig(
        version=README_VERSION,
        dir_path=DOCS_TEMPLATE_PATH,
        fpath=DOCS_CONFIG_FPATH,
    )

    if args.method == "build":
        logging.info(f"Building {README_VERSION} config ...")
        docs_config.build()
        readme_config.build()

    elif args.method == "import_md":
        logging.info(f"Importing {README_VERSION} doc export to {DOCS_TEMPLATE_PATH}")

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
        logging.info(
            f"Updating {README_VERSION} ReadMe to current {DOCS_TEMPLATE_PATH}"
        )

        docs_config.build()

        docs_condensed_config = docs_config.condensed_config
        readme_condensed_config = readme_config.condensed_config

        ## Syncing categories
        logging.debug(f"Creating categories in {DOCS_TEMPLATE_PATH}...")
        create_categories(DOCS_TEMPLATE_PATH, readme_config)

        ## Syncing pages
        new_doc_fpaths, new_readme_fpaths = get_config_diff(
            root=ROOT_PATH,
            docs_config=docs_condensed_config,
            readme_config=readme_condensed_config,
        )

        if not new_doc_fpaths and not new_readme_fpaths:
            logging.debug(f"No new updates in config ...")
        elif new_doc_fpaths:
            for path in new_doc_fpaths:
                create_readme_page(path, readme_config)
        elif new_readme_fpaths:
            for path in new_readme_fpaths:
                create_doc_page(path, readme_config)

        if new_doc_fpaths or new_readme_fpaths:
            logging.debug(f"Rebuilding config ... ")
            docs_config.build()
            readme_config.build()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"

    # ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".."
    README_VERSION_FILE = open(ROOT_PATH / "__version__").read().strip()
    README_VERSION_FILE = (
        f"v{README_VERSION_FILE}"
        if README_VERSION_FILE[0] != "v"
        else README_VERSION_FILE
    )

    parser.add_argument("-d", "--debug", help="Run debug mode", action="store_true")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument(
        "-m",
        "--method",
        default="update",
        choices=["build", "update", "import_md"],
        help="Method",
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
