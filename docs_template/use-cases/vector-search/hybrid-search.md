---
title: "Combine traditional and vector"
slug: "hybrid-search"
excerpt: "Guide to using vector search that can combine with traditional keyword matching"
hidden: true
createdAt: "2021-10-28T08:04:03.807Z"
updatedAt: "2022-01-05T10:57:22.425Z"
---
# Vector search with hybrid support
Our vector search comes with out of the box hybrid support that combines vector search and keyword matching. This allows for full control over the adjustment between word matching and semantic similarity via a weighting parameter.

By combining traditional text search with semantic search into one search bar. You can get the best of both vector and keyword search. For example vector search is usually weak out of vocabulary queries such as ID search (searching for "Product JI36D").

Instantiating the client object:
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n# getting the SDK client object\nclient = Client()",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Encoding the query:
[block:code]
{
  "codes": [
    {
      "code": "dataset_id = <dataset_id>\n\nquery = \"white shoes\"\nquery_vec = client.services.encoders.multi_text(text=query)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Hybrid search:
[block:code]
{
  "codes": [
    {
      "code": "hybrid_search = client.services.search.hybrid(\n    # dataset name\n    dataset_id=dataset_id,\n\n    multivector_query=[\n        {\n            \"vector\": query_vec[\"vector\"],\n\n            # list of vector fields against which to run the query\n            \"fields\": [\"descriptiontextmulti_vector_\"],\n        }\n    ],\n\n    # query text\n    text=query,\n\n    # text fields against which to match the query\n    fields=[\"description\"],\n\n    # number of returned results\n    page_size=5,\n  \n\t \t# weight assigned to word matching    \n    traditional_weight=0.075\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
The three parameters we will discuss separately are `traditional_weight`, included `fields` under vector search, and the weight of each vector under `multivector_query`.

### Traditional weight
This parameter identifies how much emphasis is on keyword matching. The query example includes two words, "shoes" and "white". The word "shoes" is conceptually close to other words such as "sneakers", "boots", "sandals" and the word "white" is conceptually close to other words such as "cream". These concepts are embedded in vector relations, meaning if the traditional weight is set to a small value as in the example code all these conceptual relations are considered.

The screenshot below presents a real search result. Note that the database we ran these searches on does not include many entries about white shoes. Also, we only present 25 samples here which obviously contain closer matches containing "white" and "shoes". However, as you can see there are entries such as "Chazer" (a footwear brand) and "FAUSTO Sneakers" that appear in the search without any overlapping words with the query and merely due to the capability of vector search in identifying similar concepts.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8759c45-ea2a797-hybrid-tr0.075.png",
        "ea2a797-hybrid-tr0.075.png",
        430,
        609,
        "#f2f2f2"
      ],
      "caption": "Sample result of the hybrid search endpoint when traditional weight is small; query = \"white shoes\"."
    }
  ]
}
[/block]
But if traditional_weight is increased to a high value like 0.8, the focus will be on the two words rather than the concept. You can see a real sample result in the following screenshot. Even though there is overlap with the previous search results, you can see answers like "Chazer" is moved further down in the list.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/eadc4cd-4a8c4fa-hybrid-tr0.99.png",
        "4a8c4fa-hybrid-tr0.99.png",
        419,
        591,
        "#f2f2f2"
      ],
      "caption": "Sample result of the hybrid search endpoint when traditional weight is large; query = \"white shoes\"."
    }
  ]
}
[/block]
### Fields
In the previous example, we used the `description` field as well as the `description_vector_` to perform the search.
However, there are many other possibilities when using vectors. For instance, in the next example, the text matching step is done against `product_name` while two vector fields `descriptiontextmulti_vector_` and  `product_nametextmulti_vector_` are used for vector comparison.
[block:code]
{
  "codes": [
    {
      "code": "query = \"white shoes\"\nquery_vec = client.services.encoders.multi_text(text=query)\n\nhybrid_search = client.services.search.hybrid(\n    # dataset name\n    dataset_id=dataset_id,\n\n    multivector_query=[\n        {\n            \"vector\": query_vec[\"vector\"],\n\n            # list of vector fields against which to run the query\n            \"fields\": [\"descriptiontextmulti_vector_\", \"product_nametextmulti_vector_\"],\n        }\n    ],\n\n    # query text\n    text=query,\n\n    # text fields against which to match the query\n    fields=[\"product_name\"],\n\n    # number of returned results\n    page_size=5,\n    \n  \t\n\t\t# weight assigned to word matching\n    traditional_weight=0.075\n)",
      "language": "python",
      "name": "Python(SDK)"
    },
    {
      "code": "import requests\n\ndataset_id = <dataset_id>\ncredentials = project + \":\" + api_key\nurl = \"https://gateway-api-aueast.relevance.ai/v1/\"\n\nvectorising_endpoint = \"services/encoders/text\"\nquery_vec = requests.get(\n    url + vectorising_endpoint,\n    headers={\"Authorization\": credentials},\n    params={\"text\": query},\n).json()\n\n# weight assigned to word matching\nif len(query.split()) > 2:\n    traditional_weight = 0\nelse:\n    traditional_weight = 0.075\n\nquery = \"white shoes\"\nhybrid_endpoint = \"services/search/hybrid\"\nhybrid_search = requests.post(\n    url + hybrid_endpoint,\n    headers={\"Authorization\": credentials},\n    json={\n        # dataset name\n        \"dataset_id\": dataset_id,\n\n        # query text\n        \"text\": query,\n\n        # text fields against which to match the query\n        \"fields\": [\"description\"],\n\n        \"multivector_query\": [\n            {\n                \"vector\": query_vec[\"vector\"],\n                # list of vector fields against which to run the query\n                \"fields\": [\"descriptiontextmulti_vector_\", \"product_nametextmulti_vector_\"],\n            }\n        ],\n        \n        # number of returned results\n        \"page_size\": 5,\n\n        \"traditional_weight\": traditional_weight,\n    },\n).json()\n",
      "language": "python",
      "name": "Python(requests)"
    }
  ]
}
[/block]
Real results are shown in the following table. We can see different results, showing how different vectors can bring more options to search output.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7f785bd-8e1e686-hybrid-mix-simp.png",
        "8e1e686-hybrid-mix-simp.png",
        425,
        607,
        "#f2f2f2"
      ],
      "caption": "Sample result of the hybrid search endpoint when traditional weight is small and different fields are used for search; query = \"white shoes\"."
    }
  ]
}
[/block]
### Adding weight to vector fields
To add more importance to one/some vector fields, it is possible to use weights for them in the setup. A sample code with the produced results is shown below.
[block:code]
{
  "codes": [
    {
      "code": "query = \"white shoes\"\nquery_vec = client.services.encoders.multi_text(text=query)\n\nhybrid_search = client.services.search.hybrid(\n    # dataset name\n    dataset_id=dataset_id,\n\n    multivector_query=[\n        # assigning a weight og 0.15 to descriptiontextmulti_vector_\n        {\n            \"vector\": query_vec[\"vector\"],\n            \"fields\": {\"descriptiontextmulti_vector_\":0.15},\n        },\n        # assigning a weight og 0.70 to product_nametextmulti_vector_\n        {\n            \"vector\": query_vec[\"vector\"],\n            \"fields\": {\"product_nametextmulti_vector_\":0.70},\n        }\n    ],\n\n    # query text\n    text=query,\n\n    # text fields against which to match the query\n    fields=[\"product_name\"],\n\n    # number of returned results\n    page_size=5,\n    \n\t  # weight assigned to word matching\n    traditional_weight=0.075\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f837674-13107d6-hybrid-mix-weight.png",
        "13107d6-hybrid-mix-weight.png",
        417,
        606,
        "#f2f2f2"
      ],
      "caption": "Sample result of the hybrid search endpoint when traditional weight is small and different fields with weights are used for search; query = \"white shoes\"."
    }
  ]
}
[/block]