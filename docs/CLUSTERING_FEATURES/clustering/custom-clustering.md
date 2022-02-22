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

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.1/docs/CLUSTERING_FEATURES/clustering/_notebooks/RelevanceAI-ReadMe-Custom-Clustering.ipynb)

## Code Example

**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.1/docs/CLUSTERING_FEATURES/clustering/_notebooks/RelevanceAI-ReadMe-Custom-Clustering.ipynb)

The following code shows
1. an example of a custom clustering algorithm that chooses randomly between Cluster 0 and Cluster 1
2. how to call`fit_documents` to preform clustering
3. how to update the dataset with the results


```python Python (SDK)
df = client.Dataset('faiss_kmeans_clustering')

# Inherit from ClusterBase to keep all the goodies!
import numpy as np
from faiss import Kmeans
from relevanceai import CentroidClusterBase

class FaissKMeans(CentroidClusterBase):
    def __init__(self, model):
        self.model = model

    def fit_predict(self, vectors):
        vectors = np.array(vectors).astype("float32")
        self.model.train(vectors)
        cluster_labels = self.model.assign(vectors)[1]
        return cluster_labels

    def metadata(self):
        return self.model.__dict__

    def get_centers(self):
        return self.model.centroids

n_clusters = 10
d = 512
alias = f"faiss-kmeans-{n_clusters}"
vector_fields = ['product_title_clip_vector_']

model = FaissKMeans(model=Kmeans(d=d, k=n_clusters))
clusterer = client.ClusterOps(model=model, alias=alias)
clusterer.fit_predict_update(dataset=df, vector_fields=vector_fields)
```
```python
```

