---
title: "Exists"
slug: "exists"
hidden: false
createdAt: "2021-11-25T06:09:19.375Z"
updatedAt: "2022-01-19T05:16:52.455Z"
---
<figure>
<img src="https://files.readme.io/c6d0d9c-exist.png" width="880" alt="exist.png" />
<figcaption>Filtering documents which include the field "brand" in their information.</figcaption>
<figure>
## `exists`
This filter returns entries in a database if a certain field (as opposed to the field values in previously mentioned filter types) exists or doesn't exist in them. For instance, filtering out documents in which there is no field 'purchase-info'. *Note that this filter is case-sensitive.*
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{'field' : 'brand', # field to look at
 'filter_type' : 'exists',
 "condition":"==",
 "condition_value":""}]
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
