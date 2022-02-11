---
title: "Multi-vector search"
slug: "multi-vector-search"
excerpt: "Guide to using multi-vector search"
hidden: false
createdAt: "2021-10-28T08:04:31.328Z"
updatedAt: "2021-11-22T09:19:26.663Z"
---
Multi-vector search means
- Vector search with multiple models (e.g. searching with a `text` vectorizer and an `image` vectorizer)
- Vector search across multiple fields (e.g. searching across `title` and `description` with different weightings)

Both of these can be combined to offer a powerful, flexible search.
[block:callout]
{
  "type": "info",
  "body": "Multi-vector search offers a more powerful and more flexible search by combining several vectors across different fields and vectorizers, allowing us to experiment with more combinations of models and configurations.",
  "title": "Multi vector search allows us to combine multiple vectors and vector spaces!"
}
[/block]
## Multi-vector search with multiple models
In this section, we present a step-by-step guide on how to perform search via three sets of vectors:
1. produced by a model trained on pure text data in English (called it **default** in this guide)
2. produced by a model trained on pure text data from a multi-language dataset (called it **textmulti** in this guide)
3. produced by a model trained on combined text and image (called it **imagetext** in this guide).

### Step 1. Vectorizing the dataset
Search via vector type X is possible only if the dataset includes data vectorized by model X. This means if we want to search against fields such as `title` and `description`, we need to vectorize them using the available models (i.e. default, textmulti, and imagetext in our example). Please refer to a full guide on vectorizers and how to update a database with vectors [How to vectorize](doc:vectorize-text) and [Project Basics](doc:creating-a-dataset).

### Step 2. Vectorizing the query
To make a search against vectors of type X, the query must be of the same type. So, if the plan is to use three models, we need three query vectors corresponding to the three models/vectorizers. Sample code showing how to use the three vectorizer endpoints is provided below.  Keep it in mind that, first RelevanceAI must be installed as below:

