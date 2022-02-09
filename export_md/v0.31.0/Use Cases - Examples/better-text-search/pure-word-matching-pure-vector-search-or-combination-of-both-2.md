---
title: "Semantic Search"
slug: "pure-word-matching-pure-vector-search-or-combination-of-both-2"
excerpt: "Automatic word matching and semantics"
hidden: false
createdAt: "2021-11-16T01:00:28.407Z"
updatedAt: "2022-01-05T10:54:51.991Z"
---
## Semantic search (automatic word matching and semantics)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dea2fec-Semantic.png",
        "Semantic.png",
        1910,
        1118,
        "#e4e4e4"
      ],
      "caption": "Semantic search result for query \"Pavilion DV6-20\" with a small emphasis on word-matching. As can be seen, there is no focus on \"DV6-20\" in the results, but all results are HP laptops."
    }
  ]
}
[/block]
### Concept
This endpoint is very similar to [hybrid search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both-1) and performs the search considering both word matching and search in the vector space. The only difference is that a small value is already set for `traditional_weight`.

### Sample use-case
- Searching for shoes (sneakers, boots, sandals, etc.) and preferring white-colored ones.

### Sample code
Sample codes using Relevance-AI SDK and Python requests for semantic search endpoint are shown below.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\ndataset_id = 'ecommerce-demo'\n\nclient = Client()\n\nquery = \"white shoes\"\nquery_vec = client.services.encoders.text(text=query)\n\nsemantic_search = client.services.search.semantic(\n    # dataset name\n    dataset_id=dataset_id,\n    \n    multivector_query=[\n        {\n            \"vector\": query_vec[\"vector\"],\n           \n          # list of vector fields against which to run the query\n            \"fields\": [\"description_default_vector_\"],\n        }\n    ],\n    \n    # text fields against which to match the query\n    fields=[\"description\"],\n    \n    # query text\n    text=query,\n    \n    # number of returned results\n    page_size=5,\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This search is rather quick and provides you with both word matching and search in context. Use this search when the importance of vector search outweighs the importance of word matching. Same as [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both), semantic search relies on machine learning techniques for vectorizing and similarity detection. Therefore, a vectorizer is needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body).