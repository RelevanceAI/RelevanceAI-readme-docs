---
title: "Quickstart boilerplate"
slug: "quickstart-boilerplate"
excerpt: "Try us out in 5 lines of code!"
hidden: true
createdAt: "2021-12-14T14:08:01.323Z"
updatedAt: "2021-12-14T14:08:01.323Z"
---
## Try us out in 5 lines of code!
Run this Quickstart in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qMLzS4pAQfFBQ1wvCePbkSB6lOlrAcof?usp=sharing)

### 1. Set up Relevance AI
```shell Bash
pip install -U RelevanceAI
```
```shell
```
### 2. Create a dataset and insert data
```python Python
from relevanceai import Client

#"You can sign up/login and find your credentials here: https://development.qualitative-cloud.pages.dev/login"
#"Once you have signed up, click on the value under `Authorization token` and paste it here"
client = Client()

docs = [
	{"_id": "1", "example_vector_": [0.1, 0.1, 0.1], "data": "Documentation"},
	{"_id": "2", "example_vector_": [0.2, 0.2, 0.2], "data": "Best document!"},
	{"_id": "3", "example_vector_": [0.3, 0.3, 0.3], "data": "document example"},
	{"_id": "4", "example_vector_": [0.4, 0.4, 0.4], "data": "this is another doc"},
	{"_id": "5", "example_vector_": [0.5, 0.5, 0.5], "data": "this is a doc"},
]

client.insert_documents(dataset_id="quickstart", docs=docs)
```
```python
```
### 3. Vector search
```python Python (SDK)
client.services.search.vector(
 dataset_id="quickstart",
 multivector_query=[
 {"vector": [0.2, 0.2, 0.2], "fields": ["example_vector_"]},
 ],
 page_size=3,
 query="sample search" # Stored on the dashboard but not required
)
```
```python
```
This is just the start. Relevance AI comes out of the box with support for features such as multi-vector search, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multi-vector query with those features [here](doc:vector-search-prerequisites).

Get started with some example applications you can build with Relevance AI. Check out some other guides below!
- [Text-to-image search with OpenAI's CLIP](doc:quickstart-text-to-image-search)
- [Multi-vector search with your own vectors](doc:search-with-your-own-vectors)
- [Hybrid Text search with Universal Sentence Encoder using Vectorhub](doc:quickstart-text-search)
- [Text search with Universal Sentence Encoder Question Answer from Google](doc:quickstart-question-answering)
