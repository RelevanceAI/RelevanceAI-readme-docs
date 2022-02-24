---
title: "Numeric"
slug: "numeric"
hidden: false
createdAt: "2021-11-25T06:28:37.534Z"
updatedAt: "2022-01-19T05:17:05.147Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.6/docs_template/GENERAL_FEATURES/_assets/numeric.png?raw=true" width="446" alt="Numeric.png" />
<figcaption>Filtering documents with retail price higher than 5000.</figcaption>
<figure>

## `numeric`
This filter is to perform the filtering operators on a numeric value. For instance, returning the documents with a price larger than 1000 dollars.

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset_df, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filter_setup, FIELD=RETAIL_PRICE_FIELD, FILTER_TYPE=NUMERIC_FILTER_TYPE, CONDITION=GT_COND, CONDITION_VAL=5000 @@@

@@@ filter_dataset @@@

