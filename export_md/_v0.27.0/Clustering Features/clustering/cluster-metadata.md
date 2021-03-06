---
title: "Cluster Metadata"
slug: "cluster-metadata"
hidden: false
createdAt: "2021-12-02T14:01:15.693Z"
updatedAt: "2022-01-24T06:35:28.286Z"
---
Relevance AI allows you to insert additional information (e.g. total number of clusters) into your clustering results. This information is referred to as metadata in Relevance AI.

## What you will need to have
1. uploaded a dataset to Relevance AO
2. performed clustering and uploaded the results to Relevance AI
All these steps are explained in detail on [the quickstart clustering guide](doc:quickstart-clustering)

## Code Example

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12iglenFIRelOoZKsPtE-LR7Yh3FbjejN?usp=sharing)


The following code snippets extract the metadata from the clustering algorithm and adds this information to Relevance AI where DATASET_ID refers to the name of the dataset, VECTOR_FIELD is the field based on which the clustering is done, and ALIAS is the name specified by the user to save the clustering results.
```python Python (SDK)
from relevanceai.vector_tools.cluster import KMeans

KMEAN_NUMBER_OF_CLUSTERS = 10
clusterer = KMeans(k=KMEAN_NUMBER_OF_CLUSTERS)

metadata = clusterer.to_metadata()
```
```python
```

```python Python (SDK)
client.services.cluster.centroids.metadata(
 dataset_id = DATASET_ID,
 vector_fields = [VECTOR_FIELD],
 alias = ALIAS,
 metadata = metadata
)
```
```python
```
Once you have stored the metadata, you can view them using the following code.
```python Python (SDK)
client.services.cluster.centroids.metadata(
 dataset_id = DATASET_ID,
 vector_fields = [VECTOR_FIELD],
 alias = ALIAS
)
```
```python
```
