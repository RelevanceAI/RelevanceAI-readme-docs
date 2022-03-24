---
title: "Example application boilerplate"
slug: "quickstart-1"
excerpt: "Get started with Relevance AI in 5 minutes!"
hidden: true
createdAt: "2021-11-09T04:10:49.372Z"
updatedAt: "2021-12-21T07:56:23.936Z"
---
This quickstart shows how easy it is to get started and how to quickly build search applications using Relevance AI in just a few lines of code. Visit guides and use-cases for more in-depth tutorials and explanations to help with experimenting for good vector search.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9be653c-download.png",
        "download.png",
        4288,
        1128,
        "#ebedf4"
      ],
      "caption": "Process of this quickstart"
    }
  ]
}
[/block]
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
[block:code]
{
  "codes": [
    {
      "code": "%%capture\n!pip install -U -q RelevanceAI[notebook]",
      "language": "python",
      "name": "Python"
    }
  ]
}
[/block]
First, let us get some datasets! Here, we retrieve our sets and also show what is inside them below.

### Setting Up Client

After we install, we want to also set up the client. If you are missing an API key, grab your API key from https://cloud.relevance.ai/ in the settings area and let's get started!

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\nclient = Client()",
      "language": "python",
      "name": "Python"
    }
  ]
}
[/block]
## Basic Vector Search

In this section, we show you how to encode data if you have vectors already.

### Data + Encode

Here, we get a dataset that has been encoded already (so we will be skipping the encoding step, but feel free to visit the following quickstarts to see how we encode with a variety of Pytorch/Tensorflow models!)
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.datasets import get_sample_ecommerce_dataset\nimport pandas as pd\n\n# Retrieve our sample dataset. - This comes in the form of a list of documents.\ndocs = get_sample_ecommerce_dataset()\n# Preview what is inside each of the datasets - note that the vectors are already stored.\npd.DataFrame.from_dict(docs).head()",
      "language": "python",
      "name": "Python"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/02e4bbc-Screenshot_from_2021-11-06_08-06-11.png",
        "Screenshot from 2021-11-06 08-06-11.png",
        1470,
        187,
        "#eaeaea"
      ],
      "caption": "Preview of sample e-commerce dataset!"
    }
  ]
}
[/block]
### Index

Finally, we insert our data using the `insert_documents` method. Inside this single method call, we automatically handle multi-processing and dataset creation to ensure you can insert your documents as fast as possible!
[block:code]
{
  "codes": [
    {
      "code": "# Now we instantiate our client\nclient.insert_documents(dataset_id=\"quickstart_sample\", docs=docs)",
      "language": "python",
      "name": "Python"
    }
  ]
}
[/block]
After inserting, you can then check your schema and vector health on our dashboard by clicking on the link that the client returns in its output!

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d56c769-download.png",
        "download.png",
        3638,
        1858,
        "#f9fafd"
      ],
      "caption": "Screenshot of dashboard"
    }
  ]
}
[/block]
### Search

In this section, you will see how to:
- Get a document
- Get the vector from that document
- Create a vector search query
- Display results with images using our `jsonshower`
[block:code]
{
  "codes": [
    {
      "code": "# Let us get a document and its vector \ndoc = client.datasets.documents.get(dataset_id=\"quickstart_sample\", id=\"711160239\")\nvector = doc['document']['product_image_clip_vector_']\n\n# Create a vector query - which is a list of Python dictionaries with the fields \"vector\" and \"fields\"\nvector_query = [\n    {\"vector\": vector, \"fields\": ['product_image_clip_vector_']}\n]\n\nresults = client.services.search.vector(\n    dataset_id=\"quickstart_sample\", \n    multivector_query=vector_query,\n    page_size=5\n)\n\n# Useful module for us to see the dataset\nfrom relevanceai import show_json\nshow_json(results, image_fields=[\"product_image\"], text_fields=[\"product_title\"])",
      "language": "python",
      "name": "Python"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fc6620f-Screenshot_from_2021-11-06_08-08-28.png",
        "Screenshot from 2021-11-06 08-08-28.png",
        796,
        424,
        "#f4f4f4"
      ]
    }
  ]
}
[/block]
