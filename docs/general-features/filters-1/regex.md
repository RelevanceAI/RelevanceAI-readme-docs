---
title: "Regex"
slug: "regex"
hidden: false
createdAt: "2021-11-29T23:13:52.305Z"
updatedAt: "2022-01-19T05:16:17.784Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/general-features/_assets/regex.png?raw=true" width="2048" alt="7cbd106-contains.png" />
<figcaption>Filtering documents containing "Durian (\w+)" in description using filter_type `regexp`.</figcaption>
<figure>

## `regex`
This filter returns a document only if it matches regexp (i.e. regular expression). Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.

Relevance AI has the same regular expression schema as Apache Lucene's ElasticSearch to parse queries.

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
      "code": "filter = [\n    {\n        \"field\": \"description\",\n        \"filter_type\": \"regexp\",\n        \"condition\": \"==\",\n        \"condition_value\": \".*Durian (\\w+)\"\n    }\n]",
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


