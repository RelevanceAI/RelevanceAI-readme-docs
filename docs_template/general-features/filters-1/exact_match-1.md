---
title: "Word match"
slug: "exact_match-1"
hidden: false
createdAt: "2021-11-25T05:44:25.366Z"
updatedAt: "2022-01-19T05:16:37.437Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/heads/v2.0.0/docs_template/general-features/_assets/word-match.png?raw=true" width="1974" alt="wordmatch.png" />
<figcaption>Filtering documents matching "Home curtain" in the description field.</figcaption>
<figure>

## `word_match`
This filter has similarities to both `exact_match` and `contains`. It returns a document only if it contains a **word** value matching the filter; meaning substrings are covered in this category but as long as they can be extracted with common word separators like the white-space (blank). For instance, the filter value "Home Gallery",  can lead to extraction of a document with "Buy Home Fashion Gallery Polyester ..." in the description field as both words are explicitly seen in the text. *Note that this filter is case-sensitive.*

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@

@@@ dataset, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

@@@ filter_setup, FIELD=DESCRIPTION_FIELD, FILTER_TYPE=WORD_MATCH_FILTER_TYPE, CONDITION=EQ_COND, CONDITION_VAL=CONDITION_VAL_1 @@@

@@@ filter_dataset @@@
