---
title: "Insert a CSV"
slug: "insert-a-csv"
hidden: false
createdAt: "2022-01-12T06:07:56.382Z"
updatedAt: "2022-01-17T02:40:49.066Z"
---
A very common format for saving data is `CSV`. The `insert_csv` function enables us to directly upload our CSV files to Relevance AI.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs/general-features/creating-a-dataset/_notebooks/RelevanceAI_ReadMe_Creating_A_Dataset.ipynb)


## Data:
* Format: the file passed to the `insert_csv` function must be a valid CSV file
* Fields: the CSV file can include as many columns as needed
* Vector fields: the name of vector fields must end in `_vector_`
* Id field: Relevance AI platform identifies unique data entries within a dataset using a field called `_id` (i.e. every document in the dataset must include an `_id` field with a unique value per document). There are some arguments to help you take care of this field when using `insert_csv`

### Handling document unique identifier (`_id`)
* If the dataset includes a unique identifier per document but the name of the field is not `_id`, simply pass the name under `col_for_id`. For instance, in the example below, the field `REF-No` contains the unique identifier that can be passed as `_id`.
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs_template/general-features/creating-a-dataset/_assets/csv-data-sample.png?raw=true" width="332" alt="4ac37a1-Screen_Shot_2022-01-11_at_5.43.32_pm.png" />
<figcaption>Sample data</figcaption>
<figure>

### Using `insert_csv`

First, the Relevance AI SDK package must be installed.

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI-dev[notebook]>=2.0.0",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n\"\"\"\nYou can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api\nOnce you have signed up, click on the value under `Activation token` and paste it here\n\"\"\"\nclient = Client()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


Uploading a CSV file is as simple as specifying the CSV path to your file.


[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset('quickstart_insert_csv')\ncsv_fpath = \"./sample_data/california_housing_test.csv\"\nds.insert_csv(filepath_or_buffer = csv_fpath)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

