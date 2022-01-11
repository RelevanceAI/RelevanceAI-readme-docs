#!/usr/bin/env bash

set -a
set -euo pipefail

DEBUG_MODE=${1:-false}

if [ "$DEBUG_MODE" = true ]; then
  set -x
fi



###############################################################################
# Functions to get env vars  
###############################################################################

check_readme_api_key_set(){
    if [[ -z "${RELEVANCEAI_README_API_KEY+x}" ]]; then
        echo "RELEVANCEAI_README_API_KEY is not set. Please export as ENV VAR"
        echo "export RELEVANCEAI_README_API_KEY='xxx'"
        false
    else
        true
    fi
}

###############################################################################
# Setting env vars 
###############################################################################

PIP_PACKAGE_NAME="RelevanceAI"
PACKAGE_JSON_URL="https://pypi.org/pypi/$PIP_PACKAGE_NAME/json"                
RELEVANCEAI_SDK_VERSION=$(curl -L -s "$PACKAGE_JSON_URL" | jq  -r '.releases | keys | .[]' | sort -V | tail -n1)
echo $RELEVANCEAI_SDK_VERSION

if check_readme_api_key_set; then
    README_VERSIONS=$(npx rdme versions --key $RELEVANCEAI_README_API_KEY --raw | jq -r '.[] | .version')
fi

###############################################################################
# Sync all notebooks with latest SDK version
###############################################################################

check_files() {
    while read file; do
        echo Testing $file:
        case $file in
            *.md5) md5sum -c "$file";;
            *.sha256) sha256sum -c "$file";;
            *) echo Not recognized;;
        esac
    done
}

NOTEBOOK_PATHS=$(find . -type f -name '*.ipynb')

NOTEBOOK_PATH='./examples/Intro_to_Relevance_AI.ipynb'
# for NOTEBOOK_PATH in $NOTEBOOK_PATHS; do
echo $NOTEBOOK_PATH
PIP_INSTALL_LATEST='!pip install -U RelevanceAI==$RELEVANCEAI_SDK_VERSION'
JQ_PIP_UPDATE_QUERY='.cells[] | select(.source[] | contains("!pip install -U RelevanceAI==")) .source |= "!pip install -U RelevanceAI==$RELEVANCEAI_SDK_VERSION"'

# jq --arg tag $TAG '.[].ModelECRImageTag = $tag' <<< $NOTEBOOK_PATH > $NOTEBOOK_PATH

# jq $JQ_PIP_UPDATE_QUERY <<< $NOTEBOOK_PATH > $NOTEBOOK_PATH

# cat <<< $(jq $JQ_PIP_UPDATE_QUERY "$NOTEBOOK_PATH") > "$NOTEBOOK_PATH"
# done
