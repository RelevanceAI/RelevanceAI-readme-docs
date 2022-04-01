---
title: "Quickstart (step by step)"
slug: "quickstart-clustering"
excerpt: "Get started with clustering in a few minutes!"
hidden: false
createdAt: "2021-11-26T10:21:47.021Z"
updatedAt: "2022-01-24T06:26:11.281Z"
---

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs_template/clustering-features/_assets/RelevanceAI_clustering.png?raw=true"  width="450" alt="Clustering effect on pricing" />
<figcaption>Clustering showing how a certain variety of images can improve pricing</figcaption>
<figure>

## Introduction

Clustering groups items so that those in the same group/cluster have meaningful similarities (i.e. specific features or properties). Clustering facilitates informed decision-making by giving significant meaning to data through the identification of different patterns. Relying on strong vector representations, Relevance AI provides you with powerful and easy-to-use clustering endpoints.

In this guide, you will learn to run clustering based on the K-Means algorithm which aims to partition your dataset into K distinct clusters.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Kmeans-Clustering-Step-by-Step.ipynb)

### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with RelevanceAI. For more information, please read the [installation](doc:installation) guide.

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

You also need to have a dataset under your Relevance AI account. You can either use our dummy sample data as shown in this step or follow the tutorial on [how to create your own dataset](doc:project-and-dataset).

In this guide, we use our e-commerce database, which includes fields such as `product_name`, as well as the vectorized version of the field `product_name_default_vector_`. Loading these documents can be done via:

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

Next, we can upload these documents into your personal Relevance AI account under the name *quickstart_clustering_kmeans*

[block:code]
{
  "codes": [
    {
      "code": "documents = [\n\t{\"_id\": \"1\", \"example_vector_\": [0.1, 0.1, 0.1], \"data\": \"Documentation\"},\n\t{\"_id\": \"2\", \"example_vector_\": [0.2, 0.2, 0.2], \"data\": \"Best document!\"},\n\t{\"_id\": \"3\", \"example_vector_\": [0.3, 0.3, 0.3], \"data\": \"Document example\"},\n\t{\"_id\": \"5\", \"example_vector_\": [0.4, 0.4, 0.4], \"data\": \"This is a doc\"},\n\t{\"_id\": \"4\", \"example_vector_\": [0.5, 0.5, 0.5], \"data\": \"This is another doc\"},\n]\nds = client.Dataset(\"quickstart_kmeans_clustering\")\nds.insert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Let's have a look at the schema to see what vector fields are available for clustering.

[block:code]
{
  "codes": [
    {
      "code": "ds.schema",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

The result is a JSON output similar to what is shown below. As can be seen, there are two vector fields in the dataset `product_image_clip_vector_` and `product_title_clip_vector_`.

[block:code]
{
  "codes": [
    {
      "code": "{\n 'insert_date_': 'date',\n 'product_image': 'text',\n 'product_image_clip_vector_': {'vector': 512},\n 'product_link': 'text',\n 'product_price': 'text',\n 'product_title': 'text',\n 'product_title_clip_vector_': {'vector': 512},\n 'query': 'text',\n 'source': 'text'\n}",
      "name": "JSON",
      "language": "json"
    }
  ]
}
[/block]

### 2. Run clustering algorithm

To run KMeans Clustering, we need to first define a clustering object, `KMeansModel`, which loads the clustering algorithm with a specified number of clusters.

[block:code]
{
  "codes": [
    {
      "code": "from sklearn.cluster import KMeans\n\nVECTOR_FIELD = \"product_title_clip_vector_\"\nKMEAN_NUMBER_OF_CLUSTERS = 5\nALIAS = \"kmeans-\" + str(KMEAN_NUMBER_OF_CLUSTERS)\n\nmodel = KMeansModel(k=KMEAN_NUMBER_OF_CLUSTERS)\nclusterer = client.ClusterOps(alias=ALIAS, model=model)\nclusterer.operate(dataset_id=<<DATASET_ID>>, vector_fields=[\"product_title_clip_vector_\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Next, the algorithm is fitted on the vector field, *product_title_clip_vector_*, to distinguish between clusters. The cluster to which each document belongs is returned.

[block:code]
{
  "codes": [
    {
      "code": "clustered_docs = clusterer.fit_predict_documents(\n        vector_fields=['product_title_clip_vector_'],\n        documents=documents, inplace=False\n    )",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


### 3. Update the dataset with the cluster labels

Finally, these categorised documents are uploaded back to the dataset as an additional field.

[block:code]
{
  "codes": [
    {
      "code": "ds.upsert_documents(documents=clustered_docs)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### 4. Insert the cluster centroids

Get the centroid's vector and insert them as centroids into Relevance AI.

[block:code]
{
  "codes": [
    {
      "code": "centroids = clusterer.get_centroid_documents()\nclusterer.insert_centroid_documents(centroids, df)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Downloading a few sample documents from the dataset, we show to which cluster they belong:

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import show_json\n\nsample_documents = ds.sample(n=5)\nsamples = [{\n    'product_title':d['product_title'],\n    'cluster':d['_cluster_'][VECTOR_FIELD][ALIAS]\n} for d in sample_documents]\n\nshow_json(samples, text_fields=['product_title', 'cluster'])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

