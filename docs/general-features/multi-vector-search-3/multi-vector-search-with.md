---
title: "Multi-vector search with multiple fields"
slug: "multi-vector-search-with"
excerpt: "Guide to using multi-vector search with multiple fields"
hidden: false
createdAt: "2021-12-24T03:13:06.821Z"
updatedAt: "2022-01-19T01:34:16.591Z"
---
Multi-vector search means
- Vector search with multiple models (e.g. searching with a `text` vectorizer and an `image` vectorizer)
- Vector search across multiple vector fields (e.g. searching across `title` and `description` with different weightings)

Both of these can be combined to offer a powerful, flexible search.
> 📘 Multi vector search allows us to combine multiple vectors and vector spaces!
>
> Multi-vector search offers a more powerful and more flexible search by combining several vectors across different fields and vectorizers, allowing us to experiment with more combinations of models and configurations.
## Multi-vector search with multiple models

In this section, we present how to perform search via three sets of vectors:
1. produced by a model trained on pure text data in English (called it **default** in this guide)
2. produced by a model trained on pure text data from a multi-language dataset (called it **textmulti** in this guide)
3. produced by a model trained on combined text and image (called it **imagetext** in this guide).
The models behind them are universal sentence encoder and CLIP, more information can be found on [How to vectorize](doc:vectorize-text).

### Step 1. Vectorizing the dataset
Search via vector type X is possible only if the dataset includes data vectorized by model X. This means if we want to search against fields such as `title` and `description`, we need to vectorize them using the available models (i.e. default, textmulti, and imagetext in our example). Please refer to a full guide on how to [create and upload a database](doc:creating-a-dataset) and how to use vectorizers to update a dataset with vectors at [How to vectorize](doc:vectorize-text).

### Step 2. Vectorizing the query
To make a search against vectors of type X, the query must be of the same type. So, if the plan is to use three models, we need three query vectors corresponding to the three models/vectorizers.

Vectorizing under Relevance AI's platform requires three steps:
1. installation of the related model
2. defining an encoder object
3. vectorizing

 Keep it in mind that, first RelevanceAI must be installed and a client object must be instantiated:

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

See the guide on [How to vectorize](doc:vectorize-text) to learn how to define different vectorizers. Here, we call the encoder/vectorizer `enc`.

And vectorizing your text query.

[block:code]
{
  "codes": [
    {
      "code": "query = \"white sneakers\"\nquery_vec_txt = enc.encode(query)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### Step 3. Vector search
As it was mentioned earlier, Relevance AI has provided you with a variety of vector search endpoints with different use-cases; please see guide pages such as [Better text Search](https://docs.relevance.ai/docs/better-text-search) for more information on each search endpoint.

#### 3.2. Vector search against multiple fields
Another great sample of multivector search in the Relevance AI platform is how multiple vector fields can be used in search, with possibly different importance through weighing. In the example below, we are looking for `white sneakers` in title and description vector fields in an ecommerce dataset. As can be seen the more important field can be identified with a larger weight under the `fields` argument.

[block:code]
{
  "codes": [
    {
      "code": "# Create a multivector query\nmultivector_query=[\n\t{\n\t\t\"vector\": query_vec_txt,\n\t\t\"fields\": {\"title_vector_\":0.6, \"description_vector_\":0.3}},\n\t}\n]",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "DATASET_ID = \"ecommerce-sample-dataset\"\nds = client.Dataset(DATASET_ID)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "results = ds.vector_search(\n    multivector_query=multivector_query,\n    page_size=5\n)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

**Note**: Another great sample of multivector search in the Relevance AI platform is how endpoints such as `advanced_multistep_chunk` combine normal and chunked vectors. For instance, consider many long descriptions on different items where each one includes on average 8 sentences. Only one-tenth of the entries are on footwear and half of the sentences are about material, with a few on leather. `None` related entries can be filtered out via vector search. Then if descriptions are broken into 8 chunks (corresponding to the 8 sentences) a more fine-grained search on leather shoes is possible using [advanced_multistep_chunk](https://docs.relevance.ai/docs/fine-grained-search-search-on-chunks-of-text-data-2) search.

Filtering based on specific features is a great option to perform a more refined search. We will explain Relevance AI's available filtering options on the following page.

