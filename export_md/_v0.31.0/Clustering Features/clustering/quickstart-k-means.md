---
title: "Quickstart (K Means)"
slug: "quickstart-k-means"
hidden: false
createdAt: "2021-12-10T01:56:27.206Z"
updatedAt: "2022-01-24T06:24:19.933Z"
---
<figure>
<img src="https://files.readme.io/022192b-8a1c5e7-Frame_6.png" width="742" alt="8a1c5e7-Frame_6.png" />
<figcaption>Clustering showing how a certain variety of images can improve pricing</figcaption>
<figure>
## Introduction

Clustering groups items so that those in the same group/cluster have meaningful similarities (i.e. specific features or properties). Clustering facilitates informed decision-making by giving significant meaning to data through the identification of different patterns. Relying on strong vector representations, Relevance AI provides you with powerful and easy-to-use clustering endpoints.

In this guide, you will learn to run KMeans clustering via **only one line of code**. K-Means clustering partitions your dataset into K distinct clusters.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Laa19J1QdWpjY2j35J1zgY9V6EPVKCSg?usp=sharing)

### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with RelevanceAI. For more information, please read the [installation](doc:installation) guide.

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
You also need to have a dataset under your Relevance AI account. You can either use our dummy sample data as shown in this step or follow the tutorial on [how to create your own dataset](https://docs.relevance.ai/docs/creating-a-dataset-prerequisites).

In this guide, we use our e-commerce database, which includes fields such as `product_name`, as well as the vectorized version of the field `product_name_default_vector_`. Loading these documents can be done via:
```python Python (SDK)
from relevanceai.datasets import get_dummy_ecommerce_dataset

documents = get_dummy_ecommerce_dataset()
```
```python
```
Next, we can upload these documents into your personal Relevance AI account under the name *quickstart_clustering_kmeans*
```python Python (SDK)
DATASET_ID = 'quickstart_clustering_kmeans'
client.insert_documents(dataset_id=DATASET_ID, docs=documents)
```
```python
```
Let's have a look at the schema to see what vector fields are available for clustering.
```python Python (SDK)
client.datasets.schema(dataset_id)
```
```python
```
The result is a JSON output similar to what is shown below. As can be seen, there are two vector fields in the dataset `product_image_clip_vector_` and `product_title_clip_vector_`.
```json Python (SDK)
{
 'insert_date_': 'date',
 'product_image': 'text',
 'product_image_clip_vector_': {'vector': 512},
 'product_link': 'text',
 'product_price': 'text',
 'product_title': 'text',
 'product_title_clip_vector_': {'vector': 512},
 'query': 'text',
 'source': 'text'
}
```
```json
```
### 2. Run Kmeans clustering algorithm in one go
Number of clusters or the K parameter in the K-means algorithm is set to 10 by default but it can be changed via the `k` argument.
The `kmeans_cluster()` function receives `dataset_id`, a list of vectors to be used for clustering (`vector_fields`), number of clusters (`k`) and a name to be used to save the clustering results (`alias`).
```python Python (SDK)

# Vector field based on which clustering is done
VECTOR_FIELD = 'product_title_clip_vector_'

# number of clusters
KMEAN_NUMBER_OF_CLUSTERS = 10
ALIAS = 'kmeans_'+str(KMEAN_NUMBER_OF_CLUSTERS)

client.vector_tools.cluster.kmeans_cluster(
 dataset_id = DATASET_ID,
 vector_fields = [VECTOR_FIELD],
 k = KMEAN_NUMBER_OF_CLUSTERS,
 alias = ALIAS
)
```
```python
```
The `kmeans_cluster()` function performs the following steps:
1. loading the data
2. clustering
3. writing the results back to the dataset

By loading the data from the dataset after clustering is done, you can see to which cluster each data point belongs. Here, we see how the first 5 data points are clustered:
```python Python (SDK)
from relevanceai import show_json

sample_documents = client.datasets.documents.list(DATASET_ID, page_size=5)
samples = [{
 "product_name":d["product_name"],
 "cluster":d["_cluster_"][VECTOR_FIELD][ALIAS]
} for d in sample_documents["documents"]]

show_json(samples, text_fields=["product_name", "cluster"])
```
```python
```

<figure>
<img src="https://files.readme.io/a711fd7-Screen_Shot_2021-12-10_at_3.04.50_pm.png" width="469" alt="Screen Shot 2021-12-10 at 3.04.50 pm.png" />
<figcaption>Clustering results fetched back from a dataset</figcaption>
<figure>
If you are interested to know more details about what happens behind the scene, visit our next page on step-by-step clustering.
