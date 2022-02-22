---
title: "Experimentation workflow with e-commerce text search"
slug: "nlp-search-with-e-commerce"
hidden: false
createdAt: "2021-10-28T08:22:45.636Z"
updatedAt: "2022-01-05T11:00:11.035Z"
---
# Experimentation Workflow

Here, we provide an example of comparing 2 different embeddings and how we can configure them to get the best search possible.

The contents of this guide will be:

1) Set up encoders and identify key searches to test out.
2) Vectorizing the title and description of each product with `Universal Sentence Encoder` and comparing it to `Bert-based SentenceTransformers`
3) Comparing the performance of 2 encoders. Here, we will compare `Universal Sentence Encoder` with `BERT Embeddings
4) Determine which configuration works the best for our queries.
## What do I need to follow this guide?
Grab your project and API key from https://cloud.relevance.ai/ in the settings area and let's get started!

- Project Name
- API-key
- Dataset in Relevance AI
- Python 3.6+
- Jupyter Notebook environment

## Set Up
```python Python (SDK)

# Install the requirements
!pip install -q -U RelevanceAI
!pip install -q vectorhub[encoders-text-sentence-transformers, encoders-text-tfhub]

```
```python
```
Once you set it up, we will then instantiate the 2 encoders we are going to compare:
```python Python (SDK)

from vectorhub.encoders.text.tfhub import USE2Vec
use = USE2Vec()

from vectorhub.bi_encoders.text_image.torch import Clip2Vec
clip = Clip2Vec()


```
```python
```
## Client Set Up
```python Python (SDK)

from relevanceai import Client
client = Client()

```
```python
```
## Get the Dataset
```python Python (SDK)

from relevanceai.datasets import get_ecommerce_dataset
docs = get_ecommerce_dataset()

```
```python
```
From this list of queries, we now investigate 4 queries that we are looking to test:
- 2.4GHz PC mouse
- ST2000DM001
- gifts for my daughter
- gifts for my son with cashback

## Vectorizing
In this section, we will assign the `_id` of the document and then encode them and insert into a dataset called `ecommerce-experiments`.
```python Python (SDK)
for d in docs:
 d['_id'] = str(d['_unit_id'])

docs = [{k:v for k, v in doc.items() if not isinstance(v, list) and not pd.isna(v)} for doc in docs]

encoded_docs = use.encode_documents(["product_title"], docs)

client.insert_documents("ecommerce-experiments", encoded_docs)

```
```python
```
Afterwards, let us check that this has been properly encoded by looking at the schema as follows.
```python Python (SDK)

client.datasets.schema("ecommerce-experiments")

```
```python
```
This is expected to return:
```json
{'_unit_id': 'numeric',
 'insert_date_': 'date',
 'product_description': 'text',
 'product_image': 'text',
 'product_link': 'text',
 'product_price': 'text',
 'product_title': 'text',
 'product_title_use_vector_': {'vector': 512},
 'query': 'text',
 'rank': 'numeric',
 'relevance': 'numeric',
 'relevance:variance': 'numeric',
 'source': 'text',
 'url': 'text'}
```
```json
```

## Testing Universal Sentence Encoder
Now let us begin testing our search performance on the given dataset with a few different queries.  We will begin with a simple vector search. You can read more about vector search here at the ![Vector Search API reference](https://docs.relevance.ai/reference/vector_search_api_services_search_vector_post).
```python Python (SDK)
query = "2.4GHz PC mouse"
results = client.services.search.vector(
	"ecommerce-experiments",
	[{"vector": use.encode(query), "fields": ["product_title_use_vector_"]}]
)

# We can quickly look at our results by calling this:
[r['product_title'] for r in results['results']]
```
```python
```
This should give us something similar to this:
```python Python (SDK)

