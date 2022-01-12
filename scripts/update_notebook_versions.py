#!/usr/bin/env python3

from pathlib import Path
import re
import subprocess
import sys



def check_latest_version(name):
    latest_version = str(subprocess.run([sys.executable, '-m', 'pip', 'install', '{}==random'.format(name)], capture_output=True, text=True))
    latest_version = latest_version[latest_version.find('(from versions:')+15:]
    latest_version = latest_version[:latest_version.find(')')]
    latest_version = latest_version.replace(' ','').split(',')[-1]

    current_version = str(subprocess.run([sys.executable, '-m', 'pip', 'show', '{}'.format(name)], capture_output=True, text=True))
    current_version = current_version[current_version.find('Version:')+8:]
    current_version = current_version[:current_version.find('\\n')].replace(' ','') 

    if latest_version == current_version:
        return True
    else:
        return False


def get_latest_version(name):
    latest_version = str(subprocess.run([sys.executable, '-m', 'pip', 'install', '{}==random'.format(name)], capture_output=True, text=True))
    latest_version = latest_version[latest_version.find('(from versions:')+15:]
    latest_version = latest_version[:latest_version.find(')')]
    latest_version = latest_version.replace(' ','').split(',')[-1]
    return latest_version




DOCS_PATH = Path.cwd() / 'docs'
RELEVANCEAI_SDK_VERSION = get_latest_version('RelevanceAI')
PIP_INSTALL_REGEX=f'"!pip install .* RelevanceAI==.*"'
PIP_INSTALL_STRING=f'"!pip install -U RelevanceAI=={RELEVANCEAI_SDK_VERSION}"'

notebook = Path.cwd() / 'examples' / 'Intro_to_Relevance_AI.ipynb'

with open(notebook, 'r') as f:
    lines = f.readlines()

for notebook in Path(DOCS_PATH).glob('**/*.ipynb'):
    print(notebook)

    with open(notebook, 'w') as f:

        for line in lines:            
            if bool(re.search(PIP_INSTALL_REGEX, line)):
                install_string = re.findall(PIP_INSTALL_REGEX, line)[0]
                print(f'Replacing {install_string} with {PIP_INSTALL_STRING}')
                
                line = line.replace(install_string, PIP_INSTALL_STRING)
                
            f.write(line)