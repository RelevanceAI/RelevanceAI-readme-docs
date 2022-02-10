---
title: "Multiple filters"
slug: "multiple-filters"
hidden: false
createdAt: "2021-11-25T22:31:19.531Z"
updatedAt: "2022-01-19T05:17:17.089Z"
---
<figure>
<img src="https://files.readme.io/604547f-combined_filters.png" width="1009" alt="combined filters.png" />
<figcaption>Filtering results when using multiple filters: categories, contains, and date.</figcaption>
<figure>
## Combining filters
It is possible to combine multiple filters. For instance, the sample code below shows a filter that searches for
* a Lenovo flip cover
* produced after January 2020
* by either Lapguard or 4D brand.
A screenshot of the results can be seen on top.
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [
 {"field": 'description',
 "filter_type" : 'contains',
 "condition":"==",
 "condition_value":"Lenovo"},
 	 {"field" : 'brand',
 "filter_type" : 'categories',
 "condition":"==",
 "condition_value":"Lapguard","4D"]},
 {"field": 'insert_date_',
 "filter_type" : 'date',
 "condition":">=",
 "condition_value":"2020-01-01"}
 ]
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
