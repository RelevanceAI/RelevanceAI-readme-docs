---
title: "Cluster Distribution"
slug: "cluster-distribution"
hidden: true
createdAt: "2021-12-22T00:50:44.016Z"
updatedAt: "2022-01-27T02:24:54.049Z"
---
One way to evaluate clustering performance is to examine how well the vectors are distributed across the clusters. Depending on the individual use-case, success usually means a well spread out distribution of vectors across clusters. Optionally, if there is a field that can be used as ground truth, such a field can be used to examine the distribution of the ground truth across individual clusters. This can help drive decision making around hyperparameters of clustering including the number of clusters and clustering methodology.

Open in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs/clustering-features/cluster-evaluation/_notebooks/RelevanceAI-ReadMe-Cluster-Distribution.ipynb)


## Plotting Basic Distributions

We can evaluate our cluster quality through plotting the cluster distribution.
The following code examines how the clusters are distributed, firstly, within themselves, and then against a ground truth label *Age* (i.e. *Age* is one of the fields in the dataset). Ideally, there is a clear ground truth in each cluster category. Note that the following code samples are to run after clustering is done on a dataset as was explained in [Clustering](https://docs.relevance.ai/docs/quickstart-k-means).


@@@ dataset, DATASET_ID="titanic" @@@


@@@ cluster_vizops, VECTOR_FIELDS=["value_vector_"], CLUSTER_ALIAS="kmeans_5" @@@


@@@ cluster_vizops_distribution, NUMERIC_FIELD="Age", TOP_INDICES=3@@@



## Plotting Custom Distributions

We can further plot custom distribution like below.

@@@ skew_variation @@@


@@@ cluster_vizops_custom, NUMERIC_FIELD="Age", MEASURE_FUNCTION=variation, TOP_INDICES=3 @@@


@@@ cluster_vizops_custom, NUMERIC_FIELD="Age", MEASURE_FUNCTION=skew, TOP_INDICES=2 @@@