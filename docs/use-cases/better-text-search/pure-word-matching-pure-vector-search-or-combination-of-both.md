---
title: "Vector Search"
slug: "pure-word-matching-pure-vector-search-or-combination-of-both"
excerpt: "No word matching, just semantics"
hidden: true
createdAt: "2021-11-16T00:56:09.821Z"
updatedAt: "2022-01-05T10:54:34.051Z"
---
## Vector Search (no word matching, just semantics)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3ce88b5-vector.png",
        "vector.png",
        1896,
        1286,
        "#e0e0df"
      ],
      "caption": "Vector search results for query \"gift for my mother\". As can be seen, Vector search knows `mother` and `mom` are synonyms."
    }
  ]
}
[/block]
### Concept
This search performs the search in the vector space and provides you with the ability to search for context as opposed to exact word matching.

### Sample use-cases
- Searching for "dog" in an animal dataset and looking to receive an answer list containing both "dog" and puppy".

### Sample code
Sample codes using Relevance-AI SDK and Python requests for vector search endpoint are shown below. Note that there is an installation step for using Python(SDK).
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\ndataset_id = 'ecommerce-demo'\n\nclient = Client()\n\nquery = \"gift for my mother\"  # query text\nquery_vec = client.services.encoders.multi_text(text=query)\n\nvector_search = client.services.search.vector(\n    # dataset name\n    dataset_id=dataset_id,\n    \n    multivector_query=[\n        {\n            # vectorised query\n            \"vector\": query_vec[\"vector\"],\n            \n            # different vector fields to search against\n            \"fields\": [\"product_nametextmulti_vector_\"],\n        }\n    ],\n    \n    # number of returned results\n    page_size=5,\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This search is rather quick and provides you with search in context. It relies on machine learning techniques for vectorizing and similarity detection. Therefore, at least one vectorizer is needed. It is possible to use multiple vectorizers/encoders for vectorizing and combine them all in search under the `multivector_query` parameter.

This can be achieved by expanding the multivector query as below:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = <PROJECT-NAME>  # Project name\napi_key = <API-KEY>       # api-key\ndataset_id = <dataset_id>\n\nclient = Client(project, api_key)\n\nquery = \"toy for dogs\"  # query text\nquery_vec_1 = client.services.encoders.text(text=query)\nquery_vec_2 = client.services.encoders.multi_text(text=query)\n\nvector_search = client.services.search.vector(\n    # dataset name\n    dataset_id=dataset_id,\n    \n    multivector_query=[\n        {\n            # vectorised query\n            \"vector\": query_vec_1[\"vector\"],\n            \n            # different vector fields to search against\n            \"fields\": [\"description_default_vector_\"],\n        },\n        {\n            # vectorised query\n            \"vector\": query_vec_2[\"vector\"],\n            \n            # different vector fields to search against\n            \"fields\": [\"descriptiontextmulti_vector_\"],\n        }\n    ],\n    \n    # number of returned results\n    page_size=5,\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
As can be seen in the screenshot below, this search is not successful in keyword matching. For instance, using vector search to look for product id "DV6-2059eo" will results in the following failed search results.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bef958e-vector_failed.png",
        "vector failed.png",
        1926,
        700,
        "#e8e8e7"
      ],
      "caption": "Search result for query \"DV6-2059eo\" showing how vector search is not suitable for keyword matching (\"DV6-2059eo\" exists in the database)."
    }
  ]
}
[/block]
