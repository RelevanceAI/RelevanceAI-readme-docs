---
title: "Cluster Distribution"
slug: "cluster-distribution"
hidden: false
createdAt: "2021-12-22T00:50:44.016Z"
updatedAt: "2022-01-27T02:24:54.049Z"
---
One way to evaluate clustering performance is to examine how well the vectors are distributed across the clusters. Depending on the individual use-case, success usually means a well spread out distribution of vectors across clusters. Optionally, if there is a field that can be used as ground truth, such a field can be used to examine the distribution of the ground truth across individual clusters. This can help drive decision making around hyperparameters of clustering including the number of clusters and clustering methodology.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/clustering-features/cluster-evaluation/_notebooks/RelevanceAI-ReadMe-Cluster-Distribution.ipynb)


## Plotting Basic Distributions

We can evaluate our cluster quality through plotting the cluster distribution.
The following code examines how the clusters are distributed, firstly, within themselves, and then against a ground truth label *Age* (i.e. *Age* is one of the fields in the dataset). Ideally, there is a clear ground truth in each cluster category. Note that the following code samples are to run after clustering is done on a dataset as was explained in [Clustering](https://docs.relevance.ai/docs/quickstart-k-means).


[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.utils.datasets import get_titanic_dataset\n\ndocuments = get_titanic_dataset()\nfor i,doc in enumerate(documents):\n  doc['_id']=i",
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
      "code": "ds = client.Dataset(\"titanic\")\nds.insert_documents(documents)",
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
      "code": "from sklearn.cluster import KMeans\n\nVECTOR_FIELD = \"value_vector_\"\nKMEAN_NUMBER_OF_CLUSTERS = 5\nALIAS = \"kmeans-\" + str(KMEAN_NUMBER_OF_CLUSTERS)\n\nmodel = KMeans(n_clusters=KMEAN_NUMBER_OF_CLUSTERS)\nclusterer = client.ClusterOps(alias=ALIAS, model=model)\nclusterer.operate(dataset_id=\"titanic\", vector_fields=[\"value_vector_\"])",
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
      "code": "viz_ops = client.ClusterVizOps(\n    dataset_id=DATASET_ID,\n    vector_fields=[\"value_vector_\"],\n    alias=\"kmeans_5\"\n)",
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
      "code": "viz_ops.plot_distributions(\"Age\", top_indices=3)",
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
      "code": "viz_ops.plot_distributions(\"Age\", top_indices=3)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]



## Plotting Custom Distributions

We can further plot custom distribution like below.

[block:code]
{
  "codes": [
    {
      "code": "from scipy.stats import skew, variation",
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
      "code": "viz_ops.plot_distributions(\n    numeric_field=\"Age\", dataset_id=DATASET_ID, measure_function=variation, top_indices=3\n)",
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
      "code": "viz_ops.plot_distributions(\n    numeric_field=\"Age\", dataset_id=DATASET_ID, measure_function=skew, top_indices=2\n)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]
