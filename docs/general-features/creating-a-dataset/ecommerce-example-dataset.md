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

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==1.4.5",
      "name": "Bash",
      "language": "bash"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n\"\"\"\nYou can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api\nOnce you have signed up, click on the value under `Activation token` and paste it here\n\"\"\"\nclient = Client()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


- `dest_project` and `dest_api_key` refer to your destination project and api_key or where the copied version of dataset is going to be saved.

[block:code]
{
  "codes": [
    {
      "code": "## Source project details you are copying from\nsrc_dataset_id = SOURCE_DATASET_ID\n\n## Source project details you are copying to\ndest_project = \"<Destination project name here>\"\ndest_api_key = \"<Destination API key here>\"\n\nclient.send_dataset(\n    src_dataset_id,\n    dest_project,\n    dest_api_key\n)",
      "name": "Python (SDK)",
      "language": "python"
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
      "code": "copied_dataset_id = COPIED_DATASET_ID\nclient.clone_dataset(src_dataset_id, copied_dataset_id)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

