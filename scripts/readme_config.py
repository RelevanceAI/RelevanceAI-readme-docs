
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

from readme_api import ReadMeAPI


def get_files(path: Union[Path, str], ext: Literal['md', 'ipynb']):
	return Path(path).glob(f"**/*.{ext}")

class ReadMeConfig:
    def __init__(self, fpath: str = None, version: str = None, ):
        self.version = f'v{version}' if version[0] != 'v' else version
        self.fpath = fpath
        self.readme = ReadMeAPI(self.version)
        self.select_fields = ['slug', 'title', 'excerpt', 'hidden', 'createdAt', 'updatedAt', 'parentDoc', 'order']
        self.api_categories = ['relevance-ai-endpoints']
        self.sdk_categories = ['python-sdk']

    # def _build_config(self, config):
    #     if

    def build(self, fpath=None, condensed=False, select_fields: List[str] = None):
        if fpath: self.fpath = fpath
        if select_fields: self.select_fields = select_fields

        category_slugs = [c['slug'] for c in self.readme.get_categories(select_fields=['slug'])]

        category_detail = {}
        for cs in category_slugs:
            if not any([f in cs for f in self.api_categories+self.sdk_categories]):
                category_detail[cs] = { ps['slug']: [c['slug'] for c in ps['children']]
                        for ps in self.readme.get_docs_for_category(category_slug=cs, select_fields=['slug', 'children'])}

        if not condensed:
            for category, pages in category_detail.items():
                page_details = {}
                for page, children in pages.items():
                    page_details[page] = self.readme.get_doc(page_slug=page, select_fields=self.select_fields)[0]
                    for child in children:
                        page_details[page][child] = self.readme.get_doc(page_slug=child, select_fields=self.select_fields)
                category_detail[category] = page_details

        config = {'version': self.version}
        config['categories'] = category_detail

        pprint(config)
        with open(self.fpath, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)

    def update(self):
        return NotImplementedError

def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    #logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
    logging.basicConfig(level=logging_level)

    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"
    README_VERSION = args.version
    README_CONFIG_FPATH =  Path(__file__).parent.resolve() / '..' / 'readme-config.yml'

    config = ReadMeConfig(version=README_VERSION, fpath=README_CONFIG_FPATH)

    if args.method == 'build':
        print(f'Building {README_VERSION} config ...')
        config.build()
    elif args.method == 'build-condensed':
        print(f'Building {README_VERSION} condensed config ...')
        fpath = str(README_CONFIG_FPATH).replace('readme-config', 'readme-config-condensed')
        config.build(fpath, condensed=True)
    elif args.method =='update':
        config.update()


    ###############################################################################
    # Updating semver ref in installation
    ###############################################################################
    # SNIPPET_PARAMS_FPATH = Path(DOCS_TEMPLATE_PATH) / "_snippet_params.json"
    # SNIPPET_PARAMS = json.loads(open(str(SNIPPET_PARAMS_FPATH), 'r').read())

    # if args.files:
    #     MD_FILES = [f for f in args.files if f.endswith('.md')]
    #     NOTEBOOKS = [f for f in args.files  if f.endswith('.ipynb')]
    # else:
    #     MD_FILES = Path(DOCS_TEMPLATE_PATH).glob('**/**/*.md')
    #     NOTEBOOKS = Path(DOCS_TEMPLATE_PATH).glob('**/**/*.ipynb')

    # for input_fname in MD_FILES:
    #     input_fname = Path(input_fname)
        # output_fname = Path(str(input_fname).replace('docs_template', 'docs'))
        # snippet_paths = load_snippet_paths(base_dir=DOCS_TEMPLATE_PATH, fdir=input_fname.parent)
        # logging.debug('---')
        # generate_md_file(
        #     input_fname=input_fname,
        #     output_fname=output_fname,
        #     snippet_paths=snippet_paths,
        #     snippet_params=SNIPPET_PARAMS
        #     )


    ###############################################################################
    # Updating version ref in snippet config
    ###############################################################################

    # logging.info(f'Updating version ref to {README_VERSION} in snippet config')
    # SNIPPET_PARAMS_FPATH = Path(DOCS_TEMPLATE_PATH) / "_snippet_params.json"
    # print(SNIPPET_PARAMS_FPATH)
    # SNIPPET_PARAMS = json.loads(open(str(SNIPPET_PARAMS_FPATH), 'r').read())

    # SNIPPET_PARAMS['RELEVANCEAI_SDK_VERSION'] = args.version
    # json.dump(SNIPPET_PARAMS, open(SNIPPET_PARAMS_FPATH, 'w'), separators=(',\n', ': '))





if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = 'RelevanceAI'

    ROOT_PATH = Path(__file__).parent.resolve() / '..'
    README_VERSION_FILE = open(ROOT_PATH / '__version__').read().strip()

    parser.add_argument("-d", "--debug", help="Run debug mode", action='store_true')
    parser.add_argument("-p", "--path", default=ROOT_PATH, help="Path of root folder")
    parser.add_argument("-pn", "--method", default='update', choices=['build', 'build-condensed', 'update'], help="Method")
    parser.add_argument("-v", "--version", default=README_VERSION_FILE, help="Package Version")
    args = parser.parse_args()

    main(args)
