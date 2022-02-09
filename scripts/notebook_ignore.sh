#!/usr/bin/env bash

set -a
set -euo pipefail

DEBUG_MODE=${1:-false}

if [ "$DEBUG_MODE" = true ]; then
  set -x
fi

NOTEBOOK_IGNORE=$(cat scripts/notebook_ignore.txt)
NOTEBOOKS=$(find docs -type f -name "*.ipynb" | jq -Rsc '. / "\n" - [""]')

 for n in NOTEBOOKS; do
 	if [[ $NOTEBOOK_IGNORE =~ $n ]]; then
	 NOTEBOOKS=$NOTEBOOKS[@]/$n
	fi
 done

echo $NOTEBOOKS