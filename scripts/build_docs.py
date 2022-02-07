
#!/usr/bin/env python3

import os
from pathlib import Path
import re

import json

from typing import List, Dict, Optional
from typing_extensions import Literal

import argparse
import logging


RDMD_SNIPPET_LANGUAGES = {
    'python': 'Python (SDK)',
    'bash': 'Bash',
    'json': 'JSON',
}


###############################################################################
# Helper Functions
###############################################################################

def load_snippet(
    snippet_path: str,
    ext: Literal['md', 'ipynb'],
    params: Optional[Dict]=None
):
    '''
    Loads given snippet from the given path in a given format
    '''
    try:
        with open(snippet_path, 'r') as f:
            if ext == 'ipynb':
                text = f.readlines()
            elif ext == 'md':
                text = f.read()
    except Exception as e:
        raise FileNotFoundError (f'File not found: {snippet_path}')

    if ext == 'ipynb':
        snippet = text[1:]
    elif ext == 'md':
        snippet = text.split('\n')
    if params:
        for i, line in enumerate(snippet):
            for m in re.finditer('<<(.*)>>', line):
                for k, v in params.items():
                    if k in m.group():
                        if isinstance(v, list):
                            v = str(v)
                            if isinstance(v[0], dict): ### List[dict]
                                v =  json.dumps(v)
                        line = line.replace(f'<<{k}>>', v )
            snippet[i] = line
    if ext == 'md':
        language = snippet[0].split(' ')[0]
        snippet[0] = f"```{language} {RDMD_SNIPPET_LANGUAGES[language]}"
        snippet.append("```")
        snippet.append("```"+language)
        snippet.append("```")
    return snippet


def generate_ipynb_file(
        input_fname: str,
        output_fname: str,
        snippet_paths: List[Path],
        snippet_params=Dict
    ):
    '''
    Given a list of snippet paths, generate a notebook `output_fname` with the given `input_fname`
    '''
    logging.info(f'\tInput file: {input_fname}')
    notebook_json = json.loads(open(input_fname).read())

    for cell in notebook_json['cells']:
        if bool(re.search('@@@\+.*@@@', str(cell["source"]))):
            for i, cell_source in enumerate(cell['source']):
                if '@@@+' in cell_source:
                    snippet_strs = cell_source.replace('@@@+', '').replace('@@@', '').strip().split(';')
                    logging.debug(f'Snippet strs: {snippet_strs}')
                    snippet = []
                    for snippet_str in snippet_strs:
                        snippet_str = snippet_str.strip()
                        logging.debug(f'Snippet str {snippet_str}')
                        snippet += generate_snippet(snippet_str, snippet_paths, snippet_params, ext='ipynb')
                        snippet += ['\n']
                    cell['source'][i] = ''.join(snippet)
                    print(''.join(snippet))

        elif bool(re.search('@@@.*@@@', str(cell["source"]))):
            for i, cell_source in enumerate(cell['source']):
                if '@@@' in cell_source:
                    snippet_str = cell_source.split('@@@')[1].strip()
                    snippet_name = snippet_str.split(',')[0]
                    logging.debug(f'\tSnippet name: {snippet_name}')

                    snippet = generate_snippet(snippet_str, snippet_paths, snippet_params, ext='ipynb')
                    cell['source'][i] = ''.join(snippet)
                    print(''.join(snippet))

    logging.info(f'\tOutput file: {output_fname}')
    json.dump(notebook_json, fp=open(output_fname, 'w'), indent=4)