[block:code]
{
  "codes": [
    {
      "code": "pip install RelevanceAI",
      "language": "shell"
    }
  ]
}
[/block]
And calling the three different vectorizers both using Python (SDK) or Python (requests) library:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = <PROJECT-NAME>  # Project name\napi_key = <API-KEY>       # api-key\n\nclient = Client(project, api_key)\n\nquery = \"white sneakers\"  # query text\n# three vectorizers\nquery_vec_txt = client.services.encoders.text(text=query)\nquery_vec_txtmulti = client.services.encoders.multi_text(text=query)\nquery_vec_txtimg = client.services.encoders.textimage(text=query)",
      "language": "python",
      "name": "Python (SDK)"
    },
    {
      "code": "import requests\n\ncredentials = project + \":\" + api_key\nurl = \"https://gateway-api-aueast.relevance.ai/v1/\"\n\nquery = \"white sneakers\"\n\nvectorising_endpoint = \"services/encoders/text\"\nquery_vec_txt = requests.get(\n    url + vectorising_endpoint,\n    headers={\"Authorization\": credentials},\n    params={\"text\": query},\n).json()\n\nvectorising_endpoint = \"services/encoders/multi_text\"\nquery_vec_txtmulti = requests.get(\n    url + vectorising_endpoint,\n    headers={\"Authorization\": credentials},\n    params={\"text\": query},\n).json()\n\nvectorising_endpoint = \"services/encoders/textimage\"\nquery_vec_txtimg = requests.get(\n    url + vectorising_endpoint,\n    headers={\"Authorization\": credentials},\n    params={\"text\": query},\n).json()",
      "language": "python",
      "name": "Python(requests)"
    }
  ]
}
[/block]
### Step 3. Vector search
As it was mentioned earlier, Relevance AI has provided you with a variety of vector search endpoints with different use-cases; please see guide pages such as [Better text Search](https://docs.relevance.ai/docs/better-text-search) for more information on each search endpoint.

#### 3.1. Vercor search with multiple vectors
In the sample code below, we show how a hybrid-search can be done by combining all three vector types:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = <PROJECT-NAME>  # Project name\napi_key = <API-KEY>       # api-key\ndataset_id = <dataset_id> # dataset id\n\nclient = Client(project, api_key)\n\nquery = \"white sneakers\"  # query text\n\n# three vectorizers\nquery_vec_txt = client.services.encoders.text(text=query)\nquery_vec_txtmulti = client.services.encoders.multi_text(text=query)\nquery_vec_txtimg = client.services.encoders.textimage(text=query)\n\nhybrid_search = client.services.search.vector(\n\t\t# dataset name\n  \tdataset_id=dataset_id,\n\t\t# fields to use for a vector search\n    multivector_query=[\n        {\n            \"vector\": query_vec_txt[\"vector\"],\n            \"fields\": [\"description_default_vector_\"],\n        },\n        {\n            \"vector\": query_vec_txtmulti[\"vector\"],\n            \"fields\": [\"descriptiontextmulti_vector_\"],\n        },\n        {\n            \"vector\": query_vec_txtimg[\"vector\"],\n            \"fields\": [\"description_imagetext_vector_\"],\n        }\n    ],\n    # number of returned results\n    page_size=5,\n)",
      "language": "python",
      "name": "Python(SDK)"
    },
    {
      "code": "import requests\n\ndataset_id = <dataset_id>\ncredentials = project + \":\" + api_key\nurl = \"https://gateway-api-aueast.relevance.ai/v1/\"\n\nquery = \"white sneakers\"  # query text\n\nvectorising_endpoint = \"services/encoders/text\"\nquery_vec_txt = requests.get(\n    url + vectorising_endpoint,\n    headers={\"Authorization\": credentials},\n    params={\"text\": query},\n).json()\n\nvectorising_endpoint = \"services/encoders/multi_text\"\nquery_vec_txtmulti = requests.get(\n    url + vectorising_endpoint,\n    headers={\"Authorization\": credentials},\n    params={\"text\": query},\n).json()\n\nvectorising_endpoint = \"services/encoders/textimage\"\nquery_vec_txtimg = requests.get(\n    url + vectorising_endpoint,\n    headers={\"Authorization\": credentials},\n    params={\"text\": query},\n).json()\n\nquery = \"white shoes\"\nhybrid_endpoint = \"services/search/hybrid\"\nhybrid_search = requests.post(\n    url + hybrid_endpoint,\n    headers={\"Authorization\": credentials},\n    json={\n        # dataset name\n        \"dataset_id\": dataset_id,\n\n        # query text\n        \"text\": query,\n\n        # text fields against which to match the query\n        \"fields\": [\"description\"],\n\n        \"multivector_query\": [\n            {\n                \"vector\": query_vec_txt[\"vector\"],\n                \"fields\": [\"description_default_vector_\"],\n            },\n            {\n                \"vector\": query_vec_txtmulti[\"vector\"],\n                \"fields\": [\"descriptiontextmulti_vector_\"],\n            },\n            {\n                \"vector\": query_vec_txtimg[\"vector\"],\n                \"fields\": [\"description_imagetext_vector_\"],\n            }\n        ],\n        \n        # number of returned results\n        \"page_size\": 5,\n\n        \"traditional_weight\": 0.025,\n    },\n).json()\n",
      "language": "python",
      "name": "Python(requests)"
    }
  ]
}
[/block]
#### 3.2. Vector search against multiple fields
Another great sample of multi-vector search in the Relevance AI platform is how endpoints such as `advanced_multistep_chunk` combine normal and chunked vectors. For instance, consider many long descriptions on different items where each one includes on average 8 sentences. Only one-tenth of the entries are on footwear and half of the sentences are about material, with a few on leather. None-related entries can be filtered out via vector search. Then if descriptions are broken into 8 chunks (corresponding to the 8 sentences) a more fine-grained search on leather shoes is possible using `advanced_multistep_chunk` search. Sample code using Relevance-AI SDK and Python requests for advance multi-step chunk search endpoint is provided below.  As can be seen, it combines two vector types in the first-step search and then performs a second search on a chunk_vector.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = <PROJECT-NAME>  # Project name\napi_key = <API-KEY>       # api-key\ndataset_id = <dataset_id> # dataset_id\n\nclient = Client(project, api_key)\n\nquery = \"ACL injuries in soccer\"  # query text\n\n# vectorizers\nquery_vec_txt = client.services.encoders.text(text=query)\nquery_vec_txtmulti = client.services.encoders.multi_text(text=query)\n\nfirst_step_text = \"sport injuries\"\nsecond_step_text = \"ACL\"\n\nadvance_multi_step_chunk_search = client.services.search.advanced_multistep_chunk(\n    # list of database names to use \n  \tdataset_ids=[dataset_id],\n  \n    # vector fields to run a first step vector search on\n    first_step_query=[\n        {\n          \"vector\": query_vec_txt[\"vector\"], \n          \"fields\": [\"title_txt_vector_\"]\n        },\n        {\n          \"vector\": query_vec_txtmulti[\"vector\"], \n          \"fields\": [\"description_txtmulti_vector_\"]\n        }\n    ],\n  \n    # text to look for\n    first_step_text=first_step_text,\n  \n    # text field to do the text matching\n    first_step_fields=[\"title\"],\n  \n    # parameters of chunk search query\n    chunk_search_query=[\n        # chunk field referring to the chunked data\n        {\n            \"chunk\": \"description_chunk_\",\n            # queries\n            \"queries\": [\n                {\n                    \"vector\": query_vec_txt[\"vector\"],\n                    \"fields\": {\"description_chunk_.description_1_chunkvector_\": 0.7},\n                    \"traditional_query\": {\n                        \"text\": second_step_text,\n                        \"fields\": \"description\",\n                        \"traditional_weight\": 0.3,\n                    },\n                    \"metric\": \"cosine\",\n                },\n            ],\n        }\n    ],\n  \n    # chunk field referring to the chunked data\n    chunk_field=\"description_chunk_\",\n  \n    # number of returned results\n    page_size=5,\n  \n    # minimum similarity score to return a match as a result\n    min_score=0.2,\n)\n",
      "language": "python",
      "name": "Python(SDK)"
    },
    {
      "code": "import requests\n\ndataset_id = <dataset_id>\ncredentials = project + \":\" + api_key\nurl = \"https://gateway-api-aueast.relevance.ai/v1/\"\n\nquery = \"formal shoes\"\nvectorising_endpoint = \"services/encoders/text\"\nquery_vec = requests.get(\n    url + vectorising_endpoint,\n    headers={\"Authorization\": credentials},\n    params={\"text\": query},\n).json()\n\n\nfirst_step_text = \"white shoes\"\nsecond_step_text = \"Synthetic Leather\"\nadvance_multi_step_chunk_search_endpoint = \"services/search/advanced_multistep_chunk\"\n\nadvance_multi_step_chunk_search = requests.post(\n    url + advance_multi_step_chunk_search_endpoint,\n    headers={\"Authorization\": credentials},\n    json={\n        # collection names\n            \"dataset_ids\": [dataset_id],\n\n            # vector fields to run a first step vector search on \n            \"first_step_query\": [{\n                \"vector\" : query_vec['vector'],\n                \"fields\": {\"product_name_default_vector_\":0.5}}],\n            \n            # text to look for\n            \"first_step_text\": first_step_text,\n            \n            # text field to do the text matching \n            \"first_step_fields\": [\"product_name\"],\n            \n            # parameters of chunk search query\n            \"chunk_search_query\":[\n                 # chunk field referring to the chunked data\n                { \"chunk\" : \"description_sntcs_chunk_\", \n                  \n                  # queries \n                  \"queries\" : [ \n                                {\"vector\" : query_vec['vector'], \n                                \"fields\": {\"description_sntcs_chunk_.txt2vec_chunkvector_\":0.7}, \n                                \"traditional_query\" : {\n                                    \"text\":second_step_text, \n                                    \"fields\" : [\"description\"], \n                                    \"traditional_weight\": 0.3}, \"metric\" : \"cosine\"},\n                                ] }\n            ],\n\n            # chunk field referring to the chunked data\n            \"chunk_field\":\"description_sntcs_chunk_\",\n\n            # number of returned results\n            \"page_size\": 5,\n\n            # minimum similarity score to return a match as a result\n            \"min_score\": 0.2,\n    }\n).json()",
      "language": "python",
      "name": "Python(requests)"
    }
  ]
}
[/block]
Filtering based on specific features is a great option to perform a more refined search. We will explain Relevance AI's available filtering options on the following page.