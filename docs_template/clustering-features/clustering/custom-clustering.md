---
title: "Custom Clustering"
slug: "custom-clustering"
excerpt: "How to perform custom clustering"
hidden: false
createdAt: "2021-12-02T14:01:29.321Z"
updatedAt: "2022-01-24T07:35:51.261Z"
---
Relevance AI supports the integration of custom clustering algorithms. The custom algorithm can be created as the *fit_transform* method of the *ClusterBase* class.

## What you will need
You need to have a dataset under your account in Relevance AI.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0-autoresolve-git-conflict/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Custom-Clustering.ipynb)

## Code Example

**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0-autoresolve-git-conflict/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Custom-Clustering.ipynb)

The following code shows
1. an example of a custom clustering algorithm that chooses randomly between Cluster 0 and Cluster 1
2. how to call`fit_documents` to preform clustering
3. how to update the dataset with the results


@@@ client_dataset, DATASET_ID='faiss_kmeans_clustering'; faiss_kmeans_clustering_sample, VECTOR_FIELD='product_title_clip_vector_' @@@
