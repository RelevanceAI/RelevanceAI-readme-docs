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
```python Python (SDK)
client.projector.plot(
 ### DR Args for vector plot
 dataset_id = dataset_id,
 vector_field = vector_field,
 dr = "pca",
 number_of_points_to_render=100,
 ## Plot rendering options
 vector_label = vector_label,
 vector_label_char_length = 12,
 colour_label = vector_label,
 hover_label = ['product_title']
)
```
```python
```

[block:html]
{
  "html": "<div>\n<img src=\"https://media.giphy.com/media/Gd0K0jxNnJOdZ2i4Jn/source.gif\" \n     alt=\"RelevanceAI Visualisation\"\n     style=\"width: 100% vertical-align: middle\"/> \n</div>\n\n<style></style>\n"
}
[/block]
