---
title: "Quickstart"
slug: "aggregation-quick-start"
excerpt: "Get started with vector aggregations in 3 quick steps"
hidden: false
createdAt: "2021-11-19T05:52:28.650Z"
updatedAt: "2022-03-24T02:52:13.791Z"
---
## Introduction

One of the most useful analysis tools is **grouping** and **aggregating** data based on their similarities and features. Using the Relevance AI platform, datasets can first be grouped and subsequently combined with one or more aggregation metrics which leads to a quick and easy data summarization.

This article briefly explains the main aggregation functions. We use a demo dataset containing different real-estate properties. The goal is to find out how properties differ in terms of average price and other characteristics across different locations in Sydney, Australia.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/general-features/aggregations/_notebooks//RelevanceAI_ReadMe_QuickStart_Aggregations.ipynb)

<figure>
<img src="https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/general-features/_assets/grouping-results.png" width="1458" alt="Screen Shot 2022-01-05 at 9.37.37 pm.png" />
<figcaption>Grouping properties based on location, price, number of bathrooms, etc.</figcaption>
<figure>


First, we need to install Relevance AI's Python SDK.
```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==2.0.0
```
```bash
```

### 1.  Define a client
To use Relevance AI services, you need to instantiate a client object.
```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Activation token` and paste it here
"""
client = Client()
```
```python
```

```python Python (SDK)
import pandas as pd
from relevanceai.datasets import get_realestate_dataset

# Retrieve our sample dataset. - This comes in the form of a list of documents.
documents = get_realestate_dataset()

# ToDo: Remove this cell when the dataset is updated

for d in documents:
  if '_clusters_' in d:
    del d['_clusters_']

pd.DataFrame.from_dict(documents).head()
```
```python
```

```python Python (SDK)
df = client.Dataset("quickstart_aggregation")
df.insert_documents(documents)
```
```python
```

### 3. Set aggregation parameters
There are two main parameters to aggregation, `groupby` and `metrics`. They are  both Python dictionaries with specific fields as shown in the following code snippet; more information is available on the next page.
```python Python (SDK)
#Grouping the Data
location_group = {"name": 'location',
 "field": 'propertyDetails.area',
 "agg": 'category'}

bedrooms_group = {"name": 'bedrooms',
 "field": 'propertyDetails.bedrooms',
 "agg": 'numeric'}

groupby = [location_group, bedrooms_group]

#Creating Aggregation Metrics
avg_price_metric = {"name": 'avg_price',
 "field": 'priceDetails.price',
 "agg": 'avg'}

max_price_metric = {"name": 'max_price',
 "field": 'priceDetails.price',
 "agg": 'max'}

min_price_metric = {"name": 'min_price',
 "field": 'priceDetails.price',
 "agg": 'min'}

sum_bathroom_metric = {"name": 'bathroom_sum',
 "field": 'propertyDetails.bathrooms',
 "agg": 'sum'}

#cardinality_suburbs_metric = {"name": 'num_suburbs',
# "field": 'propertyDetails.suburb',
# "agg": 'cardinality'}

metrics = [avg_price_metric,
 max_price_metric,
 min_price_metric,
 sum_bathroom_metric,
 #cardinality_suburbs_metric
 ]

```
```python
```
### 4. Hit the endpoint
Simply use the dataset_id and the `aggregate` endpoint as shown below; `jsonshower` is our tool for easy and efficient result presentation.
```python Python (SDK)
## TODO: update to the new aggregate
results = client.services.aggregate.aggregate("quickstart_aggregation", metrics = metrics, groupby = groupby)
```
```python
```

# Use jsonshower to demonstrate json result
from jsonshower import show_json
show_json(results, text_fields= list(results[0].keys()))


A detailed explanation of deriving the `groupby` and `metrics` parameters are included in subsequent pages.