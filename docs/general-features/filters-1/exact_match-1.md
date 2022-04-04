---
title: "Word match"
slug: "exact_match-1"
hidden: false
createdAt: "2021-11-25T05:44:25.366Z"
updatedAt: "2022-01-19T05:16:37.437Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0-autoresolve-git-conflict/docs_template/general-features/_assets/word-match.png?raw=true" width="1974" alt="wordmatch.png" />
<figcaption>Filtering documents matching "Home curtain" in the description field.</figcaption>
<figure>

## `word_match`
This filter has similarities to both `exact_match` and `contains`. It returns a document only if it contains a **word** value matching the filter; meaning substrings are covered in this category but as long as they can be extracted with common word separators like the white-space (blank). For instance, the filter value "Home Gallery",  can lead to extraction of a document with "Buy Home Fashion Gallery Polyester ..." in the description field as both words are explicitly seen in the text. *Note that this filter is case-sensitive.*

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
      "code": "filter = [\n    {\n        \"field\": \"description\",\n        \"filter_type\": \"word_match\",\n        \"condition\": \"==\",\n        \"condition_value\": \"Home curtain\"\n    }\n]",
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

