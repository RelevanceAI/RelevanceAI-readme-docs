---
title: "Cluster Metrics"
slug: "cluster-metrics"
hidden: false
createdAt: "2021-12-22T00:51:39.184Z"
updatedAt: "2022-01-27T02:25:16.192Z"
---
There are two key metrics for evaluating clustering success, the **Silhouette Score** and **Rand Index**. The **Silhouette Score** is an internal metric based on the clustering itself while the **Rand Index** is an external metric comparing the clustering to ground truth.

Successful clustering results in clusters which are highly separated and elements within which are highly cohesive.

- **Silhouette Score** is a score within (-1 to 1) that calculates the average cohesion and separation of each element, with 1 meaning clustered perfectly, 0 meaning indifferent and -1 meaning clustered the wrong way.

Good clusters have elements, which, when paired, pairs belong to the same cluster label with the same ground truth label.


- **Rand Index** is a score ranging from 0 to 1 that represents the percentage of element pairs that have a matching cluster and ground truth labels. Rand Index score 1 shows perfect matching while 0 represent random matching. *Note: This measure is adjusted for randomness so does not equal the exact numerical percentage.*
[block:api-header]
{
  "title": "Code Example"
}
[/block]
The following code examines metrics of clusters through the Silhouette Score and Rand Score. If a ground truth is not provided, only the Silhouette Score is shown.
[block:code]
{
  "codes": [
    {
      "code": "DATASET_ID = 'quickstart_clustering'\nVECTOR_FIELD = 'product_image_clip_vector_'\nGROUND_TRUTH_FIELD = 'query'\nk = 10 # number of clusters\nALIAS = 'kmeans_'+str(k)\n\nclient.vector_tools.cluster.metrics(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS, \n  ground_truth_field = GROUND_TRUTH_FIELD\n)\n",
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
        "https://files.readme.io/914c066-Screen_Shot_2022-01-27_at_11.51.50_am.png",
        "Screen Shot 2022-01-27 at 11.51.50 am.png",
        170,
        196,
        "#f2f2f2"
      ],
      "caption": "Cluster metrics"
    }
  ]
}
[/block]