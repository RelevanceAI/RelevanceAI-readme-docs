---
title: "Add labels"
slug: "adding-labels"
hidden: true
createdAt: "2021-11-24T03:19:31.782Z"
updatedAt: "2021-11-24T14:02:44.274Z"
---
## Projecting Text Vector Fields

Once you instantiate the client, choose a `dataset_id` from your collections and select the `vector_field` you'd like to project and visualise. A `vector_field` is any vectorised field with `_vector_` in its name; you can get a quick summary of the dataset by running `client.datasets.health(dataset_id)`.

By default, the projector will plot all available points, but if you find rendering slow, please feel free to set the `number_of_points_to_render`.

[block:code]
{
  "codes": [
    {
      "code": "client.projector.plot(\n    ### DR Args for vector plot\n    dataset_id = dataset_id,\n    vector_field = vector_field,\n    dr = \"pca\",\n    number_of_points_to_render=100,\n    ## Plot rendering options\n    vector_label = vector_label, \n    vector_label_char_length = 12,\n    colour_label = vector_label,\n    hover_label = ['product_title']\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:html]
{
  "html": "<div>\n<img src=\"https://media.giphy.com/media/8AXvtwHmgAj9Xvxe0V/source.gif\" \n     alt=\"RelevanceAI Visualisation\"\n     style=\"width: 100% vertical-align: middle\"/> \n</div>\n\n\n\n<style></style>\n"
}
[/block]