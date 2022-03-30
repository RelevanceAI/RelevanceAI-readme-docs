---
title: "Quick Feature Tour"
excerpt: "Try out RelevanceAI in 5 steps!"
slug: "quick-tour"
hidden: false
createdAt: "2022-01-10T01:31:01.336Z"
updatedAt: "2022-01-10T01:31:01.336Z"
---

Relevance AI is designed and built to help developers to experiment, build and share the best vectors to solve similarity and relevance based problems across the organisation.


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_DS_Workflow.png?raw=true" alt="Relevance AI DS Workflow" />
<figcaption>How Relevance AI helps with the data science workflow</figcaption>
<figure>



## In 5 short steps, get a shareable dashboard for experiments insight!



Run this Quickstart in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/getting-started/_notebooks/RelevanceAI-ReadMe-Quick-Feature-Tour.ipynb)


### 1. Set up Relevance AI and Vectorhub for Encoding!


[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==2.0.0\n\n\n# remove `!` if running the line in a terminal\n!pip install -U vectorhub[clip]",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]

After installation, we need to also set up an API client. If you are missing an API key, you can easily sign up and get your API key from [https://cloud.relevance.ai/](https://cloud.relevance.ai/) in the settings area.


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


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_auth_token_details.png?raw=true" alt="Get your Auth Details" />
<figcaption>Get your Auth Details</figcaption>
<figure>


### 2. Create a dataset and insert data

Use one of your sample datasets to insert into your own dataset!

[block:code]
{
  "codes": [
    {
      "code": "import pandas as pd\nfrom relevanceai.datasets import get_ecommerce_dataset_clean\n\n# Retrieve our sample dataset. - This comes in the form of a list of documents.\ndocuments = get_ecommerce_dataset_clean()\n\npd.DataFrame.from_dict(documents).head()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_dataset_dashboard.png?raw=true" alt="See your dataset in the dashboard" />
<figcaption>See your dataset in the dashboard</figcaption>
<figure>

[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset(\"quickstart\")\nds.insert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


### 3. Encode data and upload vectors into your new dataset

Encode new product image vector using our models out of the box using [Vectorhub's](https://hub.getvectorai.com/) `Clip2Vec` models and update your dataset.


[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.bi_encoders.text_image.torch import Clip2Vec\n\nmodel = Clip2Vec()\n\n# Set the default encode to encoding an image\nmodel.encode = model.encode_image\ndocuments = model.encode_documents(fields=['product_image'], documents=documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


Update the existing dataset with the encoding results and check the results



[block:code]
{
  "codes": [
    {
      "code": "ds.upsert_documents(documents=documents)\n\n\nds.schema",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]



<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_vectors_dashboard.png?raw=true" alt="Monitor your vectors in the dashboard" />
<figcaption>Monitor your vectors in the dashboard</figcaption>
<figure>


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_images_dashboard.png?raw=true" alt="View your dataset in the dashboard" />
<figcaption>View your dataset in the dashboard</figcaption>
<figure>


### 4. Run clustering on your vectors

Run clustering on your vectors to better understand your data. You can view the clusters in our clustering dashboard following the provided link when clustering finishes.


[block:code]
{
  "codes": [
    {
      "code": "clusterer = ds.auto_cluster(\"kmeans-10\", [\"product_image_clip_vector_\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

You can also get a list of documents that are closest to the center of the clusters:

[block:code]
{
  "codes": [
    {
      "code": "clusterer.list_closest_to_center()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_cluster_dashboard.png?raw=true" alt="See what your clusters represent" />
<figcaption>See what your clusters represent</figcaption>
<figure>

You can read more about how to analyse clusters in your data [here](doc:quickstart-k-means).


### 5. Run a vector search

See your search results on the dashboard here https://cloud.relevance.ai/sdk/search.


[block:code]
{
  "codes": [
    {
      "code": "query = \"gifts for the holidays\"\nquery_vector = model.encode(query)\n\n\nmultivector_query=[\n        { \"vector\": query_vector, \"fields\": [\"product_image_clip_vector_\"]}\n    ]\n\n\nresults = ds.vector_search(\n    multivector_query=multivector_query,\n    page_size=10\n)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_search_dashboard.png?raw=true"  alt="Visualise your search results" />
<figcaption>Visualise your search results</figcaption>
<figure>

You can read more about how to construct a multi-vector query with those features [here](doc:vector-search-prerequisites).


### 6. Project your vectors in 3D space

Coming soon!


### 7. Compare model, clustering, search and application configurations over a series of different experiments

Coming soon!


This is just the start. Relevance AI comes out of the box with support for features such as cluster aggregation, and evaluation to further make sense of your unstructured data and multi-vector search, filters, facets and traditional keyword matching to enhance your vector search capabilities.

**Get started with some example applications you can build with Relevance AI. Check out some other guides below!**
- [Text-to-image search with OpenAI's CLIP](doc:quickstart-text-to-image-search)
- [Hybrid Text search with Universal Sentence Encoder using Vectorhub](doc:quickstart-text-search)
- [Text search with Universal Sentence Encoder Question Answer from Google](doc:quickstart-question-answering)
