---
title: "Quickstart (K Means)"
slug: "quickstart-k-means"
hidden: false
createdAt: "2021-12-10T01:56:27.206Z"
updatedAt: "2022-02-01T00:54:13.875Z"
---

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/clustering-features/_assets/RelevanceAI_clustering.png?raw=true"  width="450" alt="Clustering effect on pricing" />
<figcaption>Clustering showing how a certain variety of images can improve pricing</figcaption>
<figure>

## Introduction

Clustering groups items so that those in the same group/cluster have meaningful similarities (i.e. specific features or properties). Clustering facilitates informed decision-making by giving significant meaning to data through the identification of different patterns. Relying on strong vector representations, Relevance AI provides you with powerful and easy-to-use clustering endpoints.

In this guide, you will learn to run KMeans clustering via **only one line of code**. K-Means clustering partitions your dataset into K distinct clusters.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Kmeans-Clustering.ipynb)

### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with RelevanceAI. For more information, please read the [installation](doc:installation) guide.

@@@ relevanceai_installation , RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

You also need to have a dataset under your Relevance AI account. You can either use our sample sample data as shown in this step or follow the tutorial on [how to create your own dataset](doc:project-and-dataset).

In this guide, we use our e-commerce database, which includes fields such as `product_name`, as well as the vectorized version of the field `product_name_default_vector_`. Loading these documents can be done via:

@@@ get_ecommerce_dataset_encoded @@@

Next, we can upload these documents into your personal Relevance AI account under the name *quickstart_clustering_kmeans*

@@@ dataset_basics, DATASET_ID=QUICKSTART_KMEANS_CLUSTERING_DATASET_ID @@@

Let's have a look at the schema to see what vector fields are available for clustering.

@@@ dataset_schema @@@

The result is a JSON output similar to what is shown below. As can be seen, there are two vector fields in the dataset `product_image_clip_vector_` and `product_title_clip_vector_`.

@@@ ecommerce_dataset_encoded_schema @@@

### 2. Run Kmeans clustering algorithm in one go
The easiest way to run a Kmeans clustering algorithm under the Relevance AI platform is the `auto_cluster` function. The following code snippet shows how generate 10 clusters using the `product_title_clip_vector_` vector field.

@@@ kmeans_cluster, N_CLUSTERS=10,  VECTOR_FIELD=PRODUCT_TITLE_CLIP_VEC @@@

Another way of clustering is to use the ClusterOps class as shown in the snippet below:

@@@ clusterops, VECTOR_FIELD=PRODUCT_TITLE_CLIP_VEC, N_KMEANS=10, DATASET_ID=QUICKSTART_KMEANS_CLUSTERING_DATASET_ID @@@


This performs the following steps:
1. loading the data
2. clustering
3. writing the results back to the dataset

By loading the data from the dataset after clustering is done, you can see to which cluster each data point belongs. Here, we see how the first 5 data points are clustered:

@@@ cluster_sample_results, N_SAMPLES=5, VECTOR_FIELD=VECTOR_FIELD, ALIAS=ALIAS, TEXT_FIELDS=['product_title', 'cluster'] @@@

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/clustering-features/_assets/RelevanceAI_clustering_quickstart_kmeans_results.png?raw=true"  width="450" alt="Clustering results" />
<figcaption></figcaption>
<figure>

If you are interested to know more details about what happens behind the scene, visit our next page on step-by-step clustering.