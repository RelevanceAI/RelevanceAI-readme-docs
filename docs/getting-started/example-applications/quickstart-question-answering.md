---
title: "Question answering (using USE QA Tensorflow Hub)"
slug: "quickstart-question-answering"
excerpt: "Get started with Relevance AI in 5 minutes!"
hidden: false
createdAt: "2021-11-05T06:25:12.543Z"
updatedAt: "2022-01-20T05:05:33.448Z"
---
This quickstart shows how easy it is to get started and how to quickly build question-answering applications using Relevance AI in just a few lines of code. Visit the documentation pages on use-cases for more in-depth tutorials and explanations for experimenting with stronger vector search.

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/getting-started/example-applications/_assets/RelevanceAI_question_answering.png?raw=true" width="650" alt="Vector Spaces" />
<figcaption></figcaption>

<figure>

For each application, we demonstrate the ease of
* encoding data,
* indexing the data
* vector search

to build powerful applications

**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/getting-started/example-applications/_notebooks/RelevanceAI-ReadMe-Question-Answering-using-USE-QA-Tensorflow-Hub.ipynb)

### What I Need
* Project and API Key: Grab your RelevanceAI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)

### Installation Requirements

Prior to starting, we need to install the main dependencies.
[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==2.0.0\n# remove `!` if running the line in a terminal\n!pip install vectorhub[encoders-text-tfhub]",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]

### Setting Up Client
To be able to use Relevance AI, you need to instantiate a client. This needs a Project and API key that can be accessed at https://cloud.relevance.ai/ in the settings area! Alternatively, you can run the code below and follow the link and the guide.

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


For this guide, we use our sample ecommerce dataset as shown below:


[block:code]
{
  "codes": [
    {
      "code": "import pandas as pd\nfrom relevanceai.utils.datasets import get_ecommerce_dataset_clean\n\n# Retrieve our sample dataset. - This comes in the form of a list of documents.\ndocuments = get_ecommerce_dataset_clean()\n\npd.DataFrame.from_dict(documents).head()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

## Question Answering (Using TFHub's Universal Sentence Encoder QA)

Question answering can be a useful application of vector databases particularly for customer support and supporting search for FAQ documents. Here, we show an example of using TFHub's Question Answering Model.

### Data Preparation
First, we will define our encoder functions:

[block:code]
{
  "codes": [
    {
      "code": "import tensorflow as tf\nimport tensorflow_hub as hub\nimport numpy as np\nimport tensorflow_text\n\n# Here we load the model and define how we encode\nmodule = hub.load('https://tfhub.dev/google/universal-sentence-encoder-qa/3')\n\n# First we define how we encode the queries\ndef encode_query(query: str):\n    return module.signatures['question_encoder'](tf.constant([query]))['outputs'][0].numpy().tolist()\n\n# We then want to define how we encode the answers\ndef encode_answer(answer: str):\n    return module.signatures['response_encoder'](\n        input=tf.constant([answer]),\n        context=tf.constant([answer]))['outputs'][0].numpy().tolist()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Next, we will encode the `product_title` field within our documents:


[block:code]
{
  "codes": [
    {
      "code": "from tqdm.auto import tqdm\n\nfor d in tqdm(documents):\n    d['product_title_use_qa_vector_'] = encode_answer(d['product_title'])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Finally, we can upload the results to a dataset called `quickstart_tfhub_qa` in the Relevance AI platform:

[block:code]
{
  "codes": [
    {
      "code": "ds = client.Dataset(\"quickstart_tfhub_qa\")\nds.insert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


### Search
To be able to search within vectors that are generated by the Universal Sentence Encoder, we need to encode the query with the same vectorizer and then form a vector search as shown below:


[block:code]
{
  "codes": [
    {
      "code": "query = 'What is a good mothers day gift?'\nquery_vector = encode_query(query)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


Forming a multi-vector query and hitting the vector search endpoint:


[block:code]
{
  "codes": [
    {
      "code": "multivector_query=[\n    { \"vector\": query_vector, \"fields\": [\"product_title_use_qa_vector_\"]}\n]\nresults = ds.vector_search(\n    multivector_query=multivector_query,\n    page_size=5\n)",
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
      "code": "from relevanceai import show_json\n\nprint('=== QUERY === ')\nprint(query)\n\nprint('=== RESULTS ===')\nshow_json(results, image_fields=[\"product_image\"], text_fields=[\"product_title\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]



<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/getting-started/example-applications/_assets/RelevanceAI_question_answering_search_results.png?raw=true" width="650" alt="Question Answering Search Results" />
<figcaption>Question Answering Search Results</figcaption>
<figure>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/getting-started/example-applications/_notebooks/RelevanceAI-ReadMe-Question-Answering-using-USE-QA-Tensorflow-Hub.ipynb)

## Final Code


[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n\"\"\"\nYou can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api\nOnce you have signed up, click on the value under `Activation token` and paste it here\n\"\"\"\nclient = Client()\nimport pandas as pd\nfrom relevanceai.utils.datasets import get_ecommerce_dataset_clean\n\n# Retrieve our sample dataset. - This comes in the form of a list of documents.\ndocuments = get_ecommerce_dataset_clean()\n\npd.DataFrame.from_dict(documents).head()\nimport tensorflow as tf\nimport tensorflow_hub as hub\nimport numpy as np\nimport tensorflow_text\n\n# Here we load the model and define how we encode\nmodule = hub.load('https://tfhub.dev/google/universal-sentence-encoder-qa/3')\n\n# First we define how we encode the queries\ndef encode_query(query: str):\n    return module.signatures['question_encoder'](tf.constant([query]))['outputs'][0].numpy().tolist()\n\n# We then want to define how we encode the answers\ndef encode_answer(answer: str):\n    return module.signatures['response_encoder'](\n        input=tf.constant([answer]),\n        context=tf.constant([answer]))['outputs'][0].numpy().tolist()\nfrom tqdm.auto import tqdm\n\nfor d in tqdm(documents):\n    d['product_title_use_qa_vector_'] = encode_answer(d['product_title'])\nds = client.Dataset(\"quickstart_tfhub_qa\")\nds.insert_documents(documents)\nquery = 'What is an expensive gift?'\nquery_vector = encode_query(query)\nmultivector_query=[\n    { \"vector\": query_vector, \"fields\": [\"product_title_use_qa_vector_\"]}\n]\nresults = ds.vector_search(\n    multivector_query=multivector_query,\n    page_size=5\n)\nfrom relevanceai import show_json\n\nprint('=== QUERY === ')\nprint(query)\n\nprint('=== RESULTS ===')\nshow_json(results, image_fields=[\"product_image\"], text_fields=[\"product_title\"])",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

