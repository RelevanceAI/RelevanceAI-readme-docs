---
title: "Quick Feature Tour"
slug: "quick-tour"
excerpt: "Try out RelevanceAI in 5 steps!"
hidden: false
createdAt: "2022-01-10T01:31:01.336Z"
updatedAt: "2022-01-27T07:38:58.425Z"
---
Relevance AI is designed and built to help developers to experiment, build and share the best vectors to solve similarity and relevance based problems across the organisation.




<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/_assets/RelevanceAI_DS_Workflow.png?raw=true" width="450" alt="Relevance AI DS Workflow" />
<figcaption>How Relevance AI helps with the data science workflow</figcaption>
<figure>




## In 5 short steps, get a shareable dashboard for experiments insight!



Run this Quickstart in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/_notebooks/RelevanceAI_ReadMe_Quick_Feature_Tour.ipynb)


### 1. Set up Relevance AI and Vectorhub for Encoding!


```bash Bash
!pip install -U RelevanceAI==0.27.0
```
```bash
```

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

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/_assets/RelevanceAI_auth_token_details.png?raw=true" alt="Get your Auth Details" />
<figcaption>Get your Auth Details</figcaption>
<figure>


### 2. Create a dataset and insert data

Use one of your sample datasets to insert into your own dataset!



```python Python (SDK)

from relevanceai.datasets import get_sample_ecommerce_dataset
documents = get_sample_ecommerce_dataset()
documents[0]

client.insert_documents(dataset_id="quickstart", docs=documents)


```
```python
```



<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/_assets/RelevanceAI_dataset_dashboard.png?raw=true" alt="See your dataset in the dashboard" />
<figcaption>See your dataset in the dashboard</figcaption>
<figure>


### 3. Encode data and upload vectors into your new dataset

Encode new product image vector using our models out of the box using [Vectorhub's](https://hub.getvectorai.com/) `Clip2Vec` models and update your dataset.



```python Python (SDK)
from vectorhub.bi_encoders.text_image.torch import Clip2Vec
enc = Clip2Vec()

# Set the default encode to encoding an image
enc.encode = enc.encode_image
documents = enc.encode_documents(fields=["product_image"], docs=documents)

client.update_documents(dataset_id="quickstart", docs=documents)

client.datasets.schema(dataset_id="quickstart")
```
```python
```


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/_assets/RelevanceAI_vectors_dashboard.png?raw=true" alt="Monitor your vectors in the dashboard" />
<figcaption>Monitor your vectors in the dashboard</figcaption>
<figure>


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/_assets/RelevanceAI_images_dashboard.png?raw=true" alt="View your dataset in the dashboard" />
<figcaption>View your dataset in the dashboard</figcaption>
<figure>




### 4. Run clustering on your vectors

Run clustering on your vectors to better understand your data. You can view the clusters in our clustering dashboard following the provided link when clustering finishes.



```python Python (SDK)
centroids = client.vector_tools.cluster.kmeans_cluster(
    dataset_id = "quickstart",
    vector_fields = ["product_image_clip_vector_"],
    k = 10
)

client.services.cluster.centroids.list_closest_to_center(
  dataset_id = "quickstart",
  vector_field = "product_image_clip_vector_",
  cluster_ids = [],                 # Leave this as an empty list if you want all of the clusters,
  alias = "kmeans_10"
)
```
```python
```


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/_assets/RelevanceAI_cluster_dashboard.png?raw=true" alt="See what your clusters represent" />
<figcaption>See what your clusters represent</figcaption>
<figure>

You can read more about how to analyse clusters in your data [here](doc:quickstart-k-means).


### 5. Run a vector search

See your search results on the dashboard here https://cloud.relevance.ai/sdk/search.



```python Python (SDK)

query = "xmas gifts"  # query text
query_vec_txt = client.services.encoders.text(text=query)

client.services.search.vector(
	dataset_id = "quickstart",
  multivector_query = [
    {"vector": query_vec_txt["vector"],
     "fields": ["product_image_clip_vector_"]},
  ],
  page_size = 3,
  query = "sample search" # Stored on the dashboard
)

```
```python
```



<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/_assets/RelevanceAI_search_dashboard.png?raw=true"  alt="Visualise your search results" />
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