---
title: "Quickstart (step by step)"
slug: "quickstart-clustering"
excerpt: "Get started with clustering in a few minutes!"
hidden: false
createdAt: "2021-11-26T10:21:47.021Z"
updatedAt: "2022-01-24T06:26:11.281Z"
---

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs_template/CLUSTERING_FEATURES/_assets/RelevanceAI_clustering.png?raw=true"  width="450" alt="Clustering effect on pricing" />
<figcaption>Clustering showing how a certain variety of images can improve pricing</figcaption>
<figure>

## Introduction

Clustering groups items so that those in the same group/cluster have meaningful similarities (i.e. specific features or properties). Clustering facilitates informed decision-making by giving significant meaning to data through the identification of different patterns. Relying on strong vector representations, Relevance AI provides you with powerful and easy-to-use clustering endpoints.

In this guide, you will learn to run clustering based on the K-Means algorithm which aims to partition your dataset into K distinct clusters.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs/CLUSTERING_FEATURES/clustering/_notebooks/RelevanceAI-ReadMe-Kmeans-Clustering-Step-by-Step.ipynb)

### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with RelevanceAI. For more information, please read the [installation](doc:installation) guide.

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

You also need to have a dataset under your Relevance AI account. You can either use our dummy sample data as shown in this step or follow the tutorial on [how to create your own dataset](doc:project-and-dataset).

In this guide, we use our e-commerce database, which includes fields such as `product_name`, as well as the vectorized version of the field `product_name_default_vector_`. Loading these documents can be done via:

@@@ get_ecommerce_dataset_encoded @@@

Next, we can upload these documents into your personal Relevance AI account under the name *quickstart_clustering_kmeans*

@@@ quickstart_docs; dataset_basics, DATASET_ID=QUICKSTART_KMEANS_CLUSTERING_DATASET_ID @@@

Let's have a look at the schema to see what vector fields are available for clustering.

@@@ dataset_schema @@@

The result is a JSON output similar to what is shown below. As can be seen, there are two vector fields in the dataset `product_image_clip_vector_` and `product_title_clip_vector_`.

@@@ ecommerce_dataset_encoded_schema @@@

### 2. Run clustering algorithm

To run KMeans Clustering, we need to first define a clustering object, `KMeansModel`, which loads the clustering algorithm with a specified number of clusters.

@@@  clusterops, VECTOR_FIELD=PRODUCT_TITLE_CLIP_VEC, N_KMEANS=5 @@@

Next, the algorithm is fitted on the vector field, *product_title_clip_vector_*, to distinguish between clusters. The cluster to which each document belongs is returned.

@@@ clusterops_fit_predict_documents, VECTOR_FIELDS=['product_title_clip_vector_'] @@@


### 3. Update the dataset with the cluster labels

Finally, these categorised documents are uploaded back to the dataset as an additional field.

@@@ upsert_documents, DOCUMENTS=clustered_docs@@@

### 4. Insert the cluster centroids

Get the centroid's vector and insert them as centroids into Relevance AI.

@@@ get_centroid_documents; insert_centroid_documents @@@

Downloading a few sample documents from the dataset, we show to which cluster they belong:

@@@ cluster_sample_results, N_SAMPLES=5, VECTOR_FIELD=VECTOR_FIELD, ALIAS=ALIAS, TEXT_FIELDS=['product_title', 'cluster'] @@@
