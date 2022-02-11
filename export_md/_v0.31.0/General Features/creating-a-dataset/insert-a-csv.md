---
title: "Insert a CSV"
slug: "insert-a-csv"
hidden: false
createdAt: "2022-01-12T06:07:56.382Z"
updatedAt: "2022-01-17T02:40:49.066Z"
---
A very common format for saving data is `CSV`. The `insert_csv` function enables us to directly upload our CSV files to Relevance AI.

## Data:
* Format: the file passed to the `insert_csv` function must be a valid CSV file
* Fields: the CSV file can include as many columns as needed
* Vector fields: the name of vector fields must end in `_vector_`
* Id field: Relevance AI platform identifies unique data entries within a dataset using a field called `_id` (i.e. every document in the dataset must include an `_id` field with a unique value per document). There are some arguments to help you take care of this field when using `insert_csv`

### Handling document unique identifier (`_id`)
* If the dataset includes a unique identifier per document but the name of the field is not `_id`, simply pass the name under `col_for_id`. For instance, in the example below, the field `REF-No` contains the unique identifier that can be passed as `_id`.
<figure>
<img src="https://files.readme.io/10ec3ec-4ac37a1-Screen_Shot_2022-01-11_at_5.43.32_pm.png" width="332" alt="4ac37a1-Screen_Shot_2022-01-11_at_5.43.32_pm.png" />
<figcaption>Sample data</figcaption>
<figure>
### Using `insert_csv`

First, the Relevance AI SDK package must be installed.
```shell Python (SDK)
pip install -U RelevanceAI==0.27.0
```
```shell
```
Next, a Relevance AI client object must be instantiated:
```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the Auth token box that appears below.
"""

client = Client()
```
```python
```
Uploading a CSV file while marking a field called `REF-No` as the unique identifier:
```python Python (SDK)
CSV_PATH = "PATH-TO-THE-CSV-FILE"
DATASET_ID = "CHOSEN-NAME-FOR-THE-DATASET"
COL_FOR_ID = "REF-No"

client.insert_csv(
 dataset_id=DATASET_ID,
 filepath_or_buffer = CSV_PATH,
 col_for_id = COL_FOR_ID,
 index_col = 0
)
```
```python
```
If your dataset does not include any unique identifier per document, we can create one for you. You can turn off this feature by setting `auto_generate_id=False` when inserting.
```python Python (SDK)
CAV_PATH = "PATH-TO-THE-CSV-FILE"
DATASET_ID = "CHOSEN-NAME-FOR-THE-DATASET"

client.insert_csv(
 dataset_id=DATASET_ID,
 filepath_or_buffer=CAV_PATH,
 auto_generate_id=True, # to allow automatic id generation
 index_col = 0
)
```
```python
```
