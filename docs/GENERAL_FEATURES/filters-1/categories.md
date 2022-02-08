---
title: "Categories"
slug: "categories"
hidden: false
createdAt: "2021-11-25T06:03:45.435Z"
updatedAt: "2022-01-19T05:16:45.084Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63e1987-categories.png",
        "categories.png",
        658,
        368,
        "#ececec"
      ],
      "caption": "Filtering documents with \"LG\" or \"Samsung\" as the brand."
    }
  ]
}
[/block]
## `categories`
This filter checks the entries in a database and returns ones in which a field value exists in a given filter list. For instance, if the product name is any of Sony, Samsung, or LG. *Note that this filter is case-sensitive.*
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [{'field' : 'brand',                          # field to look at\n            'filter_type' : 'categories', \n            \"condition\":\"==\", \n            \"condition_value\":[\"LG\",\"samsung\"]}]  # searching for brands LG and Samsung\nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
