---
title: "Why experimentation first"
excerpt: "Why we need an experimentation-first vector database"
slug: "why-experimentation-first"
hidden: false

---

## Issues with current vector database solutions

While vector databases are used to power recommendations and search engines - they are ultimately still data science products, which mean they require constant iteration, analysis and feedback to improve. However, modern vector databases are not very easy to experiment with.

### Why are vector databases not easy to experiment with?

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.7/docs_template/GETTING_STARTED/vectors-and-vector-databases/_assets/RelevanceAI_vectorbase_workflow.png?raw=true" width="800" alt="Typical Vector Database Workflow" />
<figcaption>Typical Vector Database Workflow</figcaption>
<figure>

Vector databases are at their core - designed for production-level purposes without enabling the developers to first test which vectors work best for their purposes.

> ❗️ Vectors require a significant amount of finetuning, experimentation and testing.
>
> Vectors/embeddings rarely work as well as we want out of the box. They often require careful model selection, fine-tuning to a specific domain, access to experiment with different search methods and clever data processing to ensure they are successful.



Naturally, when you are experimenting with vector databases, you will come across a number of problems:
- **Model-related problems:**
  - What model do you choose to start with for your data?
  - Was this model trained well and with the proper pre-training and fine-tuning steps?
  - Which layer of the model works best for your application?
  - Does continuing pretraining on your model allow you to improve on your dataset?
- **Search-related problems:**
  - What if you have ID values (e.g. "BYX253") where vectors traditionally fail - can you have it in one search? How much weighting is applied to exact text matching?
  - How does it handle acronyms and long-tail searches?
  - What if you want to apply different filters for different searches?
  - What if you want to combine search results from different fields (for example - the title of an article can be just as important as the description or section headers or maybe you want to reduce the weighting of section headers in preference for the title?)
- **Machine learning problems:**
  - Are there unsupervised techniques to assist with better vectors?
  - How does the vector space represent the data and is it biased or skewed?
  - How does the vector space alter when you finetune with metric learning approaches?

While these range from model problems to data problems, one thing is clear:


> 👍 The quality of your embeddings is proportional to the number of experiments you are able to try.
>
> An experimentation-first vector database allows developers to do just that - iterate on their vectors.

## Relevance AI's provides an experimentation-first vector database

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.7/docs_template/GETTING_STARTED/vectors-and-vector-databases/_assets/RelevanceAI_experimentation_first_example_flow.png?raw=true" width="800" alt="Experimentation-first Vector Database Workflow" />
<figcaption>Experimentation-first Vector Database Workflow</figcaption>
<figure>

Through our experience in developing vector-based applications, we understand the current vector search workflow and want to ensure practitioners and researchers are able to use the best model and best data for their searching/recommending/identification of nearest neighbors.

At a high level, a good vector database comprises of a few components:
- First-class metadata storage with the vectors
- A highly configurable vector search
- Software written to accelerate experimentation
- Infrastructure to help compare vector search results
- Flexible vector search querying to allow you to search across multiple models and multiple fields in 1 line of code
- Good integration and support with traditional search/hybrid search functionalities
- Support for more complex data structures for your vectors to capture structural complexity

We understand that the data and model both matter and all of which influence the vector that is produced.
Our models allow you to significantly reduce the time it takes for vector experiments from months down to weeks. They are also productionisable for developers if required.

### Relevance AI accompaniment of open-source tools accelerate experimentation workflows

In addition to our vector database, we will also be open-sourcing a few tools to help users make the most out of the experimentation workflows. These tools include:
- a Python SDK to our Vector Database
- JSONShower to allow researchers and practitioners to quickly investigate the performance of their models from JSONs inside Jupyter Notebook environments
- Search Comparator is a tool to quickly compare numerous queries and search configurations with customizable metrics and various other utilities like identifying the most different queries across configurations

| **Attribute** |  **Relevance AI**  | **Other Solutions** |
|:-----:|:--------:|:------:|
| Basic vector search with filters   | `/vector` | Weaviate, Milvus, Pinecone, ElasticSearch |
| Flexible vector search queries   |  Sits across all vector search endpoints inside `multivector_query` with adjustable weightings  | ElasticSearch|
| Facets   | Sits across all vector search endpoints inside `facets_list` |  None |
| Support for complex data structures like chunking   | Found at our `/chunk_search` and `/advanced_chunk_search` endpoints |  ElasticSearch |
| Support for hybrid search (combining vector search with traditional text search)   | Easily test this with the `/hybrid` endpoint|  Milvus, ElasticSearch |
| Diversity search   | Easily test this with the `/diversity` endpoint|  None |
| Easy to use API and SDK  | Yes! |  Pinecone |
