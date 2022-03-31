---
title: "Highlighting"
slug: "highlighting"
excerpt: "Highlight in 1 line of code using JSONShower"
hidden: false
createdAt: "2021-11-22T04:45:41.458Z"
updatedAt: "2022-01-19T04:05:36.764Z"
---
JSONShower supports highlighting in 1 line of code on your documents!

[block:code]
{
  "codes": [
    {
      "code": "from jsonshower import show_json\n\n# This is in the same format as search results\ndocuments = [\n    {\n        \"image_url\": \"https://imgs.xkcd.com/comics/voting.png\",\n    },\n    {\n        \"image_url\": \"https://imgs.xkcd.com/comics/animal_songs.png\",\n    }\n]\n\nshow_json(\n    documents=documents,\n    image_fields=[\"image_url\"],     # Image fields\n    image_width=200,                # Adjust the image width\n)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

After running this, you should see the following in your Jupyter Notebook:
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/general-features/_assets/highlighting.png?raw=true" width="183" alt="highlighting.png" />
<figcaption>Highlight Output</figcaption>
<figure>

