---
title: "Multiple filters"
slug: "multiple-filters"
hidden: false
createdAt: "2021-11-25T22:31:19.531Z"
updatedAt: "2022-01-19T05:17:17.089Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs_template/general-features/_assets/multiple-filters.png?raw=true" width="1009" alt="combined filters.png" />
<figcaption>Filtering results when using multiple filters: categories, contains, and date.</figcaption>
<figure>

## Combining filters
It is possible to combine multiple filters. For instance, the sample code below shows a filter that searches for
* a Lenovo flip cover
* produced after January 2020
* by either Lapguard or 4D brand.
A screenshot of the results can be seen on top.

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI-dev[notebook]",
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
      "code": "filter = [\n    {\n        \"field\": \"description\",\n        \"filter_type\" : \"contains\",\n        \"condition\": \"==\",\n        \"condition_value\": \"Lenovo\"\n    },\n    {\n        \"field\" : \"brand\",\n        \"filter_type\" : \"categories\",\n        \"condition\": \"==\",\n        \"condition_value\": \"['Lapguard', '4D']\"\n    },\n    {\n        \"field\" : \"\"insert_date_\"\",\n        \"filter_type\" : \"date\",\n        \"condition\": \">=\",\n        \"condition_value\": \"2020-01-01\"\n    }\n]",
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


