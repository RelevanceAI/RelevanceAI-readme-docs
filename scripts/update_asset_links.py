
#!/usr/bin/env python3

import os
import re
from pathlib import Path
# import fileinput
import itertools
from telnetlib import DO
from typing import List, Tuple

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=Path.cwd(), help="Path of root folder")
# parser.add_argument("-n", "--package-name", default="RelevanceAI", help='Package Name')
# parser.add_argument("-v", "--version", default=None, help='Package Version')
args = parser.parse_args()


def file_find_replace(fname, find_sent_regex, find_str_regex, replace_str):

    with open(fname, "r") as f:
        lines = f.readlines()

    with open(fname, "w") as f:
        for i, line in enumerate(lines):
            if bool(re.search(find_sent_regex, line)):
                find_sent = re.search(find_sent_regex, line)
                if find_sent:
                    find_sent = find_sent.group()
                    print(f"\nFound: {find_sent}\n")

                    # if find_str == replace_str: continue
                    print(f"Find string: {find_str_regex}")
                    find_replace_str = re.search(find_str_regex, find_sent)
                    if find_replace_str:
                        find_replace_str = find_replace_str.group()
                        print(f"Found: {find_replace_str}\n")

                        print(f"Replace: \n{find_replace_str}\n{replace_str}\n")
                        line = line.replace(find_replace_str, replace_str)

                        print(f"Updated:")
                        print(line.strip())
                    else:
                        print(f"Not found: {find_replace_str}\n")
                else:
                    print(f"Not found: {find_sent_regex}\n")

            f.write(line)

    

def get_files(path, ext):
	return Path(path).glob(f"**/*.{ext}")
	

def get_readme_version_from_file(fpath):
    with open(fpath, "r") as f:
        version = f.read()
    return version



def main(args):
    DOCS_PATH = Path(args.path) / "docs"
    README_VERSION = get_readme_version_from_file(Path.cwd() / "__version__")

    ## Updating asset links
    md_files = get_files(DOCS_PATH, ext='md')
    notebooks = get_files(DOCS_PATH, ext='ipynb')

    files = itertools.chain(md_files, notebooks)

    for f in files:
        ASSET_SENTENCE_REGEX = '.*/RelevanceAI-readme-docs/blob/.*'
        ASSET_STR_REGEX = '/RelevanceAI-readme-docs/blob/.*?/'
        ASSET_REPLACE_STR = f'/RelevanceAI-readme-docs/blob/v{README_VERSION}/'

        file_find_replace(f, ASSET_SENTENCE_REGEX, ASSET_STR_REGEX, ASSET_REPLACE_STR)
    
    ## Updating semver
    installation_snippet = Path(DOCS_PATH) / "_snippets" / "relevanceai_installation"
    installation_guide = Path(DOCS_PATH) / "GETTING_STARTED" / "installation.md"
    SEMVER_SENT = f'.*(\d+\.\d+(?:\.\d+)?).*'
    SEMVER_STR = f"(\d+\.\d+(?:\.\d+)?)"
    SEMVER_REPLACE_STR = f"{README_VERSION}"

    files = [installation_snippet, installation_guide] + list(itertools.chain(md_files, notebooks))

    for f in files:
        file_find_replace(f, SEMVER_SENT, SEMVER_STR, SEMVER_REPLACE_STR)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--path", default=Path.cwd(), help="Path of root folder")
    parser.add_argument("-n", "--package-name", default="RelevanceAI", help="Package Name")
    parser.add_argument("-v", "--version", default=None, help="Package Version")
    args = parser.parse_args()

    main(args)
