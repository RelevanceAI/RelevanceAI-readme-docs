---
title: "How to vectorize text using VectorHub-Transformers"
slug: "how-to-vectorize-text-using-vectorhub-transformers"
excerpt: "A guide on vectorizing text using Vectorhub"
hidden: false
createdAt: "2022-01-20T01:23:22.178Z"
updatedAt: "2022-01-24T00:15:14.549Z"
---
## Using VectorHub

[VectorHub](https://github.com/RelevanceAI/vectorhub) provides users with access to various state of the art encoders to vectorize different data types such as text or image. It manages the encoding process as well, allowing users to focus on the data they want to encode rather than the actual model behind the scene.
On this page, we introduce sentence-transformer based text encoders.

### sentence-transformers
First, `sentence-transformers` must be installed. Restart the notebook when the installation is finished.

@@@ vectorhub_encoders_sentence_transformers @@@

Then from the `sentence_transformers` category, we import our desired transformer and specific model; the full list can be accessed [here](https://huggingface.co/sentence-transformers).

@@@ transformer_enc @@@

Encoding a single text input via the `encode` function and encoding a specified text field in the whole data (i.e. list of dictionaries) via the `encode_documents` function are shown below.

@@@ encode_a_sample, SAMPLE=ENCODING_SAMPLE @@@

@@@ encode_documents, DOCS=SAMPLE_DOCS, FIELD=ENCODE_FIELD @@@

### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `pull_update_push`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encode the `product_description` field using the `SentenceTransformer2Vec` encoder.

@@@ encode_fields_in_documents_func, FIELD=PRODUCT_DESCRIPTION_FIELD @@@

@@@ pull_update_push, DATASET_ID=ECOMMERCE_DATASET_ID, FUNCTION=ENCODE_DOCUMENTS_FUNC @@@

### Some famous models
* BERT
Below, we show an example of how to get vectors from the popular [**BERT**](https://huggingface.co/transformers/v3.0.2/model_doc/bert.html) model from HuggingFace Transformers library.

@@@ bert_full_snippet @@@

* CLIP
Below, we show an example of how to get vectors from the popular [**CLIP**](https://huggingface.co/sentence-transformers/clip-ViT-B-32) model from HuggingFace Transformers library.

@@@ clip_encode_a_text_snippet, SAMPLE=ENCODING_SAMPLE @@@
