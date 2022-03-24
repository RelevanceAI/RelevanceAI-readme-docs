---
title: "Prerequisites"
slug: "better-text-search-prerequisites"
excerpt: "How to build better text search for a variety of different use cases"
hidden: true
createdAt: "2021-11-10T00:51:08.719Z"
updatedAt: "2022-01-05T10:54:04.561Z"
---
[block:api-header]
{
  "title": "Introduction"
}
[/block]

### Three main categories for text search use-cases
1. Pure word matching, pure vector search, or combination of both
     * Traditional search
     * Vector search
     * Hybrid search
     * Semantic search
2. Diversified search results
     * Diversity search
3. Fine-grained search, search on chunks of original text data
     * Chunk search
     * Multistep chunk search
     * Advance chunk search
     * Advanced multistep chunk search

Each of these endpoints is explained separately in the following sub-pages.
[block:api-header]
{
  "title": "What is a text search?"
}
[/block]
Text search is the process of matching a **text** query against the available text data in a dataset, to find the most relevant entries to the query. In Relevance AI, text search can be done using text and/or vectors.

[block:api-header]
{
  "title": "How can vectors help in text search?"
}
[/block]
## What are vectors and vector spaces

Let us imagine each word can be positioned in a 2 or 3-dimensional space; meaning each word can be represented with [x,y,z] coordinates, based on its meaning. This [x,y,z] coordinate is called a vector, and the whole space containing all the words is called a **vector space**. In reality, the number of dimensions is significantly bigger than two or three (for more information visit [What are vectors](doc:what-are-vectors))

### How is a vector space formed?
Vector spaces are formed via machine learning models. A good vector space is one that shows meaningful relationships between words (their vectors). For instance, in a good vector space, it is expected that the data points ([x,y,z]s) representing animals such as "tiger" and "lion" to be closer to each other and far from points representing words like "automobile", "whiteboard" or "Mars".
You can also expect to have similar forms of vector relation (distance, angle, etc.) between data points that are conceptually related. For instance vector relation between ("king", "man") and ("queen", "woman") are expected to be similar.

### Benefits of using vector-space for search

#### Ability to search concepts without explicit thesaurus definitions

Considering how similar concepts are supposed to be closer to each other in a vector space, vector spaces provide us with the ability to search through concepts without the need to have exact word-matching or a pre-written domain-specific thesaurus. For instance, you might make a query using the word "Pendant" in a Jewellery dataset that does not contain the word "Pendant" but has many entries containing the word "Necklace". A text match search fails in this scenario but a concept matching through vector-space can lead to finding the desired item since Necklace and Pendant are conceptually very close ([What are vectors](doc:what-are-vectors))

#### Ability to search to be tailored towards more specific audiences

When users search "tutorials for beginners" and "tutorials for advanced students", results are expected to be more specific for each target audience. Traditional text search will not be able to tell the difference between those two unless the content explicitly states "beginners" or "advanced". Vector search allows you to tailor search towards more specific audiences.

#### And much more...

Once text data is turned into vectors, the vectors can also provide much more capabilities - topic modeling, tagging, clustering - just to name a few.  Text vectors can also be matched with other forms of media such as images and audio - all of which can be inside the same content management system. This may require tweaking for specific content and it may also require a lot of work to be done.

[block:callout]
{
  "type": "info",
  "body": "Vectors are representations of concepts as a list of numbers. Conceptual relations are embedded in vectors in the form of vector algebra which allows us to perform a search within concepts without the need to use explicit words."
}
[/block]

[block:api-header]
{
  "title": "Text search in Relevance AI"
}
[/block]
## What are Relevance AI text search endpoints?
* Traditional search
* Vector search
* Hybrid search
* Semantic search
* Diversity search
* Chunk search
* Multistep chunk search
* Advance chunk search
* Advanced multistep chunk search

## What I need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)
* RelevanceAI Installed - Full installation guide can be found [here](https://docs.relevance.ai/docs/installation) or
simply run the following command to install the main dependencies.
[block:code]
{
  "codes": [
    {
      "code": "!pip install -U RelevanceAI[notebook]",
      "language": "shell"
    }
  ]
}
[/block]
### Data
The dataset that we used for code snippets in this guide is named "ecommerce-search-example" with fields such as `_id`, `retail_price`, `product_name`, `description`, `product_name_imagetext_vector_ `, `description_imagetext_vector_ `, `product_nametextmulti_vector_` and `descriptiontextmulti_vector_`. You can download the data using the code snippet below.
[block:code]
{
  "codes": [
    {
      "code": "\nfrom relevanceai.datasets import get_dummy_ecommerce_dataset\ndocs = get_dummy_ecommerce_dataset()\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
To run any of the search endpoints, you need a dataset under your project. You can use the downloaded e-commerce data or create/upload yours by following our full tutorial on how to [create/upload](https://docs.relevance.ai/docs/creating-a-dataset-prerequisites) a dataset under your project.


### Vectorizer
To be able to search in a vector space, the query must match the nature of the space; meaning we need to turn our text data to vectors.

* How to vectorize a query (i.e. turn a query-text to a query-vector)? Relevance AI provides you with several vectorizing endpoints (#TODO# link to vectorizers); Sample code using Relevance AI SDK and Python requests to use one of the vectorizers is shown below. Note that to use the Python (SDK), Relevance AI must be [installed](https://docs.relevance.ai/docs/installation) first.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nclient = Client()\n\nquery = \"ABC product\"      # query text\nquery_vec = client.services.encoders.multi_text(text = query)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "How to choose the best text-search endpoint?"
}
[/block]
Choosing the best endpoint is highly dependant on the data and what the queries look like. In the subsequent pages, we explain endpoints, their best use-case(s), their pros/cons, followed by a sample code snippet showing how to use each endpoint.
In all provided examples, we consider a database that looks like the table below. All entries have a unique id (`_id`), two text fields (`product_name` and `description`) and the  four vector fields:
* `product_name_default_vector_ ` : vectorized title using a model trained on an English corpus
* `description_default_vector_` : vectorized description using a model trained on an English corpus
* `description_imagetext_vector_` : vectorized description using a model on trained on image and text data
* `txt2vec_chunkvector_`: vectorized chunked description using a model trained on an English corpus
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1bc998d-Screen_Shot_2021-11-16_at_11.51.37_am.png",
        "Screen Shot 2021-11-16 at 11.51.37 am.png",
        1450,
        250,
        "#f2f2f2"
      ],
      "caption": "Schematic view of the ecommerce database."
    }
  ]
}
[/block]