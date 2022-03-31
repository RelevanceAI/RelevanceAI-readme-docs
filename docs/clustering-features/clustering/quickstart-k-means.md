---
title: "Quickstart (K Means)"
slug: "quickstart-k-means"
hidden: false
createdAt: "2021-12-10T01:56:27.206Z"
updatedAt: "2022-02-01T00:54:13.875Z"
---

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs_template/clustering-features/_assets/RelevanceAI_clustering.png?raw=true"  width="450" alt="Clustering effect on pricing" />
<figcaption>Clustering showing how a certain variety of images can improve pricing</figcaption>
<figure>

## Introduction

Clustering groups items so that those in the same group/cluster have meaningful similarities (i.e. specific features or properties). Clustering facilitates informed decision-making by giving significant meaning to data through the identification of different patterns. Relying on strong vector representations, Relevance AI provides you with powerful and easy-to-use clustering endpoints.

In this guide, you will learn to run KMeans clustering via **only one line of code**. K-Means clustering partitions your dataset into K distinct clusters.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs/clustering-features/clustering/_notebooks/RelevanceAI-ReadMe-Kmeans-Clustering.ipynb)

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

You also need to have a dataset under your Relevance AI account. You can either use our sample sample data as shown in this step or follow the tutorial on [how to create your own dataset](doc:project-and-dataset).

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
      "code": "ds = client.Dataset(\"quickstart_kmeans_clustering\")\nds.insert_documents(documents)",
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

### 2. Run Kmeans clustering algorithm in one go
The easiest way to run a Kmeans clustering algorithm under the Relevance AI platform is the `auto_cluster` function. The following code snippet shows how generate 10 clusters using the `product_title_clip_vector_` vector field.

[block:code]
{
  "codes": [
    {
      "code": "clusterer = ds.auto_cluster(ALIAS-10, [\"product_title_clip_vector_\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Another way of clustering is to use the ClusterOps class as shown in the snippet below:

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


The `fit_predict_update()` function performs the following steps:
1. loading the data
2. clustering
3. writing the results back to the dataset

By loading the data from the dataset after clustering is done, you can see to which cluster each data point belongs. Here, we see how the first 5 data points are clustered:

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

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs_template/clustering-features/_assets/RelevanceAI_clustering_quickstart_kmeans_results.png?raw=true"  width="450" alt="Clustering results" />
<figcaption></figcaption>
<figure>

If you are interested to know more details about what happens behind the scene, visit our next page on step-by-step clustering.
