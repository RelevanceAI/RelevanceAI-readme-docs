---
title: "Exact match"
slug: "exact_match"
hidden: false
createdAt: "2021-11-25T05:20:53.996Z"
updatedAt: "2022-01-19T05:16:30.996Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9ae7394-Exact_match.png",
        "Exact match.png",
        2062,
        472,
        "#e1e0dc"
      ],
      "caption": "Filtering documents with \"Durian Leather 2 Seater Sofa\" as the product_name."
    }
  ]
}
[/block]
## `exact_match`
This filter works with string values and only returns documents with a field value that exactly matches the filtered criteria. For instance under filtering by 'Samsung galaxy s21', the result will only contain products explicitly having 'Samsung galaxy s21' in their specified field. *Note that this filter is case-sensitive.*
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [{'field' : 'product_name',              # field to look at\n            'filter_type' : 'exact_match', \n            \"condition\":\"==\", \n            \"condition_value\":\"Durian Leather 2 Seater Sofa\"}]  # searching for \"Durian Leather 2 Seater Sofa\"\nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
