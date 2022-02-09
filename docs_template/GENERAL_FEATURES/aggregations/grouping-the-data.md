---
title: "Grouping the data"
slug: "grouping-the-data"
hidden: false
createdAt: "2021-11-14T15:41:17.447Z"
updatedAt: "2022-01-18T07:50:28.081Z"
---
-> ## The `groupby` parameter
The groupby parameter is a **list of dictionaries**, with each dictionary consisting of different fields to be used for grouping data entries. Keys in each individual dictionary are:
1. **Name**: A custom unique identifier of the group
2. **Field **: The name of the field to be used for grouping
3. **Agg**: The aggregation type (either categorical or numerical)

There are two main grouping types: categorical and numerical.

### Categorical Grouping
Categorical fields are fields with a string type value. Included within our dataset is a field named **propertyDetails.area** that describes the location of the property. We can use it in categorical grouping as shown below:
```python Python (SDK)
#In general, the group-by field is structured as
#{"name": ALIAS, "field": FIELD, "agg": TYPE-OF-GROUP}

location_group = {"name": 'location',
 "field": 'propertyDetails.area',
 "agg": 'category'}
```
```python
```
### Numerical Grouping
It is possible to group data based on numerical values as well. In our dataset number of bedrooms in the listed properties is present under the field **propertyDetails.bedrooms**. We can use that for aggregation as shown below:
```python Python (SDK)
#In general, the group-by field is structured as
#{"name": ALIAS, "field": FIELD, "agg": TYPE-OF-GROUP}

bedrooms_group = {"name": 'bedrooms',
 "field": 'propertyDetails.bedrooms',
 "agg": 'numeric'}
```
```python
```

-> ## Putting it together
Multiple different fields can be combined together to identify specific groups. In particular, this example groups by different locations and the number of bedrooms. Note that the code below includes `metrics` as well which are explained in details in the next page.
```python Python (SDK)
#Initialize Client
from relevanceai import Client
client = Client()

#Upload Data
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
from jsonshower import show_json
show_json(output, text_fields= list(output[0].keys()))
```
```python
```
