---
title: "Aggregation metrics (mean/max/min/sum)"
slug: "creating-aggregation-metrics"
hidden: false
createdAt: "2021-11-14T15:41:33.393Z"
updatedAt: "2022-01-18T07:51:30.653Z"
---
## The `metric` parameter
The metrics parameter is a **list of dictionaries**, with each dictionary consisting of different fields to be used as metrics for grouping data entries.  Keys in each individual dictionary are:
1. **Name**: A custom unique identifier of the metric
2. **Field **: The name of the field to aggregate
3. **Agg**: The aggregation type ("avg", "max", "min", "sum" or "cardinality")

We continue by explaining each aggregation and related examples.

### Average, Minimum and Maximum
Included within our dataset is the field named **priceDetails.price** which describes the price of the property. It will be interesting to see the differences in the price of properties in terms of average, minimum and maximum which can be extracted using the three defined metrics as below:

@@@ aggregation_query, VAR_NAME=avg_price_metric, NAME="avg_price", FIELD="priceDetails.price", TYPE="avg"; aggregation_query, VAR_NAME=max_price_metric, NAME="max_price", FIELD="priceDetails.price", TYPE="max"; aggregation_query, VAR_NAME=min_price_metric, NAME="min_price", FIELD="priceDetails.price", TYPE="min" @@@



### Sum
Included within our dataset is the field named **propertyDetails.bathrooms** which describes the number of bathrooms in the property.  It will be interesting to understand number of bathrooms in the properties available in the market in a region (for instance to understand where to sell specific bathroom product) using the sum metric.

@@@ aggregation_query, VAR_NAME=sum_bathroom_metric, NAME="bathroom_sum", FIELD="propertyDetails.bathrooms", TYPE="sum" @@@
### Cardinality
This type of aggregation orders the items based on unique values. Included within our dataset is the field named **propertyDetails.bathrooms** which describes the number of bathrooms in the property.

@@@ aggregation_query, VAR_NAME=cardinality_suburbs_metric, NAME="num_suburbs", FIELD="propertyDetails.suburb", TYPE="cardinality" @@@