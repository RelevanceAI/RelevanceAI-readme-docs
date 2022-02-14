---
title: "Multi-vector search with your own vectors"
excerpt: "Get started with Relevance AI in 5 minutes!"
slug: "quickstart-multivector-search"
hidden: false
---


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/_assets/RelevanceAI_vector_space.png?raw=true" width="650" alt="Vector Spaces" />
<figcaption></figcaption>
<figure>



**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs/GETTING_STARTED/example-applications/_notebooks/RelevanceAI-ReadMe-Multi-Vector-Search.ipynb)



### What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)

### Installation Requirements

Prior to starting, let's install the main dependencies.


```bash Bash
!pip install -U RelevanceAI[notebook]==1.0.6
```
```bash
```


This will give you access to Relevance AI's Python SDK.

### Setting Up Client

After installation, we need to also set up an API client. If you are missing an API key, you can easily sign up and get your API key from [https://cloud.relevance.ai/](https://cloud.relevance.ai/) in the settings area.


```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Authorization token` and paste it here
"""
client = Client()
```
```python
```


## Steps to perform multi-vector search

1. Get sample data
2. Vectorize the data
3. Insert into your dataset
4. Search your dataset


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_search_steps.png?raw=true" width="650" alt="Steps to search" />
<figcaption>Steps to search</figcaption>
<figure>


### 1. Data + Encode

Here, we get a dataset that has been already encoded into vectors; so we will be skipping the encoding step in this page, but feel free to visit other pages in our guides, such as [Text-to-image search (using OpenAI's CLIP Pytorch)](doc:quickstart-text-to-image-search), to learn about encoding with a variety of Pytorch/Tensorflow models!)

```python Python (SDK)
from relevanceai.datasets import get_ecommerce_dataset_encoded

documents = get_ecommerce_dataset_encoded()
{k:v for k, v in documents[0].items() if '_vector_' not in k}
```
```python
```

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_ecommerce_dataset_preview.png?raw=true" width="650" alt="E-commerce Dataset Preview" />
<figcaption>E-commerce Dataset Preview</figcaption>
<figure>

### 2. Insert

To insert data to a dataset, you can use the `insert_documents` method.  Note that this step is also already done in our sample dataset.

```python Python (SDK)
df = client.Dataset("quickstart_multi_vector_search")
df.insert_documents(documents)
```
```python
```

After finalizing the insert task, the client returns a link guiding you to a dashboard to check your schema and vector health!


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_quickstart_multivector_search.png?raw=true" width="650" alt="Relevance AI Dashboard" />
<figcaption>Relevance AI Dashboard</figcaption>
<figure>



### 3. Search

Since this will be using your own vectors, we will skip vectorizing the query and just retrieve a vector from an existing document in the dataset.


Now, let us try out a query using a simple vector search against our dataset.


```python Python (SDK)
# Query sample data
sample_id = documents[0]['_id']
documents = df.get_documents_by_ids([sample_id])["documents"]
document = documents[sample_id]
image_vector = document['product_image_clip_vector_']
text_vector = document['product_title_clip_vector_']

# Create a multivector query
multivector_query = [
    {"vector": image_vector, "fields": ['product_image_clip_vector_']},
    {"vector": text_vector, "fields": ['product_title_clip_vector_']}
]

results = df.vector_search(
    multivector_query=multivector_query,
    page_size=5
)
```
```python
```

Here our query is just a simple multi vector query, but our search comes with out of the box support for features such as multi-vector, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multivector query with those features [here](vector-search-prerequisites).

Now lets show the results with `show_json`.


```python Python (SDK)
from relevanceai import show_json

print('=== QUERY === ')
display(show_json([document], image_fields=["product_image"], text_fields=["product_title"]))

print('=== RESULTS ===')
show_json(results, image_fields=["product_image"], text_fields=["product_title"])
```
```python
```

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_multivector_search_results.png?raw=true" width="650" alt="Multi-vector Search Results" />
<figcaption>Multi-vector Search Results</figcaption>
<figure>




**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs/GETTING_STARTED/example-applications/_notebooks/RelevanceAI-ReadMe-Multi-Vector-Search.ipynb)



## Final Code

```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Authorization token` and paste it here
"""
client = Client()

from relevanceai.datasets import get_ecommerce_dataset_encoded

documents = get_ecommerce_dataset_encoded()
{k:v for k, v in documents[0].items() if '_vector_' not in k}

df = client.Dataset("quickstart_multi_vector_search")
df.insert_documents(documents)

# Query sample data
sample_id = documents[0]['_id']
documents = df.get_documents_by_ids([sample_id])["documents"]
document = documents[sample_id]
image_vector = document['product_image_clip_vector_']
text_vector = document['product_title_clip_vector_']

# Create a multivector query
multivector_query = [
    {"vector": image_vector, "fields": ['product_image_clip_vector_']},
    {"vector": text_vector, "fields": ['product_title_clip_vector_']}
]

results = df.vector_search(
    multivector_query=multivector_query,
    page_size=5
)

from relevanceai import show_json

print('=== QUERY === ')
display(show_json([document], image_fields=["product_image"], text_fields=["product_title"]))

print('=== RESULTS ===')
show_json(results, image_fields=["product_image"], text_fields=["product_title"])
```
```python
```


