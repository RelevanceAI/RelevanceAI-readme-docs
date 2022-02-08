---
title: "Traditional Search"
slug: "better-text-search-with-hybrid"
excerpt: "Exact word matching"
hidden: false
createdAt: "2021-10-21T02:46:57.322Z"
updatedAt: "2022-01-05T10:54:17.911Z"
---
## Traditional search (exact word matching)
<figure>
<img src="https://files.readme.io/5a47237-traditional.png" width="1930" alt="traditional.png" />
<figcaption>Traditional search results for query "HP DV6-20"</figcaption>
<figure>
### Concept
This search looks for the closest answer (most relevant data entry) via **exact word matching**.  Therefore, the best use-case for traditional search is when the search result is required to include an exact term within the query string.

### Sample use-cases
- Searching for reference numbers, IDs, or specific words such as name of a brand (e.g. Nike, Sony)
- Searching for specific filenames

### Sample code
Sample codes using Relevance-AI SDK and Python requests for traditional search endpoint are shown below. Note that as mentioned on the previous page, there is an installation step before using the Python(SDK).
```python Python (SDK)
from relevanceai import Client

dataset_id = 'ecommerce-demo'

client = Client()

# query text
query = "HP DV6-20"

traditional_search = client.services.search.traditional(
 # dataset name
 dataset_id=dataset_id,

 # the search query
 text=query,

 # text fields in the database against which to match the query
 fields=["product_name"],

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
