---
title: "Advanced Multistep Chunk Search"
slug: "fine-grained-search-search-on-chunks-of-text-data-2"
excerpt: "Fast fine-grained search - Both word matching, and semantics"
hidden: true
createdAt: "2021-11-16T02:43:54.750Z"
updatedAt: "2022-01-05T10:52:56.064Z"
---
## Advanced multistep chunk search (fast fine-grained search - Both word matching, and semantics)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5a56604-advance_multi_step_chunk_search.png",
        "advance_multi_step_chunk_search.png",
        1034,
        310,
        "#e3e3e2"
      ],
      "caption": "Advance multistep chunk search result for query \"colorful cushions cover\". As can be seen, all results are about \"cushion cover\" however we added 2 filters: 1) products with a specefic id \"PODS12P\" and 2) the word \"plain\"."
    }
  ]
}
[/block]
### Concept
This is similar to advanced chunk search but speeds up the search process by first selecting candidate results via [vector search ](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both)and then performing [advanced chunk search ](https://docs.relevance.ai/docs/fine-grained-search-search-on-chunks-of-text-data-1) on the selected candidates.

### Sample use-case
The best use-case is when dealing with many long pieces of text also specific word matching is required. For instance, consider many long articles on different topics where each page includes about 8 paragraphs. Only one-forth of the articles are on sport and half of the paragraphs are about injuries, with a few about ACL injuries. None-related articles can be filtered out via vector search. Then if the pages are broken into 8 chunks (corresponding to the 8 paragraphs) a more fine-grained search on ACL injuries is possible using this search.

### Sample code
Sample codes using Relevance-AI SDK and Python requests for advance multi-step chunk search endpoint are shown below.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = <PROJECT-NAME>  # Project name\napi_key = <API-KEY>       # api-key\ndataset_id = <dataset_id>\n\nclient = Client(project, api_key)\n\nquery = \"colorful cushions cover\"  # query text\n\nfirst_step_text = \"PODS12P\"\nsecond_step_text = \"plain\"\n\nadvance_multi_step_chunk_search = client.services.search.advanced_multistep_chunk(\n    # list of database names to use \n  \tdataset_ids=[dataset_id],\n  \n    # vector fields to run a first step vector search on\n    first_step_query=[\n        {\"vector\": client.services.encoders.multi_text(text=query)['vector'], \n         \"fields\": {\"product_nametextmulti_vector_\": 0.5}}\n    ],\n  \n    # text to look for\n    first_step_text=first_step_text,\n  \n    # text field to do the text matching\n    first_step_fields=[\"product_name\"],\n  \n    # parameters of chunk search query\n    chunk_search_query=[\n        # chunk field referring to the chunked data\n        {\n            \"chunk\": \"description_sntcs_chunk_\",\n            # queries\n            \"queries\": [\n                {\n                    \"vector\": client.services.encoders.text(text=query)[\"vector\"],\n                    \"fields\": {\"description_sntcs_chunk_.txt2vec_chunkvector_\": 0.7},\n                    \"traditional_query\": {\n                        \"text\": second_step_text,\n                        \"fields\": \"description\",\n                        \"traditional_weight\": 0.3,\n                    },\n                    \"metric\": \"cosine\",\n                },\n            ],\n        }\n    ],\n  \n    # chunk field referring to the chunked data\n    chunk_field=\"description_sntcs_chunk_\",\n  \n    # number of returned results\n    page_size=5,\n  \n    # minimum similarity score to return a match as a result\n    min_score=0.2,\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
##Some final notes:
In all mentioned searches,
* When using `fields` in the form of a list, it is possible to use multiple vectors. For example
    * `"fields": ["product_name_vector_", "descriptiondefault_vector_"]` where all vectors are produced using the same vectorizer (encoder).
* When using  `fields`, it is possible to assign a weight on how strong is the emphasis on a specific vector field. You can see two examples in the above code snippets:
    * `"fields": {"product_name_default_vector_": 0.5}`
    * `"fields": {"description_chunk_.description_1_chunkvector_":0.7}`