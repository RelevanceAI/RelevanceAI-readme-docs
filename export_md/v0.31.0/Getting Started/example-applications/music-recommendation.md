---
title: "Audio Recommendation"
slug: "music-recommendation"
hidden: true
createdAt: "2021-11-28T23:56:46.054Z"
updatedAt: "2022-01-14T06:56:46.836Z"
---
[block:api-header]
{
  "title": "Recommendations based on vector search"
}
[/block]
Vector Search based recommendation is done by employing vectors of specified **liked** and/or **disliked** existing documents. This allows us to not only do recommendations but also personalise the results.

In this section, we will show you how to create and experiment with a powerful `.wav` encoder and a vector search engine using Relevance AI.

**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1m5N1Ekh0KiMZdDESN5zYT-ugr1fwVlDW?usp=sharing)

### What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)

### Installation Requirements

Prior to starting, let's install the main dependencies. This installation provides you with what you need to connect to RelevanceAI API, read/write data, make different searches, etc. Also, the encoder needed to vectorize audio files.
[block:code]
{
  "codes": [
    {
      "code": "pip install -U -q RelevanceAI[notebook]\npip install vectorhub['encoders-audio-tfhub']",
      "language": "shell"
    }
  ]
}
[/block]
This will give you access to Relevance AI's Python SDK and the encoder required for vectorising `.wav` files.

### Setting Up Client

After installation, we need to also set up an API client. If you are missing an API key, you can easily sign up and get your API key from [https://cloud.relevance.ai/](https://cloud.relevance.ai/) in the settings area.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \n\n\"\"\"\nRunning this cell will provide you with \nthe link to sign up/login page where you can find your credentials.\nOnce you have signed up, click on the value under `Authorization token` \nin the API tab\nand paste it in the appreared Auth token box below\n\"\"\"\n\nclient = Client()",
      "language": "python"
    }
  ]
}
[/block]
### Loading the Encoder
The code snippet below loads an encoder object to vectorize `.wav` files.
[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.audio.tfhub import Trill2Vec\n\nmodel = Trill2Vec()",
      "language": "python"
    }
  ]
}
[/block]
### Encoding

Here, we encode nearly 1000 audio files in a loop and save the vectors to be inserted into our database later.
* Note1: `_id` is an obligatory field, and the name of vector fields must end in `_vector_`.
* Note2: You can decrease the number of files to be encoded using the `last_n` variable. This speeds up the encoding process, at the same time there will be fewer documents in your database.
* Note3: The audio files we used in this document are voice samples of individual speakers. You can use the full-path parameter to download and play them.
[block:code]
{
  "codes": [
    {
      "code": "from tqdm.auto import tqdm\n\ndocs = []\nissues = []\nlast_n = 1001\nmain_path = 'https://vecsearch-bucket.s3.us-east-2.amazonaws.com/voices/'\nfor i in tqdm(range(2, last_n)):\n  doc = {}\n  doc['_id'] = i\n  doc['full_path'] = main_path + f'common_voice_en_{doc[\"_id\"]}.wav'\n  doc['file_name'] =  doc['full_path'].split('/')[-1]\n  try:\n    sample = model.read(doc['full_path'])\n    doc['trill2vec_vector_'] = model.encode(sample)\n    docs.append(doc)\n  except:\n    issues.append(i)\n    \nprint(\"Could not encode files:\", issues)",
      "language": "python"
    }
  ]
}
[/block]
### Bulk insert

The data is ready and using one line of code, we can upload it to Relevance AI platform.
[block:code]
{
  "codes": [
    {
      "code": "dataset_id = \"common_voice_en\"\n\nclient.datasets.bulk_insert(dataset_id, docs)",
      "language": "python"
    }
  ]
}
[/block]
### Loading sample documents and use them as the base for recommendation
Here, we load the first two documents in our dataset. These two are later used as the base documents for the recommendation. Note that any document can be used as a positive reference (i.e. when looking for documents most similar to the reference) or a negative reference (when looking for recommendations least similar to the reference).
[block:code]
{
  "codes": [
    {
      "code": "docs = client.datasets.documents.list(dataset_id,page_size=2)\ndocs['documents'][0]['file_name']",
      "language": "python"
    }
  ]
}
[/block]
### Recommendation

Using the vector recommendation endpoint as shown in the code snippet below, we get recommendations that are similar to the first and second loaded samples. Note that we used weighted similarities 0.8 and 0.2 respectively.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import show_json\n\nvector_fields = [\"trill2vec_vector_\"]\nrecommendation_results = client.services.recommend.vector(\n    dataset_id = dataset_id,\n    vector_fields = vector_fields,\n    page_size = 5, \n    positive_document_ids = {docs['documents'][0]['_id']:0.8,\n                             docs['documents'][1]['_id']:0.2\n                            }\n\n# Showing the results\nshow_json(\n    recommendation_results['results'],\n    text_fields=['full_path']\n)",
      "language": "python"
    }
  ]
}
[/block]
Listening to the files that are recommended by the model, it is obvious they are voice samples of the same person who is the speaker of the first reference document.

## Code All-Together
[block:code]
{
  "codes": [
    {
      "code": "! pip install vectorhub['encoders-audio-tfhub']\n! pip install -U -q RelevanceAI[notebook]\n\nfrom relevanceai import Client\nfrom vectorhub.encoders.audio.tfhub import Trill2Vec\nfrom relevanceai import show_json\nfrom tqdm.auto import tqdm\n\n# encoder for audio files\nmodel = Trill2Vec()\n\n# preparing the database with vectors\ndocs = []\nissues = []\nmain_path = 'https://vecsearch-bucket.s3.us-east-2.amazonaws.com/voices/'\nfor i in tqdm(range(2, 1001)):\n  doc = {}\n  doc['_id'] = i\n  doc['full_path'] = main_path + f'common_voice_en_{doc[\"_id\"]}.wav'\n  doc['file_name'] =  doc['full_path'].split('/')[-1]\n  try:\n    sample = model.read(doc['full_path'])\n    doc['trill2vec_vector_'] = model.encode(sample)\n    docs.append(doc)\n  except:\n    issues.append(i)\n    \nprint(\"Could not encode files:\", issues)\n\n# setting up the client\n\n#\"You can sign up/login and find your credentials here: https://development.qualitative-cloud.pages.dev/login\"\n#\"Once you have signed up, click on the value under `Authorization token` and paste it here\"\nclient = Client()\n\n# creating the database and inserting the data\ndataset_id = \"common_voice_en\"\nclient.datasets.bulk_insert(dataset_id, docs)\n\n# getting to sample documents to be used as positive cases for recommendation\ndocs = client.datasets.documents.list(dataset_id,page_size=2)\ndocs['documents'][0]['file_name']\n\n# weighted recommendation\nvector_fields = [\"trill2vec_vector_\"]\nrecommendation_results = client.services.recommend.vector(\n    dataset_id = dataset_id,\n    vector_fields = vector_fields,\n    page_size = 5, \n    positive_document_ids = {\n      docs['documents'][0]['_id']:0.8,\n      docs['documents'][1]['_id']:0.2\n\t\t}\n  \n# Showing the results\nshow_json(\n    recommendation_results['results'],\n    text_fields=['full_path']\n)",
      "language": "python"
    }
  ]
}
[/block]
## Final Note

As noted above, the audio files we used in this document are voice samples of individual speakers. The corresponding vectors contain information that enables our search and recommendation model to find similar audio files (i.e. the same or very similar voices in the current guide). However, this can be expanded to more complicated audio files.