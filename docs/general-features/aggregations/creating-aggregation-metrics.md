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

[block:code]
{
  "codes": [
    {
      "code": "avg_price_metric = {\"name\": \"avg_price\", \"field\": \"priceDetails.price\", \"agg\": \"avg\"}\nmax_price_metric = {\"name\": \"max_price\", \"field\": \"priceDetails.price\", \"agg\": \"max\"}\nmin_price_metric = {\"name\": \"min_price\", \"field\": \"priceDetails.price\", \"agg\": \"min\"}",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]



### Sum
Included within our dataset is the field named **propertyDetails.bathrooms** which describes the number of bathrooms in the property.  It will be interesting to understand number of bathrooms in the properties available in the market in a region (for instance to understand where to sell specific bathroom product) using the sum metric.

[block:code]
{
  "codes": [
    {
      "code": "sum_bathroom_metric = {\"name\": \"bathroom_sum\", \"field\": \"propertyDetails.bathrooms\", \"agg\": \"sum\"}",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]
### Cardinality
This type of aggregation orders the items based on unique values. Included within our dataset is the field named **propertyDetails.bathrooms** which describes the number of bathrooms in the property.

[block:code]
{
  "codes": [
    {
      "code": "cardinality_suburbs_metric = {\"name\": \"num_suburbs\", \"field\": \"propertyDetails.suburb\", \"agg\": \"cardinality\"}",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]
