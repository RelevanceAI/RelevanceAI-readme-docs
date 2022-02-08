---
title: "Quickstart"
slug: "quickstart-2"
excerpt: "Evaluate your clusters 5 quick steps"
hidden: false
createdAt: "2021-12-22T00:47:17.465Z"
updatedAt: "2022-01-27T00:56:39.533Z"
---
## Introduction

There are several ways to evaluate the success of a clustering algorithm. Broadly speaking, they can be categorised into internal and external methods:
1. Internal methods that examine how much variation is explained in clusters
2. External methods that compare the clusters to ground truth.

Relevance AI provides you with the tools to perform all these analyses. The results of this analysis should be used to decide on the hyperparameters of your clustering algorithm,  including the number of clusters and clustering methodology.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o2eJhBT7lNyb_Yh7msrBMMQuJBgIdlRf?usp=sharing)


### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with Relevance AI.
```shell Python (SDK)
pip install -U RelevanceAI==0.27.0
```
```shell
```

```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the appreared Auth token box below
"""

client = Client()
```
```python
```
You also need to have a dataset under your Relevance AI account. You can either use our dummy sample data as shown in this step or follow the tutorial on [how to create your own dataset](https://docs.relevance.ai/docs/creating-a-dataset-prerequisites). Running the code below, the fetched documents will be uploaded into your personal Relevance AI account under the name *quickstart_clustering*.
```python Python (SDK)
from relevanceai.datasets import get_dummy_ecommerce_dataset

documents = get_dummy_ecommerce_dataset()

DATASET_ID = 'quickstart_clustering'
client.insert_documents(dataset_id=DATASET_ID, docs=documents)
```
```python
```
### 2. Run Kmeans clustering algorithm
The following code clusters the *product_image_clip_vector_* field using the KMeans algorithm. For more information, see [Quickstart (K means)](doc:quickstart-k-means)].
```python Python (SDK)
VECTOR_FIELD = 'product_image_clip_vector_'
k = 10
ALIAS = 'kmeans_'+str(k)

centroids = client.vector_tools.cluster.kmeans_cluster(
 dataset_id = DATASET_ID,
 vector_fields=[VECTOR_FIELD],
 k = k,
 alias = ALIAS,
 overwrite = True
)
```
```python
```
### 3. View distribution of clusters
You can use the `distribution` function to examine how the clusters are distributed
1) within themselves and/or
2) against a ground truth field existing in the dataset.

This is shown in the two code snippets below respectively; ideally, each cluster would represent a different category.
```python Python (SDK)
# Cluster Distribution
ALIAS = 'kmeans_'+str(k)
client.vector_tools.cluster.distribution(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS
)

```
```python
```

<figure>
<img src="https://files.readme.io/c08ed54-Screen_Shot_2022-01-27_at_11.47.09_am.png" width="261" alt="Screen Shot 2022-01-27 at 11.47.09 am.png" />
<figcaption>Cluster distribution</figcaption>
<figure>
Here, we have chosen the field *category* in our dataset as the ground truth.
```python Python (SDK)
# Select ground truth
GROUND_TRUTH_FIELD = "query"

# Cluster against Ground Truth Distribution
client.vector_tools.cluster.distribution(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS,
 ground_truth_field = GROUND_TRUTH_FIELD
)

```
```python
```

<figure>
<img src="https://files.readme.io/f799842-Screen_Shot_2022-01-27_at_11.50.36_am.png" width="461" alt="Screen Shot 2022-01-27 at 11.50.36 am.png" />
<figcaption>Cluster distribution using a ground truth</figcaption>
<figure>
### 4. View metrics of clusters
The following code examines metrics of clusters including the Silhouette Score, Rand Score, Homogeneity and Completeness, explanation of these metrics is provided at [Cluster Metrics](https://docs.relevance.ai/docs/cluster-metrics). If a ground truth is not provided, only the Silhouette Score is shown.
```python Python (SDK)
import pandas as pd

# Cluster Metrics
cluster_metrics = client.vector_tools.cluster.metrics(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS,
 ground_truth_field = GROUND_TRUTH_FIELD
)

pd.set_option('display.max_colwidth', -1)
pd.DataFrame(cluster_metrics).style.hide_index()

```
```python
```

<figure>
<img src="https://files.readme.io/9533a68-Screen_Shot_2022-01-27_at_11.51.50_am.png" width="170" alt="Screen Shot 2022-01-27 at 11.51.50 am.png" />
<figcaption>Clustering scores and metrics</figcaption>
<figure>
### 5. Plot clusters
The following code plots a 3D dimension reduced version of the vectors, colour coded by clusters, and also optionally, the ground truth.
```python Python (SDK)
# Plot Cluster
client.vector_tools.cluster.plot(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS,
 ground_truth_field = GROUND_TRUTH_FIELD
)

```
```python
```

<figure>
<img src="https://files.readme.io/11fc17c-Screen_Shot_2022-01-27_at_11.49.05_am.png" width="864" alt="Screen Shot 2022-01-27 at 11.49.05 am.png" />
<figcaption>Plot clusters</figcaption>
<figure>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o2eJhBT7lNyb_Yh7msrBMMQuJBgIdlRf?usp=sharing)
-> ## Put it all together

```python Python (SDK)
import pandas as pd
from relevanceai import Client
from relevanceai.datasets import get_dummy_ecommerce_dataset

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the appreared Auth token box below
"""

client = Client()

documents = get_dummy_ecommerce_dataset()

DATASET_ID = 'quickstart_clustering'
client.insert_documents(dataset_id=DATASET_ID, docs=documents)

# Cluster vectors
VECTOR_FIELD = 'product_image_clip_vector_'
k = 10
ALIAS = 'kmeans_'+str(k)

centroids = client.vector_tools.cluster.kmeans_cluster(
 dataset_id = DATASET_ID,
 vector_fields=[VECTOR_FIELD],
 k = k,
 alias = ALIAS,
 overwrite = True
)

# Cluster Distribution
ALIAS = 'kmeans_'+str(k)
client.vector_tools.cluster.distribution(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS
)


# Select ground truth
GROUND_TRUTH_FIELD = "query"

# Cluster against Ground Truth Distribution
client.vector_tools.cluster.distribution(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS,
 ground_truth_field = GROUND_TRUTH_FIELD
)

# Cluster Metrics
cluster_metrics = client.vector_tools.cluster.metrics(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS,
 ground_truth_field = GROUND_TRUTH_FIELD
)

pd.set_option('display.max_colwidth', -1)
pd.DataFrame(cluster_metrics).style.hide_index()

# Plot Cluster
client.vector_tools.cluster.plot(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS,
 ground_truth_field = GROUND_TRUTH_FIELD
)

```
```python
```
