#!/usr/bin/env bash

set -a
set -euox pipefail

# POETRY_VERSION=${1:-1.1.11}
# echo $POETRY_VERSION

## Python Virtualenv
echo 'Updating Python dependencies' 


echo 'Creating virtualenv' 
if [[ ! -d "$PWD/.venv" ]]; then
    python -m venv .venv
    source .venv/bin/activate
fi

pip install --upgrade pip
pip install -r requirements-dev.txt
brew install jq     
npm i

pre-commit install

# curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3 - --version $POETRY_VERSION
# # pip install poetry==$POETRY_VERSION
# # poetry self update
# poetry env use python3.8    ## Default
# poetry install --remove-untracked   ## Installing from poetry.lock - remove old dependencies no longer present in the lock file
# poetry shell


