---
title: "Text search (using USE VectorHub)"
slug: "quickstart-text-search"
hidden: false
createdAt: "2021-11-05T06:24:29.236Z"
updatedAt: "2022-01-27T04:58:43.185Z"
---
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/getting-started/example-applications/_assets/RelevanceAI_text_search.png?raw=true"
     alt="RelevanceAI Text to Image"
     style="width: 100% vertical-align: middle"/>
<figcaption>
<a href="https://tfhub.dev/google/universal-sentence-encoder/4">Universal Sentence Encoder encoding process</a>
</figcaption>

<figure>

In this section, we will show you how to create and experiment with a powerful text search engine using Google's Universal Sentence Encoder through [VectorHub library](https://github.com/RelevanceAI/vectorhub) and Relevance AI.

**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/getting-started/example-applications/_notebooks/RelevanceAI_ReadMe_Quickstart_Text_Search.ipynb)


### What I Need
* Project and API Key: Grab your RelevanceAI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)

### Installation Requirements



```bash Bash
# RelevanceAi installation
pip install -U RelevanceAI[notebook]==0.27.0

# Vectorhub installation for quick access to Sentence Transformers
pip install -q vectorhub[encoders-text-tfhub]
```
```bash
```

### Setting Up Client

To be able to use Relevance AI, you need to instantiate a client. This needs a Project and API key that can be accessed at [https://cloud.relevance.ai/](https://cloud.relevance.ai/) in the settings area! Alternatively, you can run the code below and follow the link and the guide.




```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token` in the API tab
and paste it in the Auth token box below
"""

client = Client()
```
```python
```

## Text Search with Universal Sentence Encoder using VectorHub


### 1. Data

For this experiment, we use our sample e-commerce dataset and preview one of the documents.




```python Python (SDK)
from relevanceai.datasets import get_ecommerce_dataset

# Retrieve our sample dataset. - This comes in the form of a list of documents.
documents = get_ecommerce_dataset()

documents[0]
```
```python
```

An example document should have a structure that looks like this.



```json JSON
{
  "_id": "711158459",
  "_unit_id": 711158459,
  "product_description": "The PlayStation 4 system opens the door to an incredible journey through immersive new gaming worlds and a deeply connected gaming community. Step into living, breathing worlds where you are hero of your epic journey. Explore gritty urban environments, vast galactic landscapes, and fantastic historical settings brought to life on an epic scale, without limits. With an astounding launch lineup and over 180 games in development the PS4 system offers more top-tier blockbusters and inventive indie hits than any other next-gen console. The PS4 system is developer inspired, gamer focused. The PS4 system learns how you play and intuitively curates the content you use most often. Fire it up, and your PS4 system points the way to new, amazing experiences you can jump into alone or with friends. Create your own legend using a sophisticated, intuitive network built for gamers. Broadcast your gameplay live and direct to the world, complete with your commentary. Or immortalize your most epic moments and share at the press of a button. Access the best in music, movies, sports and television. PS4 system doesn t require a membership fee to access your digital entertainment subscriptions. You get the full spectrum of entertainment that matters to you on the PS4 system. PlayStation 4: The Best Place to Play The PlayStation 4 system provides dynamic, connected gaming, powerful graphics and speed, intelligent personalization, deeply integrated social capabilities, and innovative second-screen features. Combining unparalleled content, immersive gaming experiences, all of your favorite digital entertainment apps, and PlayStation exclusives, the PS4 system focuses on the gamers.Gamer Focused, Developer InspiredThe PS4 system focuses on the gamer, ensuring that the very best games and the most immersive experiences are possible on the platform.<br>Read more about the PS4 on ebay guides.</br>",
  "product_image": "https://thumbs2.ebaystatic.com/d/l225/m/mzvzEUIknaQclZ801YCY1ew.jpg",
  "product_link": "https://www.ebay.com/itm/Sony-PlayStation-4-PS4-Latest-Model-500-GB-Jet-Black-Console-/321459436277?pt=LH_DefaultDomain_0&hash=item4ad879baf5",
  "product_price": "$329.98 ",
  "product_title": "Sony PlayStation 4 (PS4) (Latest Model)- 500 GB Jet Black Console",
  "query": "playstation 4",
  "rank": 1,
  "relevance": 3.67,
  "relevance:variance": 0.47100000000000003,
  "source": "eBay",
  "url": "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR11.TRC1.A0.H0.Xplant.TRS0&_nkw=playstation%204"
}
```
```json
```

### 2. Encode

Next, we will instantiate the universal sentence encoder from VectorHub and encode the `product_title` field among all documents.



```python Python (SDK)

from vectorhub.encoders.text.tfhub import USE2Vec
enc = USE2Vec()

# We add this function here so that when we encode documents, they are good.
documents = enc.encode_documents(["product_title"], documents)

documents[0].keys()
```
```python
```

We can see that there is now a field called `product_title_use_vector_` in our data.
`_use_vector_` is the name assigned to the model in Vectorhub and we use it when generating vectors.
If you prefer a different name, simply modify the `__name__` attribute via


```python Python (SDK)

enc.__name__ = "model_name_goes_here"documents[0].keys()
```
```python
```

### 3. Insert

The data can be easily uploaded to Relevance AI platform via `insert_documents`. Note that all documents must include an `_id` field containing a unique identifier. Here, we generate such an identifier using the Python `uuid` package.



```python Python (SDK)
import uuid

for d in documents:
  d['_id'] = uuid.uuid4().__str__()    # Each document must have an `_id` field

# Insert the documents into the quickstart-example below.
client.insert_documents("quickstart-example", documents)
documents[0].keys()
```
```python
```

### 3. Search

Note that our dataset includes vectors generated by Universal Sentence Encoder. Therefore, in this step, we first vectorize the query using the same encoder to be able to search among the similarly generated vectors.



```python Python (SDK)
query = "Gift for my son"
query_vector = enc.encode(query)
```
```python
```

Simple vector search against our dataset:



```python Python (SDK)
results = client.services.search.vector(
    # Dataset ID can go here
    dataset_id="quickstart-example",
    # Construct a multivector query here
    # You can read more about how to construct a multivector query here: MULTIVECTOR QUERY GOES HERE
    multivector_query=[
        {
            "vector": query_vector,
            "fields": ["product_title_use_vector_"] # Field to search on
        }
    ],
    page_size=5
)
```
```python
```

We can see the results on the dashboard via the provided link after the search finishes. Or using Relevance AI json_shower as shown below:


```python Python (SDK)
from relevanceai import show_json

show_json(
    results['results'],
    text_fields=["product_title"],
)
```
```python
```

This is just a quick and basic example of using Relevance AI for text search, there are many other search features such as faceted vector search, hybrid search, chunk search, multivector search. For further information please visit [Better text search](doc:better-text-search).