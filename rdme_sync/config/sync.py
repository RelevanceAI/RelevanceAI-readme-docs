#!/usr/bin/env python3

import os
from pathlib import Path

from typing import Dict, List, Literal, Optional, Tuple, Union

import logging
import argparse

import frontmatter
from deepdiff import DeepDiff, grep
import shutil

from rdme_sync.config.config import ReadMeConfig, DocsConfig


ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".."


def get_config_diff(config_1: Dict, config_2: Dict, fpath: Path) -> List[Path]:
    ddiff = DeepDiff(
        config_1,
        config_2,
        ignore_order=True,
        report_repetition=True,
        view="tree",
    )

    paths = []
    if ddiff:
        logging.debug(f"---------")
        logging.debug(f"Deepdiff: \n{ddiff} ...")

        diff_items = [i for k, v in ddiff.items() for i in ddiff[k]]
        logging.debug(f"{len(diff_items)} items added")
        for d in diff_items:
            path = [
                i
                for i in d.path(output_format="list")
                if i not in ["categories"]
                if isinstance(i, str)
            ]
            if str(d.t1) != "not present":
                md_path = d.t1
            elif str(d.t2) != "not present":
                md_path = d.t2
            path += [f"{md_path}.md"]

        DIFF_FPATH = fpath / "/".join(path)
        logging.debug(f"\n{DIFF_FPATH} ...")
        paths.append(DIFF_FPATH)
    return paths


def get_frontmatter(fpath: Path) -> Dict:
    with open(fpath, "r") as f:
        post = frontmatter.load(f)
        logging.debug(f"Loading frontmatter: {post.to_dict()}")
        # dt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        # post["createdAt"] = dt
        # post["updatedAt"] = dt
        # frontmatter.dump(post, fpath, sort_keys=False)
    return post.to_dict()


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    EXPORT_MD_PATH = Path(args.path) / "export_md" / args.version
    README_VERSION = args.version
    README_CONFIG_FPATH = ROOT_PATH / "config" / "readme-config.yaml"
    DOCS_CONDENSED_CONFIG_FPATH = ROOT_PATH / "config" / "docs-config-condensed.yaml"
    DOCS_CONFIG_FPATH = ROOT_PATH / "config" / "docs-config.yaml"

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
        logging.info(f"Updating {README_VERSION} ReadMe to current {DOCS_PATH}")

        ## TODO: Merge docs_config and readme_config schema
        docs_config.build()

        docs_condensed_config = docs_config.condensed_config
        readme_condensed_config = readme_config.condensed_config

        new_fpaths = get_config_diff(
            config_1=docs_condensed_config,
            config_2=readme_condensed_config,
            fpath=DOCS_TEMPLATE_PATH,
        )

        if not new_fpaths:
            logging.debug(f"No new updates in config ...")
        else:
            for path in new_fpaths:
                category = str(path).split("docs_template")[1].split("/")[1]
                parent = path.parent.name

                ## TODO: read slug from fname - in case slug is not the same
                post = get_frontmatter(path)
                child_dict = readme_config.config["categories"][category][parent]

                page_orders = readme_config.get_page_orders(child_dict)
                max_page_order = max(page_orders)

                logging.debug(f"Creating new ReadMe config page... \n\t{path}")
                readme_config.create(
                    title=post["title"],
                    type="basic",
                    category_slug=category,
                    parent_slug=parent,
                    hidden=post["hidden"],
                    order=max_page_order + 1,
                )

            logging.debug(f"Rebuilding config ... ")

            ## TODO: Inserting new item in readme config with new category only instead rebuilding full config
            readme_config.build()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"

    # ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".."
    README_VERSION_FILE = f"v{open(ROOT_PATH / '__version__').read().strip()}"

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
