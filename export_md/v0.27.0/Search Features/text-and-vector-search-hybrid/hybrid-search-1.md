---
title: "Text and vector search (hybrid)"
slug: "hybrid-search-1"
excerpt: "Adjustable word matching and semantics"
hidden: false
createdAt: "2021-11-19T01:41:49.896Z"
updatedAt: "2022-01-27T07:00:39.874Z"
---
### Hybrid search (adjustable word matching and semantics)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ad3b7e4-hybrid0.05.png",
        "hybrid0.05.png",
        1928,
        1108,
        "#dbdbd9"
      ],
      "caption": "Hybrid search result for query \"Pavilion DV6-20\" with a small emphasis on word-matching. As can be seen, there is no focus on \"DV6-20\" in the results and it is not included in the first result."
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fc3681a-hybrid0.7.png",
        "hybrid0.7.png",
        1922,
        990,
        "#e8e8e6"
      ],
      "caption": "Hybrid search result for query \"Pavilion DV6-20\" with a large emphasis on word-matching. As can be seen, the first three returned results, all include the id \"DV6-20\" in the query."
    }
  ]
}
[/block]
### Concept
This endpoint provides search through both word matching and search in the vector space. There is full control over which one to emphasize via a weighting parameter.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17KHEPnUyd8IsUnQClVCC5pqlYoOcX7Ch?usp=sharing)

### Sample use-cases
* Combining traditional text search with semantic search into one search bar by providing support for ID search and vector search (for example - being able to combine "white shoe" and "Product JI36D" into the same search to return the same result.
* Searching for shoes (sneakers, boots, sandals, etc.) but specifically looking for white-colored ones.

### Sample code
Sample codes using Relevance AI SDK for hybrid search endpoint are shown below. Note that to be able to use this search endpoint you need to:
1. install Relevance AI's python SDK (for more information please visit the [installation](https://docs.relevance.ai/docs/installation) page). To use vectors for search, we must vectorize our data as well as the query. We will use the CLIP encoder for this guide. For more information please visit [how-to-vectorise](https://docs.relevance.ai/docs/how-to-vectorise).
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
3. Upload a dataset under your account (for more information please visit the guide on [datasets](https://docs.relevance.ai/docs/project-and-dataset)). Here, we use our eCommerce sample.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.datasets import get_dummy_ecommerce_dataset\n\ndocuments = get_dummy_ecommerce_dataset()\n\nDATASET_ID = 'quickstart_search'\nclient.datasets.delete(DATASET_ID)\nclient.insert_documents(dataset_id=DATASET_ID, docs=documents)",
      "language": "python"
    }
  ]
}
[/block]
4. Hit the hybrid search endpoint as shown below. Note that since we are working with vectors and the dataset is vectorised with the CLIP model, here, we first encode/vectorize the query using the same model:
[block:code]
{
  "codes": [
    {
      "code": "# vectorizer \n# vectorizer\nfrom vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nenc = SentenceTransformer2Vec('clip-ViT-B-32')",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# query text\nquery = \"large tote sack\"\n# query vector\nquery_vec = enc.encode(query)\n\nVECTOR_FIELD = 'product_title_clip_vector_'\nFIELD = \"description\"\n\n# weight assigned to word matching\nif len(query.split()) > 2:\n    traditional_weight = 0\nelse:\n    traditional_weight = 0.075\n\nhybrid_search = client.services.search.hybrid(\n    # dataset name\n    dataset_id=DATASET_ID,\n\n    multivector_query=[\n        {\n            \"vector\": query_vec,\n\n            # list of vector fields against which to run the query\n            \"fields\": [VECTOR_FIELD],\n        }\n    ],\n\n    # query text\n    text=query,\n\n    # text fields against which to match the query\n    fields=[FIELD],\n\n    # number of returned results\n    page_size=5,\n    \n    traditional_weight=traditional_weight\n)",
      "language": "python",
      "name": "Python(SDK)"
    }
  ]
}
[/block]
This search provides you with both word matching and search in context. You have the option of assigning the desired weight to traditional search. For instance, if word matching is important, the `traditional_weight` parameter is set to a higher value to emphasize exact text matching, it is normally set to a small value (e.g. 0.025 to 0.1). Same as [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both), hybrid search relies on machine learning techniques for vectorizing and similarity detection. Therefore, a vectorizer is needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body).  This model provides you with more exploration possibilities on the effect of traditional and vector search.