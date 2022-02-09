---
title: "Vector Search"
slug: "vector-search-2"
hidden: true
createdAt: "2021-11-11T04:53:24.775Z"
updatedAt: "2021-11-11T04:54:24.620Z"
---
Allows you to leverage vector similarity search to create a semantic search engine.
Powerful features of VecDB vector search:
 1. Multivector search that allows you to search with multiple vectors and give each vector a different weight. e.g. Search with a product image vector and text description vector to find the most similar products by what it looks like and what its described to do. You can also give weightings of each vector field towards the search, e.g. image\_vector\_ weights 100%, whilst description\_vector\_ 50%.

An example of a simple multivector query:

```
        [
            {"vector": [0.12, 0.23, 0.34], "fields": ["name_vector_"], "alias":"text"},
            {"vector": [0.45, 0.56, 0.67], "fields": ["image_vector_"], "alias":"image"},
        ]
```

An example of a weighted multivector query:

```
        [
            {"vector": [0.12, 0.23, 0.34], "fields": {"name_vector_":0.6}, "alias":"text"},
            {"vector": [0.45, 0.56, 0.67], "fields": {"image_vector_"0.4}, "alias":"image"},
        ]
```
An example of a weighted multivector query with multiple fields for each vector:

```
        [
            {"vector": [0.12, 0.23, 0.34], "fields": {"name_vector_":0.6, "description_vector_":0.3}, "alias":"text"},
            {"vector": [0.45, 0.56, 0.67], "fields": {"image_vector_"0.4}, "alias":"image"},
        ]
```
 2. Utilise faceted search with vector search. For information on how to apply facets/filters checkout **/datasets/{dataset_id}/documents/get_where**.
 3. Sum Fields option to adjust whether you want multiple vectors to be combined in the scoring or compared in the scoring. e.g. image\_vector\_ + text\_vector\_ or image\_vector\_ vs text\_vector\_.
    setting `sum_fields=True`:
     * Multi-vector search allows you to obtain search scores by taking the sum of these scores.
     * TextSearchScore + ImageSearchScore = SearchScore
     * We then rank by the new SearchScore, so for searching 1000 documents there will be 1000 search scores and results
    setting `sum_fields=False`:
     * Multi vector search but not summing the score, instead including it in the comparison!
     * TextSearchScore = SearchScore1
     * ImagSearcheScore = SearchScore2
     * We then rank by the 2 new SearchScore, so for searching 1000 documents there should be 2000 search scores and results.
 4. Personalization with positive and negative document ids.
    For more information about the positive and negative document ids to personalize checkout the **/services/recommend/vector** endpoint.