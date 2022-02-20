---
title: "Inserting and updating documents"
slug: "inserting-data"
excerpt: "Guide on how to insert data into RelevanceAI"
hidden: false
createdAt: "2021-11-02T00:37:51.061Z"
updatedAt: "2022-01-17T02:31:59.061Z"
---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.1/docs/GENERAL_FEATURES/creating-a-dataset/_notebooks/creating-a-dataset.ipynb)

## Inserting data
In general data insertion to Relevance AI can be done through either of the following options:

1. first, uploading the data to RelevanceAI and then vectorizing certain fields with a second API call (if necessary)
2. vectorizing certain fields and uploading the data to Relevance AI with a single call.

The first option is perfect when the data already includes the desired vectors. Under both options, Relevance AI provides you with state-of-the-art models to further vectorize your data as well.

To upload multiple documents to RelevanceAI, you can use the **insert_documents** method.

### Inserting the data in one go


@@@ dataset_basics, DATASET_ID=QUICKSTART_DATASET_ID @@@

### Updating documents

To only update specific documents, use `upsert_documents` as shown in the example below:

@@@ upsert_example @@@

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


@@@ apply_encoding, FIELD="sentence", VECTOR_FIELD="sentence_vector"  @@@