def generate_snippet(
    snippet_str: str,
    snippet_paths: List,
    snippet_params: Dict,
    ext: Literal['md', 'ipynb']
):
    '''
    Load the corresponding snippet with given parameters depending on the extension type
    Loads snippets in order from root to inner folder - will overwrite the snippets with same name
    '''
    logging.debug(f'\tSnippet paths: {snippet_paths}')
    snippet = []
    for snippet_path in snippet_paths:
        available_snippets = {f: f'{Path(root).joinpath(f)}' for root, _, files in os.walk(snippet_path) for f in files }
        snippet_name = snippet_str.split(',')[0].strip()

        if snippet_name in available_snippets.keys():
            logging.debug(f'\tSnippets: {list(available_snippets.keys())}')
            logging.debug(f'\tSnippet name: {snippet_name}')
            params=None
            if len(snippet_str.split(',')) > 1:
                param_str = snippet_str.split(',')[1:]
                # logging.debug(dict(tuple(i.spl it('=')) for i in param_str.split()))
                # logging.debug(f"\t{param_str}")
                if len(param_str) == 0:
                    raise ValueError(f'You are missing a comma separator. \n \
                        Please make sure snippet reference is of format @@@ SNIPPET_NAME, PARAM_REF_1=PARAM_REF_VALUE_1,  PARAM_REF_2=PARAM_REF_VALUE_2 @@@.')
                params_ref = dict(tuple(s.strip().replace('==', '=').split('=')) for s in param_str)
                logging.debug(f"\tParams ref: {params_ref}")

                params = {}
                for k, v in params_ref.items():
                    if snippet_params.get(params_ref[k]):
                        params[k] = snippet_params[params_ref[k]]
                    else:
                        params[k] = v
                logging.debug(f'\tParams: {params}')

            # regexes = {f".*{s}.*": s for s in available_snippets}
            # snippet_name = [regexes[r] for r in regexes.keys() if re.match(r, snippet_name)][0]
            snippet_fpath = available_snippets[snippet_name]
            logging.debug(f'\tLoading snippet: {snippet_fpath}')
            if ext == 'ipynb':
                snippet = load_snippet(snippet_fpath, params=params, ext='ipynb')
            elif ext == 'md':
                snippet = load_snippet(snippet_fpath, params=params, ext='md')

    if not snippet:
        raise ValueError(f'{snippet_str} was not found in {snippet_paths}')

    return snippet


def generate_md_file(
        input_fname: str,
        output_fname: str,
        snippet_paths: List[Path],
        snippet_params: Dict
    ):
    '''
    Given a list of snippet paths, generate a file `output_fname` with the given `input_fname`
    '''
    logging.info(f'\tInput file: {input_fname}')
    with open(input_fname) as f:
        md_file = f.read()

    md_lines = list()
    for line in md_file.split('\n'):
        ## Concatenated snippets
        if  bool(re.search('@@@\+.*@@@', line)) and (not bool(re.search('.*<--.*-->.*', line))):
            snippet_strs = line.replace('@@@+', '').replace('@@@', '').strip().split(';')
            logging.debug(f'Snippet strs: {snippet_strs}')
            snippet = []
            for i, snippet_str in enumerate(snippet_strs):
                snippet_str = snippet_str.strip()
                logging.debug(f'Snippet str {snippet_str}')
                _snippet = generate_snippet(snippet_str, snippet_paths, snippet_params, ext='md')

                ## Removing snippet code wrapper union
                if i != 0:
                    _snippet[0] = ''
                if i != len(snippet_strs) -1:
                    _snippet = _snippet[:-3]
                snippet += _snippet
                print('\n'.join(snippet))

            [md_lines.append(x) for x in snippet]

        elif bool(re.search('@@@.*@@@', line)) and (not bool(re.search('.*<--.*-->.*', line))):
            snippet_str = line.split('@@@')[1].strip()
            snippet = generate_snippet(snippet_str, snippet_paths, snippet_params, ext='md')
            logging.debug('\n'.join(snippet))

            [md_lines.append(x) for x in snippet]
        else:
            md_lines.append(line)

    with open(output_fname, "w") as fout:
        for element in md_lines:
            fout.write(element + "\n")
        logging.info(f'\tOutput file: {output_fname}')


###############################################################################
# Generating ReadMe Markdown files and notebooks with automated snippets
###############################################################################

