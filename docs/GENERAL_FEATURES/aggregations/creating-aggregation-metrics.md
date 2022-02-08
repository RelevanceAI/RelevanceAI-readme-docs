---
title: "Aggregation metrics (mean/max/min/sum)"
slug: "creating-aggregation-metrics"
hidden: false
createdAt: "2021-11-14T15:41:33.393Z"
updatedAt: "2022-01-18T07:51:30.653Z"
---
[block:api-header]
{
  "title": "The `metric` parameter"
}
[/block]
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
      "code": "#In general, the metrics field is structured as\n#{\"name\": ALIAS, \"field\": FIELD, \"agg\": TYPE-OF-AGG}\n\navg_price_metric = {\"name\": 'avg_price', \"field\": 'priceDetails.price', \"agg\": 'avg'}\nmax_price_metric = {\"name\": 'max_price', \"field\": 'priceDetails.price', \"agg\": 'max'}\nmin_price_metric = {\"name\": 'min_price', \"field\": 'priceDetails.price', \"agg\": 'min'}",
      "language": "python",
      "name": "Python (SDK)"
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
      "code": "#In general, the metrics field is structured as\n#{\"name\": ALIAS, \"field\": FIELD, \"agg\": TYPE-OF-AGG}\n\nsum_bathroom_metric = {\"name\": 'bathroom_sum', \n                       \"field\": 'propertyDetails.bathrooms', \n                       \"agg\": 'sum'}",
      "language": "python",
      "name": "Python (SDK)"
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
      "code": "#In general, the metrics field is structured as\n#{\"name\": ALIAS, \"field\": FIELD, \"agg\": TYPE-OF-AGG}\n\ncardinality_suburbs_metric = {\"name\": 'bathroom_cardinality',\n                              \"field\": 'propertyDetails.bathrooms',\n                              \"agg\": 'cardinality'}",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Putting it together"
}
[/block]
Multiple different fields can be combined together to calculate different metrics. In particular, this example calculates the average price, max price, min price and the total number of bathrooms.
[block:code]
{
  "codes": [
    {
      "code": "#Initialise Client\nfrom relevanceai import Client\n\nclient = Client()\n\n#Upload Data\nfrom relevanceai.datasets import get_realestate_dataset\n\ndocs = get_realestate_dataset()\nDATASET_ID = \"quickstart_aggregation\"\nclient.insert_documents(dataset_id=DATASET_ID, docs=docs)\n\n#Grouping the Data\nlocation_group = {\"name\": 'location', \"field\": 'propertyDetails.area', \"agg\": 'category'}\nbedrooms_group = {\"name\": 'bedrooms', \"field\": 'propertyDetails.bedrooms', \"agg\": 'numeric'}\ngroupby = [location_group, bedrooms_group]\n\n#Creating Aggregation Metrics\navg_price_metric = {\"name\": 'avg_price', \"field\": 'priceDetails.price', \"agg\": 'avg'}\nmax_price_metric = {\"name\": 'max_price', \"field\": 'priceDetails.price', \"agg\": 'max'}\nmin_price_metric = {\"name\": 'min_price', \"field\": 'priceDetails.price', \"agg\": 'min'}\nsum_bathroom_metric = {\"name\": 'bathroom_sum', \"field\": 'propertyDetails.bathrooms', \"agg\": 'sum'}\ncardinality_suburbs_metric = {\"name\": 'num_suburbs', \"field\": 'propertyDetails.suburb', \"agg\": 'cardinality'}\nmetrics = [avg_price_metric, max_price_metric, min_price_metric, sum_bathroom_metric, cardinality_suburbs_metric]\n\n#Combining Grouping and Aggregating\noutput = client.services.aggregate.aggregate(dataset_id, metrics = metrics, groupby = groupby)\n\n#Use jsonshower to demonstrate json result\nfrom jsonshower import show_json\nshow_json(output, text_fields= list(output[0].keys()))",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
