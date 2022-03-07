---
title: "How to vectorize text using VectorHub - Transformers"
slug: "how-to-vectorize-text-using-vectorhub-transformers"
excerpt: "A guide on vectorizing text using Vectorhub"
hidden: false
createdAt: "2022-01-20T01:23:22.178Z"
updatedAt: "2022-01-24T00:15:14.549Z"
---
## Using VectorHub

[VectorHub](https://github.com/RelevanceAI/vectorhub) provides users with access to various state of the art encoders to vectorize different data types such as text or image. It manages the encoding process as well, allowing users to focus on the data they want to encode rather than the actual model behind the scene.
On this page, we introduce sentence-transformer based text encoders.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.0/docs/GENERAL_FEATURES/how-to-vectorizet/_notebooks/how-to-vectorize.ipynb)
### sentence-transformers
First, `sentence-transformers` must be installed. Restart the notebook when the installation is finished.

```bash Bash
# remove `!` if running the line in a terminal
!pip install vectorhub[sentence-transformers]
```
```bash
```

Then from the `sentence_transformers` category, we import our desired transformer and specific model; the full list can be accessed [here](https://huggingface.co/sentence-transformers).

```python Python (SDK)
from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec

model = SentenceTransformer2Vec("all-mpnet-base-v2")
```
```python
```

Encoding a single text input via the `encode` function and encoding a specified text field in the whole data (i.e. list of dictionaries) via the `encode_documents` function are shown below.

```python Python (SDK)
# Encode a single input
model.encode("I love working with vectors.")
```
```python
```

```python Python (SDK)
# documents are saved as a list of dictionaries
documents = [{'sentence': '"This is the first sentence."', '_id': 1}, {'sentence': '"This is the second sentence."', '_id': 2}]

# Encode the `"sentence"` field in a list of documents
encoded_documents = model.encode_documents(["sentence"], documents)

df.upsert_documents(documents=encoded_documents)
```
```python
```

### Encoding an entire dataset using df.apply()

The easiest way to update an existing dataset with encoding results is to run `df.apply`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encode the `product_description` field using the `SentenceTransformer2Vec` encoder.

```python Python (SDK)
df["sentence"].apply(lambda x: model.encode(x), output_field="sentence_vector")
```
```python
```
### Some famous models

#### Encoding using native Transformers


* BERT
Below, we show an example of how to get vectors from the popular [**BERT**](https://huggingface.co/transformers/v3.0.2/model_doc/bert.html) model from HuggingFace Transformers library.

```python Python (SDK)
import torch
from transformers import AutoTokenizer, AutoModel

model_name = "bert-base-uncased"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def vectorize(text):
 return (
 torch.mean(model(**tokenizer(text, return_tensors="pt"))[0], axis=1)
 .detach()
 .tolist()[0]
 )
```
```python
```

#### Encoding using Vectorhub's Sentence Transformers

Vectorhub helps us to more easily work with models to encode fields in our documents of different modal types.


* CLIP
Below, we show an example of how to get vectors from the popular [**CLIP**](https://huggingface.co/sentence-transformers/clip-ViT-B-32) model from HuggingFace Transformers library.

```python Python (SDK)
from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec

model = SentenceTransformer2Vec('clip-ViT-B-32')
image_vector = model.encode("I love working with vectors.")
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
