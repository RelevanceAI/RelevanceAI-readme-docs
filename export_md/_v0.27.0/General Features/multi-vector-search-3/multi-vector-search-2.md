---
title: "Multi-vector search with multiple models"
slug: "multi-vector-search-2"
excerpt: "Guide to using multi-vector search with multiple models"
hidden: false
createdAt: "2021-11-24T07:31:17.104Z"
updatedAt: "2022-01-19T03:53:54.491Z"
---
Multi-vector search means
- Vector search with multiple models (e.g. searching with a `text` vectorizer and an `image` vectorizer)
- Vector search across multiple vector fields (e.g. searching across `title` and `description` with different weightings)

Both of these can be combined to offer a powerful, flexible search.
> 📘 Multi vector search allows us to combine multiple vectors and vector spaces!
>
> Multi-vector search offers a more powerful and more flexible search by combining several vectors across different fields and vectorizers, allowing us to experiment with more combinations of models and configurations.
## Multi-vector search with multiple models

In this section, we present a step-by-step guide on how to perform search via three sets of vectors:
1. produced by a model trained on pure text data in English (called it **default** in this guide)
2. produced by a model trained on pure text data from a multi-language dataset (called it **textmulti** in this guide)
3. produced by a model trained on combined text and image (called it **imagetext** in this guide).

### Step 1. Vectorizing the dataset
Search via vector type X is possible only if the dataset includes data vectorized by model X. This means if we want to search against fields such as `title` and `description`, we need to vectorize them using the available models (i.e. default, textmulti, and imagetext in our example). Please refer to a full guide on how to [create and upload a database](doc:creating-a-dataset) and how to use vectorizers to update a dataset with vectors at [How to vectorize](doc:vectorize-text).

### Step 2. Vectorizing the query
To make a search against vectors of type X, the query must be of the same type. So, if the plan is to use three models, we need three query vectors corresponding to the three models/vectorizers. Sample code showing how to use the three vectorizer endpoints is provided below.  Keep it in mind that, first RelevanceAI must be installed and a client object must be instantiated:
```shell Python (SDK)
pip install RelevanceAI
```
```shell
```

```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the appreared Auth token box below
"""

client = Client()
```
```python
```
Calling the three different vectorizers to vectorize the quary:
```python Python (SDK)
query = "white sneakers" # query text

# three vectorizers
query_vec_txt = client.services.encoders.text(text=query)
query_vec_txtmulti = client.services.encoders.multi_text(text=query)
query_vec_txtimg = client.services.encoders.textimage(text=query)
```
```python
```
### Step 3. Vector search
As it was mentioned earlier, Relevance AI has provided you with a variety of vector search endpoints with different use-cases; please see guide pages such as [Better text Search](https://docs.relevance.ai/docs/better-text-search) for more information on each search endpoint.

#### 3.1. Vector search with multiple vectors
In the sample code below, we show how a vector search can be done by combining all three vector types:
```python Python (SDK)
from relevanceai import Client

client = Client()

query = "white sneakers" # query text

# three vectorizers
query_vec_txt = client.services.encoders.text(text=query)
query_vec_txtmulti = client.services.encoders.multi_text(text=query)
query_vec_txtimg = client.services.encoders.textimage(text=query)

DATASET_ID = 'ecommerce-demo'

vector_search = client.services.search.vector(
		# dataset name
 	dataset_id = DATASET_ID,
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