['2.4GHz Cordless Wireless Optical Mouse Mice for Laptop PC Computer+USB Receiver',
 '2.4 GHz Wireless Optical Mouse Mice + USB 2.0 Receiver for PC Laptop Black',
 'Black 2.4GHz Wireless Optical Mouse Mice+USB 2.0 Receiver For Laptop Desktop PC',
 '2015 new Black 2.4GHz Wireless Optical Mouse/Mice + USB Receiver for PC Laptop',
 'Dual Ports PS2 II Controller Console to PC USB Game Converter Adapter',
 'IBM ThinkPad LENOVO T61 LAPTOP 2.0 GHz 2GB 80 GB 14.1 WIN 7 64bit CDRW/DVD WiFi"',
 'IBM LENOVO THINKPAD T410 LAPTOP WIN 7 PRO 32bit DVDRW i5 2.4 ghz 250 gb 3gb WiFi',
 'PS1 PS2 PSX to PC USB Dual Controller Adapter Converter',
 'Classic Wired Game Controller Remote Pro Gamepad Shock For Nintendo Wii SY',
 'Controller Guitar adapter USB converter for PS2 to PS3',
 'Universal USB Microphone for PS2, PS3, Xbox 360 , PC, Wii',
 'For PS1 PS2 PSX Playstation 2 Joypad Game Controller to PC USB Converter Adapter',
 'New high qualtiy PS1 PS2 PSX to PC USB CONTROLLER ADAPTER CONVERTER SY',
 'White Classic Pro Controller for Nintendo Wii Remote',
 'D-Link DIR-657 300 Mbps 4-Port Gigabit Wireless N Router Hd Media Router 1000',
 'IBM LENOVO THINKPAD T420 LAPTOP i5 2.50ghz 8GB 320GB DVDRW Windows 7 PRO WEBCAM',
 'Sony PlayStation 4 500GB Console with 2 Controllers',
 'Oster OGG3701 Microwave 0.7 cu. ft. 700 Watts Countertop Microwave Oven OGG3701',
 'Oster OGZB1101 Countertop Microwave Oven 1000 Watts 1.1 cu ft',
 'Brand New Controller for Nintendo GameCube or Wii -- PLATINUM']
```
```python
```
Great! Looks like the results are pretty good. Now let's try something a bit more specific with more emphasis on targetting a specific item by which we know the item ID..
```python Python (SDK)
query = "ST2000DM001"
results = client.services.search.vector(
 "ecommerce-experiments",
 [{
 "vector": use.encode(query),
 "fields": ["product_title_use_vector_"]
 }])
[r['product_title'] for r in results['results']]
```
```python
```
This should return to us something similar to this:
```json
['Oster OGH6901 0.9 cu. ft. 900 Watts Countertop Microwave Oven OGH6901',
 'Oster OGZB1101 Countertop Microwave Oven 1000 Watts 1.1 cu ft',
 '120ML Ultrasonic Aroma Oil Diffuser Humidifier LED Color Changing Air Purifier',
 'Oster OGG3701 Microwave 0.7 cu. ft. 700 Watts Countertop Microwave Oven OGG3701',
 'Manual Coffee Grinder Hand-Crank Mill NEW',
 'Panasonic ARC4 ES-RF31-s Rechargeable Electric Shaver Wet/dry 4 Nanotech Blade',
 '6pcs Teenage Mutant Ninja Turtles Action Figures Classic Collection Toys Set Boy',
 'Ultrasonic Aroma Humidifier Air Diffuser Purifier Color Changing Rainbow LED',
 'Panasonic Arc3 ES 8103S Wet/Dry Rechargeable Shaver (A491)',
 'Presto 6-Quart Aluminum Pressure Cooker 01264, New, Free Shipping',
 "Panasonic ES8243A E Arc4 Men's Electric Shaver Wet/Dry",
 'Quick Change Key Trigger Acoustic Electric Folk Guitar Tune Capo Clamp',
 '500ML Aroma Diffuser Atomizer Air Humidifier LED Ultrasonic Purifier Lonizer',
 'Cuisinart DCC 3000 Coffee on Demand 12 Cup Programmable Coffeemaker',
 'Stand Ride Sit Double Baby Infant Toddler Child Walk Outdoor Stroller Maternity',
 'Whitening Cream100g Face & Body Lightening Moisturizers +[Free Gift] Facial Mask',
 'Shark SV1106 Navigator Cordless Upright Vacuum Dirt Cleaner Bagless Canister Pet',
 '2.4GHz Cordless Wireless Optical Mouse Mice for Laptop PC Computer+USB Receiver',
 'Panasonic ES8243A Arc4 Electric Shaver Wet/Dry (missing cleaning brush)',
 'NEW Microphones Mic XBOX PS3 PS2 Wii PC Rock Band Guitar Hero Karaoke']
