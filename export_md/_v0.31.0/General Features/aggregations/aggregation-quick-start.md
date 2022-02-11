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
<figure>
<img src="https://files.readme.io/cdbd56f-Screen_Shot_2022-01-05_at_9.37.37_pm.png" width="1458" alt="Screen Shot 2022-01-05 at 9.37.37 pm.png" />
<figcaption>Grouping properties based on location, price, number of bathrooms, etc.</figcaption>
<figure>
First, we need to install Relevance AI's Python SDK.
```shell Python (SDK)
pip install -U RelevanceAI[notebook]==0.27.0
```
```shell
```
### 1.  Define a client
To use Relevance AI services, you need to instantiate a client object.
```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the appreared Auth token box below
"""

client = Client()
```
```python
```
### 2. Upload data
```python Python (SDK)
from relevanceai.datasets import get_realestate_dataset

docs = get_realestate_dataset()
DATASET_ID = "quickstart_aggregation"

client.insert_documents(dataset_id=DATASET_ID, docs=docs)
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
output = client.services.aggregate.aggregate(dataset_id,
 metrics = metrics,
 groupby = groupby)

#Use jsonshower to demonstrate json result
from jsonshower import show_json

show_json(output, text_fields= list(output[0].keys()))

```
```python
```

-> ## Put it all together

```python Python (SDK)
#Initialise Client
from relevanceai import Client

client = Client()

#Upload a dataset to your account
from relevanceai.datasets import get_realestate_dataset

docs = get_realestate_dataset()
DATASET_ID = "quickstart_aggregation"

client.insert_documents(dataset_id=DATASET_ID, docs=docs)

#Grouping the Data
location_group = {"name": 'location', "field": 'propertyDetails.area', "agg": 'category'}
bedrooms_group = {"name": 'bedrooms', "field": 'propertyDetails.bedrooms', "agg": 'numeric'}
groupby = [location_group, bedrooms_group]

#Creating Aggregation Metrics
avg_price_metric = {"name": 'avg_price', "field": 'priceDetails.price', "agg": 'avg'}
max_price_metric = {"name": 'max_price', "field": 'priceDetails.price', "agg": 'max'}
min_price_metric = {"name": 'min_price', "field": 'priceDetails.price', "agg": 'min'}
sum_bathroom_metric = {"name": 'bathroom_sum', "field": 'propertyDetails.bathrooms', "agg": 'sum'}
cardinality_suburbs_metric = {"name": 'num_suburbs', "field": 'propertyDetails.suburb', "agg": 'cardinality'}
metrics = [avg_price_metric, max_price_metric, min_price_metric, sum_bathroom_metric, cardinality_suburbs_metric]

#Combining Grouping and Aggregating
output = client.services.aggregate.aggregate(dataset_id, metrics = metrics, groupby = groupby)

#Use jsonshower to demonstrate json result
from relevanceai import show_json
show_json(output, text_fields= list(output[0].keys()))
```
```python
```
A detailed explanation of deriving the `groupby` and `metrics` parameters are included in subsequent pages.
