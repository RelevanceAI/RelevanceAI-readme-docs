---
title: "Setting up the search comparator"
slug: "set-up"
hidden: true
createdAt: "2021-10-26T02:57:21.260Z"
updatedAt: "2021-12-20T07:38:46.281Z"
---
## Installation and initial setups
Installation, getting an instance of Relevance AI  (to access the database and perform the search), and getting an instance of `search-comparator` is shown in the sample below:
```shell Shell
pip install -U -q search-comparator RelevanceAI
```
```shell
```

```python Python (SDK)
from relevanceai import Client
client = Client()

from search_comparator import Comparator
comparator = Comparator()
```
```python
```
## Loading the desired models to compare
These models can be publicly available ones such as Universal Sentence Encoder (USE) and sentence transformer, or models that are trained or fine-tuned locally.
Samples of both cases are shown in the code snippet below:
>>???<< Do we include vectorhub in this guide? What models to use?

```python Python (SDK)
from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec

vectorizer1 = SentenceTransformer2Vec("msmarco-roberta-base-v3") # publically availabel online
vectorizer2 = SentenceTransformer2Vec("Path-to-finetune") # locally finetuned
```
```python
```
Note that in the database that is used for search, there should be a corresponding field for all the models. For instance, if running a search against a text field called "description" and when using three different models (vectoriser_1, vectoriser_2, vectoriser_3), the database must have the three corresponding fields such as (`description_vec1_vector_`, `description_vec2_vector_`, `description_vec3_vector_`) which are the vectorized version of the description text produced by each vectorizer/encoder.

## Setting up all the searches
All searches should be defined in the form of a Python function that receives a query text and returns a list of results; for more information, please refer to [complete documentation](https://docs.relevance.ai/docs/better-text-search) on text searches provided by Relevance AI.

In the following code snippet, we have provided 4 search functions using the loaded vectorizers above and under two different text-search endpoints (hybrid search and vector search). The end result would be a comparison between:
    * vector search with `msmarco-roberta-base-v3` as the encoder (vec-search-original)
    * hybrid search with `msmarco-roberta-base-v3` as the encoder (hyb-search-original)
    * vector search with the locally fine-tuned model as the encoder (vec-search-finetuned)
    * vector search with the locally fine-tuned model as the encoder (hyb-search-finetuned)
```python Python (SDK)
database_name = <database_name>

def vector_original_encoder(query):
 vector = vectorizer1.encode(query)
 return client.services.search.vector(
 database_name, [{"vector": vector, "fields": ["description_vec1_vector_"]}], page_size=10
 )['results']

def hybrid_original_encoder(query):
 vector = vectorizer1.encode(query)
 return client.services.search.hybrid(
 database_name, [{"vector": vector, "fields": ["description_vec1_vector_"], }], page_size=10
 )['results']

def vector_finetuned_encoder(query):
 vector = vectorizer2.encode(query)
 return client.services.search.vector(
 database_name, [{"vector": vector, "fields": ["description_vec2_vector_"]}], page_size=10
 )['results']

def hybrid_finetuned_encoder(query):
 vector = vectorizer2.encode(query)
 return client.services.search.hybrid(
 database_name, [{"vector": vector, "fields": ["description_vec2_vector_"], }], page_size=10
 )['results']
```
```python
```
## Adding the defined search functions to the search comparator
In this step, we add the search functions to the core of the search comparator so it has access to all the searches. This is for the comparator to be able to run the query and receive all the results.

Adding the four above-mentioned functions with a chosen name for each is shown below:
```python Python (SDK)
comparator.add_search(vector_original_encoder, "vec-search-original")
comparator.add_search(hybrid_original_encoder, "hyb-search-original")
comparator.add_search(vector_finetuned_encoder, "vec-search-finetuned")
comparator.add_search(hybrid_finetuned_encoder, "hyb-search-finetuned")
```
```python
```
