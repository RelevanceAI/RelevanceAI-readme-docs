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
-> ## Code Example
The following code examines metrics of clusters through the Silhouette Score and Rand Score. If a ground truth is not provided, only the Silhouette Score is shown.
```python Python (SDK)
DATASET_ID = 'quickstart_clustering'
VECTOR_FIELD = 'product_image_clip_vector_'
GROUND_TRUTH_FIELD = 'query'
k = 10 # number of clusters
ALIAS = 'kmeans_'+str(k)

client.vector_tools.cluster.metrics(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS,
 ground_truth_field = GROUND_TRUTH_FIELD
)

```
```python
```

<figure>
<img src="https://files.readme.io/914c066-Screen_Shot_2022-01-27_at_11.51.50_am.png" width="170" alt="Screen Shot 2022-01-27 at 11.51.50 am.png" />
<figcaption>Cluster metrics</figcaption>
<figure>
