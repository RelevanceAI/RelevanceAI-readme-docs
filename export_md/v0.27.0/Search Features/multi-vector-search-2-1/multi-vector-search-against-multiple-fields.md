---
title: "Multi-vector search against multiple fields"
slug: "multi-vector-search-against-multiple-fields"
hidden: false
createdAt: "2022-01-28T04:45:30.658Z"
updatedAt: "2022-01-28T07:21:47.625Z"
---
## Multi-vector search against multiple fields
In this page, we explain how to perform a search on two different fields: `title` and `description`.

### Step 1. Vectorizing the dataset
Search via vector type X is possible only if the dataset includes data vectorized by model X. This means if we want to search against fields such as `title` and `description`, we need to vectorize them using the available models. Please refer to a full guide on vectorizers and how to update a database with vectors [How to vectorize](doc:vectorize-text) and [Project Basics](doc:creating-a-dataset).

### Step 2. Vectorizing the query
To make a search against vectors of type X, the query must be of the same type. Sample code showing how to use the three vectorizer endpoints is provided below.  Keep it in mind that, first RelevanceAI and the library for vectorization must be installed. For information of vectorizing visit [How to vectorize](https://docs.relevance.ai/docs/how-to-vectorise)
[block:code]
{
  "codes": [
    {
      "code": "# Relevance AI Python SDK\npip install RelevanceAI==0.27.0",
      "language": "shell"
    }
  ]
}
[/block]
Instantiate a client object:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \n\n\"\"\"\nRunning this cell will provide you with \nthe link to sign up/login page where you can find your credentials.\nOnce you have signed up, click on the value under `Authorization token` \nin the API tab\nand paste it in the appreared Auth token box below\n\"\"\"\n\nclient = Client()",
      "language": "python"
    }
  ]
}
[/block]
Vectorize your text query using the same vectorizer/encoder/model used on the dataset. In our sample:
[block:code]
{
  "codes": [
    {
      "code": "query = \"white sneakers\"  # query text\n\n# three vectorizers\nquery_vec = model1.encode(query)",
      "language": "python"
    }
  ]
}
[/block]
### Step 3. Vector search with multiple vectors
As it was mentioned earlier, Relevance AI has provided you with a variety of vector search endpoints with different use-cases; please see guide pages such as [Better text Search](https://docs.relevance.ai/docs/better-text-search) for more information on each search endpoint.

The dataset that we used for this search includes a `title` and a `description` field which are vectorized by `model1`. Therefore included in the dataset also exist fields such as `description_model1_vector_` and `title_model1_vector_`.
[block:code]
{
  "codes": [
    {
      "code": "vector_search = client.services.search.vector(\n\t\t# dataset name\n  \tdataset_id=DATASET_ID,\n\t\t# fields to use for a vector search\n    multivector_query=[\n        {\n            \"vector\": query_vec,\n            \"fields\": [\"description_model1_vector_\", \"title_model1_vector_\"],\n        }\n    ],\n    # number of returned results\n    page_size=5,\n)",
      "language": "python"
    }
  ]
}
[/block]
Note that you can assign higher importance to a certain field as shown in the code snippet below:
[block:code]
{
  "codes": [
    {
      "code": "vector_search = client.services.search.vector(\n\t\t# dataset name\n  \tdataset_id=DATASET_ID,\n\t\t# fields to use for a vector search\n    multivector_query=[\n        {\n            \"vector\": query_vec,\n            \"fields\": \"fields\": {\"description_model1_vector_\":0.6, \n                                 \"title_model1_vector_\":0.3}\n        }\n    ],\n    # number of returned results\n    page_size=5,\n)",
      "language": "python"
    }
  ]
}
[/block]