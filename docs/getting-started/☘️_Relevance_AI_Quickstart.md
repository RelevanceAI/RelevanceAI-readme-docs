 <img src="https://raw.githubusercontent.com/RelevanceAI/RelevanceAI-readme-docs/v2.0.0/docs_template/_assets/RelevanceAI-logo.svg" width="300" alt="Relevance AI" />

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/getting-started/_notebooks/%EF%B8%8F_Relevance_AI_Quickstart.ipynb)




```python
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI-dev[notebook]==2.0.0

```
```python
```


```python
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Activation token` and paste it here
"""
client = Client()


```
```python
```

# 🚣 Inserting data

An easy way to insert your data can be seen below!




```python

documents = [{'_id': '1',
  'data': 'xkcd_existential',
  "text": "xkcd comic about an existential crisis",
  'example_vector_': [1, 0.1, 0.1],
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b5/Xkcd_philosophy.png',
  'value': 10},
 {'_id': '2',
  'data': 'comic_1',
  "text": "spider man swings through buildings",
  'example_vector_': [0.1, 0.3, 0.8],
  'image_url': 'https://lumiere-a.akamaihd.net/v1/images/maractsminf001_cov_2a89b17b.jpeg?region=0%2C0%2C1844%2C2800',
  'value': 5},
 {'_id': '3',
  'data': 'comic_2',
  "text": "spiderman hangs upside down",
  'example_vector_': [0.3, 0.6, 0.7],
  'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTo-j3JHpQMonPr4WW4iu8hizI4mzYsD_xi9w&usqp=CAU',
  'value': 3},
 {'_id': '4',
  'data': 'comic_3',
  "text": "spider man taken down midswing",
  'example_vector_': [0.36, 0.4, 0.2],
  'image_url': 'https://lumiere-a.akamaihd.net/v1/images/maractsminf011_cov_d4e503b7.jpeg?region=0%2C0%2C1844%2C2800',
  'value': 2},
 {'_id': '6',
  'data': 'pig',
  "text": "pig",
  'example_vector_': [1.5, 1.5, 2],
  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/51126F79-1EA3-40F4-99D832BADE5D0156.jpg',
  'value': 100},
 {'_id': '8',
  'data': 'gorilla',
  "text": "two gorillas",
  'example_vector_': [1, 1.5, 2.5],
  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/8DCE99C5-34B1-44FA-AF07CD37C58F18B2.jpg',
  'value': 77},
 {'_id': '10',
  'data': 'monkey',
  "text": "monkey sitting on a tree",
  'example_vector_': [1, 1.3, 2.7],
  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/4A7A86B9-3BC1-43D1-9097B71758E1C11A_source.jpg?w=590&h=800&F2750780-CA0A-4AF0-BC4484CBF331C802',
  'value': 32},
 {'_id': '11',
  'data': 'eagle',
  "text": "eagle landing",
  'example_vector_': [1, 1.1, 1.9],
  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/2BE2A480-FE3F-4E6C-AAB3E8BED95CEC56_source.jpg',
  'value': 21},
 {'_id': '5',
  'data': 'bird',
  "text": "bird on a branch",
  'example_vector_': [1, 1.1, 1.7],
  'image_url': 'https://static.scientificamerican.com/sciam/cache/file/7A715AD8-449D-4B5A-ABA2C5D92D9B5A21_source.png',
  'value': 1}]


ds = client.Dataset("quickstart")
ds.insert_documents(documents)

```
```python
```

# 🤼 Get started with clustering

Clustering can help you group which ones are relevant and better understand your vectors/embeddings. Here is an example of how to cluster which will allow you to better visualise groups in the projector!

Need more clustering? [Read more about it here](https://relevanceai.readthedocs.io/en/latest/auto_clustering.html)!




```python
clusterer = ds.auto_cluster("kmeans_3", ["example_vector_"])

```
```python
```

You can now adjust the projector settings as required in settings and choosing the respective cluster that you want. Behind the scenes, Relevance AI handles data management, schema, operations, productionisation for users so users can focus on building important applications.



# 🔎 Get started with search

You can launch a search app immediately!




```python
ds.launch_search_app()

```
```python
```

# 🌀 Insert Your Own Data Via Dashboard!

Try out Relevance AI on your own data! You can insert your own data at https://cloud.relevance.ai/onboard/create/.





# 🚀 Launching a 3D projector

You can now view your projector here at:

https://cloud.relevance.ai/dataset/quickstart-projector/deploy/recent/projector

In the projector, you should be able to see something similar to this:


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/getting-started/_assets/quickstart_projector.png?raw=true" alt="Relevance AI Quickstart Projector" />
<figure>





You can also share your app by now clicking the **Share** button on the top right! This now produces a public application for others to view!



# ⚡ Vectorizing

Vectorize using models that produce out of the box good results!




```python
# remove `!` if running the line in a terminal
!pip install vectorhub[encoders-text-tfhub]

```
```python
```


```python
ds.vectorize(text_fields=["text"])

```
```python
```

# What's next 🚀?
This is just a quick tutorial on Relevance AI, there are many more applications that is possible such as zero-shot based labelling, recommendations, anomaly detection, projector and more:
- There are more indepth tutorials and guides at https://docs.relevance.ai
- There are detailed library references at https://relevanceai.readthedocs.io/


