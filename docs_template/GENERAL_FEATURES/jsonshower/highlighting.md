---
title: "Highlighting"
slug: "highlighting"
excerpt: "Highlight in 1 line of code using JSONShower"
hidden: false
createdAt: "2021-11-22T04:45:41.458Z"
updatedAt: "2022-01-19T04:05:36.764Z"
---
JSONShower supports highlighting in 1 line of code on your documents!
```python Python (SDK)

from jsonshower import show_json

# This is in the same format as search results
documents = [
 {
 "key": "This is awesome",
 "value": "awesome",
 },
 {
 "key": "Relevance AI",
 "value": "AI",
 }
]

show_json(
 documents,
 highlight_fields={"key": ["value"]}, 	# Fields to highlight
 max_l_dist=0, 												# Parameter for adjusting length of fuzzy matching in backend
)

```
```python
```
After running this, you should see the following in your Jupyter Notebook:
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.33.2/docs_template/GENERAL_FEATURES/_assets/highlighting.png?raw=true" width="183" alt="highlighting.png" />
<figcaption>Highlight Output</figcaption>
<figure>
