---
title: "Ids"
slug: "ids"
hidden: false
createdAt: "2021-11-25T22:22:07.285Z"
updatedAt: "2022-01-19T05:17:10.638Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/2.0.0
/docs_template/general-features/_assets/id.png?raw=true" width="612" alt="id.png" />
<figcaption>Filtering documents based on their id.</figcaption>
<figure>

## `ids`
This filter returns documents whose unique id exists in a given list. It may look similar to 'categories'. The main difference is the search speed.

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset_df, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filter_setup, FIELD=ID_FIELD, FILTER_TYPE=IDS_FILTER_TYPE, CONDITION=EQ_COND, CONDITION_VAL=CONDITION_VAL_4 @@@

@@@ filter_dataset @@@
