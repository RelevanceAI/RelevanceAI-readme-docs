---
title: "Date"
slug: "date"
hidden: false
createdAt: "2021-11-25T06:20:15.175Z"
updatedAt: "2022-01-19T05:16:58.720Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.5/docs_template/GENERAL_FEATURES/_assets/date.png?raw=true" width="600"  alt="date.png" />
<figcaption>Filtering documents which were added to the database after January 2021.</figcaption>
<figure>

## `date`
This filter performs date analysis and filters documents based on their date information. For instance, it is possible to filter out any documents with a production date before January 2021.

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset_df, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filter_setup, FIELD=INSERT_DATE_FIELD, FILTER_TYPE=DATE_FILTER_TYPE, CONDITION=EQ_COND, CONDITION_VAL=DATE_VAL_1 @@@

Note that the default format is "yyyy-mm-dd" but can be changed to "yyyy-dd-mm" through the `format` parameter as shown in the example below.

@@@ filter_setup_with_format, FIELD=INSERT_DATE_FIELD, FILTER_TYPE=DATE_FILTER_TYPE, CONDITION=EQ_COND, CONDITION_VAL=DATE_VAL_1 @@@

@@@ filter_dataset @@@
