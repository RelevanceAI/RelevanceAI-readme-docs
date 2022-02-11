---
title: "Word match"
slug: "exact_match-1"
hidden: false
createdAt: "2021-11-25T05:44:25.366Z"
updatedAt: "2022-01-19T05:16:37.437Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7b28ed8-wordmatch.png",
        "wordmatch.png",
        1974,
        832,
        "#e4e4e1"
      ],
      "caption": "Filtering documents matching \"Home curtain\" in the description field."
    }
  ]
}
[/block]
## `word_match`
This filter has similarities to both `exact_match` and `contains`. It returns a document only if it contains a **word** value matching the filter; meaning substrings are covered in this category but as long as they can be extracted with common word separators like the white-space (blank). For instance, the filter value "Home Gallery",  can lead to extraction of a document with "Buy Home Fashion Gallery Polyester ..." in the description field as both words are explicitly seen in the text. *Note that this filter is case-sensitive.*
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [{'field' : 'description',           # field to look at\n            'filter_type' : 'word_match', \n            \"condition\":\"==\", \n            \"condition_value\":\"Home curtain\"}]  # searching for documents with `home` and `curtain` in description \nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]