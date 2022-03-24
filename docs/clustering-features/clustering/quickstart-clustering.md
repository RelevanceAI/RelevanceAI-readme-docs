---
title: "Quickstart (step by step)"
slug: "quickstart-clustering"
excerpt: "Get started with clustering in a few minutes!"
hidden: false
createdAt: "2021-11-26T10:21:47.021Z"
updatedAt: "2022-01-24T06:26:11.281Z"
---

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/clustering-features/_assets/RelevanceAI_clustering.png?raw=true"  width="450" alt="Clustering effect on pricing" />
<figcaption>Clustering showing how a certain variety of images can improve pricing</figcaption>
<figure>

## Introduction

Clustering groups items so that those in the same group/cluster have meaningful similarities (i.e. specific features or properties). Clustering facilitates informed decision-making by giving significant meaning to data through the identification of different patterns. Relying on strong vector representations, Relevance AI provides you with powerful and easy-to-use clustering endpoints.

In this guide, you will learn to run clustering based on the K-Means algorithm which aims to partition your dataset into K distinct clusters.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Kmeans-Clustering-Step-by-Step.ipynb)

### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with RelevanceAI. For more information, please read the [installation](doc:installation) guide.

```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==2.0.0
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

You also need to have a dataset under your Relevance AI account. You can either use our dummy sample data as shown in this step or follow the tutorial on [how to create your own dataset](doc:project-and-dataset).

In this guide, we use our e-commerce database, which includes fields such as `product_name`, as well as the vectorized version of the field `product_name_default_vector_`. Loading these documents can be done via:

```python Python (SDK)
from relevanceai.datasets import get_ecommerce_dataset_encoded

documents = get_ecommerce_dataset_encoded()
{k:v for k, v in documents[0].items() if '_vector_' not in k}
```
```python
```

Next, we can upload these documents into your personal Relevance AI account under the name *quickstart_clustering_kmeans*

```python Python (SDK)
documents = [
	{"_id": "1", "example_vector_": [0.1, 0.1, 0.1], "data": "Documentation"},
	{"_id": "2", "example_vector_": [0.2, 0.2, 0.2], "data": "Best document!"},
	{"_id": "3", "example_vector_": [0.3, 0.3, 0.3], "data": "Document example"},
	{"_id": "5", "example_vector_": [0.4, 0.4, 0.4], "data": "This is a doc"},
	{"_id": "4", "example_vector_": [0.5, 0.5, 0.5], "data": "This is another doc"},
]

df = client.Dataset("quickstart_kmeans_clustering")
df.insert_documents(documents)
```
```python
```

Let's have a look at the schema to see what vector fields are available for clustering.

```python Python (SDK)
df.schema
```
```python
```

The result is a JSON output similar to what is shown below. As can be seen, there are two vector fields in the dataset `product_image_clip_vector_` and `product_title_clip_vector_`.

```json JSON
{
 'insert_date_': 'date',
 'product_image': 'text',
 'product_image_clip_vector_': {'vector': 512},
 'product_link': 'text',
 'product_price': 'text',
 'product_title': 'text',
 'product_title_clip_vector_': {'vector': 512},
 'query': 'text',
 'source': 'text'
}
```
```json
```

### 2. Run clustering algorithm

To run KMeans Clustering, we need to first define a clustering object, `KMeansModel`, which loads the clustering algorithm with a specified number of clusters.

```python Python (SDK)
from relevanceai.clusterer import KMeansModel

VECTOR_FIELD = "product_title_clip_vector_"
KMEAN_NUMBER_OF_CLUSTERS = 5
ALIAS = "kmeans_" + str(KMEAN_NUMBER_OF_CLUSTERS)

model = KMeansModel(k=KMEAN_NUMBER_OF_CLUSTERS)
clusterer = client.ClusterOps(alias=ALIAS, model=model)
```
```python
```

Next, the algorithm is fitted on the vector field, *product_title_clip_vector_*, to distinguish between clusters. The cluster to which each document belongs is returned.

```python Python (SDK)
clustered_docs = clusterer.fit_predict_documents(
        vector_fields=['product_title_clip_vector_'],
        documents=documents, inplace=False
    )
```
```python
```


### 3. Update the dataset with the cluster labels

Finally, these categorised documents are uploaded back to the dataset as an additional field.

```python Python (SDK)
df.upsert_documents(documents=clustered_docs)
```
```python
```

### 4. Insert the cluster centroids

Get the centroid's vector and insert them as centroids into Relevance AI.

```python Python (SDK)
centroids = clusterer.get_centroid_documents()

clusterer.insert_centroid_documents(centroids, df)
```
```python
```

Downloading a few sample documents from the dataset, we show to which cluster they belong:

```python Python (SDK)
from relevanceai import show_json

sample_documents = df.sample(n=5)
samples = [{
    'product_title':d['product_title'],
    'cluster':d['_cluster_'][VECTOR_FIELD][ALIAS]
} for d in sample_documents]

show_json(samples, text_fields=['product_title', 'cluster'])
```
```python
```

