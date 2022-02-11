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

