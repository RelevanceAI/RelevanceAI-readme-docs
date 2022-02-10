---
title: "Date"
slug: "date"
hidden: false
createdAt: "2021-11-25T06:20:15.175Z"
updatedAt: "2022-01-19T05:16:58.720Z"
---
<figure>
<img src="https://files.readme.io/885c3f7-date.png" width="1208" alt="date.png" />
<figcaption>Filtering documents which were added to the database after January 2021.</figcaption>
<figure>
## `date`
This filter performs date analysis and filters documents based on their date information. For instance, it is possible to filter out any documents with a production date before January 2021.
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{'field' : 'insert_date_', # field to look at
 'filter_type' : 'date',
 "condition":">=",
 "condition_value":"2021-01-01"}] # searching for production date after 2020-01-01
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
Note that the default format is "yyyy-mm-dd" but can be changed to "yyyy-dd-mm" through the `format` parameter as shown in the example below.
```python Python (SDK)
client = Client(project, api_key)

filter = [{'field' : 'insert_date_', # field to look at
 'filter_type' : 'date',
 "condition":">=",
 "condition_value": "2020-15-05", # searching for production date after May 15th
 "format":"yyyy-dd-MM"
 }]
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
