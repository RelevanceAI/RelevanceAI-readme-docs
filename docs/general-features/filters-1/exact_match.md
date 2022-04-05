---
title: "Exact match"
slug: "exact_match"
hidden: false
createdAt: "2021-11-25T05:20:53.996Z"
updatedAt: "2022-01-19T05:16:30.996Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/general-features/_assets/exact-match.png?raw=true" width="2062" alt="Exact match.png" />
<figcaption>Filtering documents with "Durian Leather 2 Seater Sofa" as the product_name.</figcaption>
<figure>

## `exact_match`
This filter works with string values and only returns documents with a field value that exactly matches the filtered criteria. For instance under filtering by 'Samsung galaxy s21', the result will only contain products explicitly having 'Samsung galaxy s21' in their specified field. *Note that this filter is case-sensitive.*

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
      "code": "filter = [\n    {\n        \"field\": \"product_name\",\n        \"filter_type\": \"exact_match\",\n        \"condition\": \"==\",\n        \"condition_value\": \"Durian Leather 2 Seater Sofa\"\n    }\n]",
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