def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=logging_level)
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)

    ### For files in sections and subsections
    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"

    GENERAL_SNIPPETS = Path(DOCS_TEMPLATE_PATH) / "_snippets"
    SNIPPET_PARAMS_FPATH = Path(DOCS_TEMPLATE_PATH) / "_snippet_params.json"
    SNIPPET_PARAMS = json.loads(open(str(SNIPPET_PARAMS_FPATH), 'r').read())

    # # For testing/debugging
    # sample_input_fname = DOCS_TEMPLATE_PATH / 'GETTING_STARTED' /"welcome.md"
    # sample_output_fname = str(sample_input_fname).replace('docs_template', 'docs')
    # snippet_paths = [GENERAL_SNIPPETS] + [Path(DOCS_TEMPLATE_PATH) / 'GETTING_STARTED' / '_snippets']
    # generate_md_file(
    #     input_fname=sample_input_fname,
    #     output_fname=sample_output_fname,
    #     snippet_paths=snippet_paths,
    #     snippet_params=SNIPPET_PARAMS
    #     )

    # sample_input_ipynb_fname = DOCS_TEMPLATE_PATH / 'GETTING_STARTED' / '_notebooks' / "Intro_to_Relevance_AI.ipynb"
    # sample_output_ipynb_fname = str(sample_input_ipynb_fname).replace('docs_template', 'docs')
    # snippet_paths = [GENERAL_SNIPPETS] + [Path(DOCS_TEMPLATE_PATH) / 'GETTING_STARTED' / '_snippets']
    # generate_ipynb_file(
    #     input_fname=sample_input_ipynb_fname,
    #     output_fname=sample_output_ipynb_fname,
    #     snippet_paths=snippet_paths,
    #     snippet_params=SNIPPET_PARAMS
    #     )

    logging.info(f'Generating files from `docs_template` to `docs` ...')
    snippet_paths = []
    for root, dirs, files in os.walk(DOCS_TEMPLATE_PATH, topdown=True):
        root_name = root.split('/')[-1]
        if root_name[0] != '_' and files and (not '_snippets' in root):
            logging.debug(f'\tRoot {root}')
            logging.debug(f'\tDirs {dirs}')
            logging.debug(f'\tFiles {files}')

            ### Loading snippet_paths
            SNIPPETS_DIR = Path(root).joinpath("_snippets")
            if '_snippets' in dirs:
                snippet_paths += [SNIPPETS_DIR]

            logging.debug(f'\tSnippet paths {snippet_paths}')

            ## Generating for md
            MD_FILES = Path(root).glob('*.md')
            for input_fname in MD_FILES:
                output_fname = str(input_fname).replace('docs_template', 'docs')

                logging.debug('---')
                generate_md_file(
                    input_fname=input_fname,
                    output_fname=output_fname,
                    snippet_paths=snippet_paths,
                    snippet_params=SNIPPET_PARAMS
                )

            ### Generating for ipynb
            NOTEBOOK_FILES = Path(root).glob('*/*.ipynb')
            for input_fname in NOTEBOOK_FILES:
                output_fname = str(input_fname).replace('docs_template', 'docs')

                logging.debug('---')
                generate_ipynb_file(
                    input_fname=input_fname,
                    output_fname=output_fname,
                    snippet_paths=snippet_paths,
                    snippet_params=SNIPPET_PARAMS
                )

            logging.debug('---------')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = 'RelevanceAI'
    ROOT_PATH = Path(__file__).parent.resolve() / '..'
    README_VERSION_FILE = open(ROOT_PATH/ '__version__').read()

    parser.add_argument("-d", "--debug", help="Run debug mode", action='store_true')
    parser.add_argument("-p", "--path", default=ROOT_PATH, type=str, help="Path of root folder")
    parser.add_argument("-pn", "--package-name", default=PACKAGE_NAME, type=str, help="Package Name")
    parser.add_argument("-v", "--version", default=README_VERSION_FILE, help="Package Version")
    parser.add_argument("-f", "--files", default=None, help="Files to generate")
    args = parser.parse_args()

    main(args)
