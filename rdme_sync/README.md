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
├── build           ## Build scripts
├── readme          ## ReadMe wrapper classes
├── README.md
├── sync_readme.sh       ## Sync docs to ReadMe
├── tests
├── update_readme.sh     ## Master script to build and sync
└── utils.py


```


1. Create a new branch for the ReadMe version you'd like to create if not already auto-created upon SDK release eg. v1.0.0
   - Branch off the latest version that you'd like to fork from (if it is not `main`)
    ```zsh
    ❯ git checkout -b v1.0.0
    ```
2. Make your desired changes to the relevant Markdown/notebooks etc.
3. Sync changes w/ README!
    ```zsh
    ❯ ./rdme_sync/update_readme.sh
    ## Run in debug mode
    ❯ ./rdme_sync/update_readme.sh true
    ## Sync only a specific section, by default will sync everything in the generated `docs` folder.
    ❯ ./rdme_sync/update_readme.sh false docs/clustering-features
    ## Override the version, by default will create a new version from your current Git branch name
    ❯ ./rdme_sync/update_readme.sh false docs/clustering-features v1.0.0-my-new-version
    ```

## For further reference

### 👩🏻‍💻 Getting Started with rdme Client

See official [docs](https://www.npmjs.com/package/rdme/v/6.2.1) here for more details, else see rdme cheatsheet [here](./rdme.md).


### 📘 Getting Started with ReadMe Markdown

See official [docs](https://rdmd.readme.io/docs/getting-started) here for more details, else see rdmd cheatsheet [here](./rdmd.md).



### Helpful Tools

- [jqplay](https://jqplay.org/s/VTxvuAo0T2) - For crafting jq queries
- [Regexr](https://regexr.com/) - For validating Regex