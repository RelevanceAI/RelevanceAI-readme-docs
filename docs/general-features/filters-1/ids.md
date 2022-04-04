---
title: "Ids"
slug: "ids"
hidden: false
createdAt: "2021-11-25T22:22:07.285Z"
updatedAt: "2022-01-19T05:17:10.638Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/general-features/_assets/id.png?raw=true" width="612" alt="id.png" />
<figcaption>Filtering documents based on their id.</figcaption>
<figure>

## `ids`
This filter returns documents whose unique id exists in a given list. It may look similar to 'categories'. The main difference is the search speed.

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
      "code": "filter = [\n    {\n        \"field\": \"_id\",\n        \"filter_type\": \"ids\",\n        \"condition\": \"==\",\n        \"condition_value\": \"7790e058cbe1b1e10e20cd22a1e53d36\"\n    }\n]",
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

