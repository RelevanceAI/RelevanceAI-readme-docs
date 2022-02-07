---
title: "Boilerplate"
slug: "boilerplate"
hidden: true
metadata:
  title: "Boilerplat"
createdAt: "2021-11-08T00:59:35.504Z"
updatedAt: "2021-11-15T05:09:20.240Z"
---
Here, we introduce some code snippets used for the setup; these are repeated in many of our documents.
[block:api-header]
{
  "title": "Long boilerplate for set up"
}
[/block]
### What I Need
* Project and API Key: Grab your RelevanceAI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)
* RelevanceAI Installed - [Installation guide can be found here](docs:introduction-1)

### Installation Requirements

Prior to starting, let's install the main dependencies. This installation provides you with what you need to connect to RelevanceAI API, read / write data, make different searches, etc.
[block:code]
{
  "codes": [
    {
      "code": "! pip install -q RelevanceAI[notebook]",
      "language": "python"
    }
  ]
}
[/block]
### Setting Up Client

After the installation, we need to instantiate a client object to use RelevanceAI API. You can get your API key from RelevanceAI [login page](https://cloud.relevance.ai/) in the settings area!
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\nproject = input(\"Your project here...\")\napi_key = input(\"Your API key here...\")\nclient = Client(project, api_key)",
      "language": "python"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Short boilerplate for set up"
}
[/block]
### What do I need?
* **api_key** and **project** obtained in the [settings page](https://cloud.relevance.ai/settings).

[block:api-header]
{
  "title": "What is Next"
}
[/block]
You need
1- **dataset_id** : name of a dataset stored in Relevance AI. You can find out how to upload a dataset in [Creating a dataset](doc:creating-a-dataset). Alternatively, to get started with the platform, you can use our [ecommerce data](doc:ecommerce-example-dataset).
2- **Vectorizer**: to be able to search in a vector space, the query must match the nature of the space; meaning we need to move from the common data formats like text, image, sound, etc. to vectors. You can find out about different vectorizers in RelevanceAI platform in documentation pages such as [text-to-image search](https://docs.relevance.ai/v0.14.0/docs/quickstart-text-to-image-search) or [better-text-search](https://docs.relevance.ai/v0.14.0/docs/prerequisites-1).