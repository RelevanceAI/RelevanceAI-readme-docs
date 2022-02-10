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

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-clustering-feature/docs/CLUSTERING_FEATURES/clustering/_notebooks/RelevanceAI-ReadMe-Custom-Clustering.ipynb)

## Code Example
The following code shows
1. an example of a custom clustering algorithm that chooses randomly between Cluster 0 and Cluster 1
2. how to call`fit_documents` to preform clustering
3. how to update the dataset with the results


```

# Inherit from ClusterBase to keep all the goodies!
from relevanceai import ClusterBase

class CustomCluster(ClusterBase):
    def fit_predict(self, documents, vector_field, alias = 'random-clustering'):
        import random

        return [{'_cluster_': {vector_field: {alias: 'cluster-'+str(random.randint(0, 1))}},
                 '_id': document['_id']}
                for document in documents
        ]
clusterer = CustomCluster()


VECTOR_FIELD = "product_title_clip_vector_"
ALIAS = "random-clustering"
custom_docs = clusterer.fit_predict(
  vector_field = VECTOR_FIELD,
  documents=documents
)

df.upsert_documents(custom_docs)

```
```python
```