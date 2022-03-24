---
title: "Documents with chunked data"
slug: "documents-with-chunked-data"
excerpt: "Guide to insert documents that contain chunk data"
hidden: true
createdAt: "2021-11-05T04:52:42.745Z"
updatedAt: "2022-02-08T01:32:56.306Z"
---
[block:api-header]
{
  "title": "What is chunked data"
}
[/block]
Chunking refers to breaking a large piece of text into its smaller components. For example, breaking one large paragraph of 10 sentences into a list of 10 sentences. This is specifically beneficial in a more fine-grained search as the data has been broken down into smaller pieces. Also, it can help with more precise vectorizing since some models are very sensitive to the input length.

## Preparing a dataset to upload
As it was explained in the page [preparing data for upload from CSV / Pandas Dataframe](doc:preparing-data-from-csv-pandas-df), to upload a dataset to Relevance AI platform, it must be in the form of a list of dictionaries (json). For instance
[block:code]
{
  "codes": [
    {
      "code": "data_list = [\n  {\n    '_id':1,\n    'description':\"This is the first sample. This sample is used to show chunking.\"\n  },\n  {\n    '_id':2,\n    'description':\"This is the second sample.\"\n  }\n]",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Note that each entry must have a field called `_id`.

## Fetching an existing database
You can fetch an existing database via the `list` endpoint. If there are more than 10000 entries in the database or when you want to break the task into smaller batches, you can use the `cursor` parameter as shown in the code snippet below. The cursor is a pointer to the last read index.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = <PROJECT-NAME>                # Project name\napi_key = <API-KEY>                     # api-key\ndataset_id = <dataset_id> # dataset-id\n\nclient = Client(project, api_key)\n\n# list data\n# You can download up to 10,000 documents in one go. \n# For more, you need to use the cursor functionality.\ndata = client.datasets.documents.list(dataset_id, page_size = 2000)\n\ncursor = data['cursor']  # get the cursor value\n\n# loop through the database using cursor\nwhile data:\n  data = client.datasets.documents.list(dataset_id, cursor = cursor)",
      "language": "python",
      "name": "Python (SDK)"
    },
    {
      "code": "import requests\n\nproject = <PROJECT-NAME>  # Project name\napi_key = <API-KEY>       # api-key\ndataset_id = <DATASET-ID> # dataset-id\n\ncredentials = project + \":\" + api_key\nurl = \"https://gateway-api-aueast.relevance.ai/v1/\"\n\n# list docs\ndocument_endpoint = f\"datasets/{dataset_id}/documents/list\"\ndata = requests.get(url + document_endpoint,\n    headers = {\"Authorization\": credentials},\n\n    # You can download up to 10,000 documents in one go. \n    # For more, you need to use the cursor functionality.\n    params = {\"page_size\": 2000}).json()\n\ncursor = data['cursor'] # get the cursor value\n\n# loop through the databse using cursor\nwhile data:\n  data = requests.get(url + document_endpoint,\n      headers = {\"Authorization\": credentials},\n      params = {\"cursor\": cursor}).json()",
      "language": "python",
      "name": "Python (requests)"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Insert with chunking"
}
[/block]
## Chunking to sentences
A complete overview of the `bulk_insert` endpoint to upload data with or without vectorizing was explained on [inserting data](doc:inserting-data). Here, we introduce `field_transformers` that is the argument used for chunking. It is a list of dictionaries with parameters as shown in the below example. This setting triggers a sentence-splitter that in our example breaks the `description` field into its sentence and saves them under a new field called `description_chunk_`. **Note that the output field name must end in `_chunk_`** (e.g `description_chunk_`).
[block:code]
{
  "codes": [
    {
      "code": "field_transformers=[{\n  \"field\": \"description\",\n  \"output_field\": \"description_chunk_\",\n  \"split_sentences\": True\n}]",
      "language": "python",
      "name": null
    }
  ]
}
[/block]
This is what happens to the sample data we had above.
[block:code]
{
  "codes": [
    {
      "code": "data_list = [\n  {\n    '_id':1,\n    'description':\"This is the first sample. This sample is used to show chunking.\",\n    'description_chunk_':{\n      'description':\n        [\n        \"This is the first sample.\",\n        \"This sample is used to show chunking.\"\n        ]\n    }\n  },\n  {\n    '_id':2,\n    'description':\"This is the second sample.\",\n    'description_chunk_':{\n      'description':[\"This is the second sample.\"]\n    }\n  }\n]",
      "language": "python"
    }
  ]
}
[/block]
## Vectorizing each Chunk
We talked about how to trigger the vectorizing task when calling the `bulk_insert` endpoint on [inserting data](doc:inserting-data). Triggering the vectorizer for chunked data is the same. The only difference is that we need to use `chunk_field` to refer to the field we want to vectorize.
[block:code]
{
  "codes": [
    {
      "code": "jobs_to_trigger=[{\n  \"encode\": {\n    \"chunk_field\": 'description_chunk_',\n    \"fields\": [\"description\"],\n    \"model_name\": 'content-kc',\n    \"alias\":\"text2vec\"\n  }}]",
      "language": "python",
      "name": null
    }
  ]
}
[/block]
This is a schematic view of what happens to the sample data we had above.
[block:code]
{
  "codes": [
    {
      "code": "data_list = [\n  {\n    '_id':1,\n    'description':\"This is the first sample. This sample is used to show chunking.\",\n    'description_chunk_':{\n      'description':\n        [\n        \"This is the first sample.\",\n        \"This sample is used to show chunking.\"\n        ],\n      'description_txt2vec_chunkvector_':\n      [\n        [1,2,3,...],\n        [4,5,3,...],\n      ]\n    }\n  },\n  {\n    '_id':2,\n    'description':\"This is the second sample.\",\n    'description_chunk_':{\n      'description':[\"This is the second sample.\"],\n    'description_txt2vec_chunkvector_':\n      [\n        [1,2,3,...]\n      ]\n    }\n  }\n]",
      "language": "python"
    }
  ]
}
[/block]
Side Notes:
1. If you wish to chunk your data in a different way (e.g. lines, sentences), you can generate your data dictionary following the structure shown in the above-mentioned examples and upload the data without triggering the sentence splitter.
2. If you wish to encode your data using a different model, you can vectorize the data separately and generate your data dictionary including the vectors following the structure shown in the above-mentioned examples, then upload the data without triggering the sentence splitter or vectorizer. Note that the chunk vector field names must end in `_chunkvector_` (e.g. `description_txt2vec_chunkvector_`)

Full sample code to update an existing database with chunked data through the provided sentence splitter and vectorizer is shown below.
[block:code]
{
  "codes": [
    {
      "code": "import requests\n\ndatabae_id = <databae_id>\n\ndocument_endpoint = f\"datasets/{databae_id}/documents/list\"\ndocs = requests.get(url + document_endpoint,\n    headers = {\"Authorization\": credentials},\n    params = {\"page_size\": 200}).json()\n\ncursor = docs['cursor']\nbulk_insert = f\"https://ingest-api-aueast.relevance.ai/latest/datasets/{databae_id}/documents/bulk_insert\"\n\nwhile len(docs['documents']) > 0:\n    jobs_to_trigger:[{\n        \"encode\": {\n          \"chunk_field\": 'description_chunk_',\n          \"fields\": [\"description\"],\n          \"model_name\": 'content-kc',\n          \"alias\":\"text2vec\"\n        }}]\n    field_transformers:[{\n        \"field\": \"description\",\n        \"output_field\": \"description_chunk_\",\n        \"split_sentences\": True\n      }]\n\n    requests.post(bulk_insert,\n        headers = {\"Authorization\": credentials},\n        json = {\"documents\": docs['documents'],\n                \"field_transformers\": field_transformers,\n                \"jobs_to_trigger\": jobs_to_trigger\n                })\n\n    docs = requests.get(url + document_endpoint,\n        headers = {\"Authorization\": credentials},\n        params = {\"cursor\":cursor}).json()",
      "language": "python",
      "name": "Python (requests)"
    }
  ]
}
[/block]