---
title: "Dataset Basics"
slug: "project-and-dataset"
excerpt: "Dedicated section to managing your RelevanceAI space"
hidden: false
createdAt: "2021-10-28T06:57:07.293Z"
updatedAt: "2022-01-18T02:31:36.905Z"
---
To be able to conduct vector experiments using Relevance AI, you need to sign up at https://cloud.relevance.ai/. Alternatively, you can follow the [guide](doc:installation) on our installation page.

## Datasets

After uploading a dataset to your account in Relevance AI, you can preview your data in the dashboard https://cloud.relevance.ai under Dataset. Note that if you just started, your account will be empty!
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b3937c1-quickstart_datasets_view.png",
        "quickstart_datasets_view.png",
        1300,
        771,
        "#fcfcfd"
      ],
      "sizing": "80",
      "caption": "RelevanceAI Datasets"
    }
  ]
}
[/block]
## Interacting With Datasets

By storing data on our platform, you can directly invoke vectorization models, perform an optimized nearest-neighbor search, cluster data, etc.

Some basic actions to deal with datasets are:

- Create a dataset
- List the available datasets in a project/account
- Monitor a specific dataset
- Delete a dataset

You can either use the dashboard to take these actions or employ Relevance AI Python SDK. For the Python SDK, you need to install Relevance AI and initiate a client as shown in the two code snippets below:
[block:code]
{
  "codes": [
    {
      "code": "pip install -U RelevanceAI",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \n\n\"\"\"\nRunning this cell will provide you with \nthe link to sign up/login page where you can find your credentials.\nOnce you have signed up, click on the value under `Authorization token` \nin the API tab\nand paste it in the Auth token box that appears below\n\"\"\"\n\nclient = Client()",
      "language": "python"
    }
  ]
}
[/block]
### Creating a dataset
To create a new empty dataset pass the name under which you wish to save the dataset to the `create` function as shown below. In this example, we have used `ecommerce-sample-dataset` as the name.
[block:code]
{
  "codes": [
    {
      "code": "client.datasets.create(dataset_id=\"ecommerce-sample-dataset\")",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
See [Inserting and updating documents](doc:inserting-data) for more details on how to insert/upload documents into a dataset.
[block:callout]
{
  "type": "danger",
  "body": "* You cannot rename datasets or rename/edit existing field names. However, you can copy datasets and edit field names using the [`clone`](https://relevanceai.github.io/RelevanceAI/docs/html/relevanceai.api.endpoints.html?highlight=clone#relevanceai.api.endpoints.datasets.Datasets.clone) feature.\n* Id field: Relevance AI platform identifies unique data entries within a dataset using a field called `_id` (i.e. every document in the dataset must include an `_id` field with a unique value per document).\n* Vector fields: the name of vector fields must end in `_vector_`",
  "title": "Remember!"
}
[/block]

### List your datasets

You can see a list of all datasets you have uploaded to your account in the dashboard.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fd97cbd-Screen_Shot_2022-01-17_at_12.21.57_pm.png",
        "Screen Shot 2022-01-17 at 12.21.57 pm.png",
        484,
        569,
        "#f6f7f9"
      ],
      "caption": "List of datasets in the dashboard"
    }
  ]
}
[/block]
Alternatively, you can use the list endpoint under Python SDK as shown below:
[block:code]
{
  "codes": [
    {
      "code": "client.datasets.list()",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
### Monitoring a specific dataset

RelevanceAI's dashboard at https://cloud.relevance.ai is the most straightforward place to monitor your data.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e9f331a-vector_health.png",
        "vector_health.png",
        1263,
        911,
        "#f6f6fb"
      ],
      "caption": "Monitor your vector health"
    }
  ]
}
[/block]
Alternatively, you can monitor the health of a dataset using the command below which returns the count of total missing and existing fields in the data points in the named dataset.
[block:code]
{
  "codes": [
    {
      "code": "client.datasets.monitor.health(\"ecommerce-sample-dataset\")\n\n# Returns a count of total missing and existing data",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d2136ad-0aa6b74-Screen_Shot_2022-01-10_at_3.44.42_pm.png",
        "0aa6b74-Screen_Shot_2022-01-10_at_3.44.42_pm.png",
        607,
        367,
        "#ededed"
      ],
      "caption": "Monitoring dataset health"
    }
  ]
}
[/block]
### Deleting a dataset

Deleting an existing dataset can be done on the dashboard using the Delete All Data button. Or through the following code. In this case, we are deleting the `ecommerce-dataset`:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8d8f670-Screen_Shot_2022-01-17_at_12.27.05_pm.png",
        "Screen Shot 2022-01-17 at 12.27.05 pm.png",
        1900,
        197,
        "#f3f5fa"
      ],
      "caption": "Dash board view"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "client.datasets.delete(dataset_id = \"ecommerce-sample-dataset\")",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
