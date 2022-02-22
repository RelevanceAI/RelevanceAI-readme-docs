---
title: "Combining filters and vector search"
slug: "combining-filters-and-vector-search"
hidden: false
createdAt: "2021-11-25T22:33:06.798Z"
updatedAt: "2022-01-19T05:12:49.766Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.1.3-fixes/docs_template/GENERAL_FEATURES/_assets/combine.png?raw=true" width="1014" alt="filter+vectors.png" />
<figcaption>Including filters in a vector search.</figcaption>
<figure>
## Including filters in vector search
Filtering provides you with a subset of a database containing data entities that match the certain criteria set as filters. What if we need to search through this subset? The difficult way is to ingest (save) the subset as a new dataset, then make the search on the new dataset. However, RelevanceAI has provided the filtering option in almost all search endpoints. This makes the whole process much faster and more straightforward.
In the code snippet below we show a hybrid search sample which is done on a subset of a huge database via filtering. In this scenario, the user is looking for white sneakers but only the ones produced after mid-2020 and from two brands Nike and Adidas.

Note that the code below needs
1. Relevance AI's Python SDK to be installed.
2. A dataset named `ecommerce-search-example`
3. Vectorized description saved under the name `descriptiontextmulti_vector_`

Please refer to a full guide on how to [create and upload a database](doc:creating-a-dataset) and how to use vectorizers to update a dataset with vectors at [How to vectorize](doc:vectorize-text).

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset_df, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ encode_text_query, QUERY="white sneakers", ENCODER="enc_imagetext" @@@

@@@ filters_setup, FIELD1="brand", FILTER_TYPE1="contains", CONDITION1="==", CONDITION_VAL1="Asian", FIELD2="insert_date_", FILTER_TYPE2="date", CONDITION2=">=", CONDITION_VAL2="2020-07-01" @@@

@@@ multivector_query, QUERY_VECTOR="query_vec_txt", VECTOR_FIELDS="descriptiontextmulti_vector_" @@@

@@@ vector_search_with_filter, PAGE_SIZE=5 @@@
