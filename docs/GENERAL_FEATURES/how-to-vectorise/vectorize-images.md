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

First, `vectorhub[clip]` must be installed.
Notes: you might also run `!pip install "opencv-python-headless<4.3"`, restart your notebook when installation finishes.

```bash Bash
!pip install -U vectorhub[clip]
```
```bash
```

Encoding a single image input via the `encode` function and encoding a specified image field in the whole data (i.e. list of dictionaries) via the `encode_documents` function are shown below. Note that images are accessed via their URL in the web.

```python Python (SDK)
from vectorhub.bi_encoders.text_image.torch import Clip2Vec

model = Clip2Vec()
model.encode = model.encode_image

"""
If you have a fine-tuned model, place the **filepath** into the model as shown below:
"""

model = Clip2Vec("<FINETUNED_MODEL_PATH>")
```
```python
```

```python Python (SDK)
# documents are saved as a list of dictionaries
documents=[{'image_url': 'https://relevance.ai/wp-content/uploads/2021/10/statue-illustration.png'}, {'image_url': 'https://relevance.ai/wp-content/uploads/2021/09/Group-193-1.png'}]

# Encode the images accessible from the URL saved in `image_url` field in a list of documents
docs_with_vecs = model.encode_documents(["image_url"], documents)
```
```python
```


### Encoding an entire dataset using `df.apply()`

The easiest way to update an existing dataset with encoding results is to run `df.apply`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset` and encode the `product_image` field using the `clip` encoder.

```python Python (SDK)
df["sentence"].apply(lambda x: model.encode(x), output_field="sentence_vector")
```
```python
```


