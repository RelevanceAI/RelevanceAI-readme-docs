---
title: "Text-to-image search (using OpenAI's CLIP Pytorch)"
excerpt: "Get started with Relevance AI in 5 minutes!"
slug: "quickstart-text-to-image-search"
hidden: false
---


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.3.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_text_to_image.gif?raw=true"
     alt="RelevanceAI Text to Image"
     style="width: 100% vertical-align: middle"/>
<figcaption>
<a href="https://cloud.relevance.ai/demo/search/image-to-text">Try the image search live in Relevance AI Dashboard</a>
</figcaption>
<figure>


This section, we will show you how to create and experiment with a powerful text-to-image search engine using OpenAI's CLIP and Relevance AI.


**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/_assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.3.2/docs/GETTING_STARTED/example-applications/_notebooks/RelevanceAI-ReadMe-Text-to-Image-Search.ipynb)


### What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)


### Installation Requirements

Prior to starting, let's install the main dependencies. This installation provides you with what you need to connect to Relevance AI's API, read/write data, make different searches, etc.


```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==1.3.2
```
```bash
```

This will give you access to Relevance AI's Python SDK.

### Setting Up Client

To instantiate a Relevance AI's client object, you need an API key that you can get from [https://cloud.relevance.ai/](https://cloud.relevance.ai/).



```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Activation token` and paste it here
"""
client = Client()
```
```python
```


## Steps to create text to image search with CLIP

To be able to perform text-to-image search, we will show you how to:

1. Get sample data
2. Vectorize the data
3. Insert into your dataset
4. Search your dataset


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.3.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_search_steps.png?raw=true" width="650" alt="Steps to search" />
<figcaption>Steps to search</figcaption>
<figure>


### 1. Data

Here, we use our sample e-commerce dataset and preview one of the documents.

```python Python (SDK)
import pandas as pd
from relevanceai.datasets import get_ecommerce_dataset_clean

# Retrieve our sample dataset. - This comes in the form of a list of documents.
documents = get_ecommerce_dataset_clean()

pd.DataFrame.from_dict(documents).head()
```
```python
```

An example document should have a structure that looks like this:

```json JSON
{'_id': '711160239',
  'product_image': 'https://thumbs4.ebaystatic.com/d/l225/pict/321567405391_1.jpg',
  'product_link': 'https://www.ebay.com/itm/20-36-Mens-Silver-Stainless-Steel-Braided-Wheat-Chain-Necklace-Jewelry-3-4-5-6MM-/321567405391?pt=LH_DefaultDomain_0&var=&hash=item4adee9354f',
  'product_price': '$7.99 to $12.99',
  'product_title': '20-36Mens Silver Stainless Steel Braided Wheat Chain Necklace Jewelry 3/4/5/6MM"',
  'query': 'steel necklace',
  'source': 'eBay'
}
```
```json
```


As you can see each data entry contains both text (`product_title`) and image (`product_image`).


### 2. Encode

CLIP is a vectorizer from OpenAI that is trained to find similarities between text and image pairs. In the code below we set up and install CLIP.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.3.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_CLIP_contrastive_pretraining.png?raw=true" width="650" alt="Photo of OpenAI's CLIP architecture from OpenAI" />
<figcaption>Photo of OpenAI's CLIP architecture from OpenAI (https://openai.com/blog/clip/)</figcaption>
<figure>


CLIP installation

```bash Bash
# Clip installation
!pip install ftfy regex tqdm
!pip install git+https://github.com/openai/CLIP.git
```
```bash
```


We instantiate the model and create functions to encode both image and text.


```python Python (SDK)
import torch
import clip
import requests
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# First - let's encode the image based on CLIP
def encode_image(image):
    # Let us download the image and then preprocess it
    image = preprocess(Image.open(requests.get(image, stream=True).raw)).unsqueeze(0).to(device)
    # We then feed our processed image through the neural net to get a vector
    with torch.no_grad():
      image_features = model.encode_image(image)
    # Lastly we convert it to a list so that we can send it through the SDK
    return image_features.tolist()[0]

# Next - let's encode text based on CLIP
def encode_text(text):
    # let us get text and then tokenize it
    text = clip.tokenize([text]).to(device)
    # We then feed our processed text through the neural net to get a vector
    with torch.no_grad():
        text_features = model.encode_text(text)
    return text_features.tolist()[0]
```
```python
```


We then encode the data.


> 🚧 Skip encoding and insert, as we have already encoded the data into vectors for you!
>
> Skip if you don't want to wait and re-encode the data as the e-commerce dataset already includes vectors.


```python Python (SDK)
def encode_image_document(d):
  try:
    d['product_image_clip_vector_'] = encode_image(d['product_image'])
  except:
    pass

# Let's import TQDM for a nice progress bar!
from tqdm.auto import tqdm
[encode_image_document(d) for d in tqdm(documents)]
```
```python
```

### 3. Insert

Lets insert documents into the dataset `quickstart_clip`.


```python Python (SDK)
df = client.Dataset("quickstart_clip")
df.insert_documents(documents)
```
```python
```

Once we have inserted the data into the dataset, we can visit [RelevanceAI dashboard](https://cloud.relevance.ai/dataset/quickstart_clip/dashboard/monitor/vectors). The dashboard gives us a great overview of our dataset as shown below.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.3.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_quickstart_clip_dashboard.png?raw=true" width="650" alt="RelevanceAI Dashboard" />
<figcaption>Relevance AI dashboard</figcaption>
<figure>


### 4. Search

Lets first encode our text search query to vectors using CLIP.

```python Python (SDK)
query = 'for my baby daughter'
query_vector = encode_text(query)
```
```python
```


Now, let us try out a query using a simple vector search against our dataset.

```python Python (SDK)
multivector_query=[
        { "vector": query_vector, "fields": ["product_image_clip_vector_"]}
    ]

results = df.vector_search(
    multivector_query=multivector_query,
    page_size=5
)
```
```python
```

Here our query is just a simple multi-vector query, but our search comes with out of the box support for features such as multi-vector, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multivector query with those features [here](vector-search-prerequisites).

Next, we use `show_json` to visualize images and text easily and quickly!


```python Python (SDK)
from relevanceai import show_json

print('=== QUERY === ')
print(query)

print('=== RESULTS ===')
show_json(results, image_fields=["product_image"], text_fields=["product_title"])
```
```python
```


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.3.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_text_image_search_results.png?raw=true" width="650" alt="Text Image Search Results" />
<figcaption>Text Image Search Results</figcaption>
<figure>



**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/_assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.3.2/docs/GETTING_STARTED/example-applications/_notebooks/RelevanceAI-ReadMe-Text-to-Image-Search.ipynb)

## Final Code



```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Activation token` and paste it here
"""
client = Client()

