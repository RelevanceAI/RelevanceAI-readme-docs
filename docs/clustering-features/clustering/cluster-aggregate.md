---
title: "Cluster Aggregate"
slug: "cluster-aggregate"
excerpt: "How to run a cluster aggregate"
hidden: false
createdAt: "2021-12-02T12:40:13.764Z"
updatedAt: "2022-01-24T06:27:07.985Z"
---
It is often important to identify the characteristics of each cluster. One of the best ways to do this is through an aggregation query that summarises different fields within the cluster.

This can only can be used after a vector field has been clustered.

## What you will need
You will need to have followed [the quickstart clustering guide](doc:quickstart-clustering).
You will also need to have knowledge of [aggregations](doc:aggregations).

## Code Example
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Clustering-Aggregation.ipynb)

The following code example groups the data based on the `product_price` field, also use the average metrics on `product_price` for each cluster. `DATASET_ID` refers to the name of the dataset, `VECTOR_FIELD` is the field based on which the clustering is done, and ALIAS is the name specified by the user to save the clustering results.

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
      "code": "from sklearn.cluster import KMeans\n\nVECTOR_FIELD = VECTOR_FIELD\nKMEAN_NUMBER_OF_CLUSTERS = n\nALIAS = \"kmeans_\" + str(KMEAN_NUMBER_OF_CLUSTERS)\n\nmodel = KMeans(n_clusters=KMEAN_NUMBER_OF_CLUSTERS)\nclusterer = client.ClusterOps(alias=ALIAS, model=model)\nclusterer.operate(dataset_id=DATASET_ID, vector_fields=[VECTOR_FIELD])",
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
      "code": "# Aggregate based on the clusters\nresult = clusterer.aggregate(\n    dataset=DATASET_ID,\n    vector_fields = [VECTOR_FIELD],\n    groupby=[\n      {\"name\": \"brand\", \"field\": \"query\", \"agg\": \"category\"}],\n    metrics = [\n      {\"name\": \"avg_retail_price\", \"field\": \"product_price\", \"agg\": \"avg\"}]\n)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

