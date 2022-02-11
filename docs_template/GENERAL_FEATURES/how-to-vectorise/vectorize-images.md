---
title: "How to vectorize images"
slug: "vectorize-images"
excerpt: "A guide to vectorizing/encoding images using Vectorhub"
hidden: false
createdAt: "2021-10-28T09:07:53.720Z"
updatedAt: "2022-01-20T04:45:02.324Z"
---
## Using VectorHub

[VectorHub](https://github.com/RelevanceAI/vectorhub) provides users with access to various state of the art encoders to vectorize different data types such as text or image. It manages the encoding process as well, allowing users to focus on the data they want to encode rather than the actual model behind the scene.
On this page, we introduce the CLIP image encoder.

First, `vectorhub clip` must be installed.
Notes: you might also run `!pip install "opencv-python-headless<4.3"`, restart your notebook when installation finishes.

@@@ vectorhub_clip_installation @@@

Encoding a single image input via the `encode` function and encoding a specified image field in the whole data (i.e. list of dictionaries) via the `encode_documents` function are shown below. Note that images are accessed via their URL in the web.

@@@ clip_enc_image @@@

@@@ clip_enc_img_docs, IMG_DOCS=SAMPLE_IMG_DOCS, FIELD=IMG_URL_FIELD @@@


### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `pull_update_push`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset` and encode the `product_image` field using the `clip` encoder.
@@@ encode_fields_in_documents_func, FIELD=PRODUCT_IMGG_FIELD @@@

@@@ pull_update_push, DATASET_ID=ECOMMERCE_DATASET_ID, FUNCTION=ENCODE_DOCUMENTS_FUNC @@@
