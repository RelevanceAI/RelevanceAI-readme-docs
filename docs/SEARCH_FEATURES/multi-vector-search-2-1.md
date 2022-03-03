---
title: "Multi-vector search"
slug: "multi-vector-search-2-1"
excerpt: "Guide to using multi-vector search"
hidden: false
createdAt: "2021-12-14T13:33:49.517Z"
updatedAt: "2022-01-18T00:51:03.682Z"
---
Multi-vector search means
- Vector search with multiple models (e.g. searching with a `text` vectorizer and an `image` vectorizer)
- Vector search across multiple fields (e.g. searching across `title` and `description` with different weightings)

Both of these can be combined to offer a powerful, flexible search.

> 📘 Multi vector search allows us to combine multiple vectors and vector spaces!
>
> Multi-vector search offers a more powerful and more flexible search by combining several vectors across different fields and vectorizers, allowing us to experiment with more combinations of models and configurations.
>
## Multi-vector search with multiple models
In this section, we present a step-by-step guide on how to perform search via three sets of vectors:
1. produced by a model trained on pure text data in English (called it **default** in this guide)
2. produced by a model trained on pure text data from a multi-language dataset (called it **textmulti** in this guide)
3. produced by a model trained on combined text and image (called it **imagetext** in this guide).

### Step 1. Vectorizing the dataset
Search via vector type X is possible only if the dataset includes data vectorized by model X. This means if we want to search against fields such as `title` and `description`, we need to vectorize them using the available models (i.e. `default`, `textmulti`, and `imagetext` in our example). Please refer to a full guide on vectorizers and how to update a database with vectors [How to vectorize](doc:vectorize-text) and [Project Basics](doc:creating-a-dataset).

### Step 2. Vectorizing the query
To make a search against vectors of type X, the query must be of the same type. So, if the plan is to use three models, we need three query vectors corresponding to the three models/vectorizers. Sample code showing how to use the three vectorizer endpoints is provided below.  Keep it in mind that, first RelevanceAI must be installed as below:


```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==1.3.1
```
```bash
```

And calling three different vectorizers, text encoding, multi-text encoding, and text image encoding.



### Step 3. Vector search
As it was mentioned earlier, Relevance AI has provided you with a variety of vector search endpoints with different use-cases; please see guide pages such as [Better text Search](https://docs.relevance.ai/docs/better-text-search) for more information on each search endpoint.

#### 3.1. Vector search with multiple vectors
In the sample code below, we show how a hybrid search can be done by combining all three vector types:
```python Python
from relevanceai import Client

dataset_id = <dataset_id> # dataset id

client = Client()

query = "white sneakers" # query text

# three vectorizers
query_vec_txt = client.services.encoders.text(text=query)
query_vec_txtmulti = client.services.encoders.multi_text(text=query)
query_vec_txtimg = client.services.encoders.textimage(text=query)

hybrid_search = client.services.search.hybrid(
		# dataset name
 	dataset_id=dataset_id,
		# fields to use for a vector search
 multivector_query=[
 {
 "vector": query_vec_txt["vector"],
 "fields": ["description_default_vector_"],
 },
 {
 "vector": query_vec_txtmulti["vector"],
 "fields": ["descriptiontextmulti_vector_"],
 },
 {
 "vector": query_vec_txtimg["vector"],
 "fields": ["description_imagetext_vector_"],
 }
 ],
 # number of returned results
 page_size=5,
)
```
```python
```


#### 3.2. Vector search against multiple fields
Another great sample of multi-vector search in the Relevance AI platform is how endpoints such as `advanced_multistep_chunk` combine normal and chunked vectors. For instance, consider many long descriptions on different items where each one includes on average 8 sentences. Only one-tenth of the entries are on footwear and half of the sentences are about material, with a few on leather. None-related entries can be filtered out via vector search. Then if descriptions are broken into 8 chunks (corresponding to the 8 sentences) a more fine-grained search on leather shoes is possible using `advanced_multistep_chunk` search. Sample code using Relevance AI SDK for advanced multi-step chunk search endpoint is provided below.  As can be seen, it combines two vector types in the first-step search and then performs a second search on a `chunk_vector`.

```python Python
from relevanceai import Client

dataset_id = <dataset_id> # dataset_id

client = Client()

query = "ACL injuries in soccer" # query text

# vectorizers
query_vec_txt = client.services.encoders.text(text=query)
query_vec_txtmulti = client.services.encoders.multi_text(text=query)

first_step_text = "sport injuries"
second_step_text = "ACL"

advanced_multi_step_chunk_search = client.services.search.advanced_multistep_chunk(
 # list of database names to use
 	dataset_ids=[dataset_id],

 # vector fields to run a first step vector search on
 first_step_query=[
 {
 "vector": query_vec_txt["vector"],
 "fields": ["title_txt_vector_"]
 },
 {
 "vector": query_vec_txtmulti["vector"],
 "fields": ["description_txtmulti_vector_"]
 }
 ],

 # text to look for
 first_step_text=first_step_text,

 # text field to do the text matching
 first_step_fields=["title"],

 # parameters of chunk search query
 chunk_search_query=[
 # chunk field referring to the chunked data
 {
 "chunk": "description_chunk_",
 # queries
 "queries": [
 {
 "vector": query_vec_txt["vector"],
 "fields": {"description_chunk_.description_1_chunkvector_": 0.7},
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
 chunk_field="description_chunk_",

 # number of returned results
 page_size=5,

 # minimum similarity score to return a match as a result
 min_score=0.2,
)

```
```python
```
Filtering based on specific features is a great option to perform a more refined search. We will explain Relevance AI's available filtering options on the following page.

