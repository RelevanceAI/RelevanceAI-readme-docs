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
```shell Bash
pip install vectorhub[sentence-transformers]
```
```shell
```
Then from the `sentence_transformers` category, we import our desired transformer and specific model; the full list can be accessed [here](https://huggingface.co/sentence-transformers).

```python Python (SDK)
from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec

enc = SentenceTransformer2Vec("all-mpnet-base-v2 ")
```
```python
```
Encoding a single text input via the `encode` function and encoding a specified text field in the whole data (i.e. list of dictionaries) via the `encode_documents` function are shown below.
```python Python (SDK)
# Encode a single input
enc.encode("I love working with vectors.")

# documents are saved as a list of dictionaries
docs = [
 {
 "sentence":"This is the first sentence.",
 "_id":1
 },
 {
 "sentence":"This is the second sentence.",
 "_id":2
 }

]
# Encode the `sentence` field in a list of documents
docs_with_vectors = enc.encode_documents(['sentence'], docs)
```
```python
```
### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `pull_update_push`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encode the `product_description` field using the `SentenceTransformer2Vec` encoder.
```python Python (SDK)
from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec

enc = SentenceTransformer2Vec("all-mpnet-base-v2 ")

def encode_documents(documents):
 # Field and then the documents go here
 return enc.encode_documents(["product_description"], documents)

client.pull_update_push("ecommerce_dataset", encode_documents)
```
```python
```
### Some famous models
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
* CLIP
Below, we show an example of how to get vectors from the popular [**CLIP**](https://huggingface.co/sentence-transformers/clip-ViT-B-32) model from HuggingFace Transformers library.
```python Python (SDK)
from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec

enc = SentenceTransformer2Vec('clip-ViT-B-32')
vec = enc.encode("I love working with vectors.")

```
```python
```
