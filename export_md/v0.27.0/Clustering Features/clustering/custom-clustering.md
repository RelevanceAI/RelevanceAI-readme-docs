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

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18pnwrOhoCZP_hyikPoSU9fiaTUsd7_pA?usp=sharing)

## Code Example
The following code shows
1. an example of a custom clustering algorithm that chooses randomly between Cluster 0 and Cluster 1
2. how to call`fit_documents` to preform clustering
3. how to update the dataset with the results
[block:code]
{
  "codes": [
    {
      "code": "# Inherit from ClusterBase to keep all the goodies! \nfrom relevanceai.vector_tools.cluster import ClusterBase\nclass CustomCluster(ClusterBase):\n    def fit_transform(self, vectors):\n        import random\n        return [random.randint(0, 1) for i in vectors]\nclusterer = CustomCluster()\n\n# Fit documents\ncustom_documents = clusterer.fit_documents(\n  vector_fields = [CUSTOM_VECTOR_FIELD], \n  documents = custom_documents,\n  # If True, return only clusters to be updated\n  return_only_clusters = True \n)\n\n# Update documents\nclient.update_documents(DATASET_ID, custom_documents)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]