---
title: "Exact text matching"
slug: "exact-word-search"
excerpt: "Exact word matching"
hidden: false
createdAt: "2021-11-21T06:18:23.815Z"
updatedAt: "2022-01-27T05:19:58.484Z"
---
## Traditional search (exact word matching)
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs_template/SEARCH_FEATURES/_assets/traditional_search.png?raw=true" width="1000" alt="traditional search" />
<figcaption>Traditional search results for query "HP DV6-20.</figcaption>
<figure>

### Concept
This search looks for the closest answer (most relevant data entry) via **exact word matching**.  Therefore, the best use case for the traditional search is when the search result is required to include an exact term within the query string.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs/SEARCH_FEATURES/_notebooks/RelevanceAI_Exact_Text_Matching.ipynb)

### Sample use-cases
- Searching for reference numbers, IDs, or specific words such as the name of a brand (e.g. Nike, Sony)
- Searching for specific filenames

### Sample code
Sample codes using Relevance AI SDK for traditional search endpoint are shown below. Note that to be able to use this search endpoint you need to:
1. install Relevance AI's python SDK (for more information please visit the [installation](https://docs.relevance.ai/docs/installation) page).

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

2. Instantiate a client object to be able to use the services provided by Relevance AI:

@@@ client_instantiation @@@

3. Upload a dataset under your account (for more information please visit the guide on [datasets](https://docs.relevance.ai/docs/project-and-dataset)). Here, we use our eCommerce sample.

@@@ get_ecommerce_dataset_encoded @@@

@@@ dataset_basics, DATASET_ID=QUICKSTART_SEARCH_DATASET_ID @@@

4. We call the hybrid search endpoint with no vectors to perform a pure traditional search:

@@@ traditional_search, QUERY="HP 2.4GHz", FIELD=PRODUCT_TITLE_FIELD @@@

This search is quick and easy to implement. It works very well in the aforementioned use-cases but cannot offer any semantic search. This is because the model has no idea of semantic relations; for instance, the relation between  "puppy" and "dog", or "sparky" and "electrician" is completely unknown to the model. An instance of a failed search is presented in the screenshot below, where the word "puppies" was searched but the closest returned match is "puppet", even though the database includes many entries about dogs and pets.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs_template/SEARCH_FEATURES/_assets/lack_of_semantic_info.png?raw=true" width="1924" alt="lack_of_semantic_info.png" />
<figcaption>Sample search result where the traditional search fails due to lack of semantic information.</figcaption>
<figure>


