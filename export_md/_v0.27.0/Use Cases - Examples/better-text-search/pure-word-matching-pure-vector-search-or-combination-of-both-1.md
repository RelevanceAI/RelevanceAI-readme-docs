---
title: "Text and vector search (Hybrid search)"
slug: "pure-word-matching-pure-vector-search-or-combination-of-both-1"
excerpt: "Adjustable word matching and semantics"
hidden: false
createdAt: "2021-11-16T00:56:59.060Z"
updatedAt: "2022-01-05T10:51:34.353Z"
---
### Hybrid search (adjustable word matching and semantics)
[block:image]
{
  "images": [
    {
      "image": [],
      "caption": "Hybrid search result for query \"Pavilion DV6-20\" with a small emphasis on word-matching. As can be seen, there is no focus on \"DV6-20\" in the results and it is not included in the first result."
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fc3681a-hybrid0.7.png",
        "hybrid0.7.png",
        1922,
        990,
        "#e8e8e6"
      ],
      "caption": "Hybrid search result for query \"Pavilion DV6-20\" with a large emphasis on word-matching. As can be seen, the first three returned results, all include the id \"DV6-20\" in the query."
    }
  ]
}
[/block]
### Concept
This endpoint provides search through both word matching and search in the vector space. There is full control over which one to emphasize via a weighting parameter.

### Sample use-cases
* Combining traditional text search with semantic search into one search bar by providing support for ID search and vector search (for example - being able to combine "white shoe" and "Product JI36D" into the same search to return the same result.
* Searching for shoes (sneakers, boots, sandals, etc.) but specifically looking for white-colored ones.

### Sample code
Sample codes using Relevance-AI SDK and Python requests for hybrid search endpoint are shown below.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\ndataset_id = 'ecommerce-demo'\n\nclient = Client()\n\nquery = \"white shoes\"\nquery_vec = client.services.encoders.text(text=query)\n\n# weight assigned to word matching\nif len(query.split()) > 2:\n    traditional_weight = 0\nelse:\n    traditional_weight = 0.075\n\nhybrid_search = client.services.search.hybrid(\n    # dataset name\n    dataset_id=dataset_id,\n\n    multivector_query=[\n        {\n            \"vector\": query_vec[\"vector\"],\n\n            # list of vector fields against which to run the query\n            \"fields\": [\"description_default_vector_\"],\n        }\n    ],\n\n    # query text\n    text=query,\n\n    # text fields against which to match the query\n    fields=[\"description\"],\n\n    # number of returned results\n    page_size=5,\n    \n    traditional_weight=traditional_weight\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This search provides you with both word matching and search in context. You have the option of assigning the desired weight to traditional search. For instance, if word matching is important, the `traditional_weight` parameter is set to a higher value to emphasize on exact text matching, it is normally set to a small value (e.g. 0.025 to 0.1). Same as [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both), hybrid search relies on machine learning techniques for vectorizing and similarity detection. Therefore, a vectorizer is needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body).  This model provides you with more exploration possibilities on the effect of traditional and vector search.
