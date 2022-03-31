---
title: "Contains"
slug: "contains"
hidden: false
createdAt: "2021-11-25T05:18:31.045Z"
updatedAt: "2022-01-19T05:16:24.396Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/heads/v2.0.0/docs_template/general-features/_assets/contains.png?raw=true" width="2048" alt="contains.png" />
<figcaption>Filtering documents containing "Durian BID" in description using filter_type `contains`.</figcaption>
<figure>


## `contains`

This filter returns a document only if it contains a string value. Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.
*Note that this filter is case-sensitive.*

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==2.0.0",
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
      "code": "filter = [\n    {\n        \"field\": \"description\",\n        \"filter_type\": \"contains\",\n        \"condition\": \"==\",\n        \"condition_value\": \"Durian BID\"\n    }\n]",
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


