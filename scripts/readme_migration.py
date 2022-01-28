#!/usr/bin/env python3

import os
from pathlib import Path

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default='examples', help='Path of folder')
parser.add_argument("-n", "--package-name", default="RelevanceAI", help='Package Name')
parser.add_argument("-v", "--version", default=None, help='Package Version')
args = parser.parse_args()


###############################################################################
# Update Markdown files
###############################################################################

with open(args.path, encoding="utf8") as f:
    md_text = f.read()

# Extract all blocks from code
md_sentences = md_text.split('\n')
index_list = list()

blocks = ['[block:code]', '[block:image]', '[block:callout]', '[block:api-header]', '[block:parameters]']

for index in range(len(md_sentences)):
    for block in blocks:
        # Code
        if md_sentences[index][0:len(block)]==block:
            temp = dict()
            print('a', index, md_sentences[index])
            temp['type'] = md_sentences[index].split(':')[1][:-1]
            temp['index'] = [0, 0]
            temp['index'][0] = index
        # For all the indexes after [block:code] search for the closest [/block]
            for following in range(index+1, len(md_sentences)):
                if md_sentences[following][0:8]=='[/block]':
                    print('b', following, md_sentences[following])
                    temp['index'][1] = following
                    index_list.append(temp)
                    break


