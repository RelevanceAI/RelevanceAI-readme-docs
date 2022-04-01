---
title: "Cluster Metadata"
slug: "cluster-metadata"
hidden: false
createdAt: "2021-12-02T14:01:15.693Z"
updatedAt: "2022-01-24T06:35:28.286Z"
---
Relevance AI allows you to insert additional information (e.g. total number of clusters) into your clustering results. This information is referred to as metadata in Relevance AI.

## What you will need to have
1. uploaded a dataset to Relevance AO
2. performed clustering and uploaded the results to Relevance AI
All these steps are explained in detail on [the quickstart clustering guide](doc:quickstart-clustering)

## Code Example

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Clustering-Metadata.ipynb)


The following code snippets extract the metadata from the clustering algorithm and adds this information to Relevance AI where DATASET_ID refers to the name of the dataset, VECTOR_FIELD is the field based on which the clustering is done, and ALIAS is the name specified by the user to save the clustering results.

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==1.4.5",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n\"\"\"\nYou can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api\nOnce you have signed up, click on the value under `Activation token` and paste it here\n\"\"\"\nclient = Client()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Once you have stored the metadata, you can view them using the following code.

[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset(DATASET_ID)\nclusterer = ds.auto_cluster('kmeans_10', ['product_title_clip_vector_'])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

