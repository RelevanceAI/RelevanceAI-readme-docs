---
title: "Ids"
slug: "ids"
hidden: false
createdAt: "2021-11-25T22:22:07.285Z"
updatedAt: "2022-01-19T05:17:10.638Z"
---
<figure>
<img src="https://files.readme.io/2621527-id.png" width="612" alt="id.png" />
<figcaption>Filtering documents based on their id.</figcaption>
<figure>
## `ids`
This filter returns documents whose unique id exists in a given list. It may look similar to 'categories'. The main difference is the search speed.
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{'field' : '_id', # field to look at
 'filter_type' : 'ids',
 "condition":"==",
 "condition_value":"7790e058cbe1b1e10e20cd22a1e53d36"}]
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
