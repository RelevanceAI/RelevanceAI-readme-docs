---
title: "Advanced Multistep Chunk Search"
slug: "fine-grained-search-search-on-chunks-of-text-data-2"
excerpt: "Fast fine-grained search - Both word matching, and semantics"
hidden: false
createdAt: "2021-11-16T02:43:54.750Z"
updatedAt: "2022-01-05T10:52:56.064Z"
---
## Advanced multistep chunk search (fast fine-grained search - Both word matching, and semantics)
<figure>
<img src="https://files.readme.io/5a56604-advance_multi_step_chunk_search.png" width="1034" alt="advance_multi_step_chunk_search.png" />
<figcaption>Advance multistep chunk search result for query "colorful cushions cover". As can be seen, all results are about "cushion cover" however we added 2 filters: 1) products with a specefic id "PODS12P" and 2) the word "plain".</figcaption>
<figure>
### Concept
This is similar to advanced chunk search but speeds up the search process by first selecting candidate results via [vector search ](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both)and then performing [advanced chunk search ](https://docs.relevance.ai/docs/fine-grained-search-search-on-chunks-of-text-data-1) on the selected candidates.

### Sample use-case
The best use-case is when dealing with many long pieces of text also specific word matching is required. For instance, consider many long articles on different topics where each page includes about 8 paragraphs. Only one-forth of the articles are on sport and half of the paragraphs are about injuries, with a few about ACL injuries. None-related articles can be filtered out via vector search. Then if the pages are broken into 8 chunks (corresponding to the 8 paragraphs) a more fine-grained search on ACL injuries is possible using this search.

### Sample code
Sample codes using Relevance-AI SDK and Python requests for advance multi-step chunk search endpoint are shown below.
```python Python (SDK)
from relevanceai import Client

project = <PROJECT-NAME> # Project name
api_key = <API-KEY> # api-key
dataset_id = <dataset_id>

client = Client(project, api_key)

query = "colorful cushions cover" # query text

first_step_text = "PODS12P"
second_step_text = "plain"

advance_multi_step_chunk_search = client.services.search.advanced_multistep_chunk(
 # list of database names to use
 	dataset_ids=[dataset_id],

 # vector fields to run a first step vector search on
 first_step_query=[
 {"vector": client.services.encoders.multi_text(text=query)['vector'],
 "fields": {"product_nametextmulti_vector_": 0.5}}
 ],

 # text to look for
 first_step_text=first_step_text,

 # text field to do the text matching
 first_step_fields=["product_name"],

 # parameters of chunk search query
 chunk_search_query=[
 # chunk field referring to the chunked data
 {
 "chunk": "description_sntcs_chunk_",
 # queries
 "queries": [
 {
 "vector": client.services.encoders.text(text=query)["vector"],
 "fields": {"description_sntcs_chunk_.txt2vec_chunkvector_": 0.7},
 "traditional_query": {
 "text": second_step_text,
 "fields": "description",
 "traditional_weight": 0.3,
 },
 "metric": "cosine",
 },
 ],
 }
 ],

 # chunk field referring to the chunked data
 chunk_field="description_sntcs_chunk_",

 # number of returned results
 page_size=5,

 # minimum similarity score to return a match as a result
 min_score=0.2,
)

```
```python
```
##Some final notes:
In all mentioned searches,
* When using `fields` in the form of a list, it is possible to use multiple vectors. For example
    * `"fields": ["product_name_vector_", "descriptiondefault_vector_"]` where all vectors are produced using the same vectorizer (encoder).
* When using  `fields`, it is possible to assign a weight on how strong is the emphasis on a specific vector field. You can see two examples in the above code snippets:
    * `"fields": {"product_name_default_vector_": 0.5}`
    * `"fields": {"description_chunk_.description_1_chunkvector_":0.7}`
