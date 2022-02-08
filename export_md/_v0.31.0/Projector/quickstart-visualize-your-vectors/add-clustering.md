---
title: "Add clustering"
slug: "add-clustering"
excerpt: "Clustering allows you to quickly detect bias in your visualisations"
hidden: true
createdAt: "2021-11-24T03:14:57.904Z"
updatedAt: "2021-11-24T10:39:40.197Z"
---
## Clustering the Embeddings

Supported clustering algorithms for visualization in Relevance AI platform are:
- K-means
- K-medoids
- HDBSCAN

If you specify a clustering algorithm, you will be able to see the embedding space in a clustered view.
You may choose between `kmeans` and `kmedoids` and toggle the `num_clusters` to investigate the unsupervised groupings within the embedding space of the `vector_field`.

Clustering runs after a dimensionality reduction step to help detect bias in the projected vector space.
```python Python (SDK)
client.projector.plot(
 dataset_id = dataset_id,
 vector_field = vector_field,
 number_of_points_to_render=10000,

 ### Dimensionality reduction args
 dr = "pca",

 ## Plot rendering args
 vector_label = None,
 colour_label = 'query',
 colour_label_char_length = None,
 hover_label = ['product_title'],

 ### Cluster args
 cluster = "kmeans",
 num_clusters=10
)
```
```python
```

[block:html]
{
  "html": "<div>\n<img src=\"https://media.giphy.com/media/nwZueihQAdoJSqKVfI/source.gif\" \n     alt=\"RelevanceAI Visualisation\"\n     style=\"width: 100% vertical-align: middle\"/> \n</div>\n\n<style></style>\n"
}
[/block]
