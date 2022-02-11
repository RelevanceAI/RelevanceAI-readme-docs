---
title: "Exact match"
slug: "exact_match"
hidden: false
createdAt: "2021-11-25T05:20:53.996Z"
updatedAt: "2022-01-19T05:16:30.996Z"
---
<figure>
<img src="https://files.readme.io/9ae7394-Exact_match.png" width="2062" alt="Exact match.png" />
<figcaption>Filtering documents with "Durian Leather 2 Seater Sofa" as the product_name.</figcaption>
<figure>
## `exact_match`
This filter works with string values and only returns documents with a field value that exactly matches the filtered criteria. For instance under filtering by 'Samsung galaxy s21', the result will only contain products explicitly having 'Samsung galaxy s21' in their specified field. *Note that this filter is case-sensitive.*
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{'field' : 'product_name', # field to look at
 'filter_type' : 'exact_match',
 "condition":"==",
 "condition_value":"Durian Leather 2 Seater Sofa"}] # searching for "Durian Leather 2 Seater Sofa"
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
