---
title: "Basics"
slug: "visualise-your-vectors-in-3d"
excerpt: "Visualize your vectors in 3D in 1 line of code after inserting data into Relevance AI platform"
hidden: true
createdAt: "2021-11-24T03:34:58.170Z"
updatedAt: "2021-11-24T14:02:55.439Z"
---
This quickstart shows how easy it is to get started and use Relevance AI to visualize, interpret and diagnose your vectors in just a few lines of code. Visit guides and use-cases for more in-depth tutorials and explanations for how to work with vectors with Relevance AI.
[block:html]
{
  "html": "<div>\n<img src=\"https://media.giphy.com/media/Gd0K0jxNnJOdZ2i4Jn/source.gif\" \n     alt=\"RelevanceAI Visualisation\"\n     style=\"width: 100% vertical-align: middle\"/> \n</div>\n\n<style></style>\n\n"
}
[/block]
You can find a reproducible [Colab notebook here](https://colab.research.google.com/drive/1nTP4Lb89IFIqyG-nSM_UNa27lyyiiHkL?usp=sharing).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nTP4Lb89IFIqyG-nSM_UNa27lyyiiHkL?usp=sharing)

### What I Need
You can get both your project and API key by running this tutorial
- Project
- API Key
- Python 3
- Relevance AI Installed [Installation guide](https://docs.relevance.ai/docs)

Prior to starting, let's install the main dependencies.
[block:code]
{
  "codes": [
    {
      "code": "pip install -U -q RelevanceAI[notebook]",
      "language": "shell",
      "name": "Shell"
    }
  ]
}
[/block]
This will give you access to Relevance AI's Python SDK.

## Setting Up Relevance AI Client
[block:code]
{
  "codes": [
    {
      "code": "from relevanceai.datasets import get_ecommerce_2_dataset\nfrom relevanceai import Client\n\ndocuments = get_ecommerce_2_dataset()\n\nclient = Client()\nclient.insert_documents(\"ecommerce\", documents)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
## Simple projection

Once you instantiate the client, choose a `dataset_id` from your collections (`ecommerce` in the code snippet above) and select the `vector_field` you'd like to project and visualize. A `vector_field` is any vectorized field with `_vector_` in its name; you can get a quick summary of the dataset by running `client.datasets.health(dataset_id)`.

By default, the projector will plot all available points, but if you find rendering slow, simply use the `number_of_points_to_render` parameter to set a smaller value.
[block:code]
{
  "codes": [
    {
      "code": "dataset_id = \"ecommerce\"\nvector_label = \"product_title\"\nvector_field = \"product_image_clip_vector_\"\n\n# Retrieve docs in dataset  set `number_of_points_to_render = None` to retrieve all docs\n# If `vector_label` None, shows markers only and throws a warning\n# Default dim reduction is 'pca' with default args above\n\nclient.projector.plot(\n    dataset_id=dataset_id,\n    vector_field=vector_field,\n    number_of_points_to_render=1000\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:html]
{
  "html": "<img src=\"https://media.giphy.com/media/8AXvtwHmgAj9Xvxe0V/source.gif\" \n     alt=\"RelevanceAI Visualisation\"\n     style=\"width: 100% vertical-align: middle\"/> \n</div>\n"
}
[/block]