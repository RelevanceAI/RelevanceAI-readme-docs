---
title: "Grouping the data"
slug: "grouping-the-data"
hidden: false
createdAt: "2021-11-14T15:41:17.447Z"
updatedAt: "2022-01-18T07:50:28.081Z"
---
[block:api-header]
{
  "title": "The `groupby` parameter"
}
[/block]
The groupby parameter is a **list of dictionaries**, with each dictionary consisting of different fields to be used for grouping data entries. Keys in each individual dictionary are:
1. **Name**: A custom unique identifier of the group
2. **Field **: The name of the field to be used for grouping
3. **Agg**: The aggregation type (either categorical or numerical)

There are two main grouping types: categorical and numerical.

### Categorical Grouping
Categorical fields are fields with a string type value. Included within our dataset is a field named **propertyDetails.area** that describes the location of the property. We can use it in categorical grouping as shown below:
[block:code]
{
  "codes": [
    {
      "code": "#In general, the group-by field is structured as\n#{\"name\": ALIAS, \"field\": FIELD, \"agg\": TYPE-OF-GROUP}\n\nlocation_group = {\"name\": 'location', \n                  \"field\": 'propertyDetails.area', \n                  \"agg\": 'category'}",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
### Numerical Grouping
It is possible to group data based on numerical values as well. In our dataset number of bedrooms in the listed properties is present under the field **propertyDetails.bedrooms**. We can use that for aggregation as shown below:
[block:code]
{
  "codes": [
    {
      "code": "#In general, the group-by field is structured as\n#{\"name\": ALIAS, \"field\": FIELD, \"agg\": TYPE-OF-GROUP}\n\nbedrooms_group = {\"name\": 'bedrooms', \n                  \"field\": 'propertyDetails.bedrooms', \n                  \"agg\": 'numeric'}",
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
Multiple different fields can be combined together to identify specific groups. In particular, this example groups by different locations and the number of bedrooms. Note that the code below includes `metrics` as well which are explained in details in the next page.
[block:code]
{
  "codes": [
    {
      "code": "#Initialize Client\nfrom relevanceai import Client\nclient = Client()\n\n#Upload Data\nfrom relevanceai.datasets import get_realestate_dataset\n\ndocs = get_realestate_dataset()\nDATASET_ID = \"quickstart_aggregation\"\nclient.insert_documents(dataset_id=DATASET_ID, docs=docs)\n\n#Grouping the Data\nlocation_group = {\"name\": 'location', \"field\": 'propertyDetails.area', \"agg\": 'category'}\nbedrooms_group = {\"name\": 'bedrooms', \"field\": 'propertyDetails.bedrooms', \"agg\": 'numeric'}\ngroupby = [location_group, bedrooms_group]\n\n#Creating Aggregation Metrics\navg_price_metric = {\"name\": 'avg_price', \"field\": 'priceDetails.price', \"agg\": 'avg'}\nmax_price_metric = {\"name\": 'max_price', \"field\": 'priceDetails.price', \"agg\": 'max'}\nmin_price_metric = {\"name\": 'min_price', \"field\": 'priceDetails.price', \"agg\": 'min'}\nsum_bathroom_metric = {\"name\": 'bathroom_sum', \"field\": 'propertyDetails.bathrooms', \"agg\": 'sum'}\ncardinality_suburbs_metric = {\"name\": 'num_suburbs', \"field\": 'propertyDetails.suburb', \"agg\": 'cardinality'}\nmetrics = [avg_price_metric, max_price_metric, min_price_metric, sum_bathroom_metric, cardinality_suburbs_metric]\n\n#Combining Grouping and Aggregating\noutput = client.services.aggregate.aggregate(dataset_id, metrics = metrics, groupby = groupby)\n\n#Use jsonshower to demonstrate json result\nfrom jsonshower import show_json\nshow_json(output, text_fields= list(output[0].keys()))",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]