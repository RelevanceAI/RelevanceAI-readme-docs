---
title: "How to vectorize text using VectorHub - TFhub"
slug: "vectorize-text"
excerpt: "A guide on vectorizing text using Vectorhub"
hidden: false
createdAt: "2021-10-28T09:09:18.680Z"
updatedAt: "2022-01-20T04:15:52.154Z"
---
## Using VectorHub

[VectorHub](https://github.com/RelevanceAI/vectorhub) provides users with access to various state of the art encoders to vectorize different data types such as text or image. It manages the encoding process as well, allowing users to focus on the data they want to encode rather than the actual model behind the scene.
On this page, we introduce some of the text encoders:
* encoders-text-tfhub
* sentence-transformers

### encoders-text-tfhub
First, `vectorhub[encoders-text-tfhub]` must be installed. Restart the notebook when the installation is finished.

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install vectorhub[encoders-text-tfhub]",
      "name": "Bash",
      "language": "bash"
    }
  ]
}
[/block]

Then we import Universal Sentence Encoder (USE) and instantiate an encoder object.

[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.tfhub import USE2Vec\n\nmodel = USE2Vec()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Encoding a single text input via the `encode` function and encoding a specified text field in the whole data (i.e. list of dictionaries) via the `encode_documents` function are shown below.

[block:code]
{
  "codes": [
    {
      "code": "# Encode a single input\nmodel.encode(\"I love working with vectors.\")",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# documents are saved as a list of dictionaries\ndocuments = SAMPLE_DOCUMENTS\n\n# Encode the `\"sentence\"` field in a list of documents\nencoded_documents = model.encode_documents([\"sentence\"], documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


### sentence-transformers
First, `vectorhub[sentence-transformers]` must be installed. Restart the notebook when the installation is finished.

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install vectorhub[sentence-transformers]",
      "name": "Bash",
      "language": "bash"
    }
  ]
}
[/block]

Then we import SentenceTransformers and instantiate an encoder object.

[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nmodel = SentenceTransformer2Vec(\"all-mpnet-base-v2\")",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

Encoding a single text input via the `encode` function and encoding a specified text field in the whole data (i.e. list of dictionaries) via the `encode_documents` function are shown below.

[block:code]
{
  "codes": [
    {
      "code": "# Encode a single input\nmodel.encode(\"I love working with vectors.\")",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# documents are saved as a list of dictionaries\ndocuments = SAMPLE_DOCUMENTS\n\n# Encode the `\"sentence\"` field in a list of documents\nencoded_documents = model.encode_documents([\"sentence\"], documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `df.apply`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encodes the `product_description` field using the `USE2Vec` encoder.
You can see the list of the available list of models for vectorising here using [Vectorhub](https://github.com/RelevanceAI/vectorhub) or feel free to bring your own model(s).


{
  "codes": [
    {
      "code": "ds = client.Dataset('quickstart_example_encoding')\nds.insert_documents(documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "ds[\"product_title\"].apply(lambda x: model.encode(x), output_field=\"product_title_vector_\")",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

