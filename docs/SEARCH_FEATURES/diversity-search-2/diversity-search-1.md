---
title: "Diversity Search"
slug: "diversity-search-1"
excerpt: "No word matching, just semantics with clustering"
hidden: false
createdAt: "2021-11-19T01:41:21.525Z"
updatedAt: "2022-01-27T06:27:26.158Z"
---
## Diversity in search (no word matching, just semantics with clustering)
<figure>
<img src="https://files.readme.io/7c62334-diversity.png" width="1640" alt="diversity.png" />
<figcaption>Diversity search results for query "birthday gift". As can be seen, results include a variety of items.</figcaption>
<figure>
### Concept
Diversity is similar to vector search and performs the search in the vector space. It provides you with the ability to search for context as opposed to exact word matching. Diversity search, however, employs clustering as a step after search to add variety to the results: search results are clustered and top items of each cluster are shown.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EErP4mlEMx-35CZjuGO5o-RohWmgfy5L?usp=sharing)

### Sample use-case
Looking for "sneakers" under this search in a sportswear dataset will result in an answer list but not just a list of 1 particular shoe like Nike but a combination of Nike, Adidas, Asics, etc. This is important because in vector spaces - it may automatically tie a specific brand to one item in particular. As a result - we may want to get a larger diversity of the most relevant results in a streamlined manner.

### Sample code
Sample codes using RelevanceAI SDK for diversity search endpoint are shown below.
```python Python(SDK)
from relevanceai import Client

dataset_id = "ecommerce-search-example"

client = Client()

query = "birthday gift" # query text
query_vec = client.services.encoders.text(text=query)

url = "https://gateway-api-aueast.relevance.ai/v1/"
diversity_search = client.services.search.diversity(
 # dataset name
 "dataset_id": dataset_id,

 # list of vector fields to run the query against
 "multivector_query": [
 {"vector": client.services.encoders.multi_text(text=query)['vector'],
 "fields": ["descriptiontextmulti_vector_", "product_nametextmulti_vector_"]},

 {"vector": client.services.encoders.textimage(text=query)['vector'],
 "fields": ["description_imagetext_vector_"]}
 ],

 # vector field on which the clustering is done
 "cluster_vector_field": "product_nametextmulti_vector_",

 # number of clusters
 n_clusters=5,

 # number of returned results
 page_size=20,

 # minimum similarity score to return a match as a result
 min_score=0.2,
)

```
```python
```
This search is slightly longer than [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both) due to the added clustering step. It relies on machine learning techniques for vectorizing, similarity detection and clustering. Therefore, at least one vectorizer is needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body). Note the increased `page_size` parameter, so that there is enough data for clustering.

