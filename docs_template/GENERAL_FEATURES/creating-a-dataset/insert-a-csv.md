---
title: "Insert a CSV"
slug: "insert-a-csv"
hidden: false
createdAt: "2022-01-12T06:07:56.382Z"
updatedAt: "2022-01-17T02:40:49.066Z"
---
A very common format for saving data is `CSV`. The `insert_csv` function enables us to directly upload our CSV files to Relevance AI.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.1.3/docs/GENERAL_FEATURES/creating-a-dataset/_notebooks/creating-a-dataset.ipynb)


## Data:
* Format: the file passed to the `insert_csv` function must be a valid CSV file
* Fields: the CSV file can include as many columns as needed
* Vector fields: the name of vector fields must end in `_vector_`
* Id field: Relevance AI platform identifies unique data entries within a dataset using a field called `_id` (i.e. every document in the dataset must include an `_id` field with a unique value per document). There are some arguments to help you take care of this field when using `insert_csv`

### Handling document unique identifier (`_id`)
* If the dataset includes a unique identifier per document but the name of the field is not `_id`, simply pass the name under `col_for_id`. For instance, in the example below, the field `REF-No` contains the unique identifier that can be passed as `_id`.
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.1.3/docs_template/GENERAL_FEATURES/creating-a-dataset/_assets/csv-data-sample.png?raw=true" width="332" alt="4ac37a1-Screen_Shot_2022-01-11_at_5.43.32_pm.png" />
<figcaption>Sample data</figcaption>
<figure>

### Using `insert_csv`

First, the Relevance AI SDK package must be installed.

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@


Uploading a CSV file is as simple as specifying the CSV path to your file.


@@@ client_dataset, DATASET_ID='quickstart_insert_csv'; insert_csv, CSV_PATH="./sample_data/california_housing_test.csv" @@@
