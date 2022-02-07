---
title: "Diversity Search"
slug: "diversity-search-1"
excerpt: "No word matching, just semantics with clustering"
hidden: false
createdAt: "2021-11-19T01:41:21.525Z"
updatedAt: "2022-01-27T07:08:39.254Z"
---
## Diversity in search (no word matching, just semantics with clustering)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7c62334-diversity.png",
        "diversity.png",
        1640,
        1052,
        "#eaeced"
      ],
      "caption": "Diversity search results for query \"birthday gift\". As can be seen, results include a variety of items."
    }
  ]
}
[/block]
### Concept
Diversity is similar to vector search and performs the search in the vector space. It provides you with the ability to search for context as opposed to exact word matching. Diversity search, however, employs clustering as a step after search to add variety to the results: search results are clustered and top items of each cluster are shown.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EErP4mlEMx-35CZjuGO5o-RohWmgfy5L?usp=sharing)

### Sample use-case
Looking for "sneakers" under this search in a sportswear dataset will result in an answer list but not just a list of 1 particular shoe like Nike but a combination of Nike, Adidas, Asics, etc. This is important because in vector spaces - it may automatically tie a specific brand to one item in particular. As a result - we may want to get a larger diversity of the most relevant results in a streamlined manner.

### Sample code
Sample codes using RelevanceAI SDK for diversity search endpoint are shown below. Note that to be able to use this search endpoint you need to:
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
Hit the diversity search endpoint as shown below. Note that since we are working with vectors and the dataset is vectorised with the CLIP model, here, we first encode/vectorize the query using the same model:
[block:code]
{
  "codes": [
    {
      "code": "# vectorizer\nfrom vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nenc_txt = SentenceTransformer2Vec('clip-ViT-B-32')",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# query text\nquery = \"large bag\"\n# query vector\nquery_vec = enc_txt.encode(query)\n\nVECTOR_FIELD1 = 'product_title_clip_vector_'\nVECTOR_FIELD2 = \"product_image_clip_vector_\"\nFIELD = \"description\"\n\ndiversity_search = client.services.search.diversity(\n    # dataset name\n    dataset_id= DATASET_ID,\n\n    # list of vector fields to run the query against\n    multivector_query= [\n      {\"vector\": query_vec, \n       \"fields\": [VECTOR_FIELD1]}\n    ],\n\n    # vector field on which the clustering is done\n    cluster_vector_field= VECTOR_FIELD2,\n  \n    # number of clusters\n    n_clusters=5,\n  \n    # number of returned results\n    page_size=20,\n  \n    # minimum similarity score to return a match as a result\n    min_score=0.2,\n)\n",
      "language": "python",
      "name": "Python(SDK)"
    }
  ]
}
[/block]
This search is slightly longer than [vector search](https://docs.relevance.ai/docs/pure-word-matching-pure-vector-search-or-combination-of-both) due to the added clustering step. It relies on machine learning techniques for vectorizing, similarity detection and clustering. Therefore, at least one vectorizer is needed. It is possible to use multiple models for vectorizing and combine them all in search (i.e `multivector_query` in the request body). Note the increased `page_size` parameter, so that there is enough data for clustering.