---
title: "Quickstart"
slug: "cluster-evaluate"
excerpt: "Evaluate your clusters 5 quick steps"
hidden: true
createdAt: "2021-12-22T00:47:17.465Z"
updatedAt: "2022-03-24T02:52:13.644Z"
---
## Introduction

There are several ways to evaluate the success of a clustering algorithm. Broadly speaking, they can be categorised into internal and external methods:
1. Internal methods that examine how much variation is explained in clusters
2. External methods that compare the clusters to ground truth.

Relevance AI provides you with the tools to perform all these analyses. The results of this analysis should be used to decide on the hyperparameters of your clustering algorithm,  including the number of clusters and clustering methodology.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/cluster-evaluation/_notebooks/RelevanceAI-ReadMe-Cluster-Metrics.ipynb)


### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with Relevance AI.

```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==2.0.0
```
```bash
```

```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Activation token` and paste it here
"""
client = Client()
```
```python
```


You also need to have a dataset under your Relevance AI account. You can either use our ecommerce sample data as shown in this step or follow the tutorial on [how to create your own dataset](doc:project-and-dataset). Running the code below, the fetched documents will be uploaded into your personal Relevance AI account under the name *quickstart_clustering*.

```python Python (SDK)
from relevanceai.datasets import get_ecommerce_dataset_encoded

documents = get_ecommerce_dataset_encoded()
{k:v for k, v in documents[0].items() if '_vector_' not in k}
```
```python
```

```python Python (SDK)
df = client.Dataset("quickstart_kmeans_clustering")
df.insert_documents(documents)
```
```python
```

```python Python (SDK)
df.health
```
```python
```

### 2. Run Kmeans clustering algorithm
The following code clusters the *product_image_clip_vector_* field using the KMeans algorithm. For more information, see [Quickstart (K means)](doc:quickstart-k-means)].


```python Python (SDK)
from relevanceai.clusterer import KMeansModel

VECTOR_FIELD = "product_title_clip_vector_"
KMEAN_NUMBER_OF_CLUSTERS = 10
ALIAS = "kmeans_" + str(KMEAN_NUMBER_OF_CLUSTERS)

model = KMeansModel(k=KMEAN_NUMBER_OF_CLUSTERS)
clusterer = client.ClusterOps(alias=ALIAS, model=model)
clusterer.fit_predict_update(df, [VECTOR_FIELD])
```
```python
```

### 3. Cluster evaluation

```python Python (SDK)
clusterer.evaluate()
```
```python
```