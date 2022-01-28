
#!/usr/bin/env python3

import os
from pathlib import Path

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
    #load string
    with open(snippet_path) as f:
        text = f.read()

    snippet = text.split('\n')
    language = snippet[0].split(' ')[0]
    snippet[0] = "```"+snippet[0] 
    snippet.append("```")
    snippet.append("```"+language)
    snippet.append("```")
    return snippet


def generate_file(filename, snippet_path, output_path):
    #load sample
    with open(filename) as f:
        md_corpus = f.read()

    #generates a new file
    md_sentences = list() 
    for sentence in md_corpus.split('\n'):
        if sentence.find('@@@') != -1:
            #load the corresponding snippet and merge it in the code
            snippet_name = (sentence[3:])
            snippet = load_snippet(snippet_path)
            #[print(x) for x in snippet] #Verbose
            [md_sentences.append(x) for x in snippet]
        else:
            md_sentences.append(sentence)

    textfile = open(output_path+"generated_2.md", "w")
    for element in md_sentences:
        textfile.write(element + "\n")
    textfile.close()


###############################################################################
# Generating ReadMe Markdown files with automated snippets
###############################################################################

### For files in sections and subsections

DOCS_PATH = Path(args.path) / "docs"


print(DOCS_PATH)

for f in Path(DOCS_PATH).glob('**/*.md'):
    SNIPPET_PATH = Path(args.path) / "_snippets" 
    print(f)
    # print(f)
    # generate_file(f, DOCS_PATH, DOCS_PATH)

# generate_file(args.path+'_sample_2.md', args.path)