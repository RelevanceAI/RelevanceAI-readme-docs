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


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tAHGGry2JYxWqYJNXpj2HnAW3rOGJdGy?usp=sharing)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cdbd56f-Screen_Shot_2022-01-05_at_9.37.37_pm.png",
        "Screen Shot 2022-01-05 at 9.37.37 pm.png",
        1458,
        770,
        "#f2f2f2"
      ],
      "caption": "Grouping properties based on location, price, number of bathrooms, etc."
    }
  ]
}
[/block]
First, we need to install Relevance AI's Python SDK.
[block:code]
{
  "codes": [
    {
      "code": "pip install -U RelevanceAI[notebook]==0.27.0",
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
      "code": "from relevanceai import Client \n\n\"\"\"\nRunning this cell will provide you with \nthe link to sign up/login page where you can find your credentials.\nOnce you have signed up, click on the value under `Authorization token` \nin the API tab\nand paste it in the appreared Auth token box below\n\"\"\"\n\nclient = Client()",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
### 2. Upload data
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.datasets import get_realestate_dataset\n\ndocs = get_realestate_dataset()\nDATASET_ID = \"quickstart_aggregation\"\n\nclient.insert_documents(dataset_id=DATASET_ID, docs=docs)",
      "language": "python"
    }
  ]
}
[/block]
### 3. Set aggregation parameters
There are two main parameters to aggregation, `groupby` and `metrics`. They are  both Python dictionaries with specific fields as shown in the following code snippet; more information is available on the next page.
[block:code]
{
  "codes": [
    {
      "code": "#Grouping the Data\nlocation_group = {\"name\": 'location', \n                  \"field\": 'propertyDetails.area', \n                  \"agg\": 'category'}\n\nbedrooms_group = {\"name\": 'bedrooms', \n                  \"field\": 'propertyDetails.bedrooms', \n                  \"agg\": 'numeric'}\n\ngroupby = [location_group, bedrooms_group]\n\n#Creating Aggregation Metrics\navg_price_metric = {\"name\": 'avg_price', \n                    \"field\": 'priceDetails.price', \n                    \"agg\": 'avg'}\n\nmax_price_metric = {\"name\": 'max_price', \n                    \"field\": 'priceDetails.price', \n                    \"agg\": 'max'}\n\nmin_price_metric = {\"name\": 'min_price', \n                    \"field\": 'priceDetails.price', \n                    \"agg\": 'min'}\n\nsum_bathroom_metric = {\"name\": 'bathroom_sum', \n                       \"field\": 'propertyDetails.bathrooms', \n                       \"agg\": 'sum'}\n\n#cardinality_suburbs_metric = {\"name\": 'num_suburbs',\n#                              \"field\": 'propertyDetails.suburb', \n#                              \"agg\": 'cardinality'}\n\nmetrics = [avg_price_metric, \n           max_price_metric, \n           min_price_metric, \n           sum_bathroom_metric, \n           #cardinality_suburbs_metric\n          ]\n",
      "language": "python",
      "name": "Python (SDK)"
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
      "code": "output = client.services.aggregate.aggregate(dataset_id, \n                                             metrics = metrics, \n                                             groupby = groupby)\n\n#Use jsonshower to demonstrate json result\nfrom jsonshower import show_json\n\nshow_json(output, text_fields= list(output[0].keys()))\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Put it all together"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "#Initialise Client\nfrom relevanceai import Client\n\nclient = Client()\n\n#Upload a dataset to your account\nfrom relevanceai.datasets import get_realestate_dataset\n\ndocs = get_realestate_dataset()\nDATASET_ID = \"quickstart_aggregation\"\n\nclient.insert_documents(dataset_id=DATASET_ID, docs=docs)\n\n#Grouping the Data\nlocation_group = {\"name\": 'location', \"field\": 'propertyDetails.area', \"agg\": 'category'}\nbedrooms_group = {\"name\": 'bedrooms', \"field\": 'propertyDetails.bedrooms', \"agg\": 'numeric'}\ngroupby = [location_group, bedrooms_group]\n\n#Creating Aggregation Metrics\navg_price_metric = {\"name\": 'avg_price', \"field\": 'priceDetails.price', \"agg\": 'avg'}\nmax_price_metric = {\"name\": 'max_price', \"field\": 'priceDetails.price', \"agg\": 'max'}\nmin_price_metric = {\"name\": 'min_price', \"field\": 'priceDetails.price', \"agg\": 'min'}\nsum_bathroom_metric = {\"name\": 'bathroom_sum', \"field\": 'propertyDetails.bathrooms', \"agg\": 'sum'}\ncardinality_suburbs_metric = {\"name\": 'num_suburbs', \"field\": 'propertyDetails.suburb', \"agg\": 'cardinality'}\nmetrics = [avg_price_metric, max_price_metric, min_price_metric, sum_bathroom_metric, cardinality_suburbs_metric]\n\n#Combining Grouping and Aggregating\noutput = client.services.aggregate.aggregate(dataset_id, metrics = metrics, groupby = groupby)\n\n#Use jsonshower to demonstrate json result\nfrom relevanceai import show_json\nshow_json(output, text_fields= list(output[0].keys()))",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
A detailed explanation of deriving the `groupby` and `metrics` parameters are included in subsequent pages.
