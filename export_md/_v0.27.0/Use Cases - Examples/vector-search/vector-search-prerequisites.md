---
title: "Prerequisites"
slug: "vector-search-prerequisites"
excerpt: "Quick guide on how to perform vector search"
hidden: false
createdAt: "2021-11-10T00:48:21.924Z"
updatedAt: "2021-11-22T09:19:13.229Z"
---
-> ## Vector Search
Vector search is the process of searching for the best match within available data but using vectorized/encoded data and query.
<figure>
<img src="https://files.readme.io/2989a8b-2325c0c-Vector_Search_Infographic_Updated.png" width="4288" alt="2325c0c-Vector_Search_Infographic_Updated.png" />
<figcaption>Vector search full flow at Relevance AI.</figcaption>
<figure>
### Vector search in Relevance AI
There are three main categories for vector search at Relevance AI based on how search endpoints work, all of which support the ability to add traditional keyword matching, faceting, and filters.
|**Standard vector search**|**Diversified search results**|
|:-----:|:-----:|
|Multi-vector search|Diversity search|
|Hybrid search (Vector + Traditional keyword matching)|Multi-modal search|

### Key features
* Experimental
You will have access to all you need to perform a search. From the state of the art models to vectorize data, to fast indexing tools and more importantly strong, varied and easy-to-use search endpoints.

* Easy to Use
Below is an example query of how a standard vector search query with filters, multi-vector, and traditional keyword matching can be constructed.  This sample searches in an eCommerce database for shoes (of any type), produced by brand "ABC" after mid-2020.
```python Python (SDK)
client.services.search.hybrid(
		dataset_id=dataset_id,
 multivector_query=[ {
 "vector": vector,
 "fields": ["descriptiontextmulti_vector_"]}],
 text="shoes",
 fields=["description"],
 filters= [
 {"field" : 'brand',
 "filter_type" : 'contains',
 "condition":"==",
 "condition_value":"ABC"},
 {"field": 'insert_date_',
 "filter_type" : 'date',
 "condition":">=",
 "condition_value":"2020-07-01"}
 ],
 traditional_weight = 0.075,
 page_size=5,
)
```
```python
```
A full explanation of concepts, use-case, as well as a sample code snippet of all the above-mentioned endpoints can be found at [Better Text Search](https://docs.relevance.ai/v0.15.0/docs/better-text-search-prerequisites).
-> ## Why vector search?
Vectors are produced by machine learning models to map concepts and data types familiar to humans (e.g. words or images) to a list of numbers (i.e. a vector). One of the important points about vectors is how vectors referring to similar concepts are close to one another. For instance, vectors representing "tiger" and "lion" are closer to each other and far from points representing words like "automobile", "whiteboard" or "Mars".
Vector search takes advantage of this quality and looks not only for the exact match but also for similar concepts. For instance, you might make a query using the word "shoes"; vector search knows concepts like "sneakers", "sandals", and "boots" are categorized as shoes.
> 📘
>
> Relying on specific features and quality of vectors, vector search looks not only for the exact match in the database but also for similar concepts.

-> ## What I need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)
* RelevanceAI Installed - Full installation guide can be found [here](https://docs.relevance.ai/docs/installation) or
simply run the following command to install the main dependencies.
```shell Python (SDK)
pip install -U RelevanceAI[notebook]
```
```shell
```
The benefits of vectors and vector search were explained on the [Vector Search](https://docs.relevance.ai/docs/what-are-vectors) page. The focus of this guide is to emphasize how Relevance AI provides you with the ability to multiply those benefits by employing multi-vector search.
