---
title: "How to vectorize using Relevance AI's SDK"
slug: "how-to-vectorize-using-the-sdk"
excerpt: "A guide on vectorizing text using Vectorhub"
hidden: true
createdAt: "2022-01-19T22:20:35.514Z"
updatedAt: "2022-01-19T23:16:13.152Z"
---
Vectorizing (sometimes referred to as encoding) is the task of turning the input data into a list of numbers (i.e. a vector). This can be done via neural networks trained for specific tasks such as image recognition, question-answering, entailment analysis, ect.

<figure>
<img src="https://files.readme.io/c185d06-vectorizing.png" width="442" alt="vectorizing.png" />
<figcaption>Vectorizing and image</figcaption>
<figure>
Vectorizing in Relevance AI can happen directly from the Python SDK or from a second package called VectorHub. On this page, we briefly introduce some of the encoders accessible from the SDK.


## Installation
Relevance AI's Python SDK can be installed via a simple `pip install` command as shown below:
```shell Bash
pip install RelevanceAI==0.27.0
```
```shell
```
Next a client object must be instantiated:

```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the appreared Auth token box below
"""

client = Client()
```
```python
```
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
```python Python (SDK)
# input text
TEXT_TO_ENCODE = "This is the sample text to encode"

# encoding text
vec1 = client.services.encoders.text(TEXT_TO_ENCODE)
vec2 = client.services.encoders.textimage(TEXT_TO_ENCODE)
vec3 = client.services.encoders.multi_text(TEXT_TO_ENCODE)

# input image
IMAGE_TO_ENCODE = <URL OF AN IMAGE SAVED ON THE NET>
vec4 = client.services.encoders.image(IMAGE_TO_ENCODE)
```
```python
```
### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `pull_update_push`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encode the `description` field using the `multi_text` encoder. Note that the name assigned to a vector field must end in `_vector_`.
```python Python (SDK)
DATASET_ID = "ecommerce_dataset

# Take 10 samples of the dataset
DOC_SAMPLES = client.datasets.documents.list(DATASET_ID, page_size = 10)

# Define an update function
def encode_documents(DOC_SAMPLES):
 for doc in DOC_SAMPLES:
 doc["description_vector_"] = client.services.encoders.multi_text(doc['description'])
 return DOC_SAMPLES

client.pull_update_push(DATASET_ID, encode_documents)
```
```python
```

