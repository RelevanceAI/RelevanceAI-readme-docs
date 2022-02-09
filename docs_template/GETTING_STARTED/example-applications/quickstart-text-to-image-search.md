---
title: "Text-to-image search (using OpenAI's CLIP Pytorch)"
excerpt: "Get started with Relevance AI in 5 minutes!"
slug: "quickstart-text-to-image-search"
hidden: false
---


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-getting-started/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_text_to_image.gif?raw=true"
     alt="RelevanceAI Text to Image"
     style="width: 100% vertical-align: middle"/>
<figcaption>
<a href="https://cloud.relevance.ai/demo/search/image-to-text">Try the image search live in Relevance AI Dashboard</a>
</figcaption>
<figure>


This section, we will show you how to create and experiment with a powerful text-to-image search engine using OpenAI's CLIP and Relevance AI.


**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/_assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-getting-started/docs/GETTING_STARTED/example-applications/_notebooks/RelevanceAI-ReadMe-Text-to-Image-Search.ipynb)


### What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)


### Installation Requirements

Prior to starting, let's install the main dependencies. This installation provides you with what you need to connect to Relevance AI's API, read/write data, make different searches, etc.


@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

This will give you access to Relevance AI's Python SDK.

### Setting Up Client

To instantiate a Relevance AI's client object, you need an API key that you can get from [https://cloud.relevance.ai/](https://cloud.relevance.ai/).



@@@ client_instantiation @@@


## Steps to create text to image search with CLIP

To be able to perform text-to-image search, we will show you how to:

1. Get sample data
2. Vectorize the data
3. Insert into your dataset
4. Search your dataset


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-getting-started/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_search_steps.png?raw=true" width="650" alt="Steps to search" />
<figcaption>Steps to search</figcaption>
<figure>


### 1. Data

Here, we use our sample e-commerce dataset and preview one of the documents.

@@@ get_ecommerce_dataset_clean @@@

An example document should have a structure that looks like this:

@@@ ecommerce_dataset_clean_sample_document@@@


As you can see each data entry contains both text (`product_title`) and image (`product_image`).


### 2. Encode

CLIP is a vectorizer from OpenAI that is trained to find similarities between text and image pairs. In the code below we set up and install CLIP.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-getting-started/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_CLIP_contrastive_pretraining.png?raw=true" width="650" alt="Photo of OpenAI's CLIP architecture from OpenAI" />
<figcaption>Photo of OpenAI's CLIP architecture from OpenAI (https://openai.com/blog/clip/)</figcaption>
<figure>


CLIP installation

@@@ clip_installation @@@


We instantiate the model and create functions to encode both image and text.


@@@ clip_encoding_functions @@@


We then encode the data.


> 🚧 Skip encoding and insert, as we have already encoded the data into vectors for you!
>
> Skip if you don't want to wait and re-encode the data as the e-commerce dataset already includes vectors.


@@@ clip_encode_image_documents, IMAGE_VECTOR='product_image_clip_vector_', IMAGE_FIELD='product_image'  @@@

### 3. Insert

Lets insert documents into the dataset `quickstart_clip`.


@@@ dataset_basics, DATASET_ID=TEXT_IMAGE_SEARCH_DATASET_ID @@@

Once we have inserted the data into the dataset, we can visit [RelevanceAI dashboard](https://cloud.relevance.ai/dataset/quickstart_clip/dashboard/monitor/vectors). The dashboard gives us a great overview of our dataset as shown below.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-getting-started/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_quickstart_clip_dashboard.png?raw=true" width="650" alt="RelevanceAI Dashboard" />
<figcaption>Relevance AI dashboard</figcaption>
<figure>


### 4. Search

Lets first encode our text search query to vectors using CLIP.

@@@ clip_encode_query, QUERY='for my baby daughter' @@@


Now, let us try out a query using a simple vector search against our dataset.

@@@+ multivector_query, VECTOR_FIELD=query_vector, VECTOR_FIELDS=["product_image_clip_vector_"]; vector_search, MULTIVECTOR_QUERY=multivector_query, PAGE_SIZE=5 @@@

Here our query is just a simple multi-vector query, but our search comes with out of the box support for features such as multi-vector, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multivector query with those features [here](vector-search-prerequisites).

Next, we use `show_json` to visualize images and text easily and quickly!


@@@ query_show_json, QUERY='for my baby daughter', IMAGE_FIELDS=["product_image"], TEXT_FIELDS=["product_title"] @@@


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-getting-started/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_text_image_search_results.png?raw=true" width="650" alt="Text Image Search Results" />
<figcaption>Text Image Search Results</figcaption>
<figure>



**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/_assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2-getting-started/docs/GETTING_STARTED/example-applications/_notebooks/RelevanceAI-ReadMe-Text-to-Image-Search.ipynb)

## Final Code



@@@+ client_instantiation; get_ecommerce_dataset_encoded; clip_encoding_functions; clip_encode_image_documents, IMAGE_VECTOR='product_image_clip_vector_', IMAGE_FIELD='product_image; dataset_basics, DATASET_ID=TEXT_IMAGE_SEARCH_DATASET_ID; clip_encode_query, QUERY='for my baby daughter'; multivector_query, VECTOR_FIELD=query_vector, VECTOR_FIELDS=["product_image_clip_vector_"]; vector_search, MULTIVECTOR_QUERY=multivector_query, PAGE_SIZE=5;  query_show_json, QUERY='for my baby daughter', IMAGE_FIELDS=["product_image"], TEXT_FIELDS=["product_title"] @@@


In this page, we saw a quick start to text-to-image search. Following this guide, we will explain how to conduct a search using multiple vectors!