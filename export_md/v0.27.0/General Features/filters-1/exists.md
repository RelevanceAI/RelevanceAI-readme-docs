---
title: "Exists"
slug: "exists"
hidden: false
createdAt: "2021-11-25T06:09:19.375Z"
updatedAt: "2022-01-19T05:16:52.455Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c6d0d9c-exist.png",
        "exist.png",
        880,
        1072,
        "#ededed"
      ],
      "caption": "Filtering documents which include the field \"brand\" in their information."
    }
  ]
}
[/block]
## `exists`
This filter returns entries in a database if a certain field (as opposed to the field values in previously mentioned filter types) exists or doesn't exist in them. For instance, filtering out documents in which there is no field 'purchase-info'. *Note that this filter is case-sensitive.*
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [{'field' : 'brand',    # field to look at\n            'filter_type' : 'exists', \n            \"condition\":\"==\", \n            \"condition_value\":\"\"}] \nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]