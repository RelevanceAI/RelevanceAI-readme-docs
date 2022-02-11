---
title: "Text To Image Search"
slug: "text-to-image-search"
hidden: true
createdAt: "2021-10-28T09:03:03.102Z"
updatedAt: "2021-11-02T00:38:50.718Z"
---
TODO:
[ ] Complete commentary and examples
[ ] Show exploration
[ ] Add notebook


```python Python (VecDB SDK)
!pip install -U -q vecdb vectorhub[clip]

## Setting up
from vecdb import VecDBClient
from vecdb.datasets import get_ecommerce_dataset
from vectorhub.bi_encoders.text_image.torch import Clip2Vec
clip = Clip2Vec()

project = <API-USERNAME> # Project name
api_key = <API-KEY> # API Key
dataset_id = 'ecommerce-demo'

client = VecDBClient(project, api_key)

## 1. Prepare your data
docs = get_ecommerce_dataset(number_of_documents=1000)

## 2. Encode or vectorise your data with VectorHub
encoded_data = clip.encode_documents([
 									"product_title",
 									"product_description",
 									"product_image"],
 								data)

## 3. Index and upload your data to VecDB
for d in encoded_data:
 d['_id'] = str(d['_unit_id'])
client.insert_documents(dataset_id = dataset_id,
 docs = encoded_data,
 max_workers = None ## Setting max_workers to None will use all available cores
 )

## 4. Perform text to image search on your data with VecDB
query = 'Playstation 4'
results = client.services.search.vector(
 dataset_id,
 [{
 "vector": clip.encode_text(query),
 "fields": [
 "product_image_clip_vector_",
 ]
 }])

## TODO: Display images

```
```python
```
