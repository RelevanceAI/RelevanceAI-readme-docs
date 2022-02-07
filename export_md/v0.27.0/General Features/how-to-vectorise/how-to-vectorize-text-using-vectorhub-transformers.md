---
title: "How to vectorize text using VectorHub-Transformers"
slug: "how-to-vectorize-text-using-vectorhub-transformers"
excerpt: "A guide on vectorizing text using Vectorhub"
hidden: false
createdAt: "2022-01-20T01:23:22.178Z"
updatedAt: "2022-01-28T04:39:14.396Z"
---
## Using VectorHub

[VectorHub](https://github.com/RelevanceAI/vectorhub) provides users with access to various state of the art encoders to vectorize different data types such as text or image. It manages the encoding process as well, allowing users to focus on the data they want to encode rather than the actual model behind the scene.
On this page, we introduce sentence-transformer based text encoders.

### sentence-transformers
First, `sentence-transformers` must be installed. Restart the notebook when the installation is finished.
[block:code]
{
  "codes": [
    {
      "code": "pip install vectorhub[sentence-transformers]",
      "language": "shell",
      "name": "Bash"
    }
  ]
}
[/block]
Then from the `sentence_transformers` category, we import our desired transformer and specific model; the full list can be accessed [here](https://huggingface.co/sentence-transformers).

[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nenc = SentenceTransformer2Vec(\"all-mpnet-base-v2\")",
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
      "code": "# Encode a single input\nenc.encode(\"I love working with vectors.\")\n\n# documents are saved as a list of dictionaries\ndocs = [\n  {\n    \"sentence\":\"This is the first sentence.\",\n    \"_id\":1\n  },\n  {\n    \"sentence\":\"This is the second sentence.\",\n    \"_id\":2\n  }\n\n]\n# Encode the `sentence` field in a list of documents\ndocs_with_vectors = enc.encode_documents(['sentence'], docs)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
### Encoding an entire dataset

The easiest way to update an existing dataset with encoding results is to run `pull_update_push`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encode the `product_description` field using the `SentenceTransformer2Vec` encoder.
[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nenc = SentenceTransformer2Vec(\"all-mpnet-base-v2 \")\n\ndef encode_documents(documents):\n    # Field and then the documents go here\n    return enc.encode_documents([\"product_description\"], documents)\n\nclient.pull_update_push(\"ecommerce_dataset\", encode_documents)",
      "language": "python"
    }
  ]
}
[/block]
### Some famous models
* BERT
Below, we show an example of how to get vectors from the popular [**BERT**](https://huggingface.co/transformers/v3.0.2/model_doc/bert.html) model from HuggingFace Transformers library.
[block:code]
{
  "codes": [
    {
      "code": "import torch\nfrom transformers import AutoTokenizer, AutoModel\n\nmodel_name = \"bert-base-uncased\"\nmodel = AutoModel.from_pretrained(model_name)\ntokenizer = AutoTokenizer.from_pretrained(model_name)\n\ndef vectorize(text):\n    return (\n        torch.mean(model(**tokenizer(text, return_tensors=\"pt\"))[0], axis=1)\n        .detach()\n        .tolist()[0]\n    )",
      "language": "python"
    }
  ]
}
[/block]
* CLIP
Below, we show an example of how to get vectors from the popular [**CLIP**](https://huggingface.co/sentence-transformers/clip-ViT-B-32) model from HuggingFace Transformers library.
[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nenc = SentenceTransformer2Vec('clip-ViT-B-32')\nvec = enc.encode(\"I love working with vectors.\")\n",
      "language": "python"
    }
  ]
}
[/block]