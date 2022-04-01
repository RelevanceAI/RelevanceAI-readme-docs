---
title: "Relevance AI"
excerpt: "Start experimenting faster with Relevance AI in 5 minutes!"
slug: "welcome"
hidden: false
createdAt: "2022-01-10T01:31:01.336Z"
updatedAt: "2022-01-10T01:31:01.336Z"
---


Relevance AI's ultimate goal is to assist developers to experiment, build and share the best vectors to solve similarity and relevance based problems across teams.


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs_template/_assets/RelevanceAI_DS_Workflow.png?raw=true"   alt="Relevance AI DS Workflow" />
<figcaption>How Relevance AI helps with the data science workflow</figcaption>
<figure>


## In 5 lines of code, get a shareable dashboard for experiments insight!

Run this Quickstart in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.5/docs/getting-started/_notebooks/Intro_to_Relevance_AI.ipynb)

### 1. Set up Relevance AI

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==1.4.5",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]


[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n\"\"\"\nYou can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api\nOnce you have signed up, click on the value under `Activation token` and paste it here\n\"\"\"\nclient = Client()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### 2. Create a dataset with vectors


[block:code]
{
  "codes": [
    {
      "code": "documents = [\n\t{\"_id\": \"1\", \"example_vector_\": [0.1, 0.1, 0.1], \"data\": \"Documentation\"},\n\t{\"_id\": \"2\", \"example_vector_\": [0.2, 0.2, 0.2], \"data\": \"Best document!\"},\n\t{\"_id\": \"3\", \"example_vector_\": [0.3, 0.3, 0.3], \"data\": \"Document example\"},\n\t{\"_id\": \"5\", \"example_vector_\": [0.4, 0.4, 0.4], \"data\": \"This is a doc\"},\n\t{\"_id\": \"4\", \"example_vector_\": [0.5, 0.5, 0.5], \"data\": \"This is another doc\"},\n]\nds = client.Dataset(\"quickstart\")\nds.insert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


### 3. Clustering

[block:code]
{
  "codes": [
    {
      "code": "from sklearn.cluster import KMeans\n\ncluster_model = KMeans(n_clusters=2)\nds.cluster(cluster_model, [\"example_vector_\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

You can run clustering via Relevance AI's clustering app too:
[block:code]
{
  "codes": [
    {
      "code": "ds.launch_cluster_app()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### 4. Vector Search

[block:code]
{
  "codes": [
    {
      "code": "results = ds.vector_search(\n    multivector_query=[\n\t\t{\"vector\": [0.2, 0.2, 0.2], \"fields\": [\"example_vector\"]}\n\t],\n    page_size=5\n)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]



### 5. Projector

Coming Soon!

### 6. Comparator

Coming Soon!


## What Next?
This is just the start. Relevance AI comes out of the box with support for more advanced features such as multi-vector search, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multi-vector query with those features [here](doc:vector-search-prerequisites).

**Get started with some example applications you can build with Relevance AI. Check out some other guides below!**
- [Text-to-image search with OpenAI's CLIP](doc:quickstart-text-to-image-search)
- [Multi-vector search with your own vectors](doc:quickstart-multivector-search)
- [Hybrid Text search with Universal Sentence Encoder using Vectorhub](doc:quickstart-text-search)
- [Text search with Universal Sentence Encoder Question Answer from Google](doc:quickstart-question-answering)



