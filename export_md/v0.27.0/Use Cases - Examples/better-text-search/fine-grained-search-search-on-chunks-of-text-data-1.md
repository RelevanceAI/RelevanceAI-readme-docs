---
title: "Advanced Chunk Search"
slug: "fine-grained-search-search-on-chunks-of-text-data-1"
excerpt: "Fine-grained search - Both word matching, and semantics"
hidden: false
createdAt: "2021-11-16T02:43:32.734Z"
updatedAt: "2022-01-05T10:52:45.105Z"
---
## Advance chunk search (fine-grained search - Both word matching, and semantics)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ed277cd-advance_chunk_search.png",
        "advance_chunk_search.png",
        1027,
        206,
        "#eeeeec"
      ],
      "caption": "Advance chunk search result for query \"colorful cushions cover\". As can be seen, all results are about \"cushion cover\" however we added a word matching step for \"Free Shipping\"."
    }
  ]
}
[/block]
### Concept
This is similar to [hybrid](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both-1) and [semantic](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both-2) search in the sense that it combines both word matching and search in vector space. Advance chunk search, however, works with chunked data (#TODO# link to a documentation page).

### Sample use-case
The best use-case is when dealing with long pieces of text also specific word matching is required. For instance consider a page of 8 paragraphs about sport in which half of the paragraphs are about injuries, with two about ACL injuries. If the pages are broken into 8 chunks (corresponding to the 8 paragraphs) a more fine-grained search on ACL injuries is possible using this search; meaning instead of returning the whole page, only the relevant paragraphs to ACL injuries are picked as a match.

### Sample code
Sample codes using Relevance-AI SDK and Python requests for advance chunk search endpoint are shown below.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = <PROJECT-NAME>  # Project name\napi_key = <API-KEY>       # api-key\ndataset_id = <dataset_id>\n\nclient = Client(project, api_key)\n\nquery = \"colorful cushions cover\"  # query text\n\nword_to_include = \"Free Shipping\"\nadvance_chunk_search = client.services.search.advanced_chunk(\n        dataset_ids= [dataset_id],\n        chunk_search_query= [\n            {\n                \"queries\": [\n                    # Chunk vector fields\n                    {\n                        \"queries\": [\n                            {\n                                \"vector\": client.services.encoders.text(text=query)['vector'],\n                                \"fields\": [\"description_sntcs_chunk_.txt2vec_chunkvector_\"],\n                                \"traditional_query\": {\n                                    \"text\": word_to_include,\n                                    \"fields\": \"description\",\n                                    \"traditional_weight\": 0.3,\n                                },\n                                \"metric\": \"cosine\",\n                            }\n                        ],\n                        \"chunk\": \"description_sntcs_chunk_\",\n                    },\n                  \n                    # normal (not chunk) vector fields\n                    {\n                        \"vector\": client.services.encoders.textimage(text=query)['vector'],\n                        \"fields\": [\"description_imagetext_vector_\"],\n                        \"metric\": \"cosine\",\n                    },\n                ]\n            }\n        ],\n        page_size= 5,\n        min_score= 0.0\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Depending on number of chunks in the entries in the database, this search can become long. It relies on machine learning techniques for vectorizing and similarity detection on chunked data. Therefore, both a chunker and a vectorizer are needed. It is possible to run this search across multiple datasets. Also, multiple fields can be specified to search against. It is possible to mix chunked and non-chunked vector data, in addition to using multiple models for vectorizing and combining them all in search (i.e `queries` in the request body).