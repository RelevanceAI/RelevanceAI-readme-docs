---
title: "Exact match"
slug: "exact_match"
hidden: false
createdAt: "2021-11-25T05:20:53.996Z"
updatedAt: "2022-01-19T05:16:30.996Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs_template/GENERAL_FEATURES/_assets/exact-match.png?raw=true" width="2062" alt="Exact match.png" />
<figcaption>Filtering documents with "Durian Leather 2 Seater Sofa" as the product_name.</figcaption>
<figure>

## `exact_match`
This filter works with string values and only returns documents with a field value that exactly matches the filtered criteria. For instance under filtering by 'Samsung galaxy s21', the result will only contain products explicitly having 'Samsung galaxy s21' in their specified field. *Note that this filter is case-sensitive.*

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset_df, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filter_setup, FIELD=PRODUCT_NAME_FIELD, FILTER_TYPE=EXACT_MATCH_FILTER_TYPE, CONDITION=EQ_COND, CONDITION_VAL=CONDITION_VAL_2 @@@

@@@ filter_dataset @@@


