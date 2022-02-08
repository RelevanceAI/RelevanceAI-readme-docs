---
title: "Ids"
slug: "ids"
hidden: false
createdAt: "2021-11-25T22:22:07.285Z"
updatedAt: "2022-01-19T05:17:10.638Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2621527-id.png",
        "id.png",
        612,
        111,
        "#eaeaea"
      ],
      "caption": "Filtering documents based on their id."
    }
  ]
}
[/block]
## `ids`
This filter returns documents whose unique id exists in a given list. It may look similar to 'categories'. The main difference is the search speed.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [{'field' : '_id',     # field to look at\n            'filter_type' : 'ids', \n            \"condition\":\"==\", \n            \"condition_value\":\"7790e058cbe1b1e10e20cd22a1e53d36\"}]\nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
