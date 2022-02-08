---
title: "Example application boilerplate"
slug: "quickstart-1"
excerpt: "Get started with Relevance AI in 5 minutes!"
hidden: true
createdAt: "2021-11-09T04:10:49.372Z"
updatedAt: "2021-12-21T07:56:23.936Z"
---
This quickstart shows how easy it is to get started and how to quickly build search applications using Relevance AI in just a few lines of code. Visit guides and use-cases for more in-depth tutorials and explanations to help with experimenting for good vector search.
<figure>
<img src="https://files.readme.io/9be653c-download.png" width="4288" alt="download.png" />
<figcaption>Process of this quickstart</figcaption>
<figure>
For each application, we demonstrate the ease of which we encode data, index and search to build powerful applications.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mAR4VvXxJIhoFLv-9wiS3QHzePver8tQ?usp=sharing)


### What I Need

Grab your project and API key from https://cloud.relevance.ai/ in the settings area and let's get started!

* Project
* API Key
* Python 3 (ideally a Jupyter Notebook/Colab environment)
* Relevance AI Installed - [Installation guide can be found here](docs:introduction-1)

### Installation Requirements

Prior to starting, let's install the main dependencies.
```python Python
%%capture
!pip install -U -q RelevanceAI[notebook]
```
```python
```
First, let us get some datasets! Here, we retrieve our sets and also show what is inside them below.

### Setting Up Client

After we install, we want to also set up the client. If you are missing an API key, grab your API key from https://cloud.relevance.ai/ in the settings area and let's get started!

```python Python
from relevanceai import Client
client = Client()
```
```python
```
## Basic Vector Search

In this section, we show you how to encode data if you have vectors already.

### Data + Encode

Here, we get a dataset that has been encoded already (so we will be skipping the encoding step, but feel free to visit the following quickstarts to see how we encode with a variety of Pytorch/Tensorflow models!)
```python Python
from relevanceai.datasets import get_sample_ecommerce_dataset
import pandas as pd

# Retrieve our sample dataset. - This comes in the form of a list of documents.
docs = get_sample_ecommerce_dataset()
# Preview what is inside each of the datasets - note that the vectors are already stored.
pd.DataFrame.from_dict(docs).head()
```
```python
```

<figure>
<img src="https://files.readme.io/02e4bbc-Screenshot_from_2021-11-06_08-06-11.png" width="1470" alt="Screenshot from 2021-11-06 08-06-11.png" />
<figcaption>Preview of sample e-commerce dataset!</figcaption>
<figure>
### Index

Finally, we insert our data using the `insert_documents` method. Inside this single method call, we automatically handle multi-processing and dataset creation to ensure you can insert your documents as fast as possible!
```python Python
# Now we instantiate our client
client.insert_documents(dataset_id="quickstart_sample", docs=docs)
```
```python
```
After inserting, you can then check your schema and vector health on our dashboard by clicking on the link that the client returns in its output!

<figure>
<img src="https://files.readme.io/d56c769-download.png" width="3638" alt="download.png" />
<figcaption>Screenshot of dashboard</figcaption>
<figure>
### Search

In this section, you will see how to:
- Get a document
- Get the vector from that document
- Create a vector search query
- Display results with images using our `jsonshower`
```python Python
# Let us get a document and its vector
doc = client.datasets.documents.get(dataset_id="quickstart_sample", id="711160239")
vector = doc['document']['product_image_clip_vector_']

# Create a vector query - which is a list of Python dictionaries with the fields "vector" and "fields"
vector_query = [
 {"vector": vector, "fields": ['product_image_clip_vector_']}
]

results = client.services.search.vector(
 dataset_id="quickstart_sample",
 multivector_query=vector_query,
 page_size=5
)

# Useful module for us to see the dataset
from relevanceai import show_json
show_json(results, image_fields=["product_image"], text_fields=["product_title"])
```
```python
```

<figure>
<img src="https://files.readme.io/fc6620f-Screenshot_from_2021-11-06_08-08-28.png" width="796" alt="Screenshot from 2021-11-06 08-08-28.png" />
<figcaption></figcaption>
<figure>
