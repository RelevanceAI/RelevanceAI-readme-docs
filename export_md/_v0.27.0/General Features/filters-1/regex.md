---
title: "Regex"
slug: "regex"
hidden: false
createdAt: "2021-11-29T23:13:52.305Z"
updatedAt: "2022-01-19T05:16:17.784Z"
---
<figure>
<img src="https://files.readme.io/04e1816-7cbd106-contains.png" width="2048" alt="7cbd106-contains.png" />
<figcaption>Filtering documents containing "Durian (\w+)" in description using filter_type `regexp`.</figcaption>
<figure>
## `Regex`
This filter returns a document only if it matches regexp (i.e. regular expression). Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.

Relevance AI has the same regular expression schema as Apache Lucene's ElasticSearch to parse queries.

*Note that this filter is case-sensitive.*
```python Python (SDK)
from relevanceai import Client
client = Client()

# searching for "Durian" and more words following and before
filters = [{
 'field' : 'description', # field to look at
	'filter_type' : 'regexp',
	"condition":"==",
	"condition_value":".*Durian (\w+)"
}]
filtered_data = client.datasets.documents.get_where(dataset_id, filters)
```
```python
```
