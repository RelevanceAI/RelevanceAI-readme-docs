---
title: "Quickstart (step by step)"
slug: "quickstart-clustering"
excerpt: "Get started with clustering in a few minutes!"
hidden: false
createdAt: "2021-11-26T10:21:47.021Z"
updatedAt: "2022-01-24T06:26:11.281Z"
---
<figure>
<img src="https://files.readme.io/8a1c5e7-Frame_6.png" width="742" alt="Frame 6.png" />
<figcaption>Clustering showing how a certain variety of images can improve pricing</figcaption>
<figure>
## Introduction

Clustering groups items so that those in the same group/cluster have meaningful similarities (i.e. specific features or properties). Clustering facilitates informed decision-making by giving significant meaning to data through the identification of different patterns. Relying on strong vector representations, Relevance AI provides you with powerful and easy-to-use clustering endpoints.

In this guide, you will learn to run clustering based on the K-Means algorithm which aims to partition your dataset into K distinct clusters.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15fXlU8hGQ6oysCJEbAlIjtJGkTaCNlT-?usp=sharing)

### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with RelevanceAI. For more information, please read the [installation](doc:installation) guide.
```shell Python (SDK)
pip install -U RelevanceAI==0.27.0
```
```shell
```

```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the appreared Auth token box below
"""

client = Client()
```
```python
```
You also need to have a dataset under your Relevance AI account. You can either use our dummy sample data as shown in this step or follow the tutorial on [how to create your own dataset](https://docs.relevance.ai/docs/creating-a-dataset-prerequisites).

In this guide, we use our e-commerce database, which includes fields such as `product_name`, as well as the vectorized version of the field `product_name_default_vector_`. Loading these documents can be done via:
```python Python (SDK)
from relevanceai.datasets import get_dummy_ecommerce_dataset

documents = get_dummy_ecommerce_dataset()
```
```python
```
Next, we can upload these documents into your personal Relevance AI account under the name *quickstart_clustering_kmeans*
```python Python (SDK)
DATASET_ID = 'quickstart_clustering_kmeans-sbs'
client.insert_documents(dataset_id=DATASET_ID, docs=documents)
```
```python
```
Let's have a look at the schema to see what vector fields are available for clustering.

```python Python (SDK)
client.datasets.schema(dataset_id)
```
```python
```
The result is a JSON output similar to what is shown below. As can be seen, there are two vector fields in the dataset `product_image_clip_vector_` and `product_title_clip_vector_`.

```json Python (SDK)
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

To run KMeans Clustering, we need to first define a clustering object, KMeans, which loads the clustering algorithm with a specified number of clusters.
```python Python (SDK)
from relevanceai.vector_tools.cluster import KMeans

KMEAN_NUMBER_OF_CLUSTERS = 10
clusterer = KMeans(k=KMEAN_NUMBER_OF_CLUSTERS)
```
```python
```

Next, the algorithm is fitted on the vector field, *product_title_clip_vector_*, to distinguish between clusters. The cluster to which each document belongs is returned.

```python Python (SDK)
ALIAS = 'kmeans_'+str(KMEAN_NUMBER_OF_CLUSTERS)

VECTOR_FIELD = "product_title_clip_vector_"
clustered_documents = clusterer.fit_documents(
 vector_fields = [VECTOR_FIELD], # Cluster 1 field
 docs = documents,
 return_only_clusters = True, # If True, return only clusters
 alias = ALIAS
)
```
```python
```
### 3. Update the dataset with the cluster labels

Finally, these categorised documents are uploaded back to the dataset as an additional field.
```python Python (SDK)
client.update_documents(dataset_id=DATASET_ID, docs=clustered_documents)
```
```python
```
### 4. Insert the cluster centroids

Get the centroid's vector and insert them as centroids into Relevance AI.
```python Python (SDK)
centers = clusterer.get_centroid_documents()

client.services.cluster.centroids.insert(
 dataset_id = DATASET_ID,
 cluster_centers = centers,
 vector_fields = [VECTOR_FIELD],
 alias = ALIAS
)
```
```python
```
Once you have stored the cluster centroids, you can view them using the following code.
```python Python (SDK)
client.services.cluster.centroids.list(
 dataset_id = DATASET_ID,
 vector_fields = [VECTOR_FIELD],
 page_size = 10,
 include_vector = False,
 alias = ALIAS
)

cluster_centroids['documents'][0]['_id']
```
```python
```
Downloading a few sample documents from the dataset, we show to which cluster they belong:
```python Python (SDK)
from relevanceai import show_json

sample_documents = client.datasets.documents.list(DATASET_ID, page_size=5)
samples = [{
 'product_title':d['product_title'],
 'cluster':d['_cluster_'][VECTOR_FIELD][ALIAS]
} for d in sample_documents["documents"]]

show_json(samples, text_fields=['product_title', 'cluster'])
```
```python
```

<figure>
<img src="https://files.readme.io/dbe68e0-Screen_Shot_2022-01-24_at_1.57.57_pm.png" width="461" alt="Screen Shot 2022-01-24 at 1.57.57 pm.png" />
<figcaption>Showing to which cluster each of the first 5 documents belong.</figcaption>
<figure>
