---
title: "🌱 How to build image to text search using code"
slug: "how-to-build-image-to-text-search-using-code"
excerpt: "A guide on building text to image/image to text search with Relevance AI"
hidden: true
createdAt: "2021-10-20T03:08:30.713Z"
updatedAt: "2021-09-13T06:41:30.913Z"
---
**Assumed Knowledge**: Vectors, Vector Search, Python (Basic level)
**Target Audience**: General Developer, Data Scientist, Python Developer
**Reading Time**: 5 minutes
**Requirements**: Python 3.6 or Python 3.7

To build text to image search, you will need a text to image model. An example of a text to image model is OpenAI's CLIP. You can read more about CLIP as a model [here](https://hub.getvectorai.com/model/text_image%2Fclip).


```python Python (SDK)
!pip install vectorhub[clip]
from vectorhub.bi_encoders.text_image.torch import Clip2Vec
model = Clip2Vec() # This will download and run the model
```
```python
```
To encode the text, you can run the following in Python:

```python Python (SDK)
model.encode_text("This is a dog.")
```
```python
```
To encode images, you can run the following in Python (if you are curious about the encoding process for images, you can read about it here.
