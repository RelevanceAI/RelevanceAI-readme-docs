---
title: "Contains"
slug: "filters-2"
hidden: false
createdAt: "2021-11-25T05:18:31.045Z"
updatedAt: "2022-01-19T05:16:24.396Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7cbd106-contains.png",
        "contains.png",
        2048,
        366,
        "#e8e8e2"
      ],
      "caption": "Filtering documents containing \"Durian BID\" in description using filter_type `contains`."
    }
  ]
}
[/block]
## `contains`

This filter returns a document only if it contains a string value. Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.
*Note that this filter is case-sensitive.*
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [{'field' : 'description',           # field to look at\n            'filter_type' : 'contains', \n            \"condition\":\"==\", \n            \"condition_value\":\"Durian BID\"}]  # searching for \"Durian BID\" \nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]