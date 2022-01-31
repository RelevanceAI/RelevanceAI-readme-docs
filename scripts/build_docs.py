
#!/usr/bin/env python3

import os
from pathlib import Path
import re
import string
import json
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


def load_snippet(snippet_path, ext=Literal['ipynb', 'md']):
    '''
    Loads a given snippet from the given path
    '''

    try:
        with open(snippet_path, 'r') as f:
            text = f.read()
    except Exception as e:
        raise FileNotFoundError (f'File not found: {snippet_path}')
    
    snippet = text.split('\n')
    if ext == 'md':
        ### Reading language from the first line of the snippet
        ### and building rdmd snippet
        language = snippet[0].split(' ')[0]
        snippet[0] = f"```{language} {RDMD_SNIPPET_LANGUAGES[language]}" 
        snippet.append("```")
        snippet.append("```"+language)
        snippet.append("```")
    if ext == 'ipynb':
        ### Skipping first line of snippet (language only relevance for rdmd)
        ### and building ipynb snippet
        snippet = snippet[1:]
        for i, sline in enumerate(snippet):
            sline_formatted = f'{json.dumps(sline)},'
            snippet[i] = sline_formatted
    return snippet


def generate_file(input_fname: str, output_fname: str, snippet_paths: List[Path], ext=Literal['ipynb', 'md']):
    '''
    Given a list of snippet paths, generate a file `output_fname` with the given `input_fname`
    '''
    # load file
    print(f'Input file: {input_fname}')
    with open(input_fname) as f:
        md_file = f.read()

    # generates a new file
    md_lines = list() 
    for line in md_file.split('\n'):
        # print(line)
        if  bool(re.search('@@@.*', line)):
            # print(line)
            # load the corresponding snippet and merge it in the code
            # Loads snippets in order from root to inner folder - will overwrite the snippets with same name
            for snippet_path in snippet_paths:
                available_snippets = os.listdir(snippet_path)
                # print(available_snippets)

                if ext == 'md':
                    snippet_name = line.split('@@@')[1].split(' ')[0]
                if ext == 'ipynb':
                    snippet_name = line.split('@@@')[1].splitlines()[0]
                    snippet_name = re.sub(r'[^\w\s]', '', snippet_name)
                
                print(snippet_name)
                if available_snippets:

                    regexes = {f".*{s}.*": s for s in available_snippets}
                    snippet_name = [regexes[r] for r in regexes.keys() if re.match(r, snippet_name)][0]

                    snippet_fpath = Path(snippet_path) / f'{snippet_name}'
                    print(f'Loading snippet: {snippet_path}/{snippet_name}')
                    snippet = load_snippet(snippet_fpath, ext=ext)
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

    # GENERAL_SNIPPETS = Path(DOCS_PATH) / "_snippets"
    # sample_input_fname = DOCS_PATH / "_md" / "welcome.md"
    # snippet_path = GENERAL_SNIPPETS 
    # sample_output_fname = sample_input_fname.parent.parent / sample_input_fname.name

    # snippet_paths = [GENERAL_SNIPPETS] + [Path(DOCS_PATH) / 'GETTING_STARTED' / '_snippets']
    # generate_file(
    #     input_fname=sample_input_fname, 
    #     output_fname=sample_output_fname, 
    #     snippet_paths=snippet_paths
    #     )

    snippet_paths = []
    for root, dirs, files in os.walk(DOCS_PATH, topdown=True):
        root_name = root.split('/')[-1]
        if root_name[0] != '_':
            print(f'\nRoot {root}')
            print(f'Dirs {dirs}')
            print(f'Files {files}')

            ### Template generation for certain files
            SNIPPETS_DIR = Path(root).joinpath("_snippets")
            if '_snippets' in dirs:
                snippet_paths +=  [SNIPPETS_DIR]

            print(f'Snippet paths {snippet_paths}')

            ### Generating for md
            if '_md' in dirs:
                MD_DIR = Path(root) / "_md"

                for fname in os.listdir(MD_DIR):
                    input_fname = MD_DIR / fname
                    output_fname = Path(root) / fname

                    print('---')

                    generate_file(
                        input_fname=input_fname, 
                        output_fname=output_fname, 
                        snippet_paths=snippet_paths,
                        ext='md'
                    )

            ### Generating for ipynb        
            if '_ipynb' in dirs:
                IPYNB_DIR = Path(root) / "_ipynb"

                for fname in os.listdir(IPYNB_DIR):
                    input_fname = IPYNB_DIR / fname
                    output_fname = Path(root) / '_notebooks'/ fname

                    print('---')

                    generate_file(
                        input_fname=input_fname, 
                        output_fname=output_fname, 
                        snippet_paths=snippet_paths,
                        ext='ipynb'
                    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--path", default=Path.cwd(), help="Path of root folder")
    parser.add_argument("-n", "--package-name", default="RelevanceAI", help="Package Name")
    parser.add_argument("-v", "--version", default=None, help="Package Version")
    args = parser.parse_args()

    main(args)
