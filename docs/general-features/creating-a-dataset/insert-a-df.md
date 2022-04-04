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
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0-autoresolve-git-conflict/docs_template/general-features/creating-a-dataset/_assets/csv-data-sample.png?raw=true" width="332" alt="4ac37a1-Screen_Shot_2022-01-11_at_5.43.32_pm.png" />
<figcaption>Sample data</figcaption>
<figure>

### Using `insert_df`

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

[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset('quickstart_insert_df')\nds.insert_df(df)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]
