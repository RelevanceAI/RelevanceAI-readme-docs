---
title: "Numeric"
slug: "numeric"
hidden: false
createdAt: "2021-11-25T06:28:37.534Z"
updatedAt: "2022-01-19T05:17:05.147Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs_template/general-features/_assets/numeric.png?raw=true" width="446" alt="Numeric.png" />
<figcaption>Filtering documents with retail price higher than 5000.</figcaption>
<figure>

## `numeric`
This filter is to perform the filtering operators on a numeric value. For instance, returning the documents with a price larger than 1000 dollars.

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==1.4.5",
      "name": "Bash",
      "language": "bash"
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
      "code": "filter = [\n    {\n        \"field\": retail_price,\n        \"filter_type\": numeric,\n        \"condition\": >,\n        \"condition_value\": 5000\n    }\n]",
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
      "code": "### TODO: update to match the latest SDK\nfiltered_data = ds.get_where(filter)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


