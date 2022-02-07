---
title: "Quick Multi-vector search"
slug: "quick-multi-vector-search"
hidden: false
createdAt: "2022-01-28T03:42:25.682Z"
updatedAt: "2022-01-28T05:00:41.076Z"
---
Multi-vector search means
- Vector search with multiple models (e.g. searching with a `text` vectorizer and an `image` vectorizer)
- Vector search across multiple fields (e.g. searching across `title` and `description` with different weightings)

Both of these can be combined to offer a powerful, flexible search.
[block:callout]
{
  "type": "info",
  "body": "Multi-vector search offers a more powerful and more flexible search by combining several vectors across different fields and vectorizers, allowing us to experiment with more combinations of models and configurations.",
  "title": "Multi vector search allows us to combine multiple vectors and vector spaces!"
}
[/block]
The below code snippet shows how easy it is to set up a multi-vector search under Relevance AI's platform:
3 different models, and hitting the intended search endpoint; in the next pages we explain more about the encoders and the dataset.
[block:code]
{
  "codes": [
    {
      "code": "query_vec_1 = model1.encode(query)\nquery_vec_2 = model2.encode(query)\nquery_vec_3 = model3.encode(query)\n\nhybrid_search = client.services.search.hybrid(\n\t\t# dataset name\n  \tdataset_id=dataset_id,\n\t\t# fields to use for a vector search\n    multivector_query=[\n        {\n            \"vector\": query_vec_1,\n            \"fields\": [VERTOR_FIELD1],\n        },\n        {\n            \"vector\": query_vec_2,\n            \"fields\": [VERTOR_FIELD2],\n        },\n        {\n            \"vector\": query_vec_3,\n            \"fields\": [VERTOR_FIELD3],\n        }\n    ],\n    # number of returned results\n    page_size=5,\n)",
      "language": "python"
    }
  ]
}
[/block]