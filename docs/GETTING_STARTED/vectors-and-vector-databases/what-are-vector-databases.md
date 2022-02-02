---
title: "What are vector databases"
excerpt: "An introduction to vector databases"
slug: "what-are-vector-databases"
hidden: false

---


## What are vector databases?

In the previous section, we can see the importance of vectors and utilising it. However traditional databases are not optimised to store and operate on vectors. So, a database called vector databases that are optimised for storing and search vectors were made, making nearest neighbour cosine similarity search scalable in milliseconds. This nearest neighbor search is much more powerful than the traditional alternatives and allows for search that is not limited to only keyword matching.

### What can a vector database store?

A vector database can store the vector of any kind of data. This is because the advantage of vectors is that through machine learning, vectorizing any kind of data such as text, image, videos, audio, etc is all possible.



> 📘 When we store vectors we are storing the data by their similarities
> 
> Below, we visualise how we map data into a geometrical space that is able to plot the similarity distance between every sample of the dataset. Basically, the closer the vectors are located in the space, the more similar they are.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.31.0/docs_template/GETTING_STARTED/vectors-and-vector-databases/_assets/RelevanceAI_vector_analysis.png?raw=true" width="650" alt="Similar items are closer to each other" />
<figcaption>Analysing your vectors in 3D space</figcaption>
<figure>


### Limitations of open source vector database frameworks?

Some of the common open source frameworks for vector databases are FAISS, Annoy, HNSWlib, etc. However, these vector databases are only designed for vector search, and does not support other vector operations and does not allow storing of metadata alongside the vectors. 

### Hybrid vector database (metadata + vectors)

A hybrid vector database such as Relevance AI stores the vectors alongside the metadata natively, this means you don't need to set up a third party database to link the vectors. This allows you to use vectors without sacrificing any of the operations of a traditional database such as aggregation, traditional keyword search, etc to be combined with vectors. 

Some examples of a hybrid use case: 
- a hybrid search of vector-based search alongside facets and traditional keywords
- applying clustering on the vectors and applying aggregates on a numeric KPI or keyword in the text to get the topic of each cluster and its performance.

For a hybrid vector database like Relevance AI this goes beyond just search but also other forms of vector operation as well.

Some examples of vector operations beyond search:
- vector operations in turning a bunch of `product2vec` vectors into a `brand2vec` or `word2vec` into a `paragraph2vec`. This can be done by allowing aggregations to be performed on vectors such as grouping by a category field and averaging the vector field.
- clustering the vectors to put similar data into groups
- visualizing and projecting vectors for interpretation

### Use cases of vectors and vector databases

Vector databases are growing in popularity because of the importance of vectors. Since vectors and vector databases essentially solve the problems of similarity the number of use cases for it keeps growing every year. Here are some of the most common ones:

- Semantic & unstructured data search
- Recommendation Systems
- Data deduplication & matching
- Topic modelling
- User clustering
- Zero-shot classification
- K-nearest neighbors similarity-based regression
- Semantic Operation
- and many more



> 📘 The vector database is the infrastructure behind building a similarity engine for many use cases
> 
> A good vector and vector database can essentially become the similarity engine to solve all sorts of similarity problems, which enables a wide array of use cases.


## Search in different databases

Because vector databases store a completely different kind of data (vectors), they can perform searches differently from traditional databases. Let us see what are the main difference between the different search approaches employed by databases.



### Keyword-based matching in traditional databases

A traditional database usually searches data through keyword matching. Once given a search query, we can filter the content that contains the query exactly or a few characters away. Although very efficient, this approach can lead to subpar or irrelevant results as it does not handle synonyms, context and personalisation well. For example: searching for "dogs" and it not matching against "puppies".

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.31.0/docs_template/GETTING_STARTED/vectors-and-vector-databases/_assets/RelevanceAI_traditional_db.png?raw=true" width="650" alt="Traditional Databases" />
<figcaption>Traditional Databases</figcaption>
<figure>

### Vector-based search in vector databases

Vector databases uses a method called vector search (also known as nearest neighbour search) to find the closest match. This technique attempts to find the closest vectors that corresponds to our query in the multidimensional space. This means that we are not only limited to the results that correspond exactly to our search query, but we can also accept results that are similar to what we are searching for.


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.31.0/docs_template/GETTING_STARTED/vectors-and-vector-databases/_assets/RelevanceAI_nearest_neighbour.png?raw=true" width="650" alt="Nearest Neighbour" />
<figcaption>Nearest Neighbour</figcaption>
<figure>

A great thing about this, is that depending on the model used to create the vectors, a lot of the issues with keyword matching can be overcome with vector search. This is because vectors can capture the 'semantic' of the data, thus being able to associate two data that might be constructed very differently but having very similar semantics. For example: the word ('puppies' and 'dogs') or ('truck' and 'SUV') have very different character length, characters, etc, but they mean similar things and are often used in the same context. Vector is able to capture these semantic features and through vector search be able to match those two words as similar, thus overcoming the issues that come with keyword matching. 

Furthermore, vector search is also more flexible and can be used for even more use cases. For example, through building a movie recommendation system, we can perform a vector search with the query being the movie a user just viewed and return a list of results that are recommendations of movies that are similar in plot, visuals, etc.

However, there are areas where vectors fall short especially when the vector is not able to capture the similarities. For example, searching for reference numbers, IDs, or specific words that is out of the model's trained vocabulary. These examples are where keyword match would perform better than vector search.

### Combining searches in hybrid vector databases 

- **Hybrid search (keyword + vector)**: As mentioned there are strengths and weaknesses of both keyword and vector approach. A great thing about a hybrid vector database like Relevance AI is the ability to combine keyword and vector to create a hybrid search.
- **Multi-vector search**: Because different kinds of data can be encoded into vectors, searches are not limited to one data type. For example, a query would not be limited to textual data, but may also take into consideration the vectors obtained by image data as well. This is normally not supported for most vector databases, but a feature that has dedicated support in Relevance AI.
- Many more other combination possibilities to create the best search, check out the [better text search](doc:better-text-search-prerequisites) section that goes into this deeper with examples using Relevance AI.

