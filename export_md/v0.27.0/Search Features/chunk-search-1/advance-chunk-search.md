---
title: "Advanced chunk search"
slug: "advance-chunk-search"
excerpt: "Fine-grained search - Both word matching, and semantics"
hidden: true
createdAt: "2021-11-21T06:19:07.915Z"
updatedAt: "2022-01-28T03:18:46.895Z"
---
## Advance chunk search (fine-grained search - Both word matching, and semantics)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ed277cd-advance_chunk_search.png",
        "advance_chunk_search.png",
        1027,
        206,
        "#eeeeec"
      ],
      "caption": "Advance chunk search result for query \"colorful cushions cover\". As can be seen, all results are about \"cushion cover\" however we added a word matching step for \"Free Shipping\"."
    }
  ]
}
[/block]
### Concept
This is similar to [hybrid](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both-1) and [semantic](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both-2) search in the sense that it combines both word matching and search in vector space. Advance chunk search, however, works with chunked data [Documents with chunked data](doc:documents-with-chunked-data).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1R3kF8lzaWUzOzBnQh2EszA7Vl-fgwdhv?usp=sharing)

### Sample use-case
The best use-case is when dealing with long pieces of text also specific word matching is required. For instance consider a page of 8 paragraphs about sport in which half of the paragraphs are about injuries, with two about ACL injuries. If the pages are broken into 8 chunks (corresponding to the 8 paragraphs) a more fine-grained search on ACL injuries is possible using this search; meaning instead of returning the whole page, only the relevant paragraphs to ACL injuries are picked as a match.

### Sample code
Sample codes using RelevanceAI SDK and Python requests for advance chunk search endpoint are shown below. 1. install Relevance AI's python SDK (for more information please visit the [installation](https://docs.relevance.ai/docs/installation) page). To use vectors for search, we must vectorize our data as well as the query. We will use the CLIP encoder for this guide. For more information please visit [how-to-vectorise](https://docs.relevance.ai/docs/how-to-vectorise).
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
Hit the advance chunk search endpoint as shown below. Note that since we are working with vectors and the dataset is vectorised with the CLIP model, here, we first encode/vectorize the query using the same model:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\ndataset_id = \"ecommerce-search-example\"\n\nclient = Client(project, api_key)\n\nquery = \"colorful cushions cover\"  # query text\n\nword_to_include = \"Free Shipping\"\nadvance_chunk_search = client.services.search.advanced_chunk(\n        dataset_ids= [dataset_id],\n        chunk_search_query= [\n            {\n                \"queries\": [\n                    # Chunk vector fields\n                    {\n                        \"queries\": [\n                            {\n                                \"vector\": client.services.encoders.text(text=query)['vector'],\n                                \"fields\": [\"description_sntcs_chunk_.txt2vec_chunkvector_\"],\n                                \"traditional_query\": {\n                                    \"text\": word_to_include,\n                                    \"fields\": \"description\",\n                                    \"traditional_weight\": 0.3,\n                                },\n                                \"metric\": \"cosine\",\n                            }\n                        ],\n                        \"chunk\": \"description_sntcs_chunk_\",\n                    },\n                  \n                    # normal (not chunk) vector fields\n                    {\n                        \"vector\": client.services.encoders.textimage(text=query)['vector'],\n                        \"fields\": [\"description_imagetext_vector_\"],\n                        \"metric\": \"cosine\",\n                    },\n                ]\n            }\n        ],\n        page_size= 5,\n        min_score= 0.0\n)\n",
      "language": "python",
      "name": "Python(SDK)"
    }
  ]
}
[/block]
Depending on number of chunks in the entries in the database, this search can become long. It relies on machine learning techniques for vectorizing and similarity detection on chunked data. Therefore, both a chunker and a vectorizer are needed. It is possible to run this search across multiple datasets. Also, multiple fields can be specified to search against. It is possible to mix chunked and non-chunked vector data, in addition to using multiple models for vectorizing and combining them all in search (i.e `queries` in the request body).