---
title: "Copying and cloning dataset"
slug: "ecommerce-example-dataset"
excerpt: "Guide on how to copy and clone datasets"
hidden: false
createdAt: "2021-11-03T00:10:39.691Z"
updatedAt: "2022-01-17T02:57:42.720Z"
---
## Copy a dataset from another project


In this section, we show you how to create a copy of a dataset from one project to another. This allows you to freely collaborate and share datasets between accounts.
First Relevance AI's Python SDK must be installed and then a client object must be instantiated as shown below:

```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==1.1.3
```
```bash
```

```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Activation token` and paste it here
"""
client = Client()
```
```python
```


- `dest_project` and `dest_api_key` refer to your destination project and api_key or where the copied version of dataset is going to be saved.

```python Python (SDK)
## Source project details you are copying from
src_dataset_id = SOURCE_DATASET_ID

## Source project details you are copying to
dest_project = "<Destination project name here>"
dest_api_key = "<Destination API key here>"

client.send_dataset(
    src_dataset_id,
    dest_project,
    dest_api_key
)
```
```python
```

## Clone the dataset

In this section, we show you how to create a copy of a dataset within the same project. This allows you to freely version and checkpoint datasets.

```python Python (SDK)
copied_dataset_id = COPIED_DATASET_ID
client.clone_dataset(src_dataset_id, copied_dataset_id)
```
```python
```

