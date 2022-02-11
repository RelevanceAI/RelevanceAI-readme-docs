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
      "code": "\nfrom jsonshower import show_json\n\n# This is in the same format as search results\ndocuments = [\n    {\n        \"key\": \"This is awesome\",\n        \"value\": \"awesome\",\n    },\n    {\n        \"key\": \"Relevance AI\",\n        \"value\": \"AI\",\n    }\n]\n\nshow_json(\n    documents,\n    highlight_fields={\"key\": [\"value\"]}, \t# Fields to highlight\n    max_l_dist=0, \t\t\t\t\t\t\t\t\t\t\t\t# Parameter for adjusting length of fuzzy matching in backend\n)\n",
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
        "https://files.readme.io/84c254a-highlighting.png",
        "highlighting.png",
        183,
        97,
        "#f4f4f0"
      ],
      "caption": "Highlight Output"
    }
  ]
}
[/block]