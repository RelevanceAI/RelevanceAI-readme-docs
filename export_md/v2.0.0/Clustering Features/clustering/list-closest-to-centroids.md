---
title: "List closest to centroids"
slug: "list-closest-to-centroids"
excerpt: "List the documents closest to center"
hidden: false
createdAt: "2021-12-02T12:42:27.912Z"
updatedAt: "2022-03-24T02:52:13.796Z"
---
Centroids from your clustering algorithm describe the 'average' of each cluster. Relevance AI allows you to query for a list of documents that are closest to the centroids of each cluster.

## What you will need to have
1. uploaded a dataset to Relevance AO
2. performed clustering and uploaded the results to Relevance AI
All these steps are explained in detail on [the quickstart clustering guide](doc:quickstart-clustering)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Clustering-List-Closest.ipynb)


After clustering is done and the dataset is updated with the results, listing closest to centroids can be done via `list_closest_to_center` function as shown in the code snippet below where `DATASET_ID` refers to the name of the dataset, `VECTOR_FIELD` is the field based on which the clustering is done, and `ALIAS` is the name specified by the user to save the clustering results.

```python Python (SDK)
df = client.Dataset(DATASET_ID)

clusterer = df.auto_cluster('kmeans_5', [VECTOR_FIELD])

clusterer.list_closest_to_center()
```
```python
```