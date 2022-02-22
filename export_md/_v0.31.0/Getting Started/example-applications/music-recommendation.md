---
title: "Audio Recommendation"
slug: "music-recommendation"
hidden: true
createdAt: "2021-11-28T23:56:46.054Z"
updatedAt: "2022-01-14T06:56:46.836Z"
---
## Recommendations based on vector search
Vector Search based recommendation is done by employing vectors of specified **liked** and/or **disliked** existing documents. This allows us to not only do recommendations but also personalise the results.

In this section, we will show you how to create and experiment with a powerful `.wav` encoder and a vector search engine using Relevance AI.

**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1m5N1Ekh0KiMZdDESN5zYT-ugr1fwVlDW?usp=sharing)

### What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)

### Installation Requirements

Prior to starting, let's install the main dependencies. This installation provides you with what you need to connect to RelevanceAI API, read/write data, make different searches, etc. Also, the encoder needed to vectorize audio files.
```shell Python (SDK)
pip install -U -q RelevanceAI[notebook]
pip install vectorhub['encoders-audio-tfhub']
```
```shell
```
This will give you access to Relevance AI's Python SDK and the encoder required for vectorising `.wav` files.

### Setting Up Client

After installation, we need to also set up an API client. If you are missing an API key, you can easily sign up and get your API key from [https://cloud.relevance.ai/](https://cloud.relevance.ai/) in the settings area.
```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the appreared Auth token box below
"""

client = Client()
```
```python
```
### Loading the Encoder
The code snippet below loads an encoder object to vectorize `.wav` files.
```python Python (SDK)
from vectorhub.encoders.audio.tfhub import Trill2Vec

model = Trill2Vec()
```
```python
```
### Encoding

Here, we encode nearly 1000 audio files in a loop and save the vectors to be inserted into our database later.
* Note1: `_id` is an obligatory field, and the name of vector fields must end in `_vector_`.
* Note2: You can decrease the number of files to be encoded using the `last_n` variable. This speeds up the encoding process, at the same time there will be fewer documents in your database.
* Note3: The audio files we used in this document are voice samples of individual speakers. You can use the full-path parameter to download and play them.
```python Python (SDK)
from tqdm.auto import tqdm

docs = []
issues = []
last_n = 1001
main_path = 'https://vecsearch-bucket.s3.us-east-2.amazonaws.com/voices/'
for i in tqdm(range(2, last_n)):
 doc = {}
 doc['_id'] = i
 doc['full_path'] = main_path + f'common_voice_en_{doc["_id"]}.wav'
 doc['file_name'] = doc['full_path'].split('/')[-1]
 try:
 sample = model.read(doc['full_path'])
 doc['trill2vec_vector_'] = model.encode(sample)
 docs.append(doc)
 except:
 issues.append(i)

print("Could not encode files:", issues)
```
```python
```
### Bulk insert

The data is ready and using one line of code, we can upload it to Relevance AI platform.
```python Python (SDK)
dataset_id = "common_voice_en"

client.datasets.bulk_insert(dataset_id, docs)
```
```python
```
### Loading sample documents and use them as the base for recommendation
Here, we load the first two documents in our dataset. These two are later used as the base documents for the recommendation. Note that any document can be used as a positive reference (i.e. when looking for documents most similar to the reference) or a negative reference (when looking for recommendations least similar to the reference).
```python Python (SDK)
docs = client.datasets.documents.list(dataset_id,page_size=2)
docs['documents'][0]['file_name']
```
```python
```
### Recommendation

Using the vector recommendation endpoint as shown in the code snippet below, we get recommendations that are similar to the first and second loaded samples. Note that we used weighted similarities 0.8 and 0.2 respectively.
```python Python (SDK)
from relevanceai import show_json

vector_fields = ["trill2vec_vector_"]
recommendation_results = client.services.recommend.vector(
 dataset_id = dataset_id,
 vector_fields = vector_fields,
 page_size = 5,
 positive_document_ids = {docs['documents'][0]['_id']:0.8,
 docs['documents'][1]['_id']:0.2
 }

# Showing the results
show_json(
 recommendation_results['results'],
 text_fields=['full_path']
)
```
```python
```
Listening to the files that are recommended by the model, it is obvious they are voice samples of the same person who is the speaker of the first reference document.

## Code All-Together
```python Python (SDK)
! pip install vectorhub['encoders-audio-tfhub']
! pip install -U -q RelevanceAI[notebook]

from relevanceai import Client
from vectorhub.encoders.audio.tfhub import Trill2Vec
from relevanceai import show_json
from tqdm.auto import tqdm

# encoder for audio files
model = Trill2Vec()

# preparing the database with vectors
docs = []
issues = []
main_path = 'https://vecsearch-bucket.s3.us-east-2.amazonaws.com/voices/'
for i in tqdm(range(2, 1001)):
 doc = {}
 doc['_id'] = i
 doc['full_path'] = main_path + f'common_voice_en_{doc["_id"]}.wav'
 doc['file_name'] = doc['full_path'].split('/')[-1]
 try:
 sample = model.read(doc['full_path'])
 doc['trill2vec_vector_'] = model.encode(sample)
 docs.append(doc)
 except:
 issues.append(i)

print("Could not encode files:", issues)

# setting up the client

#"You can sign up/login and find your credentials here: https://development.qualitative-cloud.pages.dev/login"
#"Once you have signed up, click on the value under `Authorization token` and paste it here"
client = Client()

# creating the database and inserting the data
dataset_id = "common_voice_en"
client.datasets.bulk_insert(dataset_id, docs)

# getting to sample documents to be used as positive cases for recommendation
docs = client.datasets.documents.list(dataset_id,page_size=2)
docs['documents'][0]['file_name']

# weighted recommendation
vector_fields = ["trill2vec_vector_"]
recommendation_results = client.services.recommend.vector(
 dataset_id = dataset_id,
 vector_fields = vector_fields,
 page_size = 5,
 positive_document_ids = {
 docs['documents'][0]['_id']:0.8,
 docs['documents'][1]['_id']:0.2
		}

# Showing the results
show_json(
 recommendation_results['results'],
 text_fields=['full_path']
)
```
```python
```
## Final Note

As noted above, the audio files we used in this document are voice samples of individual speakers. The corresponding vectors contain information that enables our search and recommendation model to find similar audio files (i.e. the same or very similar voices in the current guide). However, this can be expanded to more complicated audio files.
