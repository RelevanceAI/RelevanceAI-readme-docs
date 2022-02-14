---
title: "Quick Feature Tour"
excerpt: "Try out RelevanceAI in 5 steps!"
slug: "quick-tour"
hidden: false
createdAt: "2022-01-10T01:31:01.336Z"
updatedAt: "2022-01-10T01:31:01.336Z"
---
Relevance AI is designed and built to help developers to experiment, build and share the best vectors to solve similarity and relevance based problems across the organisation.




<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/_assets/RelevanceAI_DS_Workflow.png?raw=true" alt="Relevance AI DS Workflow" />
<figcaption>How Relevance AI helps with the data science workflow</figcaption>
<figure>



## In 5 short steps, get a shareable dashboard for experiments insight!



Run this Quickstart in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs/GETTING_STARTED/_notebooks/RelevanceAI-ReadMe-Quick-Feature-Tour.ipynb)


### 1. Set up Relevance AI and Vectorhub for Encoding!


@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION; vectorhub_clip_installation @@@

After installation, we need to also set up an API client. If you are missing an API key, you can easily sign up and get your API key from [https://cloud.relevance.ai/](https://cloud.relevance.ai/) in the settings area.


@@@ client_instantiation @@@


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/_assets/RelevanceAI_auth_token_details.png?raw=true" alt="Get your Auth Details" />
<figcaption>Get your Auth Details</figcaption>
<figure>


### 2. Create a dataset and insert data

Use one of your sample datasets to insert into your own dataset!

@@@ get_ecommerce_dataset_clean @@@


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/_assets/RelevanceAI_dataset_dashboard.png?raw=true" alt="See your dataset in the dashboard" />
<figcaption>See your dataset in the dashboard</figcaption>
<figure>

@@@ dataset_basics, DATASET_ID=QUICKSTART_DATASET_ID @@@


### 3. Encode data and upload vectors into your new dataset

Encode new product image vector using our models out of the box using [Vectorhub's](https://hub.getvectorai.com/) `Clip2Vec` models and update your dataset.


@@@ clip2vec_encode_image_documents, IMAGE_VECTOR_FIELDS=['product_image'] @@@


Update the existing dataset with the encoding results and check the results



@@@ upsert_documents; dataset_schema @@@



<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/_assets/RelevanceAI_vectors_dashboard.png?raw=true" alt="Monitor your vectors in the dashboard" />
<figcaption>Monitor your vectors in the dashboard</figcaption>
<figure>


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/_assets/RelevanceAI_images_dashboard.png?raw=true" alt="View your dataset in the dashboard" />
<figcaption>View your dataset in the dashboard</figcaption>
<figure>


### 4. Run clustering on your vectors

Run clustering on your vectors to better understand your data. You can view the clusters in our clustering dashboard following the provided link when clustering finishes.


@@@ auto_cluster, KMEANS=KMEANS-10, VECTOR_FIELD=IMAGE_CLIP_VEC @@@

You can also get a list of documents that are closest to the center of the clusters:

@@@ list_closest_to_center @@@


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/_assets/RelevanceAI_cluster_dashboard.png?raw=true" alt="See what your clusters represent" />
<figcaption>See what your clusters represent</figcaption>
<figure>

You can read more about how to analyse clusters in your data [here](doc:quickstart-k-means).


### 5. Run a vector search

See your search results on the dashboard here https://cloud.relevance.ai/sdk/search.


@@@  model_encode_query, QUERY="gifts for the holidays"; multivector_query, QUERY_VECTOR=query_vector, VECTOR_FIELDS=["product_image_clip_vector_"]; vector_search, MULTIVECTOR_QUERY=multivector_query, PAGE_SIZE=10 @@@

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.0.6/docs_template/_assets/RelevanceAI_search_dashboard.png?raw=true"  alt="Visualise your search results" />
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