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
@@@ relevanceai_dev_installation @@@

### 1.  Define a client
To use Relevance AI services, you need to instantiate a client object.
@@@ client_instantiation @@@

@@@ get_realestate_dataset @@@

@@@ dataset_basics, DATASET_ID=AGGREGATION_DATASET_ID @@@

### 3. Set aggregation parameters
There are two main parameters to aggregation, `groupby` and `metrics`. They are  both Python dictionaries with specific fields as shown in the following code snippet; more information is available on the next page.

#### Grouping the Data

@@@ aggregation_query, VAR_NAME=location_group, NAME="location", FIELD="propertyDetails.area", TYPE="category"; aggregation_query, VAR_NAME=bedrooms_group, NAME="bedrooms", FIELD="propertyDetails.bedrooms", TYPE="numeric"; variable, VAR_NAME=groupby, VAR_VALUE=[location_group, bedrooms_group]  @@@


#### Creating Aggregation Metrics

@@@ aggregation_query, VAR_NAME=avg_price_metric, NAME="avg_price", FIELD="priceDetails.price", TYPE="avg"; aggregation_query, VAR_NAME=max_price_metric, NAME="max_price", FIELD="priceDetails.price", TYPE="max"; aggregation_query, VAR_NAME=min_price_metric, NAME="min_price", FIELD="priceDetails.price", TYPE="min"; aggregation_query, VAR_NAME=sum_bathroom_metric, NAME="bathroom_sum", FIELD="propertyDetails.bathrooms", TYPE="sum"; variable, VAR_NAME=metrics, VAR_VALUE=[ avg_price_metric, max_price_metric, min_price_metric, sum_bathroom_metric ] @@@

### 4. Hit the endpoint
Simply use the dataset_id and the `aggregate` endpoint as shown below; `jsonshower` is our tool for easy and efficient result presentation.


@@@ aggregate_dataset @@@

#### Use jsonshower to demonstrate json result


@@@ show_json_text_fields_result_keys, RESULTS=results @@@


A detailed explanation of deriving the `groupby` and `metrics` parameters are included in subsequent pages.
