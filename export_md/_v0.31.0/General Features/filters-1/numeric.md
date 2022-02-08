---
title: "Numeric"
slug: "numeric"
hidden: false
createdAt: "2021-11-25T06:28:37.534Z"
updatedAt: "2022-01-19T05:17:05.147Z"
---
<figure>
<img src="https://files.readme.io/27f8c47-Numeric.png" width="446" alt="Numeric.png" />
<figcaption>Filtering documents with retail price higher than 5000.</figcaption>
<figure>
## `numeric`
This filter is to perform the filtering operators on a numeric value. For instance, returning the documents with a price larger than 1000 dollars.
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{'field' : 'retail_price', # field to look at
 'filter_type' : 'numeric',
 "condition":">",
 "condition_value":5000}]
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
