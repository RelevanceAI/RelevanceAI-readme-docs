# Automation Scripts

This repository updates RelevanceAI's ReadMe Documentation [here](https://docs.relevance.ai/docs).

## 🛠️  Requirements

- [Node.JS ^12.x and NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [Python ^3.8.0](https://www.python.org/downloads/release/python-380/) - more Python version to be supported in future
- [rdme NPM client](https://www.npmjs.com/package/rdme/v/6.2.1)

## 🧰 OS Supported

- Linux (Ubuntu 18.04.6 LTS (Bionic Beaver) Debian)


## 👩🏻‍💻 Getting Started with these automation scripts


The `main` branch is the live branch in ReadMe.
By following instructions below, you will be able to preview/create any given version of the docs at one time.


```zsh
❯ tree -L 1
.
├── build_docs.py          ### Builds docs from docs_template
├── detect_secrets.py     ### Extra check to check for API keys in repo/noteboks
├── README.md
├── readme_migration.py    ## Ignore; Migration script from exports `block` to `md` format
├── sync_readme.sh    ## Syncs Readme docs w/ rdme client; creates new version if does not exist; syncs w/ latest SDK release
├── test_notebooks.py      ## Executes notebooks e2e
├── update_docs_version.py  ## Update all asset links to point to the current branch
├── update_readme.sh       ## Master script to update asset links, build docs and sync w/ README
└── utils.py

```


1. Create a new branch for the ReadMe version you'd like to create if not already auto-created upon SDK release eg. v1.0.0
   - Branch off the latest version that you'd like to fork from (if it is not `main`)
    ```zsh
    ❯ git checkout -b v1.0.0
    ```
2. Update the `__version__` file to match that semver of the branch eg. 1.0.0 (this can be automated in future)
   - All automation scripts read from this file by default if no version given
3. Make your desired changes to the relevant Markdown/notebooks etc.
4. Sync changes w/ README!
    ```zsh
    ❯ ./scripts/update_readme.sh
    ## Run in debug mode
    ❯ ./scripts/update_readme.sh true
    ## Sync only a specific section, by default will sync everything in the generated `docs` folder.
    ❯ ./scripts/update_readme.sh false docs/CLUSTERING_FEATURES
    ## Override the version, by default will create a new version from your current Git branch name
    ❯ ./scripts/update_readme.sh false docs/CLUSTERING_FEATURES v1.0.0-my-new-version
    ```



## For further reference

### 👩🏻‍💻 Getting Started with rdme Client

See official [docs](https://www.npmjs.com/package/rdme/v/6.2.1) here for more details, else see rdme cheatsheet [here](./rdme.md).


### 📘 Getting Started with ReadMe Markdown

See official [docs](https://rdmd.readme.io/docs/getting-started) here for more details, else see rdmd cheatsheet [here](./rdmd.md).



### Helpful Tools

- [jqplay](https://jqplay.org/s/VTxvuAo0T2) - For crafting jq queries
- [Regexr](https://regexr.com/) - For validating Regex