---
title: "Multiple filters"
slug: "multiple-filters"
hidden: false
createdAt: "2021-11-25T22:31:19.531Z"
updatedAt: "2022-01-19T05:17:17.089Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.1.1/docs_template/GENERAL_FEATURES/_assets/multiple-filters.png?raw=true" width="1009" alt="combined filters.png" />
<figcaption>Filtering results when using multiple filters: categories, contains, and date.</figcaption>
<figure>

## Combining filters
It is possible to combine multiple filters. For instance, the sample code below shows a filter that searches for
* a Lenovo flip cover
* produced after January 2020
* by either Lapguard or 4D brand.
A screenshot of the results can be seen on top.

```bash Bash
!pip install -U RelevanceAI[notebook]==1.1.1
```
```bash
```

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
DATASET_ID = "ecommerce-sample-dataset"
df = client.Dataset(DATASET_ID)
```
```python
```

@@@ filters_three_setup,
FIELD1=DESCRIPTION_FIELD, FILTER_TYPE1=CONTAINS_FILTER_TYPE, CONDITION1=EQ_COND, CONDITION_VAL1=CONDITION_VAL_5,
FIELD2=BRAND_FIELD, FILTER_TYPE2=CATEGORY_FILTER_TYPE, CONDITION2=EQ_COND, CONDITION_VAL2=BRAND_CATEGORY_VAL2
FIELD3=INSERT_DATE_FIELD, FILTER_TYPE3=DATE_FILTER_TYPE, CONDITION3=GE_COND, CONDITION_VAL3=DATE_VAL_2 @@@

```python Python (SDK)
### TODO: update to match the latest SDK
filtered_data = df.get_where(filter)
```
```python
```


