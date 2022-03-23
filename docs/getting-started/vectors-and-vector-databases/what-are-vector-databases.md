---
title: "What are vector databases"
excerpt: "An introduction to vector databases"
slug: "what-are-vector-databases"
hidden: false

---


## What are vector databases?

In the previous section, we saw the importance of vectors and utilising it. However traditional databases are not optimised to store and operate on vectors. So, a database called vector databases that are optimised for storing and searching vectors are made, making nearest neighbour cosine similarity search scalable in milliseconds. This nearest neighbor search is much more powerful than the traditional alternatives and enables us for a search that is not limited to keyword matching.

### What can a vector database store?

Machine learning can vectorize any kind of data (e.g. text, image, videos, audio, etc) and a vector database can store all of them regardless of the original data type.



> 📘 When we vectorize data, we are unravelling their similarities
>
> Below, we visualise how we map data into a geometrical space that is able to plot the similarity distance between every sample of the dataset. Basically, the closer the vectors are located in the space, the more similar they are.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/cus-272-create-new-page-in-readme-if-page-slug/docs_template/GETTING_STARTED/vectors-and-vector-databases/_assets/RelevanceAI_vector_analysis.png?raw=true" width="650" alt="Similar items are closer to each other" />
<figcaption>Analysing your vectors in 3D space</figcaption>
<figure>


### Limitations of open source vector database frameworks?

Some of the common open source frameworks for vector databases are FAISS, Annoy, HNSWlib, etc. However, these vector databases are only designed for vector search, and do not support other vector operations or allow storing of metadata alongside the vectors.

### Hybrid vector database (metadata + vectors)

A hybrid vector database such as Relevance AI stores the vectors alongside the metadata natively, this means you don't need to set up a third party database to link the vectors. This allows you to use vectors without sacrificing any of the operations of a traditional database such as aggregation, traditional keyword search, etc to be combined with vectors.

Some examples of a hybrid use case:
- a hybrid search of vector-based search alongside facets and traditional keywords
- applying clustering on the vectors and applying aggregates on a numeric KPI or keyword in the text to get the topic of each cluster and its performance.

For platforms covering hybrid vector databases such as Relevance AI, this goes beyond search and covers other applocations of vector operation such as clustering and recommendation.

Some examples of vector operations beyond search:
- clustering the vectors to discover hidden patterns in data
- visualizing and projecting vectors for interpretation

### Use cases of vectors and vector databases

Vector databases are growing in popularity due to the fact that vectors and vector databases allow ude to solve similarity problems more accurately. Here are some of the most common use:

- Semantic & unstructured data search
- Recommendation Systems
- Data deduplication & matching
- Topic modelling
- User clustering
- Zero-shot classification
- K-nearest neighbors similarity-based regression
- Semantic Operation
- and many more



> 📘 Vector databases are the infrastructure behind building similarity engines for many use cases
>
> A good vector and vector database can essentially become the similarity engine required to solve variety of similarity problems.


## Search in different databases

Since vector databases store different kind of data (vectors), search is conducted differently in such platforms compared to traditional databases. The main difference between available search approaches are:


### Keyword-based matching in traditional databases

A traditional database usually searches data through keyword matching. Once given a search query, we can filter the content that contains the exact query or a few characters of it. Although very efficient, this approach can lead to subpar or irrelevant results as it does not consider synonyms, context and personalisation. For example, searching for "dogs" the model has no information on the relation between "dogs" and "puppies".

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/cus-272-create-new-page-in-readme-if-page-slug/docs_template/GETTING_STARTED/vectors-and-vector-databases/_assets/RelevanceAI_traditional_db.png?raw=true" width="650" alt="Traditional Databases" />
<figcaption>Traditional Databases</figcaption>
<figure>

### Vector-based search in vector databases

Vector databases use a method called vector search (also known as nearest neighbour search) to find the closest match. This technique attempts to find the closest vectors that corresponds to our query in the multidimensional space. This means that we are not only limited to the results that correspond exactly to our search query, but we can also accept results that are similar to what we are searching for.


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/cus-272-create-new-page-in-readme-if-page-slug/docs_template/GETTING_STARTED/vectors-and-vector-databases/_assets/RelevanceAI_nearest_neighbour.png?raw=true" width="650" alt="Nearest Neighbour" />
<figcaption>Nearest Neighbour</figcaption>
<figure>

Variety of issues that are associated with keyword matching techniques can be overcome using vector search. This is because vectors can capture the 'semantic' of the data, thus being able to associate two datapoints that even could be of different types (e.g. text and image) but having very similar semantics. For example: the words ('puppies' and 'dogs') or (picture of a football pitch and the word 'succer').

However, there are areas where vectors fall short especially when the vector is not able to capture the similarities. For example, searching for reference numbers, IDs, or specific words that is out of the model's trained vocabulary. These examples are where keyword matching performs better than vector search.

### Combining searches in hybrid vector databases

- **Hybrid search (keyword + vector)**: As mentioned there are strengths and weaknesses of both keyword and vector approach. A great thing about a hybrid vector database like Relevance AI is the ability to combine keyword and vector to create a hybrid search.
- **Multi-vector search**: Because different kinds of data can be encoded into vectors, searches are not limited to one data type. For example, a query would not be limited to textual data, but may also take into consideration the vectors obtained by image data as well. This is normally not supported for most vector databases, but a feature that has dedicated support in Relevance AI.
- Many more other combination possibilities to create the best search, check out the [better text search](doc:better-text-search-prerequisites) section that goes into this deeper with examples using Relevance AI.

