---
title: "Cluster Distribution"
slug: "cluster-distribution"
hidden: false
createdAt: "2021-12-22T00:50:44.016Z"
updatedAt: "2022-01-27T02:24:54.049Z"
---
One way to evaluate clustering performance is to examine how well the vectors are distributed across the clusters. Depending on the individual use-case, success usually means a well spread out distribution of vectors across clusters. Optionally, if there is a field that can be used as ground truth, such a field can be used to examine the distribution of the ground truth across individual clusters. This can help drive decision making around hyperparameters of clustering including the number of clusters and clustering methodology.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/cluster-evaluation/_notebooks/RelevanceAI-ReadMe-Cluster-Distribution.ipynb)


## Code Example
The following code examines how the clusters are distributed, firstly, within themselves, and then against a ground truth label *category* (i.e. *category* is one of the fields in the dataset). Ideally, there is a clear ground truth in each cluster category. Note that the following code samples are to run after clustering is done on a dataset as was explained at [Clustering](https://docs.relevance.ai/docs/quickstart-k-means).
[block:code]
{
  "codes": [
    {
      "code": "DATASET_ID = 'quickstart_clustering'\nVECTOR_FIELD = 'product_image_clip_vector_'\nk = 10  # number of clusters\nALIAS = 'kmeans_'+str(k)\n\n# Cluster Distribution\nclient.vector_tools.cluster.distribution(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS\n)\n",
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
        "https://files.readme.io/43a90fd-Screen_Shot_2022-01-27_at_11.47.09_am.png",
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
Cluster against ground truth distribution
[block:code]
{
  "codes": [
    {
      "code": "DATASET_ID = 'quickstart_clustering'\nVECTOR_FIELD = 'product_image_clip_vector_'\nGROUND_TRUTH_FIELD = 'query'\nk = 10 # number of clusters\nALIAS = 'kmeans_'+str(k)\n\n\n# Cluster against Ground Truth Distribution\nclient.vector_tools.cluster.distribution(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS,\n  ground_truth_field = GROUND_TRUTH_FIELD\n)",
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
        "https://files.readme.io/0d9d70a-Screen_Shot_2022-01-27_at_11.50.36_am.png",
        "Screen Shot 2022-01-27 at 11.50.36 am.png",
        461,
        268,
        "#f1f1f1"
      ],
      "caption": "Cluster distribution against ground truth"
    }
  ]
}
[/block]
