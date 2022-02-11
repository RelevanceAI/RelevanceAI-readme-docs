# RelevanceAI-readme-docs

This repository updates RelevanceAI's ReadMe Documentation [here](https://docs.relevance.ai/docs).

## 🧠 Documentation

Migrating RelevanceAI docs from [docs.relevance.ai/v0.27.0/docs/welcome](https://docs.relevance.ai/v0.27.0/docs/welcome).
 to [docs.relevance.ai/v0.28.0/docs/welcome](https://docs.relevance.ai/v0.28.0/docs/welcome).


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
├── assets      ## Assets for this README
├── docs        ## Generated docs files
├── docs_template   ## Templates and all resources for auto-generation
├── examples        ## For testing notebook tests
├── migration_details.md ## Ignore: instructions for the initial migration
├── package.json         ## NPM deps
├── package-lock.json    ## NPM deps lock
├── rdmd.md              ## Rdmd cheatsheet
├── rdme.md              ## Rdme cheatsheet
├── README.md
├── requirements.txt     ## Python reqs
├── scripts              ## Automation scripts
└── __version__          ## Readme version
```

1. Install dependencies if first time; note, this repo has both Python and NPM deps
    ```zsh
    ❯ git clone git@github.com:RelevanceAI/RelevanceAI-readme-docs.git
    ❯ python -m venv .venv                 # Create new Python venv
    ❯ pip install -r requirements.txt      # Install Python reqs
    ❯ npm i                                # Install Node reqs
    ```
2. Create a new branch for the ReadMe version you'd like to create if not already auto-created upon SDK release eg. v1.0.0
   - Branch off the latest version that you'd like to fork from (if it is not `main`)
    ```zsh
    ❯ git checkout -b v1.0.0
    ```
3. Update the `__version__` file to match that semver of the branch eg. 1.0.0 (this can be automated in future)
   - All automation scripts read from this file by default if no version given.
4. Make your desired changes to the relevant Markdown/notebooks on `docs_templates`.
5. To add new assets:
   - Add new assets to the corresponding `_assets` folder in `docs_template`.
   - Update asset links in `md` files to point to corresponding path.
6. To add new notebooks:
   - Add new notebooks to the corresponding `_notebooks_` folder in `docs_template`.
   - Update notebooks to point to the corresponding path.
   - Colab notebook refs are of the form:
  ```zsh
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs/GETTING_STARTED/_notebooks/Intro-to-Relevance-AI.ipynb)
  ```
  - Please add this badge in top cell of notebook as well so it can be accessed from Github.
7. To add new snippet
   - Add new snippets in the corresponding `_snippets` folder.
   - Snippets are loaded in a nested fashion. Inner most `_snippets` with the same name will override general snippets in [`docs_template/_snippets/`](./docs_template/_snippets/).
   - All snippets in `*.md` and `*.ipynb` files are prefaced with `@@@`.
    ```markdown
    @@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@
    @@@ <SNIPPET_NAME>, <SNIPPET_PARAM_KEY_1>=<SNIPPET_PARAM_VALUE_1>, <SNIPPET_PARAM_KEY_2>=<SNIPPET_PARAM_VALUE_2>, ...  @@@
    ```
    - If you want to concatenate snippets, please concatenate using the following format.
    ```markdown
    @@@+ quickstart_docs; dataset_basics, DATASET_ID=QUICKSTART_DATASET_ID @@@
    @@@+ <SNIPPET_1_NAME>; <SNIPPET_2_NAME>, <SNIPPET_2_PARAMS>; <SNIPPET_3_NAME>, <SNIPPET_3_PARAMS>; @@@
    ```
8. Go the ReadMe Dash config and export the ReadMe API key `$RELEVANCEAI_README_API_KEY` variable from ReadMe Project Configuration
   ![](./assets/readme_api_key.png)
   ```zsh
   ❯ export RELEVANCEAI_README_API_KEY='xxx'
   ```
9.  To run notebook tests, make sure to export your `TEST_ACTIVATION_TOKEN` from https://cloud.relevance.ai/sdk/api/.
    ```zsh
    ❯ export TEST_ACTIVATION_TOKEN='xxx'
    ```
10. Apply the changes and update the ReadMe documentations.
    ```zsh
    ❯ ./scripts/update_readme.sh
    ## Run in debug mode
    ❯ ./scripts/update_readme.sh true
    ```
    View your synced changes in ReadMe eg. https://docs.relevance.ai/v0.31.0/docs/quick-tour
11. Test the notebooks for changes. By default, the script will process all notebooks in the `docs` folder if no `--notebooks` specified. This script will output error logs to the file `readme_notebook_error_log.txt`
    ```
    ❯ python scripts/test_notebooks.py -d True --notebooks examples/Intro-to-Relevance-AI.ipynb
    ```
12. Install pre-commit to check for API keys in notebooks!
    ```
    pre-commit install
    ```
13. Commit your changes if what you see in the ReadMe documentation is correct! 🎉💪🏻



## For further reference
### 👩🏻‍💻 Getting Started with rdme Client

See official [docs](https://www.npmjs.com/package/rdme/v/6.2.1) here for more details, else see rdme cheatsheet [here](./rdme.md).

### 📘 Getting Started with ReadMe Markdown

See official [docs](https://rdmd.readme.io/docs/getting-started) here for more details, else see rdmd cheatsheet [here](./rdmd.md).

### Helpful Tools

- [jqplay](https://jqplay.org/s/VTxvuAo0T2) - For crafting jq queries
- [Regexr](https://regexr.com/) - For validating Regex