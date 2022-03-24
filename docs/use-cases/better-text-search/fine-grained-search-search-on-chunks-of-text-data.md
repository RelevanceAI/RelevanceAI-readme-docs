---
title: "Multistep Chunk Search"
slug: "fine-grained-search-search-on-chunks-of-text-data"
excerpt: "Fast fine-grained search - No word matching, just semantics"
hidden: true
createdAt: "2021-11-16T02:42:58.371Z"
updatedAt: "2022-01-05T10:52:21.258Z"
---
## Multistep chunk search (fast fine-grained search - No word matching, just semantics)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/324f83f-multistep_chunk.png",
        "multistep_chunk.png",
        1029,
        320,
        "#e9e9e7"
      ],
      "caption": "Multi-step chunk search results for query \"colorful cushions cover\". As can be seen, top results all include \"Floral\" which is the result of having a vector search step first and a model knowing \"colorful\" and \"floral\" are conceptually close."
    }
  ]
}
[/block]
### Concept
Multistep chunk search also performs the search in the vector space. However, it relies on both normal and chunked data.  This search first selects candidate results via [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both) and then performs chunk search on the selected candidates to speed up the search process.

### Sample use-case
Imagine dealing with many long pieces of text on different topics, as well as many paragraphs per page. If only one-fourth of the pages are about sport and a few about injuries, using multistep chunk search we can filter out the 75% non-related pages and limit the chunk search to the sub-data that we actually need.

### Sample code
Sample codes using Relevance-AI SDK and Python requests for multistep chunk search endpoint are shown below.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = <PROJECT-NAME>  # Project name\napi_key = <API-KEY>       # api-key\ndataset_id = <dataset_id>\n\nclient = Client(project, api_key)\n\nquery = \"gift for my wife\"  # query text\n\nmultistep_chunk_search = client.services.search.multistep_chunk(\n        # dataset name\n        dataset_id = dataset_id,\n\n        first_step_multivector_query = [\n            {\"vector\": client.services.encoders.text[\"vector\"], \n             # vector fieldson which to run a first step vector search\n             \"fields\": [\"product_name_default_vector_\"]}\n        ],\n      \n        multivector_query = [\n            {\n                \"vector\": client.services.encoders.text[\"vector\"],\n                # list of vector fields to run the query against in the second step\n                \"fields\": [\"description_sntcs_chunk_.txt2vec_chunkvector_\"],\n            }\n        ],\n        \n        # chunk field referring to the chunked data\n        chunk_field = \"description_sntcs_chunk_\",\n\n        # number of returned results\n        page_size = 5,\n\n        # minimum similarity score to return a match as a result\n        min_score = 0.0,\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This search is very useful when chunk-search becomes long due to large number of documents and chunks within them. It relies on machine learning techniques for vectorizing and similarity detection on chunked data. Therefore, both a chunker and a vectorizer are needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body).
