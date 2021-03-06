---
title: "List closest to centroids"
slug: "list-closest-to-centroids"
excerpt: "List the documents closest to center"
hidden: false
createdAt: "2021-12-02T12:42:27.912Z"
updatedAt: "2022-01-24T05:50:44.129Z"
---
Centroids from your clustering algorithm describe the 'average' of each cluster. Relevance AI allows you to query for a list of documents that are closest to the centroids of each cluster.

## What you will need to have
1. uploaded a dataset to Relevance AO
2. performed clustering and uploaded the results to Relevance AI
All these steps are explained in detail on [the quickstart clustering guide](doc:quickstart-clustering)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xq07v70SqJ3wUHXOzOLXtrFeSjNJJoJl?usp=sharing)


After clustering is done and the dataset is updated with the results, listing closest to centroids can be done via `list_closest_to_center` function as shown in the code snippet below where DATASET_ID refers to the name of the dataset, VECTOR_FIELD is the field based on which the clustering is done, and ALIAS is the name specified by the user to save the clustering results.
[block:code]
{
  "codes": [
    {
      "code": "closest_to_center = client.services.cluster.centroids.list_closest_to_center(\n  dataset_id = DATASET_ID, \n  vector_fields = [VECTOR_FIELD], \n  cluster_ids = [], # Leave this as an empty list if you want all of the clusters\n  alias = ALIAS,\n  page_size = 3\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]