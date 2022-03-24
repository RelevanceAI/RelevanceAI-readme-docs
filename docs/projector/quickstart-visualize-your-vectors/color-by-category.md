---
title: "Color by category"
slug: "color-by-category"
hidden: true
createdAt: "2021-11-24T03:14:17.312Z"
updatedAt: "2021-11-24T10:38:34.989Z"
---
## Projecting Colour Vector Fields

You can further investigate the embeddings by setting the `colour_label` to a field you desire to filter on within your dataset schema.

You can also append additional information you'd like to in the `hover_label`; for instance, extend the `colour_label_char_length` to shorten the number of characters available in the legend.
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
  "html": "<div>\n<img src=\"https://media.giphy.com/media/Gd0K0jxNnJOdZ2i4Jn/source.gif\" \n     alt=\"RelevanceAI Visualisation\"\n     style=\"width: 100% vertical-align: middle\"/> \n</div>\n\n<style></style>\n"
}
[/block]
