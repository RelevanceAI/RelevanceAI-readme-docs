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
* encoders-text-tfhub
* sentence-transformers

### encoders-text-tfhub
First, `vectorhub[encoders-text-tfhub]` must be installed. Restart the notebook when the installation is finished.

```bash Bash
# remove `!` if running the line in a terminal
!pip install vectorhub[encoders-text-tfhub]
```
```bash
```

Then we import Universal Sentence Encoder (USE) and instantiate an encoder object.

```python Python (SDK)
from vectorhub.encoders.text.tfhub import USE2Vec

model = USE2Vec()
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
documents = SAMPLE_DOCUMENTS

# Encode the `"sentence"` field in a list of documents
encoded_documents = model.encode_documents(["sentence"], documents)
```
```python
```


### sentence-transformers
First, `vectorhub[sentence-transformers]` must be installed. Restart the notebook when the installation is finished.

```bash Bash
# remove `!` if running the line in a terminal
!pip install vectorhub[sentence-transformers]
```
```bash
```

Then we import SentenceTransformers and instantiate an encoder object.

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
documents = SAMPLE_DOCUMENTS

# Encode the `"sentence"` field in a list of documents
encoded_documents = model.encode_documents(["sentence"], documents)
```
```python
```


### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `df.apply`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encodes the `product_description` field using the `USE2Vec` encoder.
You can see the list of the available list of models for vectorising here using [Vectorhub](https://github.com/RelevanceAI/vectorhub) or feel free to bring your own model(s).

```python Python (SDK)
import pandas as pd
from relevanceai.datasets import get_ecommerce_dataset_clean

# Retrieve our sample dataset. - This comes in the form of a list of documents.
documents = get_ecommerce_dataset_clean()

pd.DataFrame.from_dict(documents).head()

ds = client.Dataset('quickstart_example_encoding')
ds.insert_documents(documents)
```
```python
```

```python Python (SDK)
ds["product_title"].apply(lambda x: model.encode(x), output_field="product_title_vector_")
```
```python
```

