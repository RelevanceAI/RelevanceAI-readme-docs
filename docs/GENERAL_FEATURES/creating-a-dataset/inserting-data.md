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

### Inserting the data in one go

```python Python (SDK)
df = client.Dataset(quickstart)
df.insert_documents(documents)
```
```python
```

### Updating documents

To only update specific documents, use `update_documents` as shown in the example below:

```python Python (SDK)
documents = [{"_id": "example_id", "value": 3}]
df.upsert_documents(documents=documents)
```
```python
```

> 🚧 When To Use Upsert Vs Insert
>
> `insert` replaces the entire document whereas `upsert` only changes the fields that are specified or newly added. It will not delete fields that are already in the dataset, nor insert new documents.
The easiest way to modify and update all documents in a dataset is to run `pull_update_push` in the Python SDK.

### Updating An Entire Dataset
> 📘 pull_update_push is the easiest way to edit documents in a single dataset
>
> To quickly try out new experiments on your entire dataset, we built `pull_update_push` to easily update all documents in a dataset. It uses Python's function callables to help accelerate the modification process and immediately update documents in the vector database.
An example of `pull_update_push` can be found here in which a new field `new_parameter` is added to every single document in a specified dataset.

```python Python (SDK)
def encode_documents(documents):
    for d in documents:
        d["new_parameter"] = "new_value"
    return documents
```
```python
```

```python Python (SDK)
client.pull_update_push(
    dataset_id="quickstart",
    update_function=encode_documents
)
```
```python
```

## About Pull Update Push

In `pull_update_push`, we are modifying documents and updating them into the vector database. However, there is always a chance that the process can break. We do not want to necessarily re-process the already processed ones. Therefore, it also logs IDs that are processed to a separate logging collection. If we want to continue processing, we can specify the `logging_collection` parameter in `pull_update_push`.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-general-features/docs_template/GENERAL_FEATURES/creating-a-dataset/assets/pull-update-push.png" width="2492" alt="untitled@2x (1).png" />
<figcaption>Architecture diagram of `pull_update_push`</figcaption>
<figure>

