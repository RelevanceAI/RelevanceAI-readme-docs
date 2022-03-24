---
title: "Diversity Search"
slug: "better-text-search-diversified-search-results"
excerpt: "No word matching, just semantics with clustering"
hidden: true
createdAt: "2021-10-21T05:01:38.342Z"
updatedAt: "2022-01-05T10:51:58.605Z"
---
## Diversity in search (no word matching, just semantics with clustering)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7c62334-diversity.png",
        "diversity.png",
        1640,
        1052,
        "#eaeced"
      ],
      "caption": "Diversity search results for query \"birthday gift\". As can be seen, results include a variety of items."
    }
  ]
}
[/block]
### Concept
Diversity is similar to vector search and performs the search in the vector space. It provides you with the ability to search for context as opposed to exact word matching. Diversity search, however, employs clustering as a step after search to add variety to the results: search results are clustered and top items of each cluster are shown.

### Sample use-case
Looking for "sneakers" under this search in a sportswear dataset will result in an answer list but not just a list of 1 particular shoe like Nike but a combination of Nike, Adidas, Asics, etc. This is important because in vector spaces - it may automatically tie a specific brand to one item in particular. As a result - we may want to get a larger diversity of the most relevant results in a streamlined manner.

### Sample code
Sample codes using Relevance-AI SDK and Python requests for diversity search endpoint are shown below.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\ndataset_id = 'ecommerce-demo'\n\nclient = Client()\n\nquery = \"birthday gift\"  # query text\nquery_vec = client.services.encoders.text(text=query)\n\nurl = \"https://gateway-api-aueast.relevance.ai/v1/\"\ndiversity_search = client.services.search.diversity(\n    # dataset name\n    \"dataset_id\": dataset_id,\n\n    # list of vector fields to run the query against\n    \"multivector_query\": [\n      {\"vector\": client.services.encoders.multi_text(text=query)['vector'], \n       \"fields\": [\"descriptiontextmulti_vector_\", \"product_nametextmulti_vector_\"]},\n\n      {\"vector\": client.services.encoders.textimage(text=query)['vector'],\n       \"fields\": [\"description_imagetext_vector_\"]}\n    ],\n\n    # vector field on which the clustering is done\n    \"cluster_vector_field\":\"product_nametextmulti_vector_\",\n  \n    # number of clusters\n    n_clusters=5,\n  \n    # number of returned results\n    page_size=20,\n  \n    # minimum similarity score to return a match as a result\n    min_score=0.2,\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This search is slightly longer than [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both) due to the added clustering step. It relies on machine learning techniques for vectorizing, similarity detection and clustering. Therefore, at least one vectorizer is needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body). Note the increased `page_size` parameter, so that there is enough data for clustering.