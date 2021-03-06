---
title: "Contains"
slug: "contains"
hidden: false
createdAt: "2021-11-25T05:18:31.045Z"
updatedAt: "2022-01-19T05:16:24.396Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/general-features/_assets/contains.png?raw=true" width="2048" alt="contains.png" />
<figcaption>Filtering documents containing "Durian BID" in description using filter_type `contains`.</figcaption>
<figure>


## `contains`

This filter returns a document only if it contains a string value. Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.
*Note that this filter is case-sensitive.*

@@@ relevanceai_installation , RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filter_setup, FIELD=DESCRIPTION_FIELD, FILTER_TYPE=CONTAINS_FILTER_TYPE, CONDITION=EQ_COND, CONDITION_VAL=CONDITION_VAL_3 @@@

@@@ filter_dataset @@@

