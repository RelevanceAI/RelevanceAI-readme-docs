---
title: "Categories"
slug: "categories"
hidden: false
createdAt: "2021-11-25T06:03:45.435Z"
updatedAt: "2022-01-19T05:16:45.084Z"
---
<figure>
<img src="https://files.readme.io/63e1987-categories.png" width="658" alt="categories.png" />
<figcaption>Filtering documents with "LG" or "Samsung" as the brand.</figcaption>
<figure>
## `categories`
This filter checks the entries in a database and returns ones in which a field value exists in a given filter list. For instance, if the product name is any of Sony, Samsung, or LG. *Note that this filter is case-sensitive.*
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{'field' : 'brand', # field to look at
 'filter_type' : 'categories',
 "condition":"==",
 "condition_value":["LG","samsung"]}] # searching for brands LG and Samsung
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
