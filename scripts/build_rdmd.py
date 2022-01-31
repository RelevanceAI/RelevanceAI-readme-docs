
#!/usr/bin/env python3

import os
from pathlib import Path
import fileinput
from typing import List, Tuple

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=Path.cwd(), help="Path of root folder")
# parser.add_argument("-n", "--package-name", default="RelevanceAI", help='Package Name')
# parser.add_argument("-v", "--version", default=None, help='Package Version')
args = parser.parse_args()


###############################################################################
# Helper Functions
###############################################################################


def load_snippet(snippet_path):
    '''
    Loads a given snippet from the given path
    '''
    #load string
    try:
        with open(snippet_path, 'r') as f:
            text = f.read()
    except Exception as e:
        raise FileNotFoundError (f'File not found: {snippet_path}')

    snippet = text.split('\n')
    
    # language = snippet[0].split(' ')[0]
    # snippet[0] = "```"+snippet[0] 
    # snippet.append("```")
    # snippet.append("```"+language)
    # snippet.append("```")
    return snippet


def generate_file(input_fname: str, output_fname: str, snippet_paths: List[Path], ext='md'):
    '''
    Given a list of snippet paths, generate a file `output_fname` with the given `input_fname`
    '''
    ext = ext.replace('.', '') 
    # load sample
    print(f'Input file: {input_fname}')
    with open(input_fname) as f:
        md_file = f.read()
    
    # generates a new file
    md_sentences = list() 
    for sentence in md_file.split('\n'):
        if sentence.find('@@@') != -1:
            # load the corresponding snippet and merge it in the code
            # Loads snippets in order from root to inner folder - will overwrite the snippets with same name
            for snippet_path in snippet_paths:
                print(f'Snippet path: {snippet_path}')
                available_snippets = [s.split(f'.{ext}')[0] for s in os.listdir(snippet_path)]

                snippet_name = sentence.split('@@@')[1].split(' ')[0]

                if available_snippets and (snippet_name in available_snippets):
                    # print(snippet_name)
                    snippet_fpath = Path(snippet_path) / f'{snippet_name}.{ext}'
                    # print(snippet_fpath)
                    snippet = load_snippet(snippet_fpath)

                    print(f'Generating {snippet_path}/{snippet_name}')
                    # print(snippet)
                    #[print(x) for x in snippet] # Verbose
                # else:
                #     print(f'No snippets found for {snippet_name} in {snippet_path}')
            [md_sentences.append(x) for x in snippet]
        else:
            md_sentences.append(sentence)

    textfile = open(output_fname, "w")
    for element in md_sentences:
        textfile.write(element + "\n")
    print(f'Output file: {output_fname}')
    textfile.close()


###############################################################################
# Generating ReadMe Markdown files with automated snippets
###############################################################################

### For files in sections and subsections

DOCS_PATH = Path(args.path) / "docs"

# GENERAL_SNIPPETS = Path(DOCS_PATH) / "_snippets"
# sample_input_fname = DOCS_PATH / "_md" / "welcome.md"
# snippet_path = GENERAL_SNIPPETS 
# sample_output_fname = sample_input_fname.parent.parent / sample_input_fname.name

# snippet_paths = [GENERAL_SNIPPETS] + [Path(DOCS_PATH) / 'GETTING_STARTED' / '_snippets']
# generate_file(input_fname=sample_input_fname, 
#             output_fname=sample_output_fname, 
#             snippet_paths=snippet_paths
#             )


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
        if '_md' in dirs and '_snippets' in dirs:
            MD_DIR = Path(root) / "_md"
            print(f'Snippet paths {snippet_paths}')

            for fname in os.listdir(MD_DIR):
                input_fname = MD_DIR / fname
                output_fname = Path(root) / fname

                print(input_fname, output_fname, snippet_paths)
                print('---')

                generate_file(input_fname=input_fname, 
                    output_fname=output_fname, 
                    snippet_paths=snippet_paths
                    )
