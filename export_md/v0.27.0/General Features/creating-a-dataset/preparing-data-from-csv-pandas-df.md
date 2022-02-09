---
title: "Preparing data from CSV / Pandas Dataframe"
slug: "preparing-data-from-csv-pandas-df"
hidden: false
createdAt: "2021-11-02T00:00:24.907Z"
updatedAt: "2022-01-17T02:18:18.269Z"
---
Often our data can come in the form of a CSV or from a Pandas DataFrame. This guide will show you how to upload such data into the Relevance AI platform.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2043fec-insert_from_csv.png",
        "insert from csv.png",
        1924,
        292,
        "#8c8ac1"
      ],
      "caption": "Inserting CSV/Pandas DataFrame"
    }
  ]
}
[/block]
### Cleaning the data for upload

In the code below, we will
- read in a CSV file in Pandas
- add a unique identifier (`_id`) column to each data entry using the UUID package
- convert the data to a list of Python dictionaries that are JSON serializable
[block:callout]
{
  "type": "info",
  "title": "When Uploading a dataset to Relevance AI, you require a `_id` field per document!",
  "body": "An `_id` field is a required unique identifier of each document - the `uuid` package is a great tool to generate such an identifier!"
}
[/block]
To my data, I will need to add a column named `_id`, which represents the unique keys associated with each document. Note that the index field name must be exactly as `_id`.
[block:code]
{
  "codes": [
    {
      "code": "import pandas as pd\nimport uuid\nimport json\n\ndef csv_to_dict(csv_fname: str, num_of_documents: int=2000):\n  df = pd.read_csv(csv_fname)\n  df['_id'] = [uuid.uuid4().__str__() for i in range(len(df))]\n  return json.loads(df.to_json(orient='records'))\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "danger",
  "title": "APIs do not accept Pandas DataFrames directly!",
  "body": "APIs are universal messaging systems, which means they are designed to be usable across all languages and computers. Therefore, Python-specific classes and objects like Pandas DataFrames cannot be passed through the API."
}
[/block]


However, APIs do not accept Pandas DataFrames. Therefore, we need to transform our dataset into a dictionary with the right properties (i.e. each document must be a dictionary containing fields, values must be universal data types such as strings, floats, arrays (Python lists), etc.).

A small sample is shown below:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\"_id\": 0,\n  \"product_name\": 'Alisha Solid Women\"s Cycling Shorts',\n  \"description\": \"Key Features of Alisha Solid...\",\n  \"retail_price\": 999.0\n    },\n    {\"_id\": 1,\n  \"product_name\": \"FabHomeDecor Fabric Double Sofa Bed\",\n  \"description\": \"FabHomeDecor Fabric Double Sofa Bed ...\",\n  \"retail_price\": 32157.0\n    },\n    {\"_id\": 2,\n  \"product_name\": \"AW Bellies\",\n  \"description\": \"Key Features of AW Bellies Sandals Wedges...\",\n  \"retail_price\": 999.0\n    },\n    {\"_id\": 3,\n  \"product_name\": \"Alisha Solid Women\"s Cycling Shorts\",\n  \"description\": \"Key Features of Alisha Solid Women\"s...\",\n  \"retail_price\": 699.0\n    },\n    {\"_id\": 4,\n  \"product_name\": \"Sicons All Purpose Arnica Dog Shampoo\",\n  \"description\": \"Specifications of Sicons All Purpose Arnica...\",\n  \"retail_price\": 220.0\n    },\n...]",
      "language": "json"
    }
  ]
}
[/block]