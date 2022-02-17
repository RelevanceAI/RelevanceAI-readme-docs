---
title: "Regex"
slug: "regex"
hidden: false
createdAt: "2021-11-29T23:13:52.305Z"
updatedAt: "2022-01-19T05:16:17.784Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.1.3-fixes/docs_template/GENERAL_FEATURES/_assets/regex.png?raw=true" width="2048" alt="7cbd106-contains.png" />
<figcaption>Filtering documents containing "Durian (\w+)" in description using filter_type `regexp`.</figcaption>
<figure>

## `regex`
This filter returns a document only if it matches regexp (i.e. regular expression). Note that substrings are covered in this category. For instance, if a product name is composed of a name and a number (e.g. ABC-123), one might remember the name but not the number. This filter can easily return all products including the ABC string.

Relevance AI has the same regular expression schema as Apache Lucene's ElasticSearch to parse queries.

*Note that this filter is case-sensitive.*

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset_df, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filter_setup, FIELD=DESCRIPTION_FIELD, FILTER_TYPE=REGEX_FILTER_TYPE, CONDITION=EQ_COND, CONDITION_VAL=CONDITION_VAL_6 @@@

@@@ filter_dataset @@@

