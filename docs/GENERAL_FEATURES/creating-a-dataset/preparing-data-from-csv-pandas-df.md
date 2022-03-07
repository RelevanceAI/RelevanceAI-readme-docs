---
title: "Preparing data from CSV / Pandas Dataframe"
slug: "preparing-data-from-csv-pandas-df"
hidden: true
createdAt: "2021-11-02T00:00:24.907Z"
updatedAt: "2022-01-17T02:18:18.269Z"
---
Often our data can come in the form of a CSV or from a Pandas DataFrame. This guide will show you how to upload such data into the Relevance AI platform.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.2/docs_template/GENERAL_FEATURES/creating-a-dataset/_assets/insert-csv-pandas.png?raw=true" alt="insert_into_csv.png" />
<figcaption>Inserting CSV/Pandas DataFrame</figcaption>
<figure>


## Cleaning the data for upload

In the code below, we will
- read in a CSV file in Pandas
- add a unique identifier (`_id`) column to each data entry using the UUID package
- convert the data to a list of Python dictionaries that are JSON serializable


> 📘 When Uploading a dataset to Relevance AI, you require a `_id` field per document!
>
> An `_id` field is a required unique identifier of each document - the `uuid` package is a great tool to generate such an identifier!


To my data, I will need to add a column named `_id`, which represents the unique keys associated with each document. Note that the index field name must be exactly as `_id`.

```python Python (SDK)
import pandas as pd
import uuid
import json

def csv_to_dict(csv_fname: str, num_of_documents: int=2000):
 df = pd.read_csv(csv_fname)
 df['_id'] = [uuid.uuid4().__str__() for i in range(len(df))]
 return json.loads(df.to_json(orient='records'))

```
```python
```

> 🚧 APIs do not accept Pandas DataFrames directly!
>
> APIs are universal messaging systems, which means they are designed to be usable across all languages and computers. Therefore, Python-specific classes and objects like Pandas DataFrames cannot be passed through the API.


However, APIs do not accept Pandas DataFrames. Therefore, we need to transform our dataset into a dictionary with the right properties (i.e. each document must be a dictionary containing fields, values must be universal data types such as strings, floats, arrays (Python lists), etc.).

A small sample is shown below:


```json Python (SDK)
[
 {"_id": 0,
 "product_name": "Alisha Solid Women's Cycling Shorts",
 "description": "Key Features of Alisha Solid...",
 "retail_price": 999.0
 },
 {"_id": 1,
 "product_name": "FabHomeDecor Fabric Double Sofa Bed",
 "description": "FabHomeDecor Fabric Double Sofa Bed ...",
 "retail_price": 32157.0
 },
 {"_id": 2,
 "product_name": "AW Bellies",
 "description": "Key Features of AW Bellies Sandals Wedges...",
 "retail_price": 999.0
 },
 {"_id": 3,
 "product_name": "Alisha Solid Women's Cycling Shorts",
 "description": "Key Features of Alisha Solid Women's...",
 "retail_price": 699.0
 },
 {"_id": 4,
 "product_name": "Sicons All Purpose Arnica Dog Shampoo",
 "description": "Specifications of Sicons All Purpose Arnica...",
 "retail_price": 220.0
 },
...
]
```
```json
```

