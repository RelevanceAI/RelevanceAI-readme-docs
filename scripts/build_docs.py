
#!/usr/bin/env python3

import os
from pathlib import Path
import re

import json
import yaml

from typing import List, Literal, Tuple

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=Path.cwd(), help="Path of root folder")
# parser.add_argument("-n", "--package-name", default="RelevanceAI", help='Package Name')
# parser.add_argument("-v", "--version", default=None, help='Package Version')
args = parser.parse_args()

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
    Loads an ipynb given snippet from the given path
    '''
    try:
        with open(snippet_path, 'r') as f:
            text = f.readlines()
    except Exception as e:
        raise FileNotFoundError (f'File not found: {snippet_path}')
        
    snippet = text[1:]
    return snippet


def load_md_snippet(snippet_path: str):
    '''
    Loads a md given snippet from the given path
    '''
    try:
        with open(snippet_path, 'r') as f:
                text = f.read()
    except Exception as e:
        raise FileNotFoundError (f'File not found: {snippet_path}')

    snippet = text.split('\n')
    ### Reading language from the first line of the snippet
    ### and building rdmd snippet
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
    print(f'Input file: {input_fname}')
    notebook_json = json.loads(open(input_fname).read())

    for cell in notebook_json['cells']:
        if str(cell['source']).find('@@@') != -1:
            # print('Cell Source')
            # print(cell['source'])
            for snippet_path in snippet_paths:
                available_snippets = os.listdir(snippet_path)

                for i, cell_source in enumerate(cell['source']):
                    if '@@@' in cell_source:
                        snippet_cell = cell_source
                
                        snippet_name = snippet_cell.split('@@@')[-1].strip()
                        # print(f'Snippet name: {snippet_name}')
            
                        if snippet_name in available_snippets:
                            # regexes = {f".*{s}.*": s for s in available_snippets}
                            # snippet_name = [regexes[r] for r in regexes.keys() if re.match(r, snippet_name)][0]
                            snippet_fpath = Path(snippet_path) / f'{snippet_name}'
                            print(f'Loading snippet: {snippet_path}/{snippet_name}')

                            snippet = load_ipynb_snippet(snippet_fpath)
                            print(snippet)
                            cell['source'][i] = ''.join(snippet)
        
    json.dump(notebook_json, fp=open(output_fname, 'w'), indent=4)




def generate_md_file(input_fname: str, output_fname: str, snippet_paths: List[Path]):
    '''
    Given a list of snippet paths, generate a file `output_fname` with the given `input_fname`
    '''
    print(f'Input file: {input_fname}')
    with open(input_fname) as f:
        md_file = f.read()

    md_lines = list() 
    for line in md_file.split('\n'):
        if  bool(re.search('@@@.*', line)):
            # load the corresponding snippet and merge it in the code
            # Loads snippets in order from root to inner folder - will overwrite the snippets with same name
            for snippet_path in snippet_paths:
                available_snippets = os.listdir(snippet_path)
                snippet_name = line.split('@@@')[1].split(' ')[0]
                # print(snippet_path)
                # print(available_snippets)
                # print(snippet_name)
                if snippet_name in available_snippets:
                    regexes = {f".*{s}.*": s for s in available_snippets}
                    # print(regexes)
                    snippet_name = [regexes[r] for r in regexes.keys() if re.match(r, snippet_name)][0]
                    # print(snippet_name)
                    snippet_fpath = Path(snippet_path) / f'{snippet_name}'
                    print(f'Loading snippet: {snippet_path}/{snippet_name}')
                    snippet = load_md_snippet(snippet_fpath)
                    # print(snippet)
                    [md_lines.append(x) for x in snippet]
        else:
            md_lines.append(line)

    with open(output_fname, "w") as fout:
        for element in md_lines:
            fout.write(element + "\n")
        print(f'Output file: {output_fname}')


###############################################################################
# Generating ReadMe Markdown files with automated snippets
###############################################################################


def main(args):
    ### For files in sections and subsections
    DOCS_PATH = Path(args.path) / "docs"
    DOCS_TEMPLATE_PATH = Path(args.path) / "docs_template"

    GENERAL_SNIPPETS = Path(DOCS_TEMPLATE_PATH) / "_snippets"
    # sample_input_fname = DOCS_PATH / "_md" / "welcome.md"
    # snippet_path = GENERAL_SNIPPETS 
    # sample_output_fname = sample_input_fname.parent.parent / sample_input_fname.name

    # snippet_paths = [GENERAL_SNIPPETS] + [Path(DOCS_PATH) / 'GETTING_STARTED' / '_snippets']
    # generate_file(
    #     input_fname=sample_input_fname, 
    #     output_fname=sample_output_fname, 
    #     snippet_paths=snippet_paths
    #     )

    snippet_paths = [GENERAL_SNIPPETS]
    for root, dirs, files in os.walk(DOCS_TEMPLATE_PATH, topdown=True):
        root_name = root.split('/')[-1]
        if root_name[0] != '_' and files:
            print(f'\nRoot {root}')
            print(f'Dirs {dirs}')
            print(f'Files {files}')

            ### Template generation for certain files
            SNIPPETS_DIR = Path(root).joinpath("_snippets")
            if '_snippets' in dirs:
                snippet_paths += [SNIPPETS_DIR]

            print(f'Snippet paths {snippet_paths}')

            # MD_FILES = Path(root).glob('**/*.md')
            # for input_fname in MD_FILES:
            #     output_fname = str(input_fname).replace('docs_template', 'docs')

            #     print('---')

            #     generate_md_file(
            #         input_fname=input_fname, 
            #         output_fname=output_fname, 
            #         snippet_paths=snippet_paths
            #     )

            ### Generating for ipynb     
            NOTEBOOK_FILES = Path(root).glob('**/*.ipynb')   
            for input_fname in NOTEBOOK_FILES:    
                output_fname = str(input_fname).replace('docs_template', 'docs')

                print('---')
                generate_ipynb_file(
                    input_fname=input_fname, 
                    output_fname=output_fname, 
                    snippet_paths=snippet_paths,
                )
                
                ### Validating JSON notebook
                data = yaml.full_load(open(output_fname))
                json.dump(data, fp=open(output_fname, 'w'), indent=4)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--path", default=Path.cwd(), help="Path of root folder")
    parser.add_argument("-n", "--package-name", default="RelevanceAI", help="Package Name")
    parser.add_argument("-v", "--version", default=None, help="Package Version")
    args = parser.parse_args()

    main(args)
