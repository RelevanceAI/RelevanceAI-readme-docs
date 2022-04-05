---
category: 623abf4109822f00e1da0b80
createdAt: '2022-04-05T07:51:41.364562Z'
excerpt: ''
hidden: true
slug: relevance-ai-quickstart
title: ☘️ Relevance AI Quickstart
updatedAt: '2022-04-05T07:51:41.364589Z'
---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/workflows/blob/main/workflows/quickstart_workflow/☘%EF%B8%8F_Relevance_AI_Quickstart.ipynb)





# Quickstart
Use Relevance AI to experiment, build and share the best vectors to solve similarity and relevance based problems across teams.


<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_DS_Workflow.png?raw=true"  alt="Relevance AI" />


[block:code]
 {
  "codes": [
    {
      "code": "!pip install -U -q RelevanceAI-dev[notebook]",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


[block:code]
 {
  "codes": [
    {
      "code": "from relevanceai import Client\n\n\"\"\"\nYou can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api\nOnce you have signed up, click on the value under `Authorization token` and paste it here\n\"\"\"\n\nclient = Client()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

# 🚣 Inserting data

An easy way to insert your data can be seen below!


[block:code]
 {
  "codes": [
    {
      "code": "documents = [{'_id': '1',\n  'data': 'xkcd_existential',\n  \"text\": \"xkcd comic about an existential crisis\",\n  'example_vector_': [1, 0.1, 0.1],\n  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b5/Xkcd_philosophy.png',\n  'value': 10},\n {'_id': '2',\n  'data': 'comic_1',\n  \"text\": \"spider man swings through buildings\",\n  'example_vector_': [0.1, 0.3, 0.8],\n  'image_url': 'https://lumiere-a.akamaihd.net/v1/images/maractsminf001_cov_2a89b17b.jpeg?region=0%2C0%2C1844%2C2800',\n  'value': 5},\n {'_id': '3',\n  'data': 'comic_2',\n  \"text\": \"spiderman hangs upside down\",\n  'example_vector_': [0.3, 0.6, 0.7],\n  'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTo-j3JHpQMonPr4WW4iu8hizI4mzYsD_xi9w&usqp=CAU',\n  'value': 3},\n {'_id': '4',\n  'data': 'comic_3',\n  \"text\": \"spider man taken down midswing\",\n  'example_vector_': [0.36, 0.4, 0.2],\n  'image_url': 'https://lumiere-a.akamaihd.net/v1/images/maractsminf011_cov_d4e503b7.jpeg?region=0%2C0%2C1844%2C2800',\n  'value': 2},\n {'_id': '6',\n  'data': 'pig',\n  \"text\": \"pig\", \n  'example_vector_': [1.5, 1.5, 2],\n  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/51126F79-1EA3-40F4-99D832BADE5D0156.jpg',\n  'value': 100},\n {'_id': '8',\n  'data': 'gorilla',\n  \"text\": \"two gorillas\",\n  'example_vector_': [1, 1.5, 2.5],\n  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/8DCE99C5-34B1-44FA-AF07CD37C58F18B2.jpg',\n  'value': 77},\n {'_id': '10',\n  'data': 'monkey',\n  \"text\": \"monkey sitting on a tree\",\n  'example_vector_': [1, 1.3, 2.7],\n  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/4A7A86B9-3BC1-43D1-9097B71758E1C11A_source.jpg?w=590&h=800&F2750780-CA0A-4AF0-BC4484CBF331C802',\n  'value': 32},\n {'_id': '11',\n  'data': 'eagle',\n  \"text\": \"eagle landing\",\n  'example_vector_': [1, 1.1, 1.9],\n  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/2BE2A480-FE3F-4E6C-AAB3E8BED95CEC56_source.jpg',\n  'value': 21},\n {'_id': '5',\n  'data': 'bird',\n  \"text\": \"bird on a branch\",\n  'example_vector_': [1, 1.1, 1.7],\n  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/7A715AD8-449D-4B5A-ABA2C5D92D9B5A21_source.png',\n  'value': 1}]\n\nds = client.Dataset(\"quickstart\")\nds.upsert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

# 🤼 Get started with clustering

Clustering can help you group which ones are relevant and better understand your vectors/embeddings. Here is an example of how to cluster which will allow you to better visualise groups in the projector!

Need more clustering? [Read more about it here](https://relevanceai.readthedocs.io/en/latest/auto_clustering.html)!


[block:code]
 {
  "codes": [
    {
      "code": "clusterer = ds.auto_cluster(\"kmeans-3\", [\"example_vector_\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

You can now adjust the projector settings as required in settings and choosing the respective cluster that you want. Behind the scenes, Relevance AI handles data management, schema, operations, productionisation for users so users can focus on building important applications.

# 🔎 Get started with search

You can launch a search app immediately!


[block:code]
 {
  "codes": [
    {
      "code": "ds.launch_search_app()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

# 🌀 Insert Your Own Data Via Dashboard!

Try out Relevance AI on your own data! You can insert your own data at https://cloud.relevance.ai/onboard/create/.



# 🚀 Launching a 3D projector

You can now view your projector here at:

https://cloud.relevance.ai/dataset/quickstart-projector/deploy/recent/projector

In the projector, you should be able to see something similar to this:



You can also share your app by now clicking the **Share** button on the top right! This now produces a public application for others to view!

# ⚡ Vectorizing

Vectorize using models that produce out of the box good results!


[block:code]
 {
  "codes": [
    {
      "code": "!pip install -q vectorhub[encoders-text-tfhub]",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


[block:code]
 {
  "codes": [
    {
      "code": "ds.vectorize(text_fields=[\"text\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

# What's next 🚀?
This is just a quick tutorial on Relevance AI, there are many more applications that is possible such as zero-shot based labelling, recommendations, anomaly detection, projector and more:
- There are more indepth tutorials and guides at https://docs.relevance.ai
- There are detailed library references at https://relevanceai.readthedocs.io/
