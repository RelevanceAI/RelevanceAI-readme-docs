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

- `src_project` and `src_api_key` variables in the code snippet below refer to the original dataset authentications
- `dest_project` and `dest_api_key` refer to your destination project and api_key or where the copied version of dataset is going to be saved.
```python Python (SDK)
from relevanceai import Client

## Source project details you are copying from
src_project = "Source project name here"
src_api_key = "Source API key here"
src_dataset_id = SOURCE_DATASET_ID

## Source project details you are copying to
dest_project = "Your project name here"
dest_api_key = "Your API key here"
dest_dataset_id = DEST_DATASET_ID

client = Client(dest_project, dest_api_key)
client.admin.copy_foreign_dataset(
 dataset_id=DEST_DATASET_ID,
 project=dest_project,
 api_key=dest_api_key,
 source_dataset_id=SOURCE_DATASET_ID,
 source_project=src_project,
 source_api_key=src_api_key
)
```
```python
```
## Clone the dataset

In this section, we show you how to create a copy of a dataset within the same project. This allows you to freely version and checkpoint datasets.
```python Python (SDK)
from relevanceai import Client

src_dataset_id = SOURCE_DATASET_ID
dest_dataset_id = DEST_DATASET_ID

schema_changes = {}
rename_fields = {}
remove_fields = []
filters = []

client = Client()
client.datasets.clone(
 old_dataset=src_dataset_id,
 new_dataset=dest_dataset_id,
 schema=schema_changes,
 rename_fields=rename_fields,
 remove_fields=remove_fields,
 filters=filters
)
```
```python
```
