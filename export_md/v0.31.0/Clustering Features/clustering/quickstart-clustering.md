---
title: "Quickstart (step by step)"
slug: "quickstart-clustering"
excerpt: "Get started with clustering in a few minutes!"
hidden: false
createdAt: "2021-11-26T10:21:47.021Z"
updatedAt: "2022-01-24T06:26:11.281Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8a1c5e7-Frame_6.png",
        "Frame 6.png",
        742,
        402,
        "#e8eaec"
      ],
      "caption": "Clustering showing how a certain variety of images can improve pricing",
      "sizing": "80"
    }
  ]
}
[/block]
## Introduction

Clustering groups items so that those in the same group/cluster have meaningful similarities (i.e. specific features or properties). Clustering facilitates informed decision-making by giving significant meaning to data through the identification of different patterns. Relying on strong vector representations, Relevance AI provides you with powerful and easy-to-use clustering endpoints.

In this guide, you will learn to run clustering based on the K-Means algorithm which aims to partition your dataset into K distinct clusters.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15fXlU8hGQ6oysCJEbAlIjtJGkTaCNlT-?usp=sharing)

### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with RelevanceAI. For more information, please read the [installation](doc:installation) guide.
[block:code]
{
  "codes": [
    {
      "code": "pip install -U RelevanceAI==0.27.0",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \n\n\"\"\"\nRunning this cell will provide you with \nthe link to sign up/login page where you can find your credentials.\nOnce you have signed up, click on the value under `Authorization token` \nin the API tab\nand paste it in the appreared Auth token box below\n\"\"\"\n\nclient = Client()",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
You also need to have a dataset under your Relevance AI account. You can either use our dummy sample data as shown in this step or follow the tutorial on [how to create your own dataset](https://docs.relevance.ai/docs/creating-a-dataset-prerequisites).

In this guide, we use our e-commerce database, which includes fields such as `product_name`, as well as the vectorized version of the field `product_name_default_vector_`. Loading these documents can be done via:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.datasets import get_dummy_ecommerce_dataset\n\ndocuments = get_dummy_ecommerce_dataset()",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Next, we can upload these documents into your personal Relevance AI account under the name *quickstart_clustering_kmeans*
[block:code]
{
  "codes": [
    {
      "code": "DATASET_ID = 'quickstart_clustering_kmeans-sbs'\nclient.insert_documents(dataset_id=DATASET_ID, docs=documents)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Let's have a look at the schema to see what vector fields are available for clustering.

[block:code]
{
  "codes": [
    {
      "code": "client.datasets.schema(dataset_id)",
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
      "language": "json"
    }
  ]
}
[/block]
### 2. Run clustering algorithm

To run KMeans Clustering, we need to first define a clustering object, KMeans, which loads the clustering algorithm with a specified number of clusters.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.vector_tools.cluster import KMeans\n\nKMEAN_NUMBER_OF_CLUSTERS = 10\nclusterer = KMeans(k=KMEAN_NUMBER_OF_CLUSTERS)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

Next, the algorithm is fitted on the vector field, *product_title_clip_vector_*, to distinguish between clusters. The cluster to which each document belongs is returned.

[block:code]
{
  "codes": [
    {
      "code": "ALIAS = 'kmeans_'+str(KMEAN_NUMBER_OF_CLUSTERS)\n\nVECTOR_FIELD = \"product_title_clip_vector_\"\nclustered_documents = clusterer.fit_documents(\n    vector_fields = [VECTOR_FIELD], # Cluster 1 field\n    docs = documents,\n    return_only_clusters = True, # If True, return only clusters\n    alias = ALIAS\n)",
      "language": "python",
      "name": "Python (SDK)"
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
      "code": "client.update_documents(dataset_id=DATASET_ID, docs=clustered_documents)",
      "language": "python",
      "name": "Python (SDK)"
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
      "code": "centers = clusterer.get_centroid_documents()\n\nclient.services.cluster.centroids.insert(\n    dataset_id = DATASET_ID,\n    cluster_centers = centers,\n    vector_fields = [VECTOR_FIELD],\n    alias = ALIAS\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Once you have stored the cluster centroids, you can view them using the following code.
[block:code]
{
  "codes": [
    {
      "code": "client.services.cluster.centroids.list(\n    dataset_id = DATASET_ID,\n    vector_fields = [VECTOR_FIELD],\n    page_size = 10,\n    include_vector = False,\n    alias = ALIAS\n)\n\ncluster_centroids['documents'][0]['_id']",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Downloading a few sample documents from the dataset, we show to which cluster they belong:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import show_json\n\nsample_documents = client.datasets.documents.list(DATASET_ID, page_size=5)\nsamples = [{\n    'product_title':d['product_title'],\n    'cluster':d['_cluster_'][VECTOR_FIELD][ALIAS]\n} for d in sample_documents[\"documents\"]]\n\nshow_json(samples, text_fields=['product_title', 'cluster'])",
      "language": "python"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dbe68e0-Screen_Shot_2022-01-24_at_1.57.57_pm.png",
        "Screen Shot 2022-01-24 at 1.57.57 pm.png",
        461,
        192,
        "#eaeaea"
      ],
      "caption": "Showing to which cluster each of the first 5 documents belong."
    }
  ]
}
[/block]