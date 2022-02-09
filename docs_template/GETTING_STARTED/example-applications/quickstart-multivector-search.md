---
title: "Multi-vector search with your own vectors"
excerpt: "Get started with Relevance AI in 5 minutes!"
slug: "quickstart-multivector-search"
hidden: false
---


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs_template/_assets/RelevanceAI_vector_space.png?raw=true" width="650" alt="Vector Spaces" />
<figcaption></figcaption>
<figure>



**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs/GETTING_STARTED/example-applications/_notebooks/RelevanceAI-ReadMe-Multi-Vector-Search.ipynb)



### What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)

### Installation Requirements

Prior to starting, let's install the main dependencies.


@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@


This will give you access to Relevance AI's Python SDK.

### Setting Up Client

After installation, we need to also set up an API client. If you are missing an API key, you can easily sign up and get your API key from [https://cloud.relevance.ai/](https://cloud.relevance.ai/) in the settings area.


@@@ client_instantiation @@@


## Steps to perform multi-vector search

1. Get sample data
2. Vectorize the data
3. Insert into your dataset
4. Search your dataset


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_search_steps.png?raw=true" width="650" alt="Steps to search" />
<figcaption>Steps to search</figcaption>
<figure>


### 1. Data + Encode

Here, we get a dataset that has been already encoded into vectors; so we will be skipping the encoding step in this page, but feel free to visit other pages in our guides, such as [Text-to-image search (using OpenAI's CLIP Pytorch)](doc:quickstart-text-to-image-search), to learn about encoding with a variety of Pytorch/Tensorflow models!)

@@@ get_ecommerce_dataset_encoded @@@

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_ecommerce_dataset_preview.png?raw=true" width="650" alt="E-commerce Dataset Preview" />
<figcaption>E-commerce Dataset Preview</figcaption>
<figure>

### 2. Insert

To insert data to a dataset, you can use the `insert_documents` method.  Note that this step is also already done in our sample dataset.

@@@ dataset_basics, DATASET_ID=MULTI_VECTOR_SEARCH_DATASET_ID @@@

After finalizing the insert task, the client returns a link guiding you to a dashboard to check your schema and vector health!


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_quickstart_multivector_search.png?raw=true" width="650" alt="Relevance AI Dashboard" />
<figcaption>Relevance AI Dashboard</figcaption>
<figure>



### 3. Search

Since this will be using your own vectors, we will skip vectorizing the query and just retrieve a vector from an existing document in the dataset.


Now, let us try out a query using a simple vector search against our dataset.


@@@+ multivector_query_sample_data, IMAGE_VECTOR='product_image_clip_vector_',TEXT_VECTOR='product_title_clip_vector_'; vector_search, MULTIVECTOR_QUERY=multivector_query, PAGE_SIZE=5 @@@

Here our query is just a simple multi vector query, but our search comes with out of the box support for features such as multi-vector, filters, facets and traditional keyword matching to combine with your vector search. You can read more about how to construct a multivector query with those features [here](vector-search-prerequisites).

Now lets show the results with `show_json`.


@@@ multivector_query_show_json, IMAGE_FIELDS=["product_image"], TEXT_FIELDS=["product_title"] @@@

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs_template/GETTING_STARTED/example-applications/_assets/RelevanceAI_multivector_search_results.png?raw=true" width="650" alt="Multi-vector Search Results" />
<figcaption>Multi-vector Search Results</figcaption>
<figure>




**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs/GETTING_STARTED/example-applications/_notebooks/RelevanceAI-ReadMe-Multi-Vector-Search.ipynb)



## Final Code

@@@+ client_instantiation; get_ecommerce_dataset_encoded; dataset_basics, DATASET_ID=MULTI_VECTOR_SEARCH_DATASET_ID; multivector_query_sample_data, IMAGE_VECTOR='product_image_clip_vector_', TEXT_VECTOR='product_title_clip_vector_'; vector_search, MULTIVECTOR_QUERY=multivector_query, PAGE_SIZE=5; multivector_query_show_json, IMAGE_FIELDS=["product_image"], TEXT_FIELDS=["product_title"] @@@

