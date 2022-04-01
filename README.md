# RelevanceAI-readme-docs

This repository updates RelevanceAI's ReadMe Documentation [here](https://docs.relevance.ai/docs).

## 🧠 Documentation

## 🛠️  Requirements

- [Node.JS ^12.x and NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [Python ^3.8.0](https://www.python.org/downloads/release/python-380/) - more Python version to be supported in future
- [rdme NPM client](https://www.npmjs.com/package/rdme/v/6.2.1)

## 🧰 OS Supported

- Linux (Ubuntu 18.04.6 LTS (Bionic Beaver) Debian)

## 👩🏻‍💻 Getting Started with this ReadMe sync repo

The `main` branch is the live branch in ReadMe.
By following instructions below, you will be able to preview/create any given version of the docs at any one time.

```zsh
❯ tree -L 1
.
├── assets                      ## Assets for this README
├── colab_requirements.txt      ## Colab env reqs
├── config                      ## Docs/ReadMe files
├── docs                        ## Generated docs files
├── docs_template               ## Templates and all resources for auto-generation
├── examples                    ## For testing notebook tests
├── export_md                   ## Ignore: Readme Markdown exports
├── migration                   ## Ignore: instructions for the initial migration
├── package.json                ## NPM deps
├── package-lock.json           ## NPM deps lock
├── rdmd.md                     ## Rdmd cheatsheet
├── rdme.md                     ## Rdme cheatsheet
├── README.md
├── requirements.txt            ## Python reqs
├── sync                        ## Automation scripts to build and sync docs
└── __version__
```


1. Install dependencies if first time; note, this repo has both Python and NPM deps
    ```zsh
    ❯ git clone git@github.com:RelevanceAI/RelevanceAI-readme-docs.git
    ❯ python -m venv .venv                 # Create new Python venv
    ❯ source .venv/bin/activate            # Activate new venv
    ❯ make install
    ```

2. Create a new branch for the ReadMe version you'd like to create if not already auto-created upon SDK release eg. v1.0.0
   - Branch off the latest version that you'd like to fork from (if it is not `main`)
    ```zsh
    ❯ git checkout -b v1.0.0
    ❯ git checkout -b v1.0.0-fix-typo
    ```
3. Make your desired changes to the relevant Markdown/notebooks in `docs_templates`. Sync your changes.

These are templates because all the files and notebooks in docs_templates are written in a templated language and are synced with code snippets.

## 👩🏻‍💻  Adding a new guide

4. To add new assets (i):
   - Add new assets to the corresponding `_assets` folder in `docs_template`.
   - Update asset links in `md` files to point to corresponding path.
5. To add new notebooks:
   - Add new notebooks to the corresponding `_notebooks` folder in `docs_template`.
   - Update notebooks to point to the corresponding path.
   - Colab notebook refs are of the form:
  ```zsh
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs/getting-started/_notebooks/Intro_to_Relevance_AI.ipynb)
  ```
  - Please add this badge in top cell of notebook as well so it can be accessed from Github.
6. To add new snippet
   - Add new snippets in the corresponding `_snippets` folder.
   - Snippets are loaded in a nested fashion. Inner most `_snippets` with the same name will override general snippets in [`docs_template/_snippets/`](./docs_template/_snippets/).
   - All snippets in `*.md` and `*.ipynb` files are prefaced with `@@@`.
    ```markdown
    @@@ relevanceai_dev_installation @@@
    @@@ <SNIPPET_NAME>, <SNIPPET_PARAM_KEY_1>=<SNIPPET_PARAM_VALUE_1>, <SNIPPET_PARAM_KEY_2>=<SNIPPET_PARAM_VALUE_2>, ...  @@@
    ```
    - If you want to concatenate snippets, please concatenate using the following format.
    ```markdown
    @@@ quickstart_docs; dataset_basics, DATASET_ID=QUICKSTART_DATASET_ID @@@
    @@@ <SNIPPET_1_NAME>; <SNIPPET_2_NAME>, <SNIPPET_2_PARAMS>; <SNIPPET_3_NAME>, <SNIPPET_3_PARAMS>; @@@
    ```

## 👩🏻‍💻 Building and previewing docs locally
7. Feel free to build the docs locally in order to preview your Markdown in Vscode.

   ```zsh
   ❯ python rdme_sync/build/build_docs.py -d

   ```

## 👩🏻‍💻  Syncing your Changes


8. Go the ReadMe Dash config and export the ReadMe API key `$RELEVANCEAI_README_API_KEY` variable from ReadMe Project Configuration
   ![](./assets/readme_api_key.png)
   ```zsh
   ❯ export RELEVANCEAI_README_API_KEY='xxx'
   ```
9.  To run notebook tests, make sure to export your `TEST_ACTIVATION_TOKEN` from https://cloud.relevance.ai/sdk/api/.
    ```zsh
    ❯ export TEST_ACTIVATION_TOKEN='xxx'
    ```
10. Apply the changes and update the ReadMe documentations. By default, this script will sync all files in `docs`.
    ```zsh
    ❯ ./rdme_sync/build_sync_readme.sh
    ## Run in debug mode
    ❯ ./rdme_sync/build_sync_readme.sh true
    ## Sync only a specific section, by default will sync everything in the generated `docs` folder.
    ❯ ./rdme_sync/build_sync_readme.sh false docs/clustering-features
    ## Override the version, by default will create a new version from your current Git branch name
    ❯ ./rdme_sync/build_sync_readme.sh false docs/clustering-features v1.0.0-my-new-version
    ```
    View your synced changes in ReadMe eg. https://docs.relevance.ai/v0.31.0/docs/quick-tour

## 👩🏻‍💻 Testing notebooks


11. Test the notebooks for changes. By default, the script will process all notebooks in the `docs` folder if no `--notebooks` specified. This script will output error logs to the file `readme_notebook_error_log.txt`
    ```zsh
    ❯ python rdme_sync/tests/test_notebooks.py
    ## Run in debug mode
    ❯ python rdme_sync/tests/test_notebooks.py -d
    ## Test on a selection of notebooks
    ❯ python rdme_sync/tests/test_notebooks.py -d --notebooks examples/Intro_to_Relevance_AI.ipynb examples/RelevanceAI-ReadMe-Quick-Feature-Tour.ipynb
    ```
    If you have a notebook you'd like to ignore in tests, add to the [notebook_ignore.txt](./rdme_sync/notebook_ignore.txt) file.


## 👩🏻‍💻  Committing your changes


12. Install pre-commit! This helps with things like merge conflicts, linting and checking API keys to help with cleaner commits. 😊
    ```
    pre-commit install
    ```
13. Commit your changes if what you see in the ReadMe documentation is correct! 🎉💪🏻

See [./rdme_sync/README.md](./rdme_sync/README.md) for more details about the build and sync scripts.


## 👩🏻‍💻  Updating the ReadMe config

To rebuild the config, if want to sync changes made in ReadMe
```
 ❯ python rdme_sync/readme_config.py --method 'build' --version 'v2.0.0'
```

## For further reference
### 👩🏻‍💻 Getting Started with rdme Client

See official [docs](https://www.npmjs.com/package/rdme/v/6.2.1) here for more details, else see rdme cheatsheet [here](./rdme.md).

### 📘 Getting Started with ReadMe Markdown

See official [docs](https://rdmd.readme.io/docs/getting-started) here for more details, else see rdmd cheatsheet [here](./rdmd.md).

### Helpful Tools

- [jqplay](https://jqplay.org/s/VTxvuAo0T2) - For crafting jq queries
- [Regexr](https://regexr.com/) - For validating Regex
