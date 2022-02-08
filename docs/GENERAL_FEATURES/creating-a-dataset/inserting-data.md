---
title: "Inserting and updating documents"
slug: "inserting-data"
excerpt: "Guide on how to insert data into RelevanceAI"
hidden: false
createdAt: "2021-11-02T00:37:51.061Z"
updatedAt: "2022-01-17T02:31:59.061Z"
---
## Inserting data
In general data insertion to Relevance AI can be done through either of the following options:

1. first, uploading the data to RelevanceAI and then vectorizing certain fields with a second API call (if necessary)
2. vectorizing certain fields and uploading the data to Relevance AI with a single call.

The first option is perfect when the data already includes the desired vectors. Under both options, Relevance AI provides you with state-of-the-art models to further vectorize your data as well.

To upload multiple documents to RelevanceAI, you can use the **insert_documents** method.

Note that if you specify a non-existing dataset upon insertion, a new dataset will be automatically created.

### Inserting the data in one go

If the dataset is not too big (not bigger than 100MB), there is no need to break it into batches. Here, you can see an example of how to upload all your data in one go. As was mentioned at [Preparing data from CSV / Pandas Dataframe](https://docs.relevance.ai/docs/preparing-data-from-csv-pandas-df), data is a list of dictionaries and is passed to the endpoint via the `documents` argument.
[block:code]
{
  "codes": [
    {
      "code": "client.insert_documents(dataset_id=\"ecommerce-sample-dataset\", documents=documents)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
### Updating documents

To only update specific documents, use `update_documents` as shown below:
[block:code]
{
  "codes": [
    {
      "code": "documents = [{\"_id\": \"example_id\", \"value\": 3}]\nclient.update_documents( dataset_id=\"ecommerce-sample-dataset\",  documents=documents)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "When To Use Update Vs Insert",
  "body": "`insert` replaces the entire document whereas `update` only changes the fields that are specified or newly added. It will not delete fields that are already in the dataset, nor insert new documents."
}
[/block]
The easiest way to modify and update all documents in a dataset is to run `pull_update_push` in the Python SDK.

### Updating An Entire Dataset
[block:callout]
{
  "type": "info",
  "title": "pull_update_push is the easiest way to edit documents in a single dataset",
  "body": "To quickly try out new experiments on your entire dataset, we built `pull_update_push` to easily update all documents in a dataset. It uses Python's function callables to help accelerate the modification process and immediately update documents in the vector database."
}
[/block]
An example of `pull_update_push` can be found here in which a new field `new_parameter` is added to every single document in a specified dataset.
[block:code]
{
  "codes": [
    {
      "code": "def encode_documents(documents):\n    for d in documents:\n        d[\"new_parameter\"] = \"new_value\"\n    return documents\n\nclient.pull_update_push(\n\tdataset_id=\"ecommerce-sample-dataset\",\n  update_function=encode_documents\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
## About Pull Update Push

In `pull_update_push`, we are modifying documents and updating them into the vector database. However, there is always a chance that the process can break. We do not want to necessarily re-process the already processed ones. Therefore, it also logs IDs that are processed to a separate logging collection. If we want to continue processing, we can specify the `logging_collection` parameter in `pull_update_push`.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ab65a6d-untitled2x_1.png",
        "untitled@2x (1).png",
        2492,
        1184,
        "#3381c6"
      ],
      "caption": "Architecture diagram of `pull_update_push`"
    }
  ]
}
[/block]
