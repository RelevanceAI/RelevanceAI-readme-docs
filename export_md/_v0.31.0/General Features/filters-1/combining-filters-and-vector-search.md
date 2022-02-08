---
title: "Combining filters and vector search"
slug: "combining-filters-and-vector-search"
hidden: false
createdAt: "2021-11-25T22:33:06.798Z"
updatedAt: "2022-01-19T05:12:49.766Z"
---
<figure>
<img src="https://files.readme.io/f819d50-filtervectors.png" width="1014" alt="filter+vectors.png" />
<figcaption>Including filters in a vector search.</figcaption>
<figure>
## Including filters in vector search
Filtering provides you with a subset of a database containing data entities that match the certain criteria set as filters. What if we need to search through this subset? The difficult way is to ingest (save) the subset as a new dataset, then make the search on the new dataset. However, RelevanceAI has provided the filtering option in almost all search endpoints. This makes the whole process much faster and more straightforward.
In the code snippet below we show a hybrid search sample which is done on a subset of a huge database via filtering. In this scenario, the user is looking for white sneakers but only the ones produced after mid-2020 and from two brands Nike and Adidas.

Note that the code below needs
1. Relevance AI's Python SDK to be installed.
2. A dataset named `ecommerce-search-example`
3. Vectorized description saved under the name `descriptiontextmulti_vector_`

Please refer to a full guide on how to [create and upload a database](doc:creating-a-dataset) and how to use vectorizers to update a dataset with vectors at [How to vectorize](doc:vectorize-text).
```python Python (SDK)
from relevanceai import Client

dataset_id = "ecommerce-search-example"

client = Client()

query = "white shoes"
query_vec = client.services.encoders.multi_text(text=query)

filters = [
 {"field" : 'brand',
 "filter_type" : 'contains',
 "condition":"==",
 "condition_value":"Asian"},
 {"field": 'insert_date_',
 "filter_type" : 'date',
 "condition":">=",
 "condition_value":"2020-07-01"}
 ]

hybrid_search = client.services.search.hybrid(
 # dataset name
 dataset_id=dataset_id,

 multivector_query=[
 {
 "vector": query_vec["vector"],

 # list of vector fields against which to run the query
 "fields": ["descriptiontextmulti_vector_"],
 }
 ],

 # text fields against which to match the query
 fields=["description"],

 # applying filters on search
 filters= filters,

 # query text
 text=query,

 # traditional_weight
 traditional_weight = 0.075,

 # number of returned results
 page_size=5,
)

```
```python
```