from relevanceai.datasets import get_ecommerce_dataset_encoded

documents = get_ecommerce_dataset_encoded()
{k:v for k, v in documents[0].items() if '_vector_' not in k}

import torch
import clip
import requests
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# First - let's encode the image based on CLIP
def encode_image(image):
    # Let us download the image and then preprocess it
    image = preprocess(Image.open(requests.get(image, stream=True).raw)).unsqueeze(0).to(device)
    # We then feed our processed image through the neural net to get a vector
    with torch.no_grad():
      image_features = model.encode_image(image)
    # Lastly we convert it to a list so that we can send it through the SDK
    return image_features.tolist()[0]

# Next - let's encode text based on CLIP
def encode_text(text):
    # let us get text and then tokenize it
    text = clip.tokenize([text]).to(device)
    # We then feed our processed text through the neural net to get a vector
    with torch.no_grad():
        text_features = model.encode_text(text)
    return text_features.tolist()[0]

def encode_image_document(d):
  try:
    d['product_image_clip_vector_'] = encode_image(d['product_image])
  except:
    pass

# Let's import TQDM for a nice progress bar!
from tqdm.auto import tqdm
[encode_image_document(d) for d in tqdm(documents)]

df = client.Dataset("quickstart_clip")
df.insert_documents(documents)

query = 'for my baby daughter'
query_vector = encode_text(query)

multivector_query=[
        { "vector": query_vector, "fields": ["product_image_clip_vector_"]}
    ]

results = df.vector_search(
    multivector_query=multivector_query,
    page_size=5
)

from relevanceai import show_json

print('=== QUERY === ')
print(query)

print('=== RESULTS ===')
show_json(results, image_fields=["product_image"], text_fields=["product_title"])
```
```python
```


In this page, we saw a quick start to text-to-image search. Following this guide, we will explain how to conduct a search using multiple vectors!
