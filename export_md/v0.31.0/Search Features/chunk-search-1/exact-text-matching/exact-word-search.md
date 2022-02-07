---
title: "Exact text matching"
slug: "exact-word-search"
excerpt: "Exact word matching"
hidden: false
createdAt: "2021-11-21T06:18:23.815Z"
updatedAt: "2022-01-27T05:19:58.484Z"
---
## Traditional search (exact word matching)
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5a47237-traditional.png",
        "traditional.png",
        1930,
        974,
        "#e8e8e6"
      ],
      "caption": "Traditional search results for query \"HP DV6-20\""
    }
  ]
}
[/block]
### Concept
This search looks for the closest answer (most relevant data entry) via **exact word matching**.  Therefore, the best use case for the traditional search is when the search result is required to include an exact term within the query string.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Laa19J1QdWpjY2j35J1zgY9V6EPVKCSg?usp=sharing)

### Sample use-cases
- Searching for reference numbers, IDs, or specific words such as the name of a brand (e.g. Nike, Sony)
- Searching for specific filenames

### Sample code
Sample codes using Relevance AI SDK for traditional search endpoint are shown below. Note that to be able to use this search endpoint you need to:
1. install Relevance AI's python SDK (for more information please visit the [installation](https://docs.relevance.ai/docs/installation) page).
[block:code]
{
  "codes": [
    {
      "code": "pip install RelevanceAI==0.27.0",
      "language": "shell"
    }
  ]
}
[/block]
2. Instantiate a client object to be able to use the services provided by Relevance AI:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client \n\n\"\"\"\nRunning this cell will provide you with \nthe link to sign up/login page where you can find your credentials.\nOnce you have signed up, click on the value under `Authorization token` \nin the API tab\nand paste it in the appreared Auth token box below\n\"\"\"\n\nclient = Client()",
      "language": "python"
    }
  ]
}
[/block]
3. Upload a dataset under your account (for more information please visit the guide on [datasets](https://docs.relevance.ai/docs/project-and-dataset)). Here, we use our eCommerce sample.
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.datasets import get_dummy_ecommerce_dataset\n\ndocuments = get_dummy_ecommerce_dataset()\n\nDATASET_ID = 'quickstart_search'\nclient.datasets.delete(DATASET_ID)\nclient.insert_documents(dataset_id=DATASET_ID, docs=documents)",
      "language": "python"
    }
  ]
}
[/block]
4. Hit the traditional search endpoint as shown below:
[block:code]
{
  "codes": [
    {
      "code": "# query text\nquery = \"HP 2.4GHz\"\nFIELD = \"product_title\"\n\ntraditional_search = client.services.search.traditional(\n    # dataset name\n    dataset_id=DATASET_ID,\n    \n    # the search query\n    text=query,\n    \n    # text fields in the database against which to match the query\n    fields=[FIELD],\n    \n    # number of returned results\n    page_size=5,\n)",
      "language": "python",
      "name": "Python(SDK)"
    }
  ]
}
[/block]
This search is quick and easy to implement. It works very well in the aforementioned use-cases but cannot offer any semantic search. This is because the model has no idea of semantic relations; for instance, the relation between  "puppy" and "dog", or "sparky" and "electrician" is completely unknown to the model. An instance of a failed search is presented in the screenshot below, where the word "puppies" was searched but the closest returned match is "puppet", even though the database includes many entries about dogs and pets.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7236eff-Screen_Shot_2021-11-18_at_10.59.19_am.png",
        "Screen Shot 2021-11-18 at 10.59.19 am.png",
        1924,
        500,
        "#e9e9e6"
      ],
      "caption": "Sample search result where the traditional search fails due to lack of semantic information."
    }
  ]
}
[/block]