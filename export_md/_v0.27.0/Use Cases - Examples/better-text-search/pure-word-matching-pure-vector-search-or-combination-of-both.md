---
title: "Vector Search"
slug: "pure-word-matching-pure-vector-search-or-combination-of-both"
excerpt: "No word matching, just semantics"
hidden: false
createdAt: "2021-11-16T00:56:09.821Z"
updatedAt: "2022-01-05T10:54:34.051Z"
---
## Vector Search (no word matching, just semantics)
<figure>
<img src="https://files.readme.io/3ce88b5-vector.png" width="1896" alt="vector.png" />
<figcaption>Vector search results for query "gift for my mother". As can be seen, Vector search knows `mother` and `mom` are synonyms.</figcaption>
<figure>
### Concept
This search performs the search in the vector space and provides you with the ability to search for context as opposed to exact word matching.

### Sample use-cases
- Searching for "dog" in an animal dataset and looking to receive an answer list containing both "dog" and puppy".

### Sample code
Sample codes using Relevance-AI SDK and Python requests for vector search endpoint are shown below. Note that there is an installation step for using Python(SDK).
```python Python (SDK)
from relevanceai import Client

dataset_id = 'ecommerce-demo'

client = Client()

query = "gift for my mother" # query text
query_vec = client.services.encoders.multi_text(text=query)

vector_search = client.services.search.vector(
 # dataset name
 dataset_id=dataset_id,

 multivector_query=[
 {
 # vectorised query
 "vector": query_vec["vector"],

 # different vector fields to search against
 "fields": ["product_nametextmulti_vector_"],
 }
 ],

 # number of returned results
 page_size=5,
)

```
```python
```
This search is rather quick and provides you with search in context. It relies on machine learning techniques for vectorizing and similarity detection. Therefore, at least one vectorizer is needed. It is possible to use multiple vectorizers/encoders for vectorizing and combine them all in search under the `multivector_query` parameter.

This can be achieved by expanding the multivector query as below:
```python Python (SDK)
from relevanceai import Client

project = <PROJECT-NAME> # Project name
api_key = <API-KEY> # api-key
dataset_id = <dataset_id>

client = Client(project, api_key)

query = "toy for dogs" # query text
query_vec_1 = client.services.encoders.text(text=query)
query_vec_2 = client.services.encoders.multi_text(text=query)

vector_search = client.services.search.vector(
 # dataset name
 dataset_id=dataset_id,

 multivector_query=[
 {
 # vectorised query
 "vector": query_vec_1["vector"],

 # different vector fields to search against
 "fields": ["description_default_vector_"],
 },
 {
 # vectorised query
 "vector": query_vec_2["vector"],

 # different vector fields to search against
 "fields": ["descriptiontextmulti_vector_"],
 }
 ],

 # number of returned results
 page_size=5,
)
```
```python
```
As can be seen in the screenshot below, this search is not successful in keyword matching. For instance, using vector search to look for product id "DV6-2059eo" will results in the following failed search results.
<figure>
<img src="https://files.readme.io/bef958e-vector_failed.png" width="1926" alt="vector failed.png" />
<figcaption>Search result for query "DV6-2059eo" showing how vector search is not suitable for keyword matching ("DV6-2059eo" exists in the database).</figcaption>
<figure>
