---
title: "Multiple filters"
slug: "multiple-filters"
hidden: false
createdAt: "2021-11-25T22:31:19.531Z"
updatedAt: "2022-01-19T05:17:17.089Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/604547f-combined_filters.png",
        "combined filters.png",
        1009,
        368,
        "#e7e7e7"
      ],
      "caption": "Filtering results when using multiple filters: categories, contains, and date."
    }
  ]
}
[/block]
## Combining filters
It is possible to combine multiple filters. For instance, the sample code below shows a filter that searches for
* a Lenovo flip cover
* produced after January 2020
* by either Lapguard or 4D brand.
A screenshot of the results can be seen on top.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [\n   {\"field\": 'description', \n    \"filter_type\" : 'contains', \n    \"condition\":\"==\", \n    \"condition_value\":\"Lenovo\"},\n \t {\"field\" : 'brand', \n    \"filter_type\" : 'categories', \n    \"condition\":\"==\", \n    \"condition_value\":\"Lapguard\",\"4D\"]},\n   {\"field\": 'insert_date_',\n    \"filter_type\" : 'date', \n    \"condition\":\">=\", \n    \"condition_value\":\"2020-01-01\"}\n ]\nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
