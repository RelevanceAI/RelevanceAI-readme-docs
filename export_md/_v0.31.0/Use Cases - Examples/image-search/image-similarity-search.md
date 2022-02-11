---
title: "Image Similarity Search"
slug: "image-similarity-search"
hidden: true
createdAt: "2021-10-28T08:55:01.732Z"
updatedAt: "2021-12-11T14:24:57.292Z"
---
TODO:
[ ] Complete commentary and examples
[ ] Show exploration
[ ] Add notebook

```python Python (VecDB SDK)
!pip install -U -q relevanceai[notebook] vectorhub[encoders-image-tfhub]

## Setting up
from relevanceai import Client
from relevanceai.datasets import get_ecommerce_dataset
from vectorhub.encoders.image.tfhub import BitMedium2Vec
bit = BitMedium2Vec()

project = <API-USERNAME> # Project name
api_key = <API-KEY> # API Key
dataset_id = 'ecommerce-demo'

client = Client(project, api_key)

## 1. Prepare your data
docs = get_ecommerce_dataset(number_of_documents=1000)

## 2. Encode or vectorise your data with VectorHub
encoded_data = bit.encode_documents(["product_image"], data)

## 3. Index and upload your data to VecDB
for d in encoded_data:
 d['_id'] = str(d['_unit_id'])
client.insert_documents(dataset_id = dataset_id,
 docs = encoded_data,
 max_workers = None ## Setting max_workers to None will use all available cores
 )

## 4. Perform vector search on your data with RelevanceAI
query = 'Playstation 4'
results = client.services.search.vector(
 dataset_id,
 [{
 "vector": bit.encode(query),
 "fields": [
 "product_image_bit_vector_",
 ]
 }])

## TODO: Display similar images

r = [res for res in results['product_description']]
```
```python
```
