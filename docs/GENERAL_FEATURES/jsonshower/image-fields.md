---
title: "Preview Images"
slug: "image-fields"
excerpt: "View image fields inside image documents easily in JSONShower!"
hidden: false
createdAt: "2021-11-22T04:01:02.046Z"
updatedAt: "2022-01-05T10:49:14.282Z"
---
JSONShower supports previewing images if they can be rendered in HTML. This is achievable in 1 line of code as shown below:
[block:code]
{
  "codes": [
    {
      "code": "from jsonshower import show_json\n\n# This is in the same format as search results\ndocuments = [ {\n        \"image_url\": \"https://imgs.xkcd.com/comics/voting.png\",\n    },\n    {\n        \"image_url\": \"https://imgs.xkcd.com/comics/animal_songs.png\",\n    }\n]\n\nshow_json(\n    documents=documents, \n    image_fields=[\"image_url\"], # Image fields\n    image_width=200, # Adjust the image width\n)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
After running this, you should see the following in your Jupyter Notebook:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9ff260f-xkcd_comics.png",
        "xkcd_comics.png",
        278,
        273,
        "#eaeaea"
      ],
      "caption": "Example showing images"
    }
  ]
}
[/block]
