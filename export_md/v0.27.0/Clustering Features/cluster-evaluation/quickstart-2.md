---
title: "Quickstart"
slug: "quickstart-2"
excerpt: "Evaluate your clusters 5 quick steps"
hidden: false
createdAt: "2021-12-22T00:47:17.465Z"
updatedAt: "2022-01-27T00:56:39.533Z"
---
## Introduction

There are several ways to evaluate the success of a clustering algorithm. Broadly speaking, they can be categorised into internal and external methods:
1. Internal methods that examine how much variation is explained in clusters
2. External methods that compare the clusters to ground truth.

Relevance AI provides you with the tools to perform all these analyses. The results of this analysis should be used to decide on the hyperparameters of your clustering algorithm,  including the number of clusters and clustering methodology.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o2eJhBT7lNyb_Yh7msrBMMQuJBgIdlRf?usp=sharing)


### 1. Create a dataset and insert data

First, you need to install Relevance AI's Python SDK and set up a client object to interact with Relevance AI.
[block:code]
{
  "codes": [
    {
      "code": "pip install -U RelevanceAI==0.27.0",
      "language": "shell",
      "name": "Python (SDK)"
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
You also need to have a dataset under your Relevance AI account. You can either use our dummy sample data as shown in this step or follow the tutorial on [how to create your own dataset](https://docs.relevance.ai/docs/creating-a-dataset-prerequisites). Running the code below, the fetched documents will be uploaded into your personal Relevance AI account under the name *quickstart_clustering*.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.datasets import get_dummy_ecommerce_dataset\n\ndocuments = get_dummy_ecommerce_dataset()\n\nDATASET_ID = 'quickstart_clustering'\nclient.insert_documents(dataset_id=DATASET_ID, docs=documents)",
      "language": "python",
      "name": "Python (SDK)"
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
      "code": "VECTOR_FIELD = 'product_image_clip_vector_'\nk = 10\nALIAS = 'kmeans_'+str(k)\n\ncentroids = client.vector_tools.cluster.kmeans_cluster(\n    dataset_id = DATASET_ID, \n    vector_fields=[VECTOR_FIELD],\n    k = k,\n    alias = ALIAS,\n    overwrite = True\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
### 3. View distribution of clusters
You can use the `distribution` function to examine how the clusters are distributed
1) within themselves and/or
2) against a ground truth field existing in the dataset.

This is shown in the two code snippets below respectively; ideally, each cluster would represent a different category.
[block:code]
{
  "codes": [
    {
      "code": "# Cluster Distribution\nALIAS = 'kmeans_'+str(k)\nclient.vector_tools.cluster.distribution(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c08ed54-Screen_Shot_2022-01-27_at_11.47.09_am.png",
        "Screen Shot 2022-01-27 at 11.47.09 am.png",
        261,
        187,
        "#f2f2f2"
      ],
      "caption": "Cluster distribution"
    }
  ]
}
[/block]
Here, we have chosen the field *category* in our dataset as the ground truth.
[block:code]
{
  "codes": [
    {
      "code": "# Select ground truth \nGROUND_TRUTH_FIELD = \"query\"\n\n# Cluster against Ground Truth Distribution\nclient.vector_tools.cluster.distribution(\n    dataset_id = DATASET_ID, \n    vector_field = VECTOR_FIELD, \n    cluster_alias = ALIAS,\n    ground_truth_field = GROUND_TRUTH_FIELD\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f799842-Screen_Shot_2022-01-27_at_11.50.36_am.png",
        "Screen Shot 2022-01-27 at 11.50.36 am.png",
        461,
        268,
        "#f1f1f1"
      ],
      "caption": "Cluster distribution using a ground truth"
    }
  ]
}
[/block]
### 4. View metrics of clusters
The following code examines metrics of clusters including the Silhouette Score, Rand Score, Homogeneity and Completeness, explanation of these metrics is provided at [Cluster Metrics](https://docs.relevance.ai/docs/cluster-metrics). If a ground truth is not provided, only the Silhouette Score is shown.
[block:code]
{
  "codes": [
    {
      "code": "import pandas as pd\n\n# Cluster Metrics\ncluster_metrics = client.vector_tools.cluster.metrics(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS, \n  ground_truth_field = GROUND_TRUTH_FIELD\n)\n\npd.set_option('display.max_colwidth', -1)\npd.DataFrame(cluster_metrics).style.hide_index()\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9533a68-Screen_Shot_2022-01-27_at_11.51.50_am.png",
        "Screen Shot 2022-01-27 at 11.51.50 am.png",
        170,
        196,
        "#f2f2f2"
      ],
      "caption": "Clustering scores and metrics"
    }
  ]
}
[/block]
### 5. Plot clusters
The following code plots a 3D dimension reduced version of the vectors, colour coded by clusters, and also optionally, the ground truth.
[block:code]
{
  "codes": [
    {
      "code": "# Plot Cluster\nclient.vector_tools.cluster.plot(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS, \n  ground_truth_field = GROUND_TRUTH_FIELD\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/11fc17c-Screen_Shot_2022-01-27_at_11.49.05_am.png",
        "Screen Shot 2022-01-27 at 11.49.05 am.png",
        864,
        727,
        "#fcfbfc"
      ],
      "caption": "Plot clusters"
    }
  ]
}
[/block]

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o2eJhBT7lNyb_Yh7msrBMMQuJBgIdlRf?usp=sharing)
[block:api-header]
{
  "title": "Put it all together"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "import pandas as pd\nfrom relevanceai import Client \nfrom relevanceai.datasets import get_dummy_ecommerce_dataset\n\n\"\"\"\nRunning this cell will provide you with \nthe link to sign up/login page where you can find your credentials.\nOnce you have signed up, click on the value under `Authorization token` \nin the API tab\nand paste it in the appreared Auth token box below\n\"\"\"\n\nclient = Client()\n\ndocuments = get_dummy_ecommerce_dataset()\n\nDATASET_ID = 'quickstart_clustering'\nclient.insert_documents(dataset_id=DATASET_ID, docs=documents)\n\n# Cluster vectors\nVECTOR_FIELD = 'product_image_clip_vector_'\nk = 10\nALIAS = 'kmeans_'+str(k)\n\ncentroids = client.vector_tools.cluster.kmeans_cluster(\n    dataset_id = DATASET_ID, \n    vector_fields=[VECTOR_FIELD],\n    k = k,\n    alias = ALIAS,\n    overwrite = True\n)\n\n# Cluster Distribution\nALIAS = 'kmeans_'+str(k)\nclient.vector_tools.cluster.distribution(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS\n)\n\n\n# Select ground truth \nGROUND_TRUTH_FIELD = \"query\"\n\n# Cluster against Ground Truth Distribution\nclient.vector_tools.cluster.distribution(\n    dataset_id = DATASET_ID, \n    vector_field = VECTOR_FIELD, \n    cluster_alias = ALIAS,\n    ground_truth_field = GROUND_TRUTH_FIELD\n)\n\n# Cluster Metrics\ncluster_metrics = client.vector_tools.cluster.metrics(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS, \n  ground_truth_field = GROUND_TRUTH_FIELD\n)\n\npd.set_option('display.max_colwidth', -1)\npd.DataFrame(cluster_metrics).style.hide_index()\n\n# Plot Cluster\nclient.vector_tools.cluster.plot(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS, \n  ground_truth_field = GROUND_TRUTH_FIELD\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]