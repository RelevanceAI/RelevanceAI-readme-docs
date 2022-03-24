---
title: "Cluster Plot"
slug: "cluster-plot"
hidden: true
createdAt: "2021-12-22T00:52:15.116Z"
updatedAt: "2022-01-27T02:25:35.045Z"
---
Plots of vectors, colour coordinated by their cluster labels can be used to visually evaluate the success of clustering. Dimension reduction to 3D is applied to the vector field before plotting. The number of dimensions (3) is chosen to be as large as possible to preserve as much information of the original vector space as possible while being able to visualise on a plot. Optionally, a ground truth field can also be provided, for which, the vectors, colour coordinated by the ground truth label will also be plotted on the side for comparison.

## Code Example
The following code plots a 3D dimension reduced version of the vectors, colour coded by clusters, also the ground truth (i.e. an optional argument).
[block:code]
{
  "codes": [
    {
      "code": "DATASET_ID = 'quickstart_clustering'\nVECTOR_FIELD = 'product_image_clip_vector_'\nGROUND_TRUTH_FIELD = 'query'\nk = 10 # number of clusters\nALIAS = 'kmeans_'+str(k)\n\nclient.vector_tools.cluster.plot(\n  dataset_id = DATASET_ID, \n  vector_field = VECTOR_FIELD, \n  cluster_alias = ALIAS, \n  ground_truth_field = GROUND_TRUTH_FIELD\n)\n",
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
        "https://files.readme.io/fed36d3-Screen_Shot_2022-01-27_at_11.49.05_am.png",
        "Screen Shot 2022-01-27 at 11.49.05 am.png",
        864,
        727,
        "#fcfbfc"
      ],
      "caption": "Cluster plot"
    }
  ]
}
[/block]
