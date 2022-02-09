---
title: "Waiting for the encoding to end"
slug: "waiting-for-the-encoding-to-end"
excerpt: "Encoding requires some time to finish, in the meantime..."
hidden: true
createdAt: "2021-11-08T22:12:52.358Z"
updatedAt: "2022-01-20T05:04:32.597Z"
---
In the past few pages, we learnt about several famous and very useful encoders for text and image and how to update our dataset with vectors. Before we can start using these vectors for tasks such as search, recommendation or clustering, we must make sure the encoding process is finished; this is particularly important for large datasets.

## Checking health status

The `monitor.health` API call is probably one of the most important endpoints at your disposal for debugging purposes. Once you have started the encoding process on the dataset, it might take a while for the task to finish. Especially if the dataset is large or many fields are specified for encoding.
The `monitor.health` endpoint reports what fields exist in the whole dataset, how many documents include those fields and how many are missing the fields (i.e. every single document is checked separately). It can be accessed through the [dashboard](https://cloud.relevance.ai/dataset/) or via the Python SDK.


### Checking if the encoding is finished via the `monitor.health` API call
First, we need to install Relevance AI's Python SDK and then instantiate a client object:
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
Making the API call
[block:code]
{
  "codes": [
    {
      "code": "DATASET_ID = <name of the dataset>\n\nclient.datasets.health(DATASET_ID)",
      "language": "python",
      "name": "Pyhton (SDK)"
    }
  ]
}
[/block]
The output is similar to the json result shown below.
All existing fields in our eCommerce dataset are listed with two components for each field `missing` and  `exists`. Looking at the numbers under `description_text2vec_vector_` indicates that the encoding has just begun since only 120 documents include the vector.
While vectorizing is in progress, the missing and existing numbers keep changing for the vector fields due to the fact that more documents receive their vectors.
[block:code]
{
  "codes": [
    {
      "code": "{'description': {'missing': 0, 'exists': 19920},\n 'description_text2vec_vector_': {'missing': 19800, 'exists': 120, 'number_of_documents_with_zero_vectors': 0},\n 'insert_date_': {'missing': 0, 'exists': 19920},\n 'product_name': {'missing': 0, 'exists': 19920},\n 'retail_price': {'missing': 0, 'exists': 19920}}",
      "language": "json"
    }
  ]
}
[/block]
The interpretation of this data is simple, it means that the encoding process has started and has only been completed partially. We will need more time before experimenting with the API.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6d10760-better_search_9.png",
        "better_search_9.png",
        1463,
        653,
        "#e4dfda"
      ]
    }
  ]
}
[/block]