---
title: "Documents with chunked data"
slug: "documents-with-chunked-data"
excerpt: "Guide to insert documents that contain chunk data"
hidden: true
createdAt: "2021-11-05T04:52:42.745Z"
updatedAt: "2022-01-14T01:35:17.721Z"
---
## What is chunked data
Chunking refers to breaking a large piece of text into its smaller components. For example, breaking one large paragraph of 10 sentences into a list of 10 sentences. This is specifically beneficial in a more fine-grained search as the data has been broken down into smaller pieces. Also, it can help with more precise vectorizing since some models are very sensitive to the input length.

## Preparing a dataset to upload
As it was explained in the page [preparing data for upload from CSV / Pandas Dataframe](doc:preparing-data-from-csv-pandas-df), to upload a dataset to Relevance AI platform, it must be in the form of a list of dictionaries (json). For instance
```python Python (SDK)
data_list = [
 {
 '_id':1,
 'description':"This is the first sample. This sample is used to show chunking."
 },
 {
 '_id':2,
 'description':"This is the second sample."
 }
]
```
```python
```
Note that each entry must have a field called `_id`.

## Fetching an existing database
You can fetch an existing database via the `list` endpoint. If there are more than 10000 entries in the database or when you want to break the task into smaller batches, you can use the `cursor` parameter as shown in the code snippet below. The cursor is a pointer to the last read index.
```python Python (SDK)
from relevanceai import Client

project = <PROJECT-NAME> # Project name
api_key = <API-KEY> # api-key
dataset_id = <dataset_id> # dataset-id

client = Client(project, api_key)

# list data
# You can download up to 10,000 documents in one go.
# For more, you need to use the cursor functionality.
data = client.datasets.documents.list(dataset_id, page_size = 2000)

cursor = data['cursor'] # get the cursor value

# loop through the database using cursor
while data:
 data = client.datasets.documents.list(dataset_id, cursor = cursor)
```
```python
```

## Insert with chunking
## Chunking to sentences
A complete overview of the `bulk_insert` endpoint to upload data with or without vectorizing was explained on [inserting data](doc:inserting-data). Here, we introduce `field_transformers` that is the argument used for chunking. It is a list of dictionaries with parameters as shown in the below example. This setting triggers a sentence-splitter that in our example breaks the `description` field into its sentence and saves them under a new field called `description_chunk_`. **Note that the output field name must end in `_chunk_`** (e.g `description_chunk_`).
```python
field_transformers=[{
 "field": "description",
 "output_field": "description_chunk_",
 "split_sentences": True
}]
```
```python
```
This is what happens to the sample data we had above.
```python Python (SDK)
data_list = [
 {
 '_id':1,
 'description':"This is the first sample. This sample is used to show chunking.",
 'description_chunk_':{
 'description':
 [
 "This is the first sample.",
 "This sample is used to show chunking."
 ]
 }
 },
 {
 '_id':2,
 'description':"This is the second sample.",
 'description_chunk_':{
 'description':["This is the second sample."]
 }
 }
]
```
```python
```
## Vectorizing each Chunk
We talked about how to trigger the vectorizing task when calling the `bulk_insert` endpoint on [inserting data](doc:inserting-data). Triggering the vectorizer for chunked data is the same. The only difference is that we need to use `chunk_field` to refer to the field we want to vectorize.
```python
jobs_to_trigger=[{
 "encode": {
 "chunk_field": 'description_chunk_',
 "fields": ["description"],
 "model_name": 'content-kc',
 "alias":"text2vec"
 }}]
```
```python
```
This is a schematic view of what happens to the sample data we had above.
```python Python (SDK)
data_list = [
 {
 '_id':1,
 'description':"This is the first sample. This sample is used to show chunking.",
 'description_chunk_':{
 'description':
 [
 "This is the first sample.",
 "This sample is used to show chunking."
 ],
 'description_txt2vec_chunkvector_':
 [
 [1,2,3,...],
 [4,5,3,...],
 ]
 }
 },
 {
 '_id':2,
 'description':"This is the second sample.",
 'description_chunk_':{
 'description':["This is the second sample."],
 'description_txt2vec_chunkvector_':
 [
 [1,2,3,...]
 ]
 }
 }
]
```
```python
```
Side Notes:
1. If you wish to chunk your data in a different way (e.g. lines, sentences), you can generate your data dictionary following the structure shown in the above-mentioned examples and upload the data without triggering the sentence splitter.
2. If you wish to encode your data using a different model, you can vectorize the data separately and generate your data dictionary including the vectors following the structure shown in the above-mentioned examples, then upload the data without triggering the sentence splitter or vectorizer. Note that the chunk vector field names must end in `_chunkvector_` (e.g. `description_txt2vec_chunkvector_`)

Full sample code to update an existing database with chunked data through the provided sentence splitter and vectorizer is shown below.
```python Python (requests)
import requests

databae_id = <databae_id>

document_endpoint = f"datasets/{databae_id}/documents/list"
docs = requests.get(url + document_endpoint,
 headers = {"Authorization": credentials},
 params = {"page_size": 200}).json()

cursor = docs['cursor']
bulk_insert = f"https://ingest-api-aueast.relevance.ai/latest/datasets/{databae_id}/documents/bulk_insert"

while len(docs['documents']) > 0:
 jobs_to_trigger:[{
 "encode": {
 "chunk_field": 'description_chunk_',
 "fields": ["description"],
 "model_name": 'content-kc',
 "alias":"text2vec"
 }}]
 field_transformers:[{
 "field": "description",
 "output_field": "description_chunk_",
 "split_sentences": True
 }]

 requests.post(bulk_insert,
 headers = {"Authorization": credentials},
 json = {"documents": docs['documents'],
 "field_transformers": field_transformers,
 "jobs_to_trigger": jobs_to_trigger
 })

 docs = requests.get(url + document_endpoint,
 headers = {"Authorization": credentials},
 params = {"cursor":cursor}).json()
```
```python
```
