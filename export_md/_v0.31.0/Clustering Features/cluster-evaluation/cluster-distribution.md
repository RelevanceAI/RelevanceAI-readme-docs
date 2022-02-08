---
title: "Cluster Distribution"
slug: "cluster-distribution"
hidden: false
createdAt: "2021-12-22T00:50:44.016Z"
updatedAt: "2022-01-27T02:24:54.049Z"
---
One way to evaluate clustering performance is to examine how well the vectors are distributed across the clusters. Depending on the individual use-case, success usually means a well spread out distribution of vectors across clusters. Optionally, if there is a field that can be used as ground truth, such a field can be used to examine the distribution of the ground truth across individual clusters. This can help drive decision making around hyperparameters of clustering including the number of clusters and clustering methodology.

## Code Example
The following code examines how the clusters are distributed, firstly, within themselves, and then against a ground truth label *category* (i.e. *category* is one of the fields in the dataset). Ideally, there is a clear ground truth in each cluster category. Note that the following code samples are to run after clustering is done on a dataset as was explained at [Clustering](https://docs.relevance.ai/docs/quickstart-k-means).
```python Python (SDK)
DATASET_ID = 'quickstart_clustering'
VECTOR_FIELD = 'product_image_clip_vector_'
k = 10 # number of clusters
ALIAS = 'kmeans_'+str(k)

# Cluster Distribution
client.vector_tools.cluster.distribution(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS
)

```
```python
```

<figure>
<img src="https://files.readme.io/43a90fd-Screen_Shot_2022-01-27_at_11.47.09_am.png" width="261" alt="Screen Shot 2022-01-27 at 11.47.09 am.png" />
<figcaption>Cluster distribution</figcaption>
<figure>
Cluster against ground truth distribution
```python Python (SDK)
DATASET_ID = 'quickstart_clustering'
VECTOR_FIELD = 'product_image_clip_vector_'
GROUND_TRUTH_FIELD = 'query'
k = 10 # number of clusters
ALIAS = 'kmeans_'+str(k)


# Cluster against Ground Truth Distribution
client.vector_tools.cluster.distribution(
 dataset_id = DATASET_ID,
 vector_field = VECTOR_FIELD,
 cluster_alias = ALIAS,
 ground_truth_field = GROUND_TRUTH_FIELD
)
```
```python
```

<figure>
<img src="https://files.readme.io/0d9d70a-Screen_Shot_2022-01-27_at_11.50.36_am.png" width="461" alt="Screen Shot 2022-01-27 at 11.50.36 am.png" />
<figcaption>Cluster distribution against ground truth</figcaption>
<figure>
