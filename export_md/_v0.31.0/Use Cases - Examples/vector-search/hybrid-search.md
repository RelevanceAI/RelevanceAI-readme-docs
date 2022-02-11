---
title: "Combine traditional and vector"
slug: "hybrid-search"
excerpt: "Guide to using vector search that can combine with traditional keyword matching"
hidden: false
createdAt: "2021-10-28T08:04:03.807Z"
updatedAt: "2022-01-05T10:57:22.425Z"
---
# Vector search with hybrid support
Our vector search comes with out of the box hybrid support that combines vector search and keyword matching. This allows for full control over the adjustment between word matching and semantic similarity via a weighting parameter.

By combining traditional text search with semantic search into one search bar. You can get the best of both vector and keyword search. For example vector search is usually weak out of vocabulary queries such as ID search (searching for "Product JI36D").

Instantiating the client object:
```python Python (SDK)
from relevanceai import Client

# getting the SDK client object
client = Client()
```
```python
```
Encoding the query:
```python Python (SDK)
dataset_id = <dataset_id>

query = "white shoes"
query_vec = client.services.encoders.multi_text(text=query)

```
```python
```
Hybrid search:
```python Python (SDK)
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

 # query text
 text=query,

 # text fields against which to match the query
 fields=["description"],

 # number of returned results
 page_size=5,

	 	# weight assigned to word matching
 traditional_weight=0.075
)
```
```python
```
The three parameters we will discuss separately are `traditional_weight`, included `fields` under vector search, and the weight of each vector under `multivector_query`.

### Traditional weight
This parameter identifies how much emphasis is on keyword matching. The query example includes two words, "shoes" and "white". The word "shoes" is conceptually close to other words such as "sneakers", "boots", "sandals" and the word "white" is conceptually close to other words such as "cream". These concepts are embedded in vector relations, meaning if the traditional weight is set to a small value as in the example code all these conceptual relations are considered.

The screenshot below presents a real search result. Note that the database we ran these searches on does not include many entries about white shoes. Also, we only present 25 samples here which obviously contain closer matches containing "white" and "shoes". However, as you can see there are entries such as "Chazer" (a footwear brand) and "FAUSTO Sneakers" that appear in the search without any overlapping words with the query and merely due to the capability of vector search in identifying similar concepts.
<figure>
<img src="https://files.readme.io/8759c45-ea2a797-hybrid-tr0.075.png" width="430" alt="ea2a797-hybrid-tr0.075.png" />
<figcaption>Sample result of the hybrid search endpoint when traditional weight is small; query = "white shoes".</figcaption>
<figure>
But if traditional_weight is increased to a high value like 0.8, the focus will be on the two words rather than the concept. You can see a real sample result in the following screenshot. Even though there is overlap with the previous search results, you can see answers like "Chazer" is moved further down in the list.
<figure>
<img src="https://files.readme.io/eadc4cd-4a8c4fa-hybrid-tr0.99.png" width="419" alt="4a8c4fa-hybrid-tr0.99.png" />
<figcaption>Sample result of the hybrid search endpoint when traditional weight is large; query = "white shoes".</figcaption>
<figure>
### Fields
In the previous example, we used the `description` field as well as the `description_vector_` to perform the search.
However, there are many other possibilities when using vectors. For instance, in the next example, the text matching step is done against `product_name` while two vector fields `descriptiontextmulti_vector_` and  `product_nametextmulti_vector_` are used for vector comparison.
```python Python(SDK)
query = "white shoes"
query_vec = client.services.encoders.multi_text(text=query)

hybrid_search = client.services.search.hybrid(
 # dataset name
 dataset_id=dataset_id,

 multivector_query=[
 {
 "vector": query_vec["vector"],

 # list of vector fields against which to run the query
 "fields": ["descriptiontextmulti_vector_", "product_nametextmulti_vector_"],
 }
 ],

 # query text
 text=query,

 # text fields against which to match the query
 fields=["product_name"],

 # number of returned results
 page_size=5,


		# weight assigned to word matching
 traditional_weight=0.075
)
```
```python
```
Real results are shown in the following table. We can see different results, showing how different vectors can bring more options to search output.
<figure>
<img src="https://files.readme.io/7f785bd-8e1e686-hybrid-mix-simp.png" width="425" alt="8e1e686-hybrid-mix-simp.png" />
<figcaption>Sample result of the hybrid search endpoint when traditional weight is small and different fields are used for search; query = "white shoes".</figcaption>
<figure>
### Adding weight to vector fields
To add more importance to one/some vector fields, it is possible to use weights for them in the setup. A sample code with the produced results is shown below.
```python Python (SDK)
query = "white shoes"
query_vec = client.services.encoders.multi_text(text=query)

hybrid_search = client.services.search.hybrid(
 # dataset name
 dataset_id=dataset_id,

 multivector_query=[
 # assigning a weight og 0.15 to descriptiontextmulti_vector_
 {
 "vector": query_vec["vector"],
 "fields": {"descriptiontextmulti_vector_":0.15},
 },
 # assigning a weight og 0.70 to product_nametextmulti_vector_
 {
 "vector": query_vec["vector"],
 "fields": {"product_nametextmulti_vector_":0.70},
 }
 ],

 # query text
 text=query,

 # text fields against which to match the query
 fields=["product_name"],

 # number of returned results
 page_size=5,

	 # weight assigned to word matching
 traditional_weight=0.075
)
```
```python
```

<figure>
<img src="https://files.readme.io/f837674-13107d6-hybrid-mix-weight.png" width="417" alt="13107d6-hybrid-mix-weight.png" />
<figcaption>Sample result of the hybrid search endpoint when traditional weight is small and different fields with weights are used for search; query = "white shoes".</figcaption>
<figure>
