---
title: "List furthest from centroids"
slug: "list-furthest-from-centroids"
hidden: false
createdAt: "2021-12-02T13:13:54.940Z"
updatedAt: "2022-01-24T05:52:17.148Z"
---
Centroids from your clustering algorithm describe the 'average' of each cluster. Relevance AI allows you to query for a list of documents that are furthest from the centroids. This determines how successful your clustering algorithm is by specifying the boundary of what is considered to be in the same cluster.

## What you will need to have
1. uploaded a dataset to Relevance AO
2. performed clustering and uploaded the results to Relevance AI
All these steps are explained in detail on [the quickstart clustering guide](doc:quickstart-clustering)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0-autoresolve-git-conflict/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Clustering-List-Furthest.ipynb)

After clustering is done and the dataset is updated with the results, listing the furthest points from the center of each cluster can be done via `list_furthest_from_center` function as shown in the code snippet below where `DATASET_ID` refers to the name of the dataset, `VECTOR_FIELD` is the field based on which the clustering is done, and `ALIAS` is the name specified by the user to save the clustering results.


[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset(DATASET_ID)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]
[block:code]
{
  "codes": [
    {
      "code": "from sklearn.cluster import KMeans\n\nVECTOR_FIELD = \"product_title_clip_vector_\"\nKMEAN_NUMBER_OF_CLUSTERS = 5\nALIAS = \"kmeans_\" + str(KMEAN_NUMBER_OF_CLUSTERS)\n\nmodel = KMeans(n_clusters=KMEAN_NUMBER_OF_CLUSTERS)\nclusterer = client.ClusterOps(alias=ALIAS, model=model)\nclusterer.operate(dataset_id=\"quickstart_kmeans_clustering\", vector_fields=[\"product_title_clip_vector_\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]
[block:code]
{
  "codes": [
    {
      "code": "clusterer.list_closest(dataset_id = \"quickstart_kmeans_clustering\", vector_field=\"product_title_clip_vector_\")",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

