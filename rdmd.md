# ReadMe Markdown CheatSheet

ReadMe has it's own flavour of Markdown to render ReadMe specific components.

See official [docs](https://rdmd.readme.io/docs/getting-started) here for more details.


##  Code Blocks

Add an extra block to show tabbed blocks.
Add tab header next to language syntax.
To show tabbed code blocks, an extra empty code block needs be appended.


```python Python (SDK)
from relevanceai import show_json

show_json(
    results['results'], 
    image_fields=["product_image"], 
    text_fields=["product_title"]
)
```
```python
```
![](./assets/readme_tabbed_code_block.png)


![](./assets/readme_tabbed_code_block_render.png)


See official [docs](https://rdmd.readme.io/docs/callouts) here for more details.


## Callouts

Callouts are rendered by ReadMe's custom CSS depending on your emoji choice.

> 👍 Free for individual use. 100K free requests for commercial use.
> 
> Sign up for your free at https://cloud.relevance.ai/sdk/api, no credit card required! You can view our pricing here at https://relevance.ai/pricing.

eg. 

![](./assets/readme_callouts.png)

![](./assets/readme_callouts_render.png)



Default themes are specified using one of the following emojis. (If you don't like the one we've chosen, you can always switch to the alternate!)

|**Emoji**|**Class**|**Alternate**|
|:-----:|:-----:|:-----:|
|📘.| `.callout_info` |ℹ️ |
|👍	 | `.callout_okay` |  ✅ |
|🚧 | `.callout_warn` |  ⚠️ |
|❗️| `.callout_error` | 🛑 |


See official [docs](https://rdmd.readme.io/docs/callouts) here for more details.


##  Images

Images need to be wrapped in HTML `<figure>` and `<figcaption>` to show the caption below image.

```html
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/Example_applications/_assets/RelevanceAI_quickstart_clip_dashboard.png?raw=true" width="650" alt="RelevanceAI Dashboard" />
<figcaption>Relevance AI dashboard</figcaption>
<figure>

```

![](https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/main/docs/GETTING_STARTED/Example_applications/_assets/RelevanceAI_quickstart_clip_dashboard.png)