```
```json
```
Unfortunately - this is one of the weaknesses of vector search - sometimes the vectors themselves are not great because dense representations can be quite limiting.
> 📘 Vectors can sometimes underperform without exact match boosting.
>
> While vectors generally perform well in semantic search applications, they sometimes fail at exact text matching. Vector search, unfortunately, is not a superset of traditional search. It is merely an alternative. Read on below to see how we tackle this problem with **hybrid search**.

## Hybrid Search

While the previous results were okay - it's strange that `ST2000DM001` doesn't immediately dominate the top search results. For that - we might want to combine traditional search with vector search such that if the title contains the same words as the query - it gets boosted up.

First - let us do a quick check of what is *expected* to be at the top via traditional search. You can read about the traditional search endpoint [here](https://docs.relevance.ai/reference/traditional_search_api_services_search_traditional_post) if you are unfaimilar.

We can do so by firstly performing an exact text search to see what search results we should be expecting:
```python Python (SDK)
results = client.services.search.traditional(
 "ecommerce-experiments",
 text="ST2000DM001",
 fields=["product_title"]
 )['results']
results[['product_title', "_search_score"]]
```
```python
```
You should see the screenshot below:
<figure>
<img src="https://files.readme.io/f7841b7-Capture.PNG" width="821" alt="Capture.PNG" />
<figcaption></figcaption>
<figure>
So there appears to be 3 results. While the top result exactly matches the query - the rest do not. Why is that? The rest of the results are just the ones closest in regards to Levishtein distance, which can be set using the edit_distance parameter in Hybrid search (we have it defaulted to -1 for automatic conversion.


```python Python (SDK)
query = "ST2000DM001"
results = client.services.search.hybrid(
 "ecommerce-experiments",
 multivector_query=[{
 "vector": use.encode(query),
 "fields": ["product_title_use_vector_"]
 }],
 text=query,
 fields=["product_title"], # NEW FIELD FOR HYBRID SEARCH
 traditional_weight=0.025, # NEW FIELD FOR TRADITIONAL WEIGHTING
 edit_distance=-1, # NEW FIELD FOR LEVISHTEIN DISTANCE
)

[r['product_title'] for r in results['results']]

# Expected result

['Lot of 2 Seagate ST2000DM001 2TB SATA disks',
 'Seagate ST2000DX001 2 TB 3.5 Internal Hybrid Hard Drive"',
 'Samsung Seagate Momentus SpinPoint ST2000LM003 2 TB 2.5 SATA Notebook PS4 HDD"',
 'Oster OGH6901 0.9 cu. ft. 900 Watts Countertop Microwave Oven OGH6901',
 'Oster OGZB1101 Countertop Microwave Oven 1000 Watts 1.1 cu ft',
 '120ML Ultrasonic Aroma Oil Diffuser Humidifier LED Color Changing Air Purifier',
 'Oster OGG3701 Microwave 0.7 cu. ft. 700 Watts Countertop Microwave Oven OGG3701',
 'Manual Coffee Grinder Hand-Crank Mill NEW',
 'Panasonic ARC4 ES-RF31-s Rechargeable Electric Shaver Wet/dry 4 Nanotech Blade',
 '6pcs Teenage Mutant Ninja Turtles Action Figures Classic Collection Toys Set Boy',
 'Ultrasonic Aroma Humidifier Air Diffuser Purifier Color Changing Rainbow LED',
 'Panasonic Arc3 ES 8103S Wet/Dry Rechargeable Shaver (A491)',
 'Presto 6-Quart Aluminum Pressure Cooker 01264, New, Free Shipping',
 "Panasonic ES8243A E Arc4 Men's Electric Shaver Wet/Dry",
 'Quick Change Key Trigger Acoustic Electric Folk Guitar Tune Capo Clamp',
 '500ML Aroma Diffuser Atomizer Air Humidifier LED Ultrasonic Purifier Lonizer',
 'Cuisinart DCC 3000 Coffee on Demand 12 Cup Programmable Coffeemaker',
 'Stand Ride Sit Double Baby Infant Toddler Child Walk Outdoor Stroller Maternity',
 'Whitening Cream100g Face & Body Lightening Moisturizers +[Free Gift] Facial Mask',
 'Shark SV1106 Navigator Cordless Upright Vacuum Dirt Cleaner Bagless Canister Pet']
```
```python
```
This is more like it! By combining with traditional search - we are able to get the bost of both worlds.
Now - while items are great, sometimes, we want to be able to also search on the content of the actual product - we will take a look into how we do that next.

## Combining with product descriptions
While we can search titles just fine, we may want to also search for content inside the product description. So let us build this.

We begin by defining how we want to display the results as such:
```python Python (SDK)
def show_results(results, fields_to_show=["title", "content"]):
 return pd.DataFrame(results['results'])[fields_to_show]
```
```python
```
This is a helpful function to allow us to visualise the results.

## Clean and encode product descriptions
Here, we encode content - here we show you how to combine both searches and the easiest way to clean and encode your dataset. In this section, we will:

1) Clean the HTML from product descriptions.
2) Encode the documents
3) Get our documents, edit them locally and push them back via the pull_update_push functionality.
```python Python (SDK)
# The easiest way to encode content
from io import StringIO
import unicodedata
from html.parser import HTMLParser

class MLStripper(HTMLParser):
 """Remove HTML from the code and retrieves data.
 """
 def __init__(self):
 super().__init__()
 self.reset()
 self.strict = False
 self.convert_charrefs= True
 self.text = StringIO()

 def handle_data(self, d):
 self.text.write(d)

 def get_data(self):
 return self.text.getvalue()

def clean_html(html):
 """Cleans HTML from text."""
 s = MLStripper()
 html = unicodedata.normalize("NFKD", html).replace("\r", "").replace("\t", " ").replace("\n", " ")
 s.feed(html)
 return s.get_data()


def encode_content(docs: list):
 """
encode_content takes in a list of documents
 """
 for d in docs:
 d['product_description_clean'] = clean_html(d['product_description'])
 return use.encode_documents(["product_description_clean"], docs)

# Pull update push takes in a Python callable and automatically
# loops through your dataset with automatic logging and progress bar!
client.pull_update_push("ecommerce-experiments", encode_content)
```
```python
```

> 📘 pull_update_push is a very useful function built to accelerate idea testing
>
> Under the hood, pull_update_push retrieves a set of documents, runs the function that you stored against it and then updates them accordingly - allowing us to focus on writing good functionality and logs the errors.

Now let us see what these results look like when we include description with them.
```python Python (SDK)
query = "gifts for my daughter"
results = client.services.search.hybrid(
 "ecommerce-experiments",
 multivector_query=[{
 "vector": use.encode(query),
 "fields": [
 	"product_title_use_vector_",
 "product_description_clean_use_vector_" # UPDATED to include descriptions
 ],
 }],
 text=query,
 fields=["product_title"],
 traditional_weight=0.025,
 edit_distance=-1,
)

pd.DataFrame(results['results'])[['product_title', "product_description_clean"]]
```
```python
```
Attached below is a screenshot of what the results look like below.
<figure>
<img src="https://files.readme.io/39d8648-Capture.PNG" width="1436" alt="Capture.PNG" />
<figcaption></figcaption>
<figure>
These results look better! Looking at the content, we can start testing some interesting queries to see what they return. For example, we may want to test `gifts for my son with cashback` using the code below. It is useful to note that only rarely does the title ever mention "cashback" but this can occur quite often in the actual product description. A code snippet is shown below:
```python Python (SDK)
query = "gifts for my son with cashback"
results = client.services.search.hybrid(
 "ecommerce-experiments",
 multivector_query=[{
 "vector": use.encode(query),
 "fields": {
 "product_title_use_vector_": 0.5,
 "product_description_clean_use_vector_": 0.5 # UPDATED: Included product descriptions
 }
 }],
 text=query,
 fields=["product_title",],
 traditional_weight=0.025,
 edit_distance=-1,
 page_size=5
)
pd.set_option('display.max_colwidth', 20000)
pd.DataFrame(results['results'])[['product_title', "product_description_clean"]]
```
```python
```
The results should look something like this:
<figure>
<img src="https://files.readme.io/4556670-Capture.PNG" width="1466" alt="Capture.PNG" />
<figcaption></figcaption>
<figure>
From the above we can see that while there are gifts for sons (playstations, clocks, games), the results can definitely still be better. However - none of them seem to offer cashback. However, there were still results floated up mentioning cashback was an option if users wanted them.

We may now want to improve our vector search through 2 main ways.
- **Improve via chunking.** The content has a lot of sentences. We might want to break down each content section into smaller sentences and perform search on each of them (thus allowing more specific stuff like cashback to come up earlier). This can be really useful if we want more fine-grained control over our search results.
- **Improve via asymmetric search models** We may want to rely on these models that support searching with short queries against longer paragraphs (not something that Universal Sentence Encoder is known to do well!). This is known as "asymmetric search".

We can further explore these 2 ideas testing either:
* a new encoder
* chunk Search by breaking down content into different sentences.

We will leave testing chunk search for another tutorial but we will test a new encoder to compare its performance with Universal Sentence Encoder.

## Comparing Against SentenceTransformer Vectorizer
We begin by instantiating a new encoder. This encoder has been built on distilroberta as a backbone and finetuned on MSMarco data.
```python Python (SDK)
from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec
sent_enc = SentenceTransformer2Vec('distilroberta-base-msmarco-v1')
```
```python
```
Now, we use the same `pull_update_push` function before to easily update our documents with the new sentence encoder.
```python Python (SDK)
def encode_sentences(docs):
 """Encodes documents
 """
 return sent_enc.encode_documents(["product_title", "product_description_clean"], docs)

client.pull_update_push("ecommerce-experiments", encode_sentences)

# After running the above, we want to delete the logs.
client.delete_all_logs("ecommerce-experiments")
```
```python
```
We can take a quick look at the schema to identify what it has been encoded with. Under the hood, VectorHub actually separates out the field with the \_\_name\_\_ attribute of the model so that it does not overwrite the original `use` vector field ("title_use_vector_") - allowing us to quickly test the model.
```python Python (SDK)
client.datasets.schema('ecommerce-experiments')

```
```python
```

```json
{'_unit_id': 'numeric',
 'insert_date_': 'date',
 'product_description': 'text',
 'product_description_clean': 'text',
 'product_description_clean_sentence_transformers_vector_': {'vector': 768},
 'product_description_clean_use_vector_': {'vector': 512},
 'product_description_use_vector_': {'vector': 512},
 'product_image': 'text',
 'product_link': 'text',
 'product_price': 'text',
 'product_title': 'text',
 'product_title_sentence_transformers_vector_': {'vector': 768},
 'product_title_use_vector_': {'vector': 512},
 'query': 'text',
 'rank': 'numeric',
 'relevance': 'numeric',
 'relevance:variance': 'numeric',
 'source': 'text',
 'url': 'text'}
```
```json
```
Now, let us quickly loop through the same queries but switch them with the sentence transformer.


```python Python (SDK)
from IPython.display import display, HTML
queries = [
 "2.4GHz PC mouse",
 "gifts for my son",
 "gifts for my son with cashback"
]

for query in queries:
 results = client.services.search.hybrid(
 "ecommerce-experiments",
 [
 {
 "vector": sent_enc.encode(query),
 "fields": [
 "product_title_sentence_transformers_vector_", # UPDATED: we now use sentence transformers encoder
 "product_description_clean_sentence_transformers_vector_", # UPDATED: We now use sentence transformers
 ]
 }
 ],
 text=query,
 fields=["product_title"],
 traditional_weight=0.025,
 page_size=5)
 display(HTML("<h2>" + query + "</h2>"))
 display(show_results(results, ["product_title", "product_description_clean"]))
```
```python
```
Re-evaluating the results, we notice that the model itself does not seem to perform as well as Universal Sentence Encoder on this dataset. As the initial results do not seem promising, we may decide to end our experimentation here to go either with another encoder or to try out chunking because this approach does not seem to be working.

## Conclusion
This notebook shows us a simple experimentation workflow with just a few simple queries. Often in practice, we may try to examine way 30+ queries in order to get a sense of the model's performance. We may want to test against our most popular searches, whether specific scenarios work and then identify how to improve these edge-cases. For these situations, we have built a search comparator to help users test out their searches en masse. Until then!
