---
title: "Or"
slug: "or"
excerpt: "How to filter when you have multiple filter requirements"
hidden: false
createdAt: "2021-12-14T02:24:01.377Z"
updatedAt: "2022-01-19T05:18:17.107Z"
---
# Or


The `or` filter helps you filter for multiple conditions. Unlike other filters, the only values used here are `filter_type` and `condition_value`.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilters = [{\n\t'filter_type' : 'or',\n\t\"condition_value\": [\n    {\n      'field' : 'price', \n      'filter_type' : 'numeric', \n      \"condition\":\"<=\", \"condition_value\":90\n    },\n    {\n      'field' : 'price', \n      'filter_type' : 'numeric', \n      \"condition\":\">=\", \n      \"condition_value\": 150\n    }\n  ]}\n]\n\nfiltered_data = client.datasets.documents.get_where(dataset_id, filters)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

## (A or B) and (C or D)

Below, we show an example of how to use 2 lists of filters with `or` logic.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter = [{\n\t'filter_type' : 'or',\n\t\"condition_value\": [\n    {\n      'field' : 'price', \n      'filter_type' : 'numeric', \n      \"condition\":\"<=\", \n      \"condition_value\":90\n    },\n    {\n      'field' : 'price', \n      'filter_type' : 'numeric', \n      \"condition\":\">=\", \n      \"condition_value\": 150\n    }\n  ]},\n  'filter_type' : 'or',\n\t\"condition_value\": [\n    {\n      'field' : 'animal', \n      'filter_type' : 'category', \n      \"condition\":\"==\", \n      \"condition_value\":\"cat\"\n    },\n    {\n      'field' : 'animal', \n      'filter_type' : 'category', \n      \"condition\":\"==\", \n      \"condition_value\": \"dog\"\n    }\n  ]},\n]\n\nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
## (A or B or C) and D

Below, we show an example of how to use 2 lists of filters with `or` logic.

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter = [{\n\t'filter_type' : 'or',\n\t\"condition_value\": [\n    {\n      'field' : 'price', \n      'filter_type' : 'numeric', \n      \"condition\":\"<=\", \n      \"condition_value\":90\n    },\n    {\n      'field' : 'price', \n      'filter_type' : 'numeric', \n      \"condition\":\">=\", \n      \"condition_value\": 150\n    },\n    {\n      'field' : 'value', \n      'filter_type' : 'numeric', \n      \"condition\":\">=\", \n      \"condition_value\": 2\n    },\n  ],\n  {\n      'field' : 'animal', \n      'filter_type' : 'category', \n      \"condition\":\"==\", \n      \"condition_value\":\"cat\"\n  },\n]\n\nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]