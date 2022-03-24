---
title: "Filters"
slug: "filters-1"
hidden: false
createdAt: "2021-11-21T07:05:21.922Z"
updatedAt: "2022-03-24T02:52:13.805Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fb01cb3-604547f-combined_filters.png",
        "604547f-combined_filters.png",
        1009,
        368,
        "#e7e7e7"
      ],
      "caption": "Example output of filtering Lenovo products all inserted into the database after 01/01/2020"
    }
  ]
}
[/block]
Filters are great tools to retrieve a subset of documents whose data match the criteria specified in the filter.
For instance, in an e-commerce dataset, we can retrieve all products:
* with prices between 200 and 300 dollars
* with the phrase "free return" included in `description` field
* that are produced after January 2020
[block:callout]
{
  "type": "info",
  "body": "Filters are great tools to retrieve a subset of documents whose data match certain criteria. This allows us to have a more fine-grained overview of the data since only documents that meet the filtering criteria will be displayed.",
  "title": "Filters help us find what we need."
}
[/block]
# How to form a filter?

Filters at Relevance AI are defined as Python dictionaries with four main keys:
- `field` (i.e. the data filed in the document you want to filter on)
- `condition` (i.e. operators such as greater than or equal)
- `filter_type` (i.e. the type of filter you want to apply - whether it be date/numeric/text etc.)
- `condition_value` (dependent on the filter type but decides what value to filter on)
[block:code]
{
  "codes": [
    {
      "code": "filter =  [{'field' : 'description',           # field to look at\n            'filter_type' : 'contains',        \n            \"condition\":\"==\",                  \n            \"condition_value\":\"Durian Club\"}]  # searching for \"Durian Club 3 sofa\" ",
      "language": "python"
    }
  ]
}
[/block]
## Filtering operators
Relevance AI covers all common operators:
* "==" (a == b, a equals b)
* "!="  (a != b, a not equals b)
* ">=" (a >= b, a greater that or equals b)
* ">"   (a > b, a greater than b)
* "<"   (a < b, a smaller than b)
* "<=" (a <= b, a smaller than or equals b)

## Filter types
Supported filter types at Relevance AI are listed below.

* contains
* exact_match
* word_match
* categories
* exists
* date
* numeric
* ids
* support for mixing together multiple filters such as in OR situations

We will explain each filter type followed by a sample code snippet in the next pages. There is also a [guide](https://docs.relevance.ai/docs/combining-filters-and-vector-search) on how to combine filters and vector search.