---
title: "How to vectorize text using VectorHub - TFhub"
slug: "vectorize-text"
excerpt: "A guide on vectorizing text using Vectorhub"
hidden: false
createdAt: "2021-10-28T09:09:18.680Z"
updatedAt: "2022-01-20T04:15:52.154Z"
---
## Using VectorHub

[VectorHub](https://github.com/RelevanceAI/vectorhub) provides users with access to various state of the art encoders to vectorize different data types such as text or image. It manages the encoding process as well, allowing users to focus on the data they want to encode rather than the actual model behind the scene.
On this page, we introduce some of the text encoders:
* **encoders-text-tfhub**
* sentence-transformers

### encoders-text-tfhub
First, `vectorhub encoders-text-tfhub` must be installed. Restart the notebook when the installation is finished.
```shell Bash
pip install vectorhub[encoders-text-tfhub]
```
```shell
```
Then we import Universal Sentence Encoder (USE) and instantiate and encoder object.
```python Python (SDK)
from vectorhub.encoders.text.tfhub import USE2Vec

enc = USE2Vec()
```
```python
```
Encoding a single text input via the `encode` function and encoding a specified text field in the whole data (i.e. list of dictionaries) via the `encode_documents` function are shown below.
```python Python (SDK)
# Encode a single input
enc.encode("I love working with vectors.")

# documents are saved as a list of dictionaries
docs = [{"sentence":"This is the first sentence.",
 "_id":1},
 {"sentence":"This is the second sentence.",
 "_id":2}
 ]
# Encode the `sentence` field in a list of documents
docs_with_vectors = enc.encode_documents(['sentence'], docs)
```
```python
```
### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `pull_update_push`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encodes the `product_description` field using the `USE2Vec` encoder.
You can see the list of the available list of models for vectorising here using [Vectorhub](https://github.com/RelevanceAI/vectorhub) or feel free to bring your own model(s).
```python Python (SDK)
from vectorhub.encoders.text.tfhub import USE2Vec

enc = USE2Vec()

def encode_documents(documents):
 # Field and then the documents go here
 return enc.encode_documents(["product_description"], documents)

client.pull_update_push("ecommerce_dataset", encode_documents)
```
```python
```
