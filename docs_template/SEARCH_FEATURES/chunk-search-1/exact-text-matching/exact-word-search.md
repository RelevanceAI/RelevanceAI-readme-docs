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
<img src="https://files.readme.io/5a47237-traditional.png" width="1930" alt="traditional.png" />
<figcaption>Traditional search results for query "HP DV6-20"</figcaption>
<figure>
### Concept
This search looks for the closest answer (most relevant data entry) via **exact word matching**.  Therefore, the best use case for the traditional search is when the search result is required to include an exact term within the query string.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Laa19J1QdWpjY2j35J1zgY9V6EPVKCSg?usp=sharing)

### Sample use-cases
- Searching for reference numbers, IDs, or specific words such as the name of a brand (e.g. Nike, Sony)
- Searching for specific filenames

### Sample code
Sample codes using Relevance AI SDK for traditional search endpoint are shown below. Note that to be able to use this search endpoint you need to:
1. install Relevance AI's python SDK (for more information please visit the [installation](https://docs.relevance.ai/docs/installation) page).
```shell Python (SDK)
pip install RelevanceAI==0.27.0
```
```shell
```
2. Instantiate a client object to be able to use the services provided by Relevance AI:
```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the appreared Auth token box below
"""

client = Client()
```
```python
```
3. Upload a dataset under your account (for more information please visit the guide on [datasets](https://docs.relevance.ai/docs/project-and-dataset)). Here, we use our eCommerce sample.
```python Python (SDK)
from relevanceai.datasets import get_dummy_ecommerce_dataset

documents = get_dummy_ecommerce_dataset()

DATASET_ID = 'quickstart_search'
client.datasets.delete(DATASET_ID)
client.insert_documents(dataset_id=DATASET_ID, docs=documents)
```
```python
```
4. Hit the traditional search endpoint as shown below:
```python Python(SDK)
# query text
query = "HP 2.4GHz"
FIELD = "product_title"

traditional_search = client.services.search.traditional(
 # dataset name
 dataset_id=DATASET_ID,

 # the search query
 text=query,

 # text fields in the database against which to match the query
 fields=[FIELD],

 # number of returned results
 page_size=5,
)
```
```python
```
This search is quick and easy to implement. It works very well in the aforementioned use-cases but cannot offer any semantic search. This is because the model has no idea of semantic relations; for instance, the relation between  "puppy" and "dog", or "sparky" and "electrician" is completely unknown to the model. An instance of a failed search is presented in the screenshot below, where the word "puppies" was searched but the closest returned match is "puppet", even though the database includes many entries about dogs and pets.
<figure>
<img src="https://files.readme.io/7236eff-Screen_Shot_2021-11-18_at_10.59.19_am.png" width="1924" alt="Screen Shot 2021-11-18 at 10.59.19 am.png" />
<figcaption>Sample search result where the traditional search fails due to lack of semantic information.</figcaption>
<figure>
