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

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/cluster-evaluation/_notebooks/RelevanceAI-ReadMe-Cluster-Metrics.ipynb)

### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with Relevance AI.

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==2.0.0",
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


You also need to have a dataset under your Relevance AI account. You can either use our ecommerce sample data as shown in this step or follow the tutorial on [how to create your own dataset](doc:project-and-dataset). Running the code below, the fetched documents will be uploaded into your personal Relevance AI account under the name *quickstart_clustering*.

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.utils.datasets import get_ecommerce_dataset_encoded\n\ndocuments = get_ecommerce_dataset_encoded()\n{k:v for k, v in documents[0].items() if '_vector_' not in k}",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset(\"quickstart_kmeans_clustering\")\nds.insert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "ds.health()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### 2. Run Kmeans clustering algorithm
The following code clusters the *product_image_clip_vector_* field using the KMeans algorithm. For more information, see [Quickstart (K means)](doc:quickstart-k-means)].


[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.clusterer import KMeansModel\n\nVECTOR_FIELD = \"product_title_clip_vector_\"\nKMEAN_NUMBER_OF_CLUSTERS = 10\nALIAS = \"kmeans_\" + str(KMEAN_NUMBER_OF_CLUSTERS)\n\nmodel = KMeansModel(k=KMEAN_NUMBER_OF_CLUSTERS)\nclusterer = client.ClusterOps(alias=ALIAS, model=model)\nclusterer.fit_predict_update(df, [VECTOR_FIELD])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### 3. Cluster evaluation

[block:code]
{
  "codes": [
    {
      "code": "clusterer.evaluate()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]



