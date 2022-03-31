---
title: "Categories"
slug: "categories"
hidden: false
createdAt: "2021-11-25T06:03:45.435Z"
updatedAt: "2022-01-19T05:16:45.084Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/heads/v2.0.0/docs_template/general-features/_assets/category.png?raw=true" width="658" alt="categories.png" />
<figcaption>Filtering documents with "LG" or "Samsung" as the brand.</figcaption>
<figure>

## `categories`

This filter checks the entries in a database and returns ones in which a field value exists in a given filter list. For instance, if the product name is any of Sony, Samsung, or LG. *Note that this filter is case-sensitive.*

[block:code]
{
  "codes": [
    {
      "code": "filter = [\n    {\n        \"field\": \"brand\",\n        \"filter_type\": \"categories\",\n        \"condition\": \">=\",\n        \"condition_value\": \"['LG', 'samsung']\"\n    }\n]",
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

