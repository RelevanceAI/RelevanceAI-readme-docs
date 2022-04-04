---
title: "Quickstart"
slug: "aggregation-quick-start"
excerpt: "Get started with vector aggregations in 3 quick steps"
hidden: false
createdAt: "2021-11-19T05:52:28.650Z"
updatedAt: "2022-01-18T07:44:28.413Z"
---
## Introduction

One of the most useful analysis tools is **grouping** and **aggregating** data based on their similarities and features. Using the Relevance AI platform, datasets can first be grouped and subsequently combined with one or more aggregation metrics which leads to a quick and easy data summarization.

This article briefly explains the main aggregation functions. We use a demo dataset containing different real-estate properties. The goal is to find out how properties differ in terms of average price and other characteristics across different locations in Sydney, Australia.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/general-features/aggregations/_notebooks/RelevanceAI_ReadMe_Quickstart_Aggregations.ipynb)


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/general-features/_assets/grouping-results.png" width="1458" alt="Grouping Results />
<figcaption>Grouping properties based on location, price, number of bathrooms, etc.</figcaption>
<figure>


First, we need to install Relevance AI's Python SDK.
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

### 1.  Define a client
To use Relevance AI services, you need to instantiate a client object.
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
      "code": "import pandas as pd\nfrom relevanceai.utils.datasets import get_realestate_dataset\n\n# Retrieve our sample dataset. - This comes in the form of a list of documents.\ndocuments = get_realestate_dataset()\n\n# ToDo: Remove this cell when the dataset is updated\n\nfor d in documents:\n  if '_clusters_' in d:\n    del d['_clusters_']\n\npd.DataFrame.from_dict(documents).head()",
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
      "code": "ds = client.Dataset(\"quickstart_aggregation\")\nds.insert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### 3. Set aggregation parameters
There are two main parameters to aggregation, `groupby` and `metrics`. They are  both Python dictionaries with specific fields as shown in the following code snippet; more information is available on the next page.

#### Grouping the Data

[block:code]
{
  "codes": [
    {
      "code": "location_group = {\"name\": \"location\", \"field\": \"propertyDetails.area\", \"agg\": \"category\"}\nbedrooms_group = {\"name\": \"bedrooms\", \"field\": \"propertyDetails.bedrooms\", \"agg\": \"numeric\"}\ngroupby = [location_group, bedrooms_group]",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


#### Creating Aggregation Metrics

[block:code]
{
  "codes": [
    {
      "code": "avg_price_metric = {\"name\": \"avg_price\", \"field\": \"priceDetails.price\", \"agg\": \"avg\"}\nmax_price_metric = {\"name\": \"max_price\", \"field\": \"priceDetails.price\", \"agg\": \"max\"}\nmin_price_metric = {\"name\": \"min_price\", \"field\": \"priceDetails.price\", \"agg\": \"min\"}\nsum_bathroom_metric = {\"name\": \"bathroom_sum\", \"field\": \"propertyDetails.bathrooms\", \"agg\": \"sum\"}\ncardinality_suburbs_metric = {\"name\": \"num_suburbs\", \"field\": \"propertyDetails.suburb\", \"agg\": \"cardinality\"}\ngroupby = [ avg_price_metric, max_price_metric, min_price_metric, sum_bathroom_metric, cardinality_suburbs_metric ]",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### 4. Hit the endpoint
Simply use the dataset_id and the `aggregate` endpoint as shown below; `jsonshower` is our tool for easy and efficient result presentation.
[block:code]
{
  "codes": [
    {
      "code": "results = clusterops.aggregate(\"quickstart_aggregation\", metrics=metrics, groupby=groupby)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

#### Use jsonshower to demonstrate json result


[block:code]
{
  "codes": [
    {
      "code": "from jsonshower import show_json\nshow_json(results, text_fields=list(results[0].keys()))",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


A detailed explanation of deriving the `groupby` and `metrics` parameters are included in subsequent pages.

