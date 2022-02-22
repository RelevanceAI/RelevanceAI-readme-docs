---
title: "Preview Images"
slug: "image-fields"
excerpt: "View image fields inside image documents easily in JSONShower!"
hidden: false
createdAt: "2021-11-22T04:01:02.046Z"
updatedAt: "2022-01-05T10:49:14.282Z"
---
JSONShower supports previewing images if they can be rendered in HTML. This is achievable in 1 line of code as shown below:
```python Python (SDK)
from jsonshower import show_json

# This is in the same format as search results
documents = [ {
 "image_url": "https://imgs.xkcd.com/comics/voting.png",
 },
 {
 "image_url": "https://imgs.xkcd.com/comics/animal_songs.png",
 }
]

show_json(
 documents=documents,
 image_fields=["image_url"], # Image fields
 image_width=200, # Adjust the image width
)
```
```python
```
After running this, you should see the following in your Jupyter Notebook:
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.2.3/docs_template/GENERAL_FEATURES/_assets/preview_images.png?raw=true" width="278" alt="xkcd_comics.png" />
<figcaption>Example showing images</figcaption>
<figure>
