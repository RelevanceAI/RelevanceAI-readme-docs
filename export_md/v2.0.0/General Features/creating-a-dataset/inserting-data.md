---
title: "Inserting and updating documents"
slug: "inserting-data"
excerpt: "Guide on how to insert data into RelevanceAI"
hidden: false
createdAt: "2021-11-02T00:37:51.061Z"
updatedAt: "2022-03-24T02:52:13.793Z"
---
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/general-features/creating-a-dataset/_notebooks/RelevanceAI_ReadMe_Creating_A_Dataset.ipynb)

## Inserting data
In general data insertion to Relevance AI can be done through either of the following options:

1. first, uploading the data to RelevanceAI and then vectorizing certain fields with a second API call (if necessary)
2. vectorizing certain fields and uploading the data to Relevance AI with a single call.

The first option is perfect when the data already includes the desired vectors. Under both options, Relevance AI provides you with state-of-the-art models to further vectorize your data as well.

To upload multiple documents to RelevanceAI, you can use the **insert_documents** method.

### Inserting the data in one go


```python Python (SDK)
df = client.Dataset("quickstart")
df.insert_documents(documents)
```
```python
```

### Updating documents

To only update specific documents, use `upsert_documents` as shown in the example below:

```python Python (SDK)
df.upsert_documents(documents=[{"_id": "example_id", "value": 3}])
```
```python
```

> 🚧 When To Use Upsert Vs Insert
>
> `insert` replaces the entire document whereas `upsert` only changes the fields that are specified or newly added. It will not delete fields that are already in the dataset, nor insert new documents.
The easiest way to modify and update all documents in a dataset is to run `df.apply` in the Python SDK.




### Applying functions to fields

> 📘How to update fields
>
> The easiest way to update an existing dataset with encoding results is to run `df.apply`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.
>

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encodes the `product_description` field using the `USE2Vec` encoder.
You can see the list of the available list of models for vectorising here using [Vectorhub](https://github.com/RelevanceAI/vectorhub) or feel free to bring your own model(s).


```python Python (SDK)
df["sentence"].apply(lambda x: model.encode(x), output_field="sentence_vector")
```
```python
```