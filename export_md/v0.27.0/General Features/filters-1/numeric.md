---
title: "Numeric"
slug: "numeric"
hidden: false
createdAt: "2021-11-25T06:28:37.534Z"
updatedAt: "2022-01-19T05:17:05.147Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/27f8c47-Numeric.png",
        "Numeric.png",
        446,
        486,
        "#ededed"
      ],
      "caption": "Filtering documents with retail price higher than 5000."
    }
  ]
}
[/block]
## `numeric`
This filter is to perform the filtering operators on a numeric value. For instance, returning the documents with a price larger than 1000 dollars.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [{'field' : 'retail_price',     # field to look at\n            'filter_type' : 'numeric', \n            \"condition\":\">\", \n            \"condition_value\":5000}]\nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]