---
title: "How to vectorize text using VectorHub - Transformers"
slug: "how-to-vectorize-text-using-vectorhub-transformers"
excerpt: "A guide on vectorizing text using Vectorhub"
hidden: false
createdAt: "2022-01-20T01:23:22.178Z"
updatedAt: "2022-01-24T00:15:14.549Z"
---
## Using VectorHub

[VectorHub](https://github.com/RelevanceAI/vectorhub) provides users with access to various state of the art encoders to vectorize different data types such as text or image. It manages the encoding process as well, allowing users to focus on the data they want to encode rather than the actual model behind the scene.
On this page, we introduce sentence-transformer based text encoders.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/general-features/how-to-vectorize/_notebooks/RelevanceAI_ReadMe_How_to_Vectorize.ipynb)
### sentence-transformers
First, `sentence-transformers` must be installed. Restart the notebook when the installation is finished.

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

Then from the `sentence_transformers` category, we import our desired transformer and specific model; the full list can be accessed [here](https://huggingface.co/sentence-transformers).

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


{
  "codes": [
    {
      "code": "ds.upsert_documents(documents=encoded_documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

### Encoding an entire dataset using df.apply()

The easiest way to update an existing dataset with encoding results is to run `df.apply`. This function fetches all the data-points in a dataset, runs the specified function (i.e. encoding in this case) and writes the result back to the dataset.

For instance, in the sample code below, we use a dataset called `ecommerce_dataset`, and encode the `product_description` field using the `SentenceTransformer2Vec` encoder.

[block:code]
{
  "codes": [
    {
      "code": "ds[\"sentence\"].apply(lambda x: model.encode(x), output_field=\"sentence_vector\")",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]
### Some famous models

#### Encoding using native Transformers


* BERT
Below, we show an example of how to get vectors from the popular [**BERT**](https://huggingface.co/transformers/v3.0.2/model_doc/bert.html) model from HuggingFace Transformers library.

[block:code]
{
  "codes": [
    {
      "code": "import torch\nfrom transformers import AutoTokenizer, AutoModel\n\nmodel_name = \"bert-base-uncased\"\nmodel = AutoModel.from_pretrained(model_name)\ntokenizer = AutoTokenizer.from_pretrained(model_name)\n\ndef vectorize(text):\n return (\n torch.mean(model(**tokenizer(text, return_tensors=\"pt\"))[0], axis=1)\n .detach()\n .tolist()[0]\n )",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

#### Encoding using Vectorhub's Sentence Transformers

Vectorhub helps us to more easily work with models to encode fields in our documents of different modal types.


* CLIP
Below, we show an example of how to get vectors from the popular [**CLIP**](https://huggingface.co/sentence-transformers/clip-ViT-B-32) model from HuggingFace Transformers library.

[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\n\nmodel = SentenceTransformer2Vec('clip-ViT-B-32')\ntext_vector = model.encode(\"I love working with vectors.\")",
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
      "code": "# documents are saved as a list of dictionaries\ndocuments=[{'image_url': 'https://relevance.ai/wp-content/uploads/2021/10/statue-illustration.png'}, {'image_url': 'https://relevance.ai/wp-content/uploads/2021/09/Group-193-1.png'}]\n\n# Encode the images accessible from the URL saved in `image_url` field in a list of documents\ndocs_with_vecs = model.encode_documents([\"image_url\"], documents)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]
