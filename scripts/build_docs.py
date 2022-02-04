
#!/usr/bin/env python3

import os
from pathlib import Path
import re

import json
import yaml

from typing import List, Literal, Tuple, Dict, Optional

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

def load_ipynb_snippet(snippet_path: str):
    '''
    Loads given snippet in ipynb format from the given path
    '''
    try:
        with open(snippet_path, 'r') as f:
            text = f.readlines()
    except Exception as e:
        raise FileNotFoundError (f'File not found: {snippet_path}')
        
    snippet = text[1:]
    return snippet


def load_md_snippet(snippet_path: str, params: Optional[Dict]=None):
    '''
    Loads given snippet in md format from the given path
    '''
    try:
        with open(snippet_path, 'r') as f:
                text = f.read()
    except Exception as e:
        raise FileNotFoundError (f'File not found: {snippet_path}')

    snippet = text.split('\n')
    ### Reading language from the first line of the snippet
    ### and building rdmd snippet
    ## Replacing params
    if params:
        for i,  line in enumerate(snippet):
            if re.search('<<(.*)>>', line):
                for k, v in params.items():
                    snippet[i] = line.replace(f'<<{k}>>', v)
                    
    language = snippet[0].split(' ')[0]
    snippet[0] = f"```{language} {RDMD_SNIPPET_LANGUAGES[language]}" 
    snippet.append("```")
    snippet.append("```"+language)
    snippet.append("```")
    return snippet


def generate_ipynb_file(input_fname: str, output_fname: str, snippet_paths: List[Path]):
    '''
    Given a list of snippet paths, generate a file `output_fname` with the given `input_fname`
    '''
    logging.info(f'\tInput file: {input_fname}')
    notebook_json = json.loads(open(input_fname).read())

    for cell in notebook_json['cells']:
        if str(cell['source']).find('@@@') != -1:
            for snippet_path in snippet_paths:
                available_snippets = os.listdir(snippet_path)

                for i, cell_source in enumerate(cell['source']):
                    if '@@@' in cell_source:
                        snippet_cell = cell_source
                
                        snippet_name = snippet_cell.split('@@@')[-1].strip()
                        logging.debug(f'\tSnippet name: {snippet_name}')
            
                        if snippet_name in available_snippets:
                            snippet_fpath = Path(snippet_path) / f'{snippet_name}'
                            logging.debug(f'\tLoading snippet: {snippet_path}/{snippet_name}')

                            snippet = load_ipynb_snippet(snippet_fpath)
                            cell['source'][i] = ''.join(snippet)
    
    logging.info(f'\tOutput file: {output_fname}')    
    json.dump(notebook_json, fp=open(output_fname, 'w'), indent=4)




def generate_md_file(input_fname: str, output_fname: str, snippet_paths: List[Path], snippet_params: Dict):
    '''
    Given a list of snippet paths, generate a file `output_fname` with the given `input_fname`
    '''
    logging.info(f'\tInput file: {input_fname}')
    with open(input_fname) as f:
        md_file = f.read()

    md_lines = list() 
    for line in md_file.split('\n'):
        if  bool(re.search('@@@.*@@@', line)):
            # Load the corresponding snippet and merge it in the code
            # Loads snippets in order from root to inner folder - will overwrite the snippets with same name
            for snippet_path in snippet_paths:
                available_snippets = os.listdir(snippet_path)
                logging.debug(f'\tSnippet paths: {snippet_paths}')
                snippet_str = line.split('@@@')[1].strip()
                snippet_name = snippet_str.split(',')[0]
                logging.debug(f'\tSnippet name: {snippet_name}')

                if snippet_name in available_snippets:
                    logging.debug(f'\tSnippets: {available_snippets}')
                    params=None
                    if len(snippet_str.split(',')) > 1:
                        param_str = snippet_str.split(',')[1].strip()
                        # logging.debug(dict(tuple(i.split('=')) for i in param_str.split()))
                        # logging.debug(f"\t{param_str.split()}")
                        params_ref = dict(tuple(s.replace('==', '=').split('=')) for s in param_str.split())
                        # logging.debug(f"\t{params_ref}")
                        ## Iterating over param_dict and loading with k in snippet_var
                        params = {k: snippet_params[params_ref[k]] for k in params_ref}
                        logging.debug(f'\tParams: {params}') 

                    regexes = {f".*{s}.*": s for s in available_snippets}
                    snippet_name = [regexes[r] for r in regexes.keys() if re.match(r, snippet_name)][0]
                    snippet_fpath = Path(snippet_path) / f'{snippet_name}'
                    logging.debug(f'\tLoading snippet: {snippet_path}/{snippet_name}')
                    snippet = load_md_snippet(snippet_fpath, params)
                    # print(snippet)
                    [md_lines.append(x) for x in snippet]
        else:
            md_lines.append(line)

    with open(output_fname, "w") as fout:
        for element in md_lines:
            fout.write(element + "\n")
        logging.info(f'\tOutput file: {output_fname}')


###############################################################################
# Generating ReadMe Markdown files with automated snippets
###############################################################################

def main(args):
    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=logging_level)
    # logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)

    ### For files in sections and subsections
    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"

    GENERAL_SNIPPETS = Path(DOCS_TEMPLATE_PATH) / "_snippets"
    SNIPPET_PARAMS_FPATH = Path(DOCS_TEMPLATE_PATH) / "_snippet_params.yml"
    SNIPPET_PARAMS = yaml.safe_load(open(str(SNIPPET_PARAMS_FPATH), 'r'))
    
    # ## For testing/debugging
    # sample_input_fname = DOCS_TEMPLATE_PATH / 'GETTING_STARTED' /"welcome.md"
    # sample_output_fname = str(sample_input_fname).replace('docs_template', 'docs')

    # snippet_paths = [GENERAL_SNIPPETS] + [Path(DOCS_TEMPLATE_PATH) / 'GETTING_STARTED' / '_snippets']
    # generate_md_file(
    #     input_fname=sample_input_fname, 
    #     output_fname=sample_output_fname, 
    #     snippet_paths=GENERAL_SNIPPETS,
    #     snippet_params=SNIPPET_PARAMS
    #     )

    logging.info(f'Generating files from `docs_template` to `docs` ...')
    snippet_paths = []
    for root, dirs, files in os.walk(DOCS_TEMPLATE_PATH, topdown=True):
        root_name = root.split('/')[-1]
        if root_name[0] != '_' and files:
            logging.debug(f'\tRoot {root}')
            logging.debug(f'\tDirs {dirs}')
            logging.debug(f'\tFiles {files}')

            ### Loading snippets_paths 
            SNIPPETS_DIR = Path(root).joinpath("_snippets")
            if '_snippets' in dirs:
                snippet_paths += [SNIPPETS_DIR]

            logging.debug(f'\tSnippet paths {snippet_paths}')

            ### Generating for md     
            MD_FILES = Path(root).glob('**/*.md')
            for input_fname in MD_FILES:
                output_fname = str(input_fname).replace('docs_template', 'docs')

                logging.debug('---')
                generate_md_file(
                    input_fname=input_fname, 
                    output_fname=output_fname, 
                    snippet_paths=snippet_paths,
                    snippet_params=SNIPPET_PARAMS
                )

            # ### Generating for ipynb     
            # NOTEBOOK_FILES = Path(root).glob('**/*.ipynb')   
            # for input_fname in NOTEBOOK_FILES:    
            #     output_fname = str(input_fname).replace('docs_template', 'docs')

            #     logging.debug('---')
            #     generate_ipynb_file(
            #         input_fname=input_fname, 
            #         output_fname=output_fname, 
            #         snippet_paths=snippet_paths,
            #     )
                
            #     ### Validating JSON notebook
            #     data = yaml.full_load(open(output_fname))
            #     json.dump(data, fp=open(output_fname, 'w'), indent=4)
            
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    PACKAGE_NAME = 'RelevanceAI'
    ROOT_PATH = Path(__file__).parent.resolve() / '..'
    README_VERSION_FILE = open(ROOT_PATH/ '__version__').read()

    parser.add_argument("-d", "--debug", default=False, help="Run debug mode")
    parser.add_argument("-p", "--path", default=ROOT_PATH, type=str, help="Path of root folder")
    parser.add_argument("-n", "--package-name", default=PACKAGE_NAME, type=str, help="Package Name")
    parser.add_argument("-v", "--version", default=README_VERSION_FILE, help="Package Version")
    args = parser.parse_args()

    main(args)
