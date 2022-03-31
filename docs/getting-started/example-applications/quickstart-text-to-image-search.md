---
title: "Text-to-image search (using OpenAI's CLIP Pytorch)"
excerpt: "Get started with Relevance AI in 5 minutes!"
slug: "quickstart-text-to-image-search"
hidden: false
---


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/getting-started/example-applications/_assets/RelevanceAI_text_to_image.gif?raw=true"
     alt="RelevanceAI Text to Image"
     style="width: 100% vertical-align: middle"/>
<figcaption>
<a href="https://cloud.relevance.ai/demo/search/image-to-text">Try the image search live in Relevance AI Dashboard</a>
</figcaption>
<figure>


This section, we will show you how to create and experiment with a powerful text-to-image search engine using OpenAI's CLIP and Relevance AI.


**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/_assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs/getting-started/example-applications/_notebooks/RelevanceAI-ReadMe-Text-to-Image-Search.ipynb)


### What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)


### Installation Requirements

Prior to starting, let's install the main dependencies. This installation provides you with what you need to connect to Relevance AI's API, read/write data, make different searches, etc.


[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==2.0.0",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]

This will give you access to Relevance AI's Python SDK.

### Setting Up Client

To instantiate a Relevance AI's client object, you need an API key that you can get from [https://cloud.relevance.ai/](https://cloud.relevance.ai/).



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


## Steps to create text to image search with CLIP

To be able to perform text-to-image search, we will show you how to:

1. Get sample data
2. Vectorize the data
3. Insert into your dataset
4. Search your dataset


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/getting-started/example-applications/_assets/RelevanceAI_search_steps.png?raw=true" width="650" alt="Steps to search" />
<figcaption>Steps to search</figcaption>
<figure>


### 1. Data

Here, we use our sample e-commerce dataset and preview one of the documents.

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

An example document should have a structure that looks like this:

[block:code]
{
  "codes": [
    {
      "code": "{'_id': '711160239',\n  'product_image': 'https://thumbs4.ebaystatic.com/d/l225/pict/321567405391_1.jpg',\n  'product_link': 'https://www.ebay.com/itm/20-36-Mens-Silver-Stainless-Steel-Braided-Wheat-Chain-Necklace-Jewelry-3-4-5-6MM-/321567405391?pt=LH_DefaultDomain_0&var=&hash=item4adee9354f',\n  'product_price': '$7.99 to $12.99',\n  'product_title': '20-36Mens Silver Stainless Steel Braided Wheat Chain Necklace Jewelry 3/4/5/6MM\"',\n  'query': 'steel necklace',\n  'source': 'eBay'\n}",
      "name": "JSON",
      "language": "json"
    }
  ]
}
[/block]


As you can see each data entry contains both text (`product_title`) and image (`product_image`).


### 2. Encode

CLIP is a vectorizer from OpenAI that is trained to find similarities between text and image pairs. In the code below we set up and install CLIP.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/getting-started/example-applications/_assets/RelevanceAI_CLIP_contrastive_pretraining.png?raw=true" width="650" alt="Photo of OpenAI's CLIP architecture from OpenAI" />
<figcaption>Photo of OpenAI's CLIP architecture from OpenAI (https://openai.com/blog/clip/)</figcaption>
<figure>


CLIP installation

[block:code]
{
  "codes": [
    {
      "code": "# Clip installation\n!pip install ftfy regex tqdm\n!pip install git+https://github.com/openai/CLIP.git",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]


We instantiate the model and create functions to encode both image and text.


[block:code]
{
  "codes": [
    {
      "code": "import torch\nimport clip\nimport requests\nfrom PIL import Image\n\ndevice = \"cuda\" if torch.cuda.is_available() else \"cpu\"\nmodel, preprocess = clip.load(\"ViT-B/32\", device=device)\n\n# First - let's encode the image based on CLIP\ndef encode_image(image):\n    # Let us download the image and then preprocess it\n    image = preprocess(Image.open(requests.get(image, stream=True).raw)).unsqueeze(0).to(device)\n    # We then feed our processed image through the neural net to get a vector\n    with torch.no_grad():\n      image_features = model.encode_image(image)\n    # Lastly we convert it to a list so that we can send it through the SDK\n    return image_features.tolist()[0]\n\n# Next - let's encode text based on CLIP\ndef encode_text(text):\n    # let us get text and then tokenize it\n    text = clip.tokenize([text]).to(device)\n    # We then feed our processed text through the neural net to get a vector\n    with torch.no_grad():\n        text_features = model.encode_text(text)\n    return text_features.tolist()[0]",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


We then encode the data.


> 🚧 Skip encoding and insert, as we have already encoded the data into vectors for you!
>
> Skip if you don't want to wait and re-encode the data as the e-commerce dataset already includes vectors.


[block:code]
{
  "codes": [
    {
      "code": "def encode_image_document(d):\n  try:\n    d['product_image_clip_vector_'] = encode_image(d['product_image'])\n  except:\n    pass\n\n# Let's import TQDM for a nice progress bar!\nfrom tqdm.auto import tqdm\n[encode_image_document(d) for d in tqdm(documents)]",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### 3. Insert

Lets insert documents into the dataset `quickstart_clip`.


[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset(\"quickstart_clip\")\nds.insert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Once we have inserted the data into the dataset, we can visit [RelevanceAI dashboard](https://cloud.relevance.ai/dataset/quickstart_clip/dashboard/monitor/vectors). The dashboard gives us a great overview of our dataset as shown below.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/getting-started/example-applications/_assets/RelevanceAI_quickstart_clip_dashboard.png?raw=true" width="650" alt="RelevanceAI Dashboard" />
<figcaption>Relevance AI dashboard</figcaption>
<figure>


### 4. Search

Lets first encode our text search query to vectors using CLIP.

[block:code]
{
  "codes": [
    {
      "code": "query = 'for my baby daughter'\nquery_vector = encode_text(query)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


Now, let us try out a query using a simple vector search against our dataset.

[block:code]
{
  "codes": [
    {
      "code": "multivector_query=[\n    { \"vector\": query_vector, \"fields\": [\"product_image_clip_vector_\"]}\n]\nresults = ds.vector_search(\n    multivector_query=multivector_query,\n    page_size=5\n)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Here our query is just a simple multi-vector query, but our search comes with out of the box support for features such as multi-vector, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multivector query with those features [here](vector-search-prerequisites).

Next, we use `show_json` to visualize images and text easily and quickly!


[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import show_json\n\nprint('=== QUERY === ')\nprint(query)\n\nprint('=== RESULTS ===')\nshow_json(results, image_fields=[\"product_image\"], text_fields=[\"product_title\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/getting-started/example-applications/_assets/RelevanceAI_text_image_search_results.png?raw=true" width="650" alt="Text Image Search Results" />
<figcaption>Text Image Search Results</figcaption>
<figure>



**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/_assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs/getting-started/example-applications/_notebooks/RelevanceAI-ReadMe-Text-to-Image-Search.ipynb)

## Final Code



[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n\"\"\"\nYou can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api\nOnce you have signed up, click on the value under `Activation token` and paste it here\n\"\"\"\nclient = Client()\nfrom relevanceai.datasets import get_ecommerce_dataset_encoded\n\ndocuments = get_ecommerce_dataset_encoded()\n{k:v for k, v in documents[0].items() if '_vector_' not in k}\nimport torch\nimport clip\nimport requests\nfrom PIL import Image\n\ndevice = \"cuda\" if torch.cuda.is_available() else \"cpu\"\nmodel, preprocess = clip.load(\"ViT-B/32\", device=device)\n\n# First - let's encode the image based on CLIP\ndef encode_image(image):\n    # Let us download the image and then preprocess it\n    image = preprocess(Image.open(requests.get(image, stream=True).raw)).unsqueeze(0).to(device)\n    # We then feed our processed image through the neural net to get a vector\n    with torch.no_grad():\n      image_features = model.encode_image(image)\n    # Lastly we convert it to a list so that we can send it through the SDK\n    return image_features.tolist()[0]\n\n# Next - let's encode text based on CLIP\ndef encode_text(text):\n    # let us get text and then tokenize it\n    text = clip.tokenize([text]).to(device)\n    # We then feed our processed text through the neural net to get a vector\n    with torch.no_grad():\n        text_features = model.encode_text(text)\n    return text_features.tolist()[0]\ndef encode_image_document(d):\n  try:\n    d['product_image_clip_vector_'] = encode_image(d['product_image])\n  except:\n    pass\n\n# Let's import TQDM for a nice progress bar!\nfrom tqdm.auto import tqdm\n[encode_image_document(d) for d in tqdm(documents)]\nds = client.Dataset(\"quickstart_clip\")\nds.insert_documents(documents)\nquery = 'for my baby daughter'\nquery_vector = encode_text(query)\nmultivector_query=[\n    { \"vector\": query_vector, \"fields\": [\"product_image_clip_vector_\"]}\n]\nresults = ds.vector_search(\n    multivector_query=multivector_query,\n    page_size=5\n)\nfrom relevanceai import show_json\n\nprint('=== QUERY === ')\nprint(query)\n\nprint('=== RESULTS ===')\nshow_json(results, image_fields=[\"product_image\"], text_fields=[\"product_title\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


In this page, we saw a quick start to text-to-image search. Following this guide, we will explain how to conduct a search using multiple vectors!
