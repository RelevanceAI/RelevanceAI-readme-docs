---
title: "Text and vector search (hybrid)"
slug: "hybrid-search-1"
excerpt: "Adjustable word matching and semantics"
hidden: false
createdAt: "2021-11-19T01:41:49.896Z"
updatedAt: "2022-01-27T06:22:06.285Z"
---
### Hybrid search (adjustable word matching and semantics)

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs_template/SEARCH_FEATURES/_assets/RelevanceAI-paviliondv6-20-small_w.png?raw=true" alt="hybrid0.05.png" />
<figcaption>Hybrid search result for query "Pavilion DV6-20" with a small emphasis on word-matching. As can be seen, there is no focus on "DV6-20" in the results and it is not included in the first result.</figcaption>
<figure>


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs_template/SEARCH_FEATURES/_assets/RelevanceAI-paviliondv6-20-large_w.png?raw=true" alt="hybrid0.7.png" />
<figcaption>Hybrid search result for query "Pavilion DV6-20" with a large emphasis on word-matching. As can be seen, the first three returned results, all include the id "DV6-20" in the query.</figcaption>
<figure>


### Concept
This endpoint provides search through both word matching and search in the vector space. There is full control over which one to emphasize via a weighting parameter.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs/SEARCH_FEATURES/_notebooks/RelevanceAI_hybrid_search.ipynb)

### Sample use-cases
* Combining traditional text search with semantic search into one search bar by providing support for ID search and vector search (for example - being able to combine "white shoe" and "Product JI36D" into the same search to return the same result.
* Searching for shoes (sneakers, boots, sandals, etc.) but specifically looking for white-colored ones.

### Sample code
Sample codes using Relevance AI SDK for hybrid search endpoint are shown below. Note that to be able to use this search endpoint you need to:
1. install Relevance AI's python SDK (for more information please visit the [installation](https://docs.relevance.ai/docs/installation) page). To use vectors for search, we must vectorize our data as well as the query. We will use the CLIP encoder for this guide. For more information please visit [how-to-vectorise](https://docs.relevance.ai/docs/how-to-vectorise).

```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==1.2.3
```
```bash
```

```bash Bash
# remove `!` if running the line in a terminal
!pip install vectorhub[sentence-transformers]
```
```bash
```

2. Instantiate a client object to be able to use the services provided by Relevance AI:

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

3. Upload a dataset under your account (for more information please visit the guide on [datasets](https://docs.relevance.ai/docs/project-and-dataset)). Here, we use our eCommerce sample.

```python Python (SDK)
from relevanceai.datasets import get_ecommerce_dataset_encoded

documents = get_ecommerce_dataset_encoded()
{k:v for k, v in documents[0].items() if '_vector_' not in k}
```
```python
```

```python Python (SDK)
df = client.Dataset("quickstart_search")
df.insert_documents(documents)
```
```python
```

4. Hit the hybrid search endpoint as shown below. Note that since we are working with vectors and the dataset is vectorised with the CLIP model, here, we first encode/vectorize the query using the same model:

```python Python (SDK)
query = "large tote sack"
query_vec_txt = model.encode(query)
```
```python
```

```python Python (SDK)
multivector_query=[
        { "vector": query_vec_txt, "fields": [PRODUCT_TITLE_CLIP_VEC]}
    ]
```
```python
```

```python Python (SDK)
results = df.hybrid_search(
    multivector_query=multivector_query,
    text=query,
    fields=[<<FIELD>>]
    page_size=5
)
```
```python
```

This search provides you with both word matching and search in context. You have the option of assigning the desired weight to traditional search. For instance, if word matching is important, the `traditional_weight` parameter is set to a higher value to emphasize exact text matching, it is normally set to a small value (e.g. 0.025 to 0.1). Hybrid search relies on machine learning techniques for vectorizing and similarity detection. Therefore, a vectorizer is needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body).  This model provides you with more exploration possibilities on the effect of traditional and vector search.

