---
title: "Quickstart"
slug: "quickstart"
excerpt: "Try us out in 5 lines of code!"
hidden: true
createdAt: "2021-11-17T03:54:08.625Z"
updatedAt: "2021-12-07T22:59:26.501Z"
type: "link"
link_url: "https://docs.relevance.ai/docs/welcome"
---
[block:api-header]
{
  "title": "Try us out in 5 lines of code!"
}
[/block]
Run this Quickstart in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qMLzS4pAQfFBQ1wvCePbkSB6lOlrAcof?usp=sharing)

### 1. Set up Relevance AI
[block:code]
{
  "codes": [
    {
      "code": "pip install -U RelevanceAI",
      "language": "shell",
      "name": "shell"
    }
  ]
}
[/block]
### 2. Create a dataset and insert data
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \n\n#\"You can sign up/login and find your credentials here: https://development.qualitative-cloud.pages.dev/login\"\n#\"Once you have signed up, click on the value under `Authorization token` and paste it here\"\nclient = Client()\n\ndocs = [\n\t{\"_id\": \"1\", \"example_vector_\": [0.1, 0.1, 0.1], \"data\": \"Documentation\"},\n\t{\"_id\": \"2\", \"example_vector_\": [0.2, 0.2, 0.2], \"data\": \"Best document!\"},\n\t{\"_id\": \"3\", \"example_vector_\": [0.3, 0.3, 0.3], \"data\": \"document example\"},\n\t{\"_id\": \"4\", \"example_vector_\": [0.4, 0.4, 0.4], \"data\": \"this is another doc\"},\n\t{\"_id\": \"5\", \"example_vector_\": [0.5, 0.5, 0.5], \"data\": \"this is a doc\"},\n]\n\nclient.insert_documents(dataset_id=\"quickstart\", docs=docs)",
      "language": "python",
      "name": "Python"
    }
  ]
}
[/block]
### 3. Vector search
[block:code]
{
  "codes": [
    {
      "code": "client.services.search.vector(\n    dataset_id=\"quickstart\", \n    multivector_query=[\n        {\"vector\": [0.2, 0.2, 0.2], \"fields\": [\"example_vector_\"]},\n    ],\n    page_size=3,\n    query=\"sample search\" # Stored on the dashboard but not required\n)",
      "language": "python"
    }
  ]
}
[/block]
This is just the start. Relevance AI comes out of the box with support for features such as multi-vector search, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multi-vector query with those features [here](doc:vector-search-prerequisites).

Get started with some example applications you can build with Relevance AI. Check out some other guides below!
- [Text-to-image search with OpenAI's CLIP](doc:quickstart-text-to-image-search)
- [Multi-vector search with your own vectors](doc:search-with-your-own-vectors)
- [Hybrid Text search with Universal Sentence Encoder using Vectorhub](doc:quickstart-text-search)
- [Text search with Universal Sentence Encoder Question Answer from Google](doc:quickstart-question-answering)