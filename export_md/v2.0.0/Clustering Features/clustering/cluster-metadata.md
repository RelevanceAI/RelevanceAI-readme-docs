---
title: "Cluster Metadata"
slug: "cluster-metadata"
hidden: false
createdAt: "2021-12-02T14:01:15.693Z"
updatedAt: "2022-03-24T02:52:13.738Z"
---
Relevance AI allows you to insert additional information (e.g. total number of clusters) into your clustering results. This information is referred to as metadata in Relevance AI.

## What you will need to have
1. uploaded a dataset to Relevance AO
2. performed clustering and uploaded the results to Relevance AI
All these steps are explained in detail on [the quickstart clustering guide](doc:quickstart-clustering)

## Code Example

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Clustering-Metadata.ipynb)


The following code snippets extract the metadata from the clustering algorithm and adds this information to Relevance AI where DATASET_ID refers to the name of the dataset, VECTOR_FIELD is the field based on which the clustering is done, and ALIAS is the name specified by the user to save the clustering results.

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

Once you have stored the metadata, you can view them using the following code.

```python Python (SDK)
df = client.Dataset(DATASET_ID)

clusterer = df.auto_cluster('kmeans_10', ['product_title_clip_vector_'])
```
```python
```