---
title: "Filters"
slug: "filters"
hidden: false
metadata:
  description: "Guide to using filters and combing it with vector search"
createdAt: "2021-10-28T05:34:05.336Z"
updatedAt: "2022-01-19T01:58:50.657Z"
---
<figure>
<img src="https://files.readme.io/fb01cb3-604547f-combined_filters.png" width="1009" alt="604547f-combined_filters.png" />
<figcaption>Example output of filtering Lenovo products all inserted into the database after 01/01/2020</figcaption>
<figure>
Filters are great tools to retrieve a subset of documents whose data match the criteria specified in the filter.
For instance, in an e-commerce dataset, we can retrieve all products:
* with prices between 200 and 300 dollars
* with the phrase "free return" included in the `description` field
* that are produced after January 2020
> 📘 Filters help us find what we need.
>
> Filters are great tools to retrieve a subset of documents whose data match certain criteria. This allows us to have a more fine-grained overview of the data since only documents that meet the filtering criteria will be displayed.
# How to form a filter?

Filters at Relevance AI are defined as Python dictionaries with four main keys:
- `field` (i.e. the data filed in the document you want to filter on)
- `condition` (i.e. operators such as greater than or equal)
- `filter_type` (i.e. the type of filter you want to apply -  such as date/numeric/text etc.)
- `condition_value` (dependent on the filter type but decides what value to filter on)
```python Python (SDK)
filter = [{'field' : 'description', # field to look at
 'filter_type' : 'contains',
 "condition":"==",
 "condition_value":"Durian Club"}] # searching for "Durian Club 3 sofa"
```
```python
```
## Filtering operators
Relevance AI covers all common operators:
* "==" (a == b, a equals b)
* "!="  (a != b, a not equals b)
* ">=" (a >= b, a greater that or equals b)
* ">"   (a > b, a greater than b)
* "<"   (a < b, a smaller than b)
* "<=" (a <= b, a smaller than or equals b)

## Filter types
Supported filter types at Relevance AI are listed below. We will provide you with small sample code snippets corresponding to each filter type in the rest of this page.

* contains
* exact_match
* word_match
* categories
* exists
* date
* numeric
* ids
* support for mixing together multiple filters such as in OR situations


## contains
This filter returns a document only if it contains a string value. Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.
*Note that this filter is case-sensitive.*
```python Python (SDK)
filter = [{'field' : 'description', # field to look at
 'filter_type' : 'contains',
 "condition":"==",
 "condition_value":"Durian Club"}] # searching for "Durian Club 3 sofa"
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```


### exact_match
This filter works with string but it only returns documents with a field value that exactly matches the filtered criteria. For instance under filtering by 'Samsung galaxy s21', the result will only contain products explicitly having 'Samsung galaxy s21' in their specified field. *Note that this filter is case-sensitive.*
```python Python (SDK)
filter = [{'field' : 'product_name', # field to look at
 'filter_type' : 'exact_match',
 "condition":"==",
 "condition_value":"Samsung galaxy s21"}] # searching for "Samsung galaxy s21"
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```


