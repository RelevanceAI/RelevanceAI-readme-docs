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

In this section, we present how to perform search via three sets of vectors:
1. produced by a model trained on pure text data in English (called it **default** in this guide)
2. produced by a model trained on pure text data from a multi-language dataset (called it **textmulti** in this guide)
3. produced by a model trained on combined text and image (called it **imagetext** in this guide).
The models behind them are universal sentence encoder and CLIP, more information can be found on [How to vectorize](doc:vectorize-text).

### Step 1. Vectorizing the dataset
Search via vector type X is possible only if the dataset includes data vectorized by model X. This means if we want to search against fields such as `title` and `description`, we need to vectorize them using the available models (i.e. default, textmulti, and imagetext in our example). Please refer to a full guide on how to [create and upload a database](doc:creating-a-dataset) and how to use vectorizers to update a dataset with vectors at [How to vectorize](doc:vectorize-text).

### Step 2. Vectorizing the query
To make a search against vectors of type X, the query must be of the same type. So, if the plan is to use three models, we need three query vectors corresponding to the three models/vectorizers.

Vectorizing under Relevance AI's platform requires three steps:
1. installation of the related model
2. defining an encoder object
3. vectorizing

 Keep it in mind that, first RelevanceAI must be installed and a client object must be instantiated:

```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==1.3.1
```
```bash
```

```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Activation token` and paste it here
"""
client = Client()
```
```python
```

See the guide on [How to vectorize](doc:vectorize-text) to learn how to define different vectorizers. Here, we call them `enc_default`, `enc_textmulti` and `enc_imagetext`.

Calling the three different vectorizers to vectorize the quary:

```python Python (SDK)
query = "white sneakers"
query_vec_txt = enc_default.encode(query)
```
```python
```
```python Python (SDK)
query = "white sneakers"
query_vec_txt = enc_textmulti.encode(query)
```
```python
```
```python Python (SDK)
query = "white sneakers"
query_vec_txt = "enc_imagetext".encode(query)
```
```python
```

### Step 3. Vector search
As it was mentioned earlier, Relevance AI has provided you with a variety of vector search endpoints with different use-cases; please see guide pages such as [Better text Search](https://docs.relevance.ai/docs/better-text-search) for more information on each search endpoint.

#### 3.1. Vector search with multiple vectors
In the sample code below, we show how a vector search can be done by combining all three vector types:

```python Python (SDK)
# Create a multivector query
multivector_query = [
    {"vector": query_vec_txt, "fields": "description_default_vector_"},
    {"vector": query_vec_txtmulti, "fields": "descriptiontextmulti_vector_"},
    {"vector": query_vec_txtimg, "fields": "description_imagetext_vector_"}
]
```
```python
```

```python Python (SDK)
DATASET_ID = "ecommerce-sample-dataset"
df = client.Dataset(DATASET_ID)
```
```python
```

```python Python (SDK)
results = df.vector_search(
    multivector_query=multivector_query,
    page_size=5
)
```
```python
```

