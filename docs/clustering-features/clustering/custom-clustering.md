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

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/heads/v2.0.0/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Custom-Clustering.ipynb)

## Code Example

**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/heads/v2.0.0/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Custom-Clustering.ipynb)

The following code shows
1. an example of a custom clustering algorithm that chooses randomly between Cluster 0 and Cluster 1
2. how to call`fit_documents` to preform clustering
3. how to update the dataset with the results


[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset('faiss_kmeans_clustering')\n# Inherit from ClusterBase to keep all the goodies!\nimport numpy as np\nfrom faiss import Kmeans\nfrom relevanceai import CentroidClusterBase\n\nclass FaissKMeans(CentroidClusterBase):\n    def __init__(self, model):\n        self.model = model\n\n    def fit_predict(self, vectors):\n        vectors = np.array(vectors).astype(\"float32\")\n        self.model.train(vectors)\n        cluster_labels = self.model.assign(vectors)[1]\n        return cluster_labels\n\n    def metadata(self):\n        return self.model.__dict__\n\n    def get_centers(self):\n        return self.model.centroids\n\nn_clusters = 10\nd = 512\nalias = f\"faiss-kmeans_{n_clusters}\"\nvector_fields = ['product_title_clip_vector_']\n\nmodel = FaissKMeans(model=Kmeans(d=d, k=n_clusters))\nclusterer = client.ClusterOps(model=model, alias=alias)\nclusterer.fit_predict_update(dataset=df, vector_fields=vector_fields)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