### word_match
This filter has similarities to both exact_match and contains. It returns a document only if it contains a **word** value matching the filter; meaning substrings are covered in this category but as long as they can be extracted with common word separators like the white-space (blank). For instance, the filter value "Home Gallery",  can lead to extraction of a document with "Buy Home Fashion Gallery Polyester ..." in the description field as both words are explicitly seen in the text. *Note that this filter is case-sensitive.*
```python Python (SDK)
filter = [{'field' : 'description', # field to look at
 'filter_type' : 'word_match',
 "condition":"==",
 "condition_value":"Home Gallery"}] # searching for documents with `home` and `gallery` in description
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
### categories
This filter checks the entries in a database and returns ones in which a field value exists in a given filter list. For instance, if the product name is any of Sony, Samsung, or LG. *Note that this filter is case-sensitive.*
```python Python (SDK)
filter = [{'field' : 'brand', # field to look at
 'filter_type' : 'categories',
 "condition":"==",
 "condition_value":["LG","samsung"]}] # searching for brands LG and Samsung
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
### exists
This filter returns entries in a database if a certain field (as opposed to the field values above) exists or does not exist in them. For instance, filtering out documents in which there is no field 'purchase-info'. *Note that this filter is case-sensitive.*
```python Python (SDK)
filter = [{'field' : 'purchase-info', # field to look at
 'filter_type' : 'exists',
 "condition":"==",
 "condition_value":""}]
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
### date
This filter performs date analysis and filters documents based on their date information. For instance, it is possible to filter out any documents with a production date before January 2020. Note that the default format is "yyyy-mm-dd" but can be changed to "yyyy-dd-mm" through the `format` parameter as shown in the second example below.
```python Python (SDK)
filter = [{'field' : 'insert_date_', # field to look at
 'filter_type' : 'date',
 "condition":">=",
 "condition_value":"2020-01-01"}] # searching for production date after 2020-01-01
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```

```python Python (SDK)
filter = [{'field' : 'insert_date_', # field to look at
 'filter_type' : 'date',
 "condition":">=",
 "condition_value":"2020-15-05",
 "format":"yyyy-dd-MM"
 }] # searching for production date after May 15th =
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
### numeric
This filter is to perform the filtering operators on a numeric value. For instance, returning the documents with a price larger than 1000 dollars.
```python Python (SDK)
filter = [{'field' : 'retail_price', # field to look at
 'filter_type' : 'numeric',
 "condition":">",
 "condition_value":1000}]
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
### ids
This filter returns documents whose unique id exists in a given list. It may look similar to 'Categories'. The main difference is the search speed.
```python Python (SDK)
filter = [{'field' : '_id', # field to look at
 'filter_type' : 'ids',
 "condition":"==",
 "condition_value":"1adv27"}]
filtered_data = client.datasets.documents.get_where(dataset_id, filter)
```
```python
```
# Multiple filters
It is possible to combine multiple filters. For instance, the sample code below shows a filter that searches for a Lenovo flip cover that is produced after January 2020 and by either Lapguard or 4D brand. A screenshot of the results can be seen after the code snippet.
```python Python (SDK)
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

<figure>
<img src="https://files.readme.io/604547f-combined_filters.png" width="1009" alt="combined filters.png" />
<figcaption>Filtering results when using multiple filters: categories, contains, and date.</figcaption>
<figure>
# Combining filters and vector search
Filtering provides you with a subset of a database containing data entities that match the certain criteria set as filters. What if we need to search through this subset? The difficult way is to ingest (save) the subset as a new database, then make the search on the new dataset. However, Relevance AI has provided the filtering option in almost all search endpoints. This makes the whole process much faster and more straightforward.
In the code snippet below we show a hybrid search sample which is done on a subset of a huge database via filtering. In this scenario, the user is looking for white sneakers but only the ones produced after mid-2020 and from two brands Nike and Adidas.
```python Python (SDK)
! pip install RelevanceAI

from relevanceai import Client

project = <PROJECT-NAME> # Project name
api_key = <API-KEY> # api-key
dataset_id = <DATASET_ID>

client = Client(project, api_key)

query = "white shoes"
query_vec = client.services.encoders.multi_text(text=query)

filters = [
 {"field" : 'brand',
 "filter_type" : 'contains',
 "condition":"==",
 "condition_value":"Asian"},
 {"field": 'insert_date_',
 "filter_type" : 'date',
 "condition":">=",
 "condition_value":"2020-07-01"}
 ]

hybrid_search = client.services.search.hybrid(
 # dataset name
 dataset_id=dataset_id,

 multivector_query=[
 {
 "vector": query_vec["vector"],

 # list of vector fields against which to run the query
 "fields": ["descriptiontextmulti_vector_"],
 }
 ],

 # text fields against which to match the query
 fields=["description"],

 # applying filters on search
 filters= filters,

 # query text
 text=query,

 # traditional_weight
 traditional_weight = 0.075,

 # number of returned results
 page_size=5,
)

```
```python
```

<figure>
<img src="https://files.readme.io/f819d50-filtervectors.png" width="1014" alt="filter+vectors.png" />
<figcaption>Including filters in a vector search.</figcaption>
<figure>
