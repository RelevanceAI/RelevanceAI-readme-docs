---
title: "Centroids"
slug: "inserting-centroids"
excerpt: "How to insert/read your cluster centroids into/from Relevance AI"
hidden: false
createdAt: "2021-12-02T14:00:02.849Z"
updatedAt: "2022-01-24T04:32:36.426Z"
---
Centroids from your clustering algorithm describe the 'average' of each cluster. You can insert these centroids into RelevanceAI to facilitate:

- Future acceleration of vector search
- Identification of the cluster to which a new document belongs
- Storing the centroid vectors with relevant metadata such as a topic


## Insert centroids
You will need to have
1. uploaded a dataset to Relevance AO
2. performed clustering and uploaded the results to Relevance AI
3. Have the centroids ready to be inserted into the dataset
These steps are all included on [step-by-step Kmeans clustering](https://docs.relevance.ai/docs/quickstart-clustering) page.

The following code snippet gets the centroids from a clustering object and adds them to the corresponding dataset on RelevanceAI's platform. `DATASET_ID` refers to the name of the dataset, `VECTOR_FIELD` is the field based on which the clustering is done, and ALIAS is the name specified by the user to save the clustering results.

[block:code]
{
  "codes": [
    {
      "code": "centroids = clusterer.get_centroid_documents()\n\n\nclusterer.insert_centroid_documents(centroids, df)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

