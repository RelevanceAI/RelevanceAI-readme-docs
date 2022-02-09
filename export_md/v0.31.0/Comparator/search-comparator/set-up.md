---
title: "Setting up the search comparator"
slug: "set-up"
hidden: true
createdAt: "2021-10-26T02:57:21.260Z"
updatedAt: "2021-12-20T07:38:46.281Z"
---
## Installation and initial setups
Installation, getting an instance of Relevance AI  (to access the database and perform the search), and getting an instance of `search-comparator` is shown in the sample below:
[block:code]
{
  "codes": [
    {
      "code": "pip install -U -q search-comparator RelevanceAI",
      "language": "shell",
      "name": "Shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\nclient = Client()\n\nfrom search_comparator import Comparator\ncomparator = Comparator()",
      "language": "python"
    }
  ]
}
[/block]
## Loading the desired models to compare
These models can be publicly available ones such as Universal Sentence Encoder (USE) and sentence transformer, or models that are trained or fine-tuned locally.
Samples of both cases are shown in the code snippet below:
>>???<< Do we include vectorhub in this guide? What models to use?

[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nvectorizer1 = SentenceTransformer2Vec(\"msmarco-roberta-base-v3\")  # publically availabel online\nvectorizer2 = SentenceTransformer2Vec(\"Path-to-finetune\")         # locally finetuned",
      "language": "python"
    }
  ]
}
[/block]
Note that in the database that is used for search, there should be a corresponding field for all the models. For instance, if running a search against a text field called "description" and when using three different models (vectoriser_1, vectoriser_2, vectoriser_3), the database must have the three corresponding fields such as (`description_vec1_vector_`, `description_vec2_vector_`, `description_vec3_vector_`) which are the vectorized version of the description text produced by each vectorizer/encoder.

## Setting up all the searches
All searches should be defined in the form of a Python function that receives a query text and returns a list of results; for more information, please refer to [complete documentation](https://docs.relevance.ai/docs/better-text-search) on text searches provided by Relevance AI.

In the following code snippet, we have provided 4 search functions using the loaded vectorizers above and under two different text-search endpoints (hybrid search and vector search). The end result would be a comparison between:
    * vector search with `msmarco-roberta-base-v3` as the encoder (vec-search-original)
    * hybrid search with `msmarco-roberta-base-v3` as the encoder (hyb-search-original)
    * vector search with the locally fine-tuned model as the encoder (vec-search-finetuned)
    * vector search with the locally fine-tuned model as the encoder (hyb-search-finetuned)
[block:code]
{
  "codes": [
    {
      "code": "database_name = <database_name>\n\ndef vector_original_encoder(query):\n  vector = vectorizer1.encode(query)\n  return client.services.search.vector(\n      database_name, [{\"vector\": vector, \"fields\": [\"description_vec1_vector_\"]}], page_size=10\n  )['results']\n\ndef hybrid_original_encoder(query):\n  vector = vectorizer1.encode(query)\n  return client.services.search.hybrid(\n      database_name, [{\"vector\": vector, \"fields\": [\"description_vec1_vector_\"], }], page_size=10\n  )['results']\n  \ndef vector_finetuned_encoder(query):\n  vector = vectorizer2.encode(query)\n  return client.services.search.vector(\n      database_name, [{\"vector\": vector, \"fields\": [\"description_vec2_vector_\"]}], page_size=10\n  )['results']\n\ndef hybrid_finetuned_encoder(query):\n  vector = vectorizer2.encode(query)\n  return client.services.search.hybrid(\n      database_name, [{\"vector\": vector, \"fields\": [\"description_vec2_vector_\"], }], page_size=10\n  )['results']",
      "language": "python"
    }
  ]
}
[/block]
## Adding the defined search functions to the search comparator
In this step, we add the search functions to the core of the search comparator so it has access to all the searches. This is for the comparator to be able to run the query and receive all the results.

Adding the four above-mentioned functions with a chosen name for each is shown below:
[block:code]
{
  "codes": [
    {
      "code": "comparator.add_search(vector_original_encoder, \"vec-search-original\")\ncomparator.add_search(hybrid_original_encoder, \"hyb-search-original\")\ncomparator.add_search(vector_finetuned_encoder, \"vec-search-finetuned\")\ncomparator.add_search(hybrid_finetuned_encoder, \"hyb-search-finetuned\")",
      "language": "python"
    }
  ]
}
[/block]