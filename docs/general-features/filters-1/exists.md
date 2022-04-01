---
title: "Exists"
slug: "exists"
hidden: false
createdAt: "2021-11-25T06:09:19.375Z"
updatedAt: "2022-01-19T05:16:52.455Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs_template/general-features/_assets/exists.png?raw=true" width="500" alt="exist.png" />
<figcaption>Filtering documents which include the field "brand" in their information.</figcaption>
<figure>

## `exists`
This filter returns entries in a database if a certain field (as opposed to the field values in previously mentioned filter types) exists or doesn't exist in them. For instance, filtering out documents in which there is no field 'purchase-info'. *Note that this filter is case-sensitive.*

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==1.4.5",
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
      "code": "DATASET_ID = \"ecommerce-sample-dataset\"\nds = client.Dataset(DATASET_ID)",
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
      "code": "filter = [\n    {\n        \"field\": \"brand\",\n        \"filter_type\": \"exists\",\n        \"condition\": \"==\",\n        \"condition_value\": \" \"\n    }\n]",
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
      "code": "\nfiltered_data = ds.get_documents(filters=filter, n = 20)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


