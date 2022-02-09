---
title: "How to vectorize using Relevance AI's SDK"
slug: "how-to-vectorize-using-the-sdk"
excerpt: "A guide on vectorizing text using Vectorhub"
hidden: true
createdAt: "2022-01-19T22:20:35.514Z"
updatedAt: "2022-01-19T23:16:13.152Z"
---
Vectorizing (sometimes referred to as encoding) is the task of turning the input data into a list of numbers (i.e. a vector). This can be done via neural networks trained for specific tasks such as image recognition, question-answering, entailment analysis, ect.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c185d06-vectorizing.png",
        "vectorizing.png",
        442,
        200,
        "#fafafc"
      ],
      "caption": "Vectorizing and image"
    }
  ]
}
[/block]
Vectorizing in Relevance AI can happen directly from the Python SDK or from a second package called VectorHub. On this page, we briefly introduce some of the encoders accessible from the SDK.


## Installation
Relevance AI's Python SDK can be installed via a simple `pip install` command as shown below:
[block:code]
{
  "codes": [
    {
      "code": "pip install RelevanceAI==0.27.0",
      "language": "shell",
      "name": "Bash"
    }
  ]
}
[/block]
Next a client object must be instantiated:
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
Various encoders are accessible under `services.encoders`, such as
* Text encoders:
```
client.services.encoders.text()
client.services.encoders.textimage()
client.services.encoders.multi_text()
```
* Image encoders
```
client.services.encoders.image()
client.services.encoders.imagetext()
```
The difference between the encoders in each category comes from 1) what model (neural network) is behind them and 2) what data is used to train the network. For instance, the model behind `client.services.encoders.text()` is trained on English data whereas the model behind `client.services.encoders.multi_text()` is trained on multiple languages.


The following code snippet shows how easy it is to encode text or image data with these encoders:
[block:code]
{
  "codes": [
    {
      "code": "# input text\nTEXT_TO_ENCODE = \"This is the sample text to encode\"\n\n# encoding text\nvec1 = client.services.encoders.text(TEXT_TO_ENCODE)\nvec2 = client.services.encoders.textimage(TEXT_TO_ENCODE)\nvec3 = client.services.encoders.multi_text(TEXT_TO_ENCODE)\n\n# input image\nIMAGE_TO_ENCODE = <URL OF AN IMAGE SAVED ON THE NET>\nvec4 = client.services.encoders.image(IMAGE_TO_ENCODE)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `pull_update_push`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encode the `description` field using the `multi_text` encoder. Note that the name assigned to a vector field must end in `_vector_`.
[block:code]
{
  "codes": [
    {
      "code": "DATASET_ID = \"ecommerce_dataset\n\n# Take 10 samples of the dataset\nDOC_SAMPLES = client.datasets.documents.list(DATASET_ID, page_size = 10)\n\n# Define an update function\ndef encode_documents(DOC_SAMPLES):\n    for doc in DOC_SAMPLES:\n      doc[\"description_vector_\"] = client.services.encoders.multi_text(doc['description'])\n    return DOC_SAMPLES\n\nclient.pull_update_push(DATASET_ID, encode_documents)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]