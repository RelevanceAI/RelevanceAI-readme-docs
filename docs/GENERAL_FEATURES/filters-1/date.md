---
title: "Date"
slug: "date"
hidden: false
createdAt: "2021-11-25T06:20:15.175Z"
updatedAt: "2022-01-19T05:16:58.720Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/885c3f7-date.png",
        "date.png",
        1208,
        1074,
        "#eeeeee"
      ],
      "caption": "Filtering documents which were added to the database after January 2021."
    }
  ]
}
[/block]
## `date`
This filter performs date analysis and filters documents based on their date information. For instance, it is possible to filter out any documents with a production date before January 2021.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \nclient = Client()\n\nfilter =  [{'field' : 'insert_date_',    # field to look at\n            'filter_type' : 'date', \n            \"condition\":\">=\", \n            \"condition_value\":\"2021-01-01\"}] # searching for production date after 2020-01-01\nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Note that the default format is "yyyy-mm-dd" but can be changed to "yyyy-dd-mm" through the `format` parameter as shown in the example below.
[block:code]
{
  "codes": [
    {
      "code": "client = Client(project, api_key)\n\nfilter =  [{'field' : 'insert_date_',  # field to look at\n            'filter_type' : 'date', \n            \"condition\":\">=\", \n            \"condition_value\": \"2020-15-05\", # searching for production date after May 15th \n            \"format\":\"yyyy-dd-MM\"\n           }] \nfiltered_data = client.datasets.documents.get_where(dataset_id, filter)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
