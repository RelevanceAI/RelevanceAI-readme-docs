---
title: "Multiple filters"
slug: "multiple-filters"
hidden: false
createdAt: "2021-11-25T22:31:19.531Z"
updatedAt: "2022-01-19T05:17:17.089Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/cus-272-create-new-page-in-readme-if-page-slug/docs_template/GENERAL_FEATURES/_assets/multiple-filters.png?raw=true" width="1009" alt="combined filters.png" />
<figcaption>Filtering results when using multiple filters: categories, contains, and date.</figcaption>
<figure>

## Combining filters
It is possible to combine multiple filters. For instance, the sample code below shows a filter that searches for
* a Lenovo flip cover
* produced after January 2020
* by either Lapguard or 4D brand.
A screenshot of the results can be seen on top.

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset_df, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filters_three_setup, FIELD1=DESCRIPTION_FIELD, FILTER_TYPE1=CONTAINS_FILTER_TYPE, CONDITION1=EQ_COND, CONDITION_VAL1=CONDITION_VAL_5, FIELD2=BRAND_FIELD, FILTER_TYPE2=CATEGORY_FILTER_TYPE, CONDITION2=EQ_COND, CONDITION_VAL2=BRAND_CATEGORY_VAL2, FIELD3=INSERT_DATE_FIELD, FILTER_TYPE3=DATE_FILTER_TYPE, CONDITION3=GE_COND, CONDITION_VAL3=DATE_VAL_2 @@@

@@@ filter_dataset @@@

