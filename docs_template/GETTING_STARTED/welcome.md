---
title: "Relevance AI"
excerpt: "Start experimenting faster with Relevance AI in 5 minutes!"
slug: "welcome"
hidden: false
createdAt: "2022-01-10T01:31:01.336Z"
updatedAt: "2022-01-10T01:31:01.336Z"
---


Relevance AI's ultimate goal is to assist developers to experiment, build and share the best vectors to solve similarity and relevance based problems across teams.


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.31.0/docs_template/_assets/RelevanceAI_DS_Workflow.png?raw=true"  width="450" alt="Relevance AI DS Workflow" />
<figcaption>How Relevance AI helps with the data science workflow</figcaption>
<figure>


## In 5 lines of code, get a shareable dashboard for experiments insight!

Run this Quickstart in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v0.31.0/docs/GETTING_STARTED/_notebooks/Intro_to_Relevance_AI.ipynb)

### 1. Set up Relevance AI

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

### 2. Create a dataset with vectors


@@@ quickstart_docs, DATASET_ID=QUICKSTART_DATASET_ID @@@

### 3. Clustering

```python Python (SDK)

clusterer = df.auto_cluster("kmeans-2", ["example_vector_"])

```
```python
```


### 4. Vector Search


```python Python (SDK)
vector_search = df.vector_search(
    multivector_query=[
        {"vector": [0.2, 0.2, 0.2], "fields": ["example_vector_"]},
    ],
    page_size=3,
    query="sample search" )
```
```python
```



### 5. Projector

Coming Soon!

### 6. Comparator

Coming Soon!


## What Next?
This is just the start. Relevance AI comes out of the box with support for more advanced features such as multi-vector search, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multi-vector query with those features [here](doc:vector-search-prerequisites).

**Get started with some example applications you can build with Relevance AI. Check out some other guides below!**
- [Text-to-image search with OpenAI's CLIP](doc:quickstart-text-to-image-search)
- [Multi-vector search with your own vectors](doc:search-with-your-own-vectors)
- [Hybrid Text search with Universal Sentence Encoder using Vectorhub](doc:quickstart-text-search)
- [Text search with Universal Sentence Encoder Question Answer from Google](doc:quickstart-question-answering)

