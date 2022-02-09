---
title: "Combining filters and vector search"
slug: "combining-filters-and-vector-search"
hidden: false
createdAt: "2021-11-25T22:33:06.798Z"
updatedAt: "2022-01-19T05:12:49.766Z"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f819d50-filtervectors.png",
        "filter+vectors.png",
        1014,
        328,
        "#e6e6e6"
      ],
      "caption": "Including filters in a vector search."
    }
  ]
}
[/block]
## Including filters in vector search
Filtering provides you with a subset of a database containing data entities that match the certain criteria set as filters. What if we need to search through this subset? The difficult way is to ingest (save) the subset as a new dataset, then make the search on the new dataset. However, RelevanceAI has provided the filtering option in almost all search endpoints. This makes the whole process much faster and more straightforward.
In the code snippet below we show a hybrid search sample which is done on a subset of a huge database via filtering. In this scenario, the user is looking for white sneakers but only the ones produced after mid-2020 and from two brands Nike and Adidas.

Note that the code below needs
1. Relevance AI's Python SDK to be installed.
2. A dataset named `ecommerce-search-example`
3. Vectorized description saved under the name `descriptiontextmulti_vector_`

Please refer to a full guide on how to [create and upload a database](doc:creating-a-dataset) and how to use vectorizers to update a dataset with vectors at [How to vectorize](doc:vectorize-text).
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\ndataset_id = \"ecommerce-search-example\"\n\nclient = Client()\n\nquery = \"white shoes\"\nquery_vec = client.services.encoders.multi_text(text=query)\n\nfilters = [\n  {\"field\" : 'brand', \n    \"filter_type\" : 'contains', \n    \"condition\":\"==\", \n    \"condition_value\":\"Asian\"},\n  {\"field\": 'insert_date_',\n    \"filter_type\" : 'date', \n    \"condition\":\">=\", \n    \"condition_value\":\"2020-07-01\"}\n ]\n\nhybrid_search = client.services.search.hybrid(\n    # dataset name\n    dataset_id=dataset_id,\n    \n    multivector_query=[\n        {\n            \"vector\": query_vec[\"vector\"],\n           \n            # list of vector fields against which to run the query\n            \"fields\": [\"descriptiontextmulti_vector_\"],\n        }\n    ],\n    \n    # text fields against which to match the query\n    fields=[\"description\"],\n  \n    # applying filters on search\n    filters= filters,\n\n    # query text\n    text=query,\n  \n    # traditional_weight\n    traditional_weight = 0.075,\n    \n    # number of returned results\n    page_size=5,\n)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]