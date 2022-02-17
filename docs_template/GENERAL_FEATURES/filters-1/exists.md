---
title: "Exists"
slug: "exists"
hidden: false
createdAt: "2021-11-25T06:09:19.375Z"
updatedAt: "2022-01-19T05:16:52.455Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/1.1.5/docs_template/GENERAL_FEATURES/_assets/exists.png?raw=true" width="500" alt="exist.png" />
<figcaption>Filtering documents which include the field "brand" in their information.</figcaption>
<figure>

## `exists`
This filter returns entries in a database if a certain field (as opposed to the field values in previously mentioned filter types) exists or doesn't exist in them. For instance, filtering out documents in which there is no field 'purchase-info'. *Note that this filter is case-sensitive.*

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset_df, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filter_setup, FIELD=BRAND_FIELD, FILTER_TYPE=EXISTS_FILTER_TYPE, CONDITION=EQ_COND, CONDITION_VAL=NO_CONDITION_VAL @@@

@@@ filter_dataset @@@

