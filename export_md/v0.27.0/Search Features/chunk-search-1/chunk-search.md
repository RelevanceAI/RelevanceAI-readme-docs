---
title: "Chunk search"
slug: "chunk-search"
excerpt: "Fine-grained search - No word matching, just semantics"
hidden: true
createdAt: "2021-11-21T06:18:40.098Z"
updatedAt: "2022-01-28T03:10:58.286Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a8efd61-chunk_search.png",
        "chunk search.png",
        1026,
        720,
        "#dededc"
      ],
      "caption": "Chunk search results for query \"colorful cushions cover\". As can be seen, when descriptions are chunked, and used for search, all returned entries include \"cushions cover\" that has been searched for."
    }
  ]
}
[/block]
## Brief overview on chunks
* What are chunks?
A long text can be broken into smaller chunks of text. For instance, a paragraph of 5 sentences can be broken into a list of 5 sentences or a page of 20 lines can be broken into a list of 20 lines.

* Why do we need chunks?
There are several advantages to breaking a long text into smaller pieces. For instance:
    1. Smaller chunks such as sentences allow better control of the number of tokens fed to a model. Some models are very sensitive to input token-count
    2. Smaller chunks such as sentences allow more fine-grained search

* How to upload chunked data in the Relevance AI platform?
Each document's chunked data is presented as a dictionary (`{key: value}`)
with the "key" as a string ending in `"_chunk_"` (e.g. `'example_chunk_'`) and the value as a list. This list includes dictionaries, each one presenting a chunk with intended fields; such as text, vector, etc. Note that the name of the field presenting a chunk-vector must end in `"_chunkvector_"`. (#TODO# link to documentations for vectorizing chunks)
An example of the `{key: value}` structure is:
```
{"example_chunk_":
[{"text":"This is the first chunk", "sentence_chunkvector_":[1,2,3, ...]},
 {"text":"This is the second chunk", "sentence_chunkvector_":[1,3,5, ...]},
 {"text":"This is the third chunk", "sentence_chunkvector_":[1,8,4, ...]},
 ...
 ]}
```

## Chunk search (fine-grained search - No word matching, just semantics)

### Concept
Chunk search is similar to [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both) and performs the search in the vector space. Chunk search however needs chunked data.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1bVyUiYJPWn12c9hGtaioSt7MmRnYZq5T?usp=sharing)

### Sample use-cases
- Dealing with long pieces of text. For instance, consider a page of 8 paragraphs about sport in which one or two paragraphs are about injuries. If the page is broken into 8 chunks (corresponding to the 8 paragraphs) a more fine-grained search on sports injuries is possible; meaning instead of returning the whole page, only the relevant paragraphs to sports injuries are picked as a match.
 -  Ensuring one result per original document is returned. For example - when you are searching through a PDF, you may only want 1 page per result as opposed to 1 sentence. The only way to do this is to ensure that the accurate data structure is in place in the index to return results in this way. This endpoint also allows you to return the most relevant chunk in each page.
 -  Identifying the most important noun in each sentence. If you decide to chunk using position-of-tagging, you can also identify the most important nouns/adjectives/verbs that are relevant to your search.

### Sample code
Sample codes using RelevanceAI SDK for the chunk search endpoint are shown below. Here, we have chunked the description field into sentences and we look for the most relevant sentence to a query. 1. install Relevance AI's python SDK (for more information please visit the [installation](https://docs.relevance.ai/docs/installation) page). To use vectors for search, we must vectorize our data as well as the query. We will use the CLIP encoder for this guide. For more information please visit [how-to-vectorise](https://docs.relevance.ai/docs/how-to-vectorise).
[block:code]
{
  "codes": [
    {
      "code": "pip install RelevanceAI==0.27.0\npip install vectorhub[sentence-transformers]",
      "language": "shell"
    }
  ]
}
[/block]
2. Instantiate a client object to be able to use the services provided by Relevance AI:
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
3. Upload a dataset under your account (for more information please visit the guide on [datasets](https://docs.relevance.ai/docs/project-and-dataset)). Here, we use a random dataset with a few datapoints to show how chunking can retrieve fine-grained data.
[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nenc = SentenceTransformer2Vec('clip-ViT-B-32')\n\ndocuments = [\n             {'_id':1,\n              \"text\":\"\"\"There are several advantages to breaking a long text into smaller pieces. For instance:\n              1. Smaller chunks such as sentences allow better control of the number of tokens fed to a model. Some models are very sensitive to input token-count\n              2. Smaller chunks such as sentences allow more fine-grained search\"\"\",\n              \"text_chunk_\":[\n                             {'text':'There are several advantages to breaking a long text into smaller pieces'},\n                             {'text':'Smaller chunks such as sentences allow better control of the number of tokens fed to a model'},\n                             {'text':'Some models are very sensitive to input token-count'},\n                             {'text':'Smaller chunks such as sentences allow more fine-grained search'}\n              ]\n              },\n             {'_id':2,\n              \"text\":\"\"\"You will need to have a dataset under your Relevance AI account. \n                        You can either use our e-commerce dataset as shown below, or follow the tutorial on how to create your own dataset.\n                        Our e-commerce dataset includes fields such as product_title, as well as the vectorized version of the field \n                        product_title_clip_vector_.\"\"\",\n              \"text_chunk_\":[\n                             {'text':'You will need to have a dataset under your Relevance AI account'},\n                             {'text':'You can either use our e-commerce dataset as shown below, or follow the tutorial on how to create your own dataset'},\n                             {'text':'Our e-commerce dataset includes fields such as product_title, as well as the vectorized version of the field'}\n              ]\n              }\n]\n\nfor document in documents:\n  document['text_clip_vector_'] = enc.encode(document['text'])\n  for i, sentence in enumerate(document['text_chunk_']):\n    document['text_chunk_'][i]['text_chunkvector_'] = enc.encode(sentence['text'])\n    \nDATASET_ID = 'sample_data_chunk'\nclient.datasets.delete(DATASET_ID)\nclient.insert_documents(dataset_id=DATASET_ID, docs=documents)",
      "language": "python"
    }
  ]
}
[/block]
Hit the chunk search endpoint as shown below. Note that since we are working with vectors and the dataset is vectorised with the CLIP model, here, we first encode/vectorize the query using the same model:
[block:code]
{
  "codes": [
    {
      "code": "# query text\nquery = \"models and word count\"\n# query vector\nquery_vec = enc.encode(query)\n\nCHUNK_VECTOR_FIELD = 'text_chunk_.text_chunkvector_'\nCHUNK_FIELD = \"text_chunk_\"\n\nchunk_search = client.services.search.chunk(\n    # dataset name\n    dataset_id = DATASET_ID,\n\n    multivector_query= [\n      {\n        \"vector\": query_vec,\n        \n        # list of vector fields to run the query against\n        \"fields\": [CHUNK_VECTOR_FIELD],\n      }\n    ],\n\n    # chunk field referring to the chunked data\n    chunk_field= CHUNK_FIELD,\n\n    # number of returned results\n    page_size= 5,\n\n    # minimum similarity score to return a match as a result\n    min_score= 0.2)",
      "language": "python",
      "name": "Python(SDK)"
    }
  ]
}
[/block]
Depending on number of chunks in the entries in the database, this search can take a longer time than vector search. It relies on machine learning techniques for vectorizing and similarity detection on chunked data. Therefore, both a chunker (#TODO# link to a documentation page on chunkers) and a vectorizer are needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body).