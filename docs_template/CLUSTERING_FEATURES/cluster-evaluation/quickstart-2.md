---
title: "Quickstart"
slug: "cluster-evaluate"
excerpt: "Evaluate your clusters 5 quick steps"
hidden: true
createdAt: "2021-12-22T00:47:17.465Z"
updatedAt: "2022-01-27T00:56:39.533Z"
---
## Introduction

There are several ways to evaluate the success of a clustering algorithm. Broadly speaking, they can be categorised into internal and external methods:
1. Internal methods that examine how much variation is explained in clusters
2. External methods that compare the clusters to ground truth.

Relevance AI provides you with the tools to perform all these analyses. The results of this analysis should be used to decide on the hyperparameters of your clustering algorithm,  including the number of clusters and clustering methodology.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.1.4-search/docs/CLUSTERING_FEATURES/cluster-evaluation/_notebooks/RelevanceAI-ReadMe-Cluster-Metrics.ipynb)


### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with Relevance AI.

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@


You also need to have a dataset under your Relevance AI account. You can either use our ecommerce sample data as shown in this step or follow the tutorial on [how to create your own dataset](https://docs.relevance.ai/docs/creating-a-dataset-prerequisites). Running the code below, the fetched documents will be uploaded into your personal Relevance AI account under the name *quickstart_clustering*.

@@@ get_ecommerce_dataset_encoded @@@

@@@ dataset_basics, DATASET_ID=QUICKSTART_KMEANS_CLUSTERING_DATASET_ID @@@

@@@ dataset_health @@@

### 2. Run Kmeans clustering algorithm
The following code clusters the *product_image_clip_vector_* field using the KMeans algorithm. For more information, see [Quickstart (K means)](doc:quickstart-k-means)].


@@@ clusterops_fit_predict_update, VECTOR_FIELD=PRODUCT_TITLE_CLIP_VEC, N_KMEANS=10 @@@

### 3. Cluster evaluation

@@@ evaluate @@@


