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
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n## Source project details you are copying from\nsrc_project = \"Source project name here\" \nsrc_api_key = \"Source API key here\"\t \nsrc_dataset_id = SOURCE_DATASET_ID\t         \n\n## Source project details you are copying to\ndest_project = \"Your project name here\"\ndest_api_key = \"Your API key here\"\ndest_dataset_id = DEST_DATASET_ID   \n\nclient = Client(dest_project, dest_api_key)\nclient.admin.copy_foreign_dataset(\n    dataset_id=DEST_DATASET_ID,\n    project=dest_project,\n    api_key=dest_api_key,\n    source_dataset_id=SOURCE_DATASET_ID,\n    source_project=src_project,\n    source_api_key=src_api_key\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
## Clone the dataset

In this section, we show you how to create a copy of a dataset within the same project. This allows you to freely version and checkpoint datasets.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nsrc_dataset_id = SOURCE_DATASET_ID\ndest_dataset_id = DEST_DATASET_ID\n\nschema_changes = {}\nrename_fields = {}\nremove_fields = []\nfilters = []\n\nclient = Client()\nclient.datasets.clone(\n    old_dataset=src_dataset_id,\n    new_dataset=dest_dataset_id,\n    schema=schema_changes,\n    rename_fields=rename_fields,\n    remove_fields=remove_fields,\n    filters=filters\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
