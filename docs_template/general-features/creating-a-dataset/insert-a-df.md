---
title: "Insert A Dataframe"
slug: "insert-a-df"
hidden: false
createdAt: "2022-01-12T06:07:56.382Z"
updatedAt: "2022-03-21T04:38:41.650Z"
---
You can insert a dataframe easily with Relevance AI.

## Data:
* Format: the file passed to the `insert_csv` function must be a valid Pandas dataframe
* Fields: the dataframe can include as many columns as needed
* Vector fields: the name of vector fields must end in `_vector_`
* Id field: Relevance AI platform identifies unique data entries within a dataset using a field called `_id` (i.e. every document in the dataset must include an `_id` field with a unique value per document). There are some arguments to help you take care of this field when using `insert_df`.

### Handling document unique identifier (`_id`)
* If the dataset includes a unique identifier per document but the name of the field is not `_id`, simply pass the name under `col_for_id`. For instance, in the example below, the field `REF-No` contains the unique identifier that can be passed as `_id`.
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/heads/v2.0.0/docs_template/general-features/creating-a-dataset/_assets/csv-data-sample.png?raw=true" width="332" alt="4ac37a1-Screen_Shot_2022-01-11_at_5.43.32_pm.png" />
<figcaption>Sample data</figcaption>
<figure>

### Using `insert_df`

First, the Relevance AI SDK package must be installed.

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ client_dataset, DATASET_ID='quickstart_insert_df'; insert_df @@@