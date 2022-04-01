#!/usr/bin/env python3

from pathlib import Path

import logging
import argparse
import json
import yaml

from rdme_sync.utils.files import get_files, file_find_replace


def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    README_VERSION = args.version

    ###############################################################################
    # Updating semver ref in installation
    ###############################################################################

    logging.info(f"Updating semver ref to {README_VERSION} for all installation files")

    SEMVER_SENT = f".*v(\d+\.\d+(?:\.\d+)?).*"
    SEMVER_STR = f"v(\d+\.\d+(?:\.\d+)?)"
    SEMVER_REPLACE_STR = (
        README_VERSION if README_VERSION[0] == "v" else f"v{README_VERSION}"
    )

    installation_guide = [
        Path(args.path) / "docs_template" / "getting-started" / "installation.md"
    ] + [Path(args.path) / "docs" / "getting-started" / "installation.md"]

    for f in installation_guide:
        logging.debug(f"\tUpdating {f} to {README_VERSION} ...")
        file_find_replace(f, SEMVER_SENT, SEMVER_STR, SEMVER_REPLACE_STR)

    ###############################################################################
    # Updating version ref in snippet config
    ###############################################################################

    logging.info(f"Updating version ref to {README_VERSION} in snippet config")
    SNIPPET_PARAMS_FPATH = Path(DOCS_TEMPLATE_PATH) / "_snippet_params.json"
    logging.debug(f"\tUpdating {SNIPPET_PARAMS_FPATH} to {README_VERSION} ...")
    SNIPPET_PARAMS = json.loads(open(str(SNIPPET_PARAMS_FPATH), "r").read())

    SNIPPET_PARAMS["RELEVANCEAI_SDK_VERSION"] = args.version
    json.dump(SNIPPET_PARAMS, open(SNIPPET_PARAMS_FPATH, "w"), separators=(",\n", ": "))

    ###############################################################################
    # Updating version ref in readme config
    ###############################################################################

    logging.info(f"Updating version ref to {README_VERSION} in readme config")

    config_paths = Path(ROOT_PATH / "config").glob("**/*.yaml")
    for fpath in config_paths:
        logging.debug(f"\tUpdating {fpath} to {README_VERSION} ...")
        config = yaml.safe_load(open(fpath, "r"))

        config["version"] = (
            args.version if args.version[0] == "v" else f"v{args.version}"
        )
        with open(fpath, "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = "RelevanceAI"

    ROOT_PATH = Path(__file__).parent.resolve() / ".." / ".." / ".."
    README_VERSION_FILE = f"v{open(ROOT_PATH / '__version__').read().strip()}"

    parser.add_argument("-d", "--debug", help="Run debug mode", action="store_true")
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument(
        "-pn", "--package-name", default=PACKAGE_NAME, help="Package Name"
    )
    parser.add_argument(
        "-v", "--version", default=README_VERSION_FILE, help="Package Version"
    )
    args = parser.parse_args()

    main(args)
