---
title: "Traditional Search"
slug: "better-text-search-with-hybrid"
excerpt: "Exact word matching"
hidden: true
createdAt: "2021-10-21T02:46:57.322Z"
updatedAt: "2022-01-05T10:54:17.911Z"
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
This search looks for the closest answer (most relevant data entry) via **exact word matching**.  Therefore, the best use-case for traditional search is when the search result is required to include an exact term within the query string.

### Sample use-cases
- Searching for reference numbers, IDs, or specific words such as name of a brand (e.g. Nike, Sony)
- Searching for specific filenames

### Sample code
Sample codes using Relevance-AI SDK and Python requests for traditional search endpoint are shown below. Note that as mentioned on the previous page, there is an installation step before using the Python(SDK).
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\ndataset_id = 'ecommerce-demo'\n\nclient = Client()\n\n# query text\nquery = \"HP DV6-20\"\n\ntraditional_search = client.services.search.traditional(\n    # dataset name\n    dataset_id=dataset_id,\n    \n    # the search query\n    text=query,\n    \n    # text fields in the database against which to match the query\n    fields=[\"product_name\"],\n    \n    # number of returned results\n    page_size=5,\n)\n",
      "language": "python",
      "name": "Python (SDK)"
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
