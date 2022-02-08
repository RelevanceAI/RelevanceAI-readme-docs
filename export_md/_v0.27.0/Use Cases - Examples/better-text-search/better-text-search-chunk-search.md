---
title: "Chunk Search"
slug: "better-text-search-chunk-search"
excerpt: "Fine-grained search - No word matching, just semantics"
hidden: false
createdAt: "2021-10-21T06:51:03.377Z"
updatedAt: "2022-01-05T10:52:07.856Z"
---
<figure>
<img src="https://files.readme.io/a8efd61-chunk_search.png" width="1026" alt="chunk search.png" />
<figcaption>Chunk search results for query "colorful cushions cover". As can be seen, when descriptions are chunked, and used for search, all returned entries include "cushions cover" that has been searched for.</figcaption>
<figure>
## Brief overview on chunks
* What are chunks?
A long text can be broken into smaller chunks of text. For instance, a paragraph of 5 sentences can be broken into a list of 5 sentences or a page of 20 lines can be broken into a list of 20 sentences.

* Why do we need chunks?
There are several advantages to breaking a long text into smaller pieces. For instance:
    1. Smaller chunks such as sentences allow better control on the number of tokens fed to a model. Some models are very sensitive to input token-count
    2. Smaller chunks such as sentences allow more fine-grained search

* How to upload chunked data in the Relevance AI platform?
Each document's chunked data is presented as a dictionary ( `{key: value}` )
with the "key" as a string ending in `"_chunk_"` (e.g. `'example_chunk_'`) and the value as a list. This list includes dictionaries, each one presenting a chunk with intended fields; such as text, vector, etc. Note that the name of the field presenting a chunk-vector must end in `"_chunkvector_"`. (#TODO# link to documentations for vectorizing chunks)
An example of the `{key: value}` structure is:
```
{"example_chunk_":
[{"text":"This is the first chunk", "sentence_chunkvector_":[1, 2, 3, ...]},
 {"text":"This is the second chunk", "sentence_chunkvector_":[1, 3, 5, ...]},
 {"text":"This is the third chunk", "sentence_chunkvector_":[1, 8, 4, ...]},
 ...
 ]}
```

## Chunk search (fine-grained search - No word matching, just semantics)

### Concept
Chunk search is similar to [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both) and performs the search in the vector space. Chunk search however needs chunked data.

### Sample use-cases
- Dealing with long pieces of text. For instance, consider a page of 8 paragraphs about sport in which one or two paragraphs are about injuries. If the page is broken into 8 chunks (corresponding to the 8 paragraphs) a more fine-grained search on sports injuries is possible; meaning instead of returning the whole page, only the relevant paragraphs to sports injuries are picked as a match.
 -  Ensuring one result per original document is returned. For example - when you are searching through a PDF, you may only want 1 page per result as opposed to 1 sentence. The only way to do this is to ensure that the accurate data structure is in place in the index to return results in this way. This endpoint also allows you to return the most relevant chunk in each page.
 -  Identifying the most important noun in each sentence. If you decide to chunk using position-of-tagging, you can also identify the most important nouns/adjectives/verbs that are relevant to your search.

### Sample code
Sample codes using Relevance-AI SDK and Python requests for chunk search endpoint are shown below. Here, we have chunked the description field into sentences and we look for the most relevant sentence to a query.
```python Python (SDK)
from relevanceai import Client

project = <PROJECT-NAME> # Project name
api_key = <API-KEY> # api-key
dataset_id = <dataset_id>

client = Client(project, api_key)

query = "colorful Cushions Cover" # query text
query_vec = client.services.encoders.text(text=query)

chunk_search = client.services.search.chunk(
 # dataset name
 dataset_id = dataset_id,

 multivector_query= [
 {
 "vector": query_vec["vector"],

 # list of vector fields to run the query against
 "fields": ["description_sntcs_chunk_.txt2vec_chunkvector_"],
 }
 ],

 # chunk field referring to the chunked data
 chunk_field= "description_sntcs_chunk_",

 # number of returned results
 page_size= 5,

 # minimum similarity score to return a match as a result
 min_score= 0.2)
```
```python
```
Depending on number of chunks in the entries in the database, this search can take a longer time than vector search. It relies on machine learning techniques for vectorizing and similarity detection on chunked data. Therefore, both a chunker (#TODO# link to a documentation page on chunkers) and a vectorizer are needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body).
