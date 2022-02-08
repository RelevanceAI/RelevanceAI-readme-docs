---
title: "Contains"
slug: "filters-2"
hidden: false
createdAt: "2021-11-25T05:18:31.045Z"
updatedAt: "2022-01-19T05:16:24.396Z"
---
<figure>
<img src="https://files.readme.io/7cbd106-contains.png" width="2048" alt="contains.png" />
<figcaption>Filtering documents containing "Durian BID" in description using filter_type `contains`.</figcaption>
<figure>
## `contains`

This filter returns a document only if it contains a string value. Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.
*Note that this filter is case-sensitive.*
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{'field' : 'description', # field to look at
 'filter_type' : 'contains',
 "condition":"==",
 "condition_value":"Durian BID"}] # searching for "Durian BID"
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
