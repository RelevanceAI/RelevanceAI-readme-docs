---
title: "Regex"
slug: "regex"
hidden: false
createdAt: "2021-11-29T23:13:52.305Z"
updatedAt: "2022-01-19T05:16:17.784Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/04e1816-7cbd106-contains.png",
        "7cbd106-contains.png",
        2048,
        366,
        "#e8e8e2"
      ],
      "caption": "Filtering documents containing \"Durian (\\w+)\" in description using filter_type `regexp`."
    }
  ]
}
[/block]
## `Regex`
This filter returns a document only if it matches regexp (i.e. regular expression). Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.

Relevance AI has the same regular expression schema as Apache Lucene's ElasticSearch to parse queries.

*Note that this filter is case-sensitive.*
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\n# searching for \"Durian\" and more words following and before\nfilters =  [{\n  'field' : 'description', # field to look at\n\t'filter_type' : 'regexp', \n\t\"condition\":\"==\", \n\t\"condition_value\":\".*Durian (\\w+)\"\n}] \nfiltered_data = client.datasets.documents.get_where(dataset_id, filters)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
