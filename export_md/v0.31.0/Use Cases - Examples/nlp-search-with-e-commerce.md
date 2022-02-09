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
[block:api-header]
{
  "title": "What do I need to follow this guide?"
}
[/block]
Grab your project and API key from https://cloud.relevance.ai/ in the settings area and let's get started!

- Project Name
- API-key
- Dataset in Relevance AI
- Python 3.6+
- Jupyter Notebook environment

## Set Up
[block:code]
{
  "codes": [
    {
      "code": "\n# Install the requirements\n!pip install -q -U RelevanceAI\n!pip install -q vectorhub[encoders-text-sentence-transformers, encoders-text-tfhub]\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Once you set it up, we will then instantiate the 2 encoders we are going to compare:
[block:code]
{
  "codes": [
    {
      "code": "\nfrom vectorhub.encoders.text.tfhub import USE2Vec\nuse = USE2Vec()\n\nfrom vectorhub.bi_encoders.text_image.torch import Clip2Vec\nclip = Clip2Vec()\n\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
## Client Set Up
[block:code]
{
  "codes": [
    {
      "code": "\nfrom relevanceai import Client\nclient = Client()\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
## Get the Dataset
[block:code]
{
  "codes": [
    {
      "code": "\nfrom relevanceai.datasets import get_ecommerce_dataset\ndocs = get_ecommerce_dataset()\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
From this list of queries, we now investigate 4 queries that we are looking to test:
- 2.4GHz PC mouse
- ST2000DM001
- gifts for my daughter
- gifts for my son with cashback

[block:api-header]
{
  "title": "Vectorizing"
}
[/block]
In this section, we will assign the `_id` of the document and then encode them and insert into a dataset called `ecommerce-experiments`.
[block:code]
{
  "codes": [
    {
      "code": "for d in docs:\n    d['_id'] = str(d['_unit_id'])\n\ndocs = [{k:v for k, v in doc.items() if not isinstance(v, list) and not pd.isna(v)} for doc in docs]\n\nencoded_docs = use.encode_documents([\"product_title\"], docs)\n\nclient.insert_documents(\"ecommerce-experiments\", encoded_docs)\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Afterwards, let us check that this has been properly encoded by looking at the schema as follows.
[block:code]
{
  "codes": [
    {
      "code": "\nclient.datasets.schema(\"ecommerce-experiments\")\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This is expected to return:
[block:code]
{
  "codes": [
    {
      "code": "{'_unit_id': 'numeric',\n 'insert_date_': 'date',\n 'product_description': 'text',\n 'product_image': 'text',\n 'product_link': 'text',\n 'product_price': 'text',\n 'product_title': 'text',\n 'product_title_use_vector_': {'vector': 512},\n 'query': 'text',\n 'rank': 'numeric',\n 'relevance': 'numeric',\n 'relevance:variance': 'numeric',\n 'source': 'text',\n 'url': 'text'}",
      "language": "json",
      "name": null
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Testing Universal Sentence Encoder"
}
[/block]
Now let us begin testing our search performance on the given dataset with a few different queries.  We will begin with a simple vector search. You can read more about vector search here at the ![Vector Search API reference](https://docs.relevance.ai/reference/vector_search_api_services_search_vector_post).
[block:code]
{
  "codes": [
    {
      "code": "query = \"2.4GHz PC mouse\"\nresults = client.services.search.vector(\n\t\"ecommerce-experiments\", \n\t[{\"vector\": use.encode(query), \"fields\": [\"product_title_use_vector_\"]}]\n)\n\n# We can quickly look at our results by calling this:\n[r['product_title'] for r in results['results']]",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This should give us something similar to this:
[block:code]
{
  "codes": [
    {
      "code": "\n['2.4GHz Cordless Wireless Optical Mouse Mice for Laptop PC Computer+USB Receiver',\n '2.4 GHz Wireless Optical Mouse Mice + USB 2.0 Receiver for PC Laptop Black',\n 'Black 2.4GHz Wireless Optical Mouse Mice+USB 2.0 Receiver For Laptop Desktop PC',\n '2015 new Black 2.4GHz Wireless Optical Mouse/Mice + USB Receiver for PC Laptop',\n 'Dual Ports PS2 II Controller Console to PC USB Game Converter Adapter',\n 'IBM ThinkPad LENOVO T61 LAPTOP 2.0 GHz 2GB 80 GB 14.1 WIN 7 64bit CDRW/DVD WiFi\"',\n 'IBM LENOVO THINKPAD T410 LAPTOP WIN 7 PRO 32bit DVDRW i5 2.4 ghz 250 gb 3gb WiFi',\n 'PS1 PS2 PSX to PC USB Dual Controller Adapter Converter',\n 'Classic Wired Game Controller Remote Pro Gamepad Shock For Nintendo Wii SY',\n 'Controller Guitar adapter USB converter for PS2 to PS3',\n 'Universal USB Microphone for PS2, PS3, Xbox 360 , PC, Wii',\n 'For PS1 PS2 PSX Playstation 2 Joypad Game Controller to PC USB Converter Adapter',\n 'New high qualtiy PS1 PS2 PSX to PC USB CONTROLLER ADAPTER CONVERTER SY',\n 'White Classic Pro Controller for Nintendo Wii Remote',\n 'D-Link DIR-657 300 Mbps 4-Port Gigabit Wireless N Router Hd Media Router 1000',\n 'IBM LENOVO THINKPAD T420 LAPTOP i5 2.50ghz 8GB 320GB DVDRW Windows 7 PRO WEBCAM',\n 'Sony PlayStation 4 500GB Console with 2 Controllers',\n 'Oster OGG3701 Microwave 0.7 cu. ft. 700 Watts Countertop Microwave Oven OGG3701',\n 'Oster OGZB1101 Countertop Microwave Oven 1000 Watts 1.1 cu ft',\n 'Brand New Controller for Nintendo GameCube or Wii -- PLATINUM']",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Great! Looks like the results are pretty good. Now let's try something a bit more specific with more emphasis on targetting a specific item by which we know the item ID..
[block:code]
{
  "codes": [
    {
      "code": "query = \"ST2000DM001\"\nresults = client.services.search.vector(\n    \"ecommerce-experiments\",\n    [{\n      \"vector\": use.encode(query), \n      \"fields\": [\"product_title_use_vector_\"]\n      }])\n[r['product_title'] for r in results['results']]",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This should return to us something similar to this:
[block:code]
{
  "codes": [
    {
      "code": "['Oster OGH6901 0.9 cu. ft. 900 Watts Countertop Microwave Oven OGH6901',\n 'Oster OGZB1101 Countertop Microwave Oven 1000 Watts 1.1 cu ft',\n '120ML Ultrasonic Aroma Oil Diffuser Humidifier LED Color Changing Air Purifier',\n 'Oster OGG3701 Microwave 0.7 cu. ft. 700 Watts Countertop Microwave Oven OGG3701',\n 'Manual Coffee Grinder  Hand-Crank Mill NEW',\n 'Panasonic ARC4 ES-RF31-s Rechargeable Electric Shaver Wet/dry 4 Nanotech Blade',\n '6pcs Teenage Mutant Ninja Turtles Action Figures Classic Collection Toys Set Boy',\n 'Ultrasonic Aroma Humidifier Air Diffuser Purifier Color Changing Rainbow LED',\n 'Panasonic Arc3 ES 8103S Wet/Dry Rechargeable Shaver (A491)',\n 'Presto 6-Quart Aluminum Pressure Cooker 01264, New, Free Shipping',\n \"Panasonic ES8243A E Arc4 Men's Electric Shaver Wet/Dry\",\n 'Quick Change Key Trigger Acoustic Electric Folk Guitar Tune Capo Clamp',\n '500ML Aroma Diffuser Atomizer Air Humidifier LED Ultrasonic Purifier Lonizer',\n 'Cuisinart DCC 3000 Coffee on Demand 12 Cup Programmable Coffeemaker',\n 'Stand Ride Sit Double Baby Infant Toddler Child Walk Outdoor Stroller Maternity',\n 'Whitening Cream100g Face & Body Lightening Moisturizers +[Free Gift] Facial Mask',\n 'Shark SV1106 Navigator Cordless Upright Vacuum Dirt Cleaner Bagless Canister Pet',\n '2.4GHz Cordless Wireless Optical Mouse Mice for Laptop PC Computer+USB Receiver',\n 'Panasonic ES8243A Arc4 Electric Shaver Wet/Dry (missing cleaning brush)',\n 'NEW Microphones Mic XBOX PS3 PS2 Wii PC Rock Band Guitar Hero Karaoke']",
      "language": "json",
      "name": ""
    }
  ]
}
[/block]
Unfortunately - this is one of the weaknesses of vector search - sometimes the vectors themselves are not great because dense representations can be quite limiting.
[block:callout]
{
  "type": "info",
  "title": "Vectors can sometimes underperform without exact match boosting.",
  "body": "While vectors generally perform well in semantic search applications, they sometimes fail at exact text matching. Vector search, unfortunately, is not a superset of traditional search. It is merely an alternative. Read on below to see how we tackle this problem with **hybrid search**."
}
[/block]

[block:api-header]
{
  "title": "Hybrid Search"
}
[/block]

While the previous results were okay - it's strange that `ST2000DM001` doesn't immediately dominate the top search results. For that - we might want to combine traditional search with vector search such that if the title contains the same words as the query - it gets boosted up.

First - let us do a quick check of what is *expected* to be at the top via traditional search. You can read about the traditional search endpoint [here](https://docs.relevance.ai/reference/traditional_search_api_services_search_traditional_post) if you are unfaimilar.

We can do so by firstly performing an exact text search to see what search results we should be expecting:
[block:code]
{
  "codes": [
    {
      "code": "results = client.services.search.traditional(\n    \"ecommerce-experiments\", \n    text=\"ST2000DM001\", \n    fields=[\"product_title\"]\n  )['results']\nresults[['product_title', \"_search_score\"]]",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
You should see the screenshot below:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f7841b7-Capture.PNG",
        "Capture.PNG",
        821,
        186,
        "#454545"
      ]
    }
  ]
}
[/block]
So there appears to be 3 results. While the top result exactly matches the query - the rest do not. Why is that? The rest of the results are just the ones closest in regards to Levishtein distance, which can be set using the edit_distance parameter in Hybrid search (we have it defaulted to -1 for automatic conversion.


[block:code]
{
  "codes": [
    {
      "code": "query = \"ST2000DM001\"\nresults = client.services.search.hybrid(\n        \"ecommerce-experiments\", \n        multivector_query=[{\n        \"vector\": use.encode(query),\n        \"fields\": [\"product_title_use_vector_\"]\n        }],\n        text=query,\n        fields=[\"product_title\"], # NEW FIELD FOR HYBRID SEARCH\n        traditional_weight=0.025, # NEW FIELD FOR TRADITIONAL WEIGHTING\n        edit_distance=-1,         # NEW FIELD FOR LEVISHTEIN DISTANCE\n)\n\n[r['product_title'] for r in results['results']]\n\n# Expected result\n\n['Lot of 2 Seagate ST2000DM001 2TB SATA disks',\n 'Seagate ST2000DX001 2 TB 3.5 Internal Hybrid Hard Drive\"',\n 'Samsung Seagate Momentus SpinPoint ST2000LM003 2 TB 2.5 SATA Notebook PS4 HDD\"',\n 'Oster OGH6901 0.9 cu. ft. 900 Watts Countertop Microwave Oven OGH6901',\n 'Oster OGZB1101 Countertop Microwave Oven 1000 Watts 1.1 cu ft',\n '120ML Ultrasonic Aroma Oil Diffuser Humidifier LED Color Changing Air Purifier',\n 'Oster OGG3701 Microwave 0.7 cu. ft. 700 Watts Countertop Microwave Oven OGG3701',\n 'Manual Coffee Grinder  Hand-Crank Mill NEW',\n 'Panasonic ARC4 ES-RF31-s Rechargeable Electric Shaver Wet/dry 4 Nanotech Blade',\n '6pcs Teenage Mutant Ninja Turtles Action Figures Classic Collection Toys Set Boy',\n 'Ultrasonic Aroma Humidifier Air Diffuser Purifier Color Changing Rainbow LED',\n 'Panasonic Arc3 ES 8103S Wet/Dry Rechargeable Shaver (A491)',\n 'Presto 6-Quart Aluminum Pressure Cooker 01264, New, Free Shipping',\n \"Panasonic ES8243A E Arc4 Men's Electric Shaver Wet/Dry\",\n 'Quick Change Key Trigger Acoustic Electric Folk Guitar Tune Capo Clamp',\n '500ML Aroma Diffuser Atomizer Air Humidifier LED Ultrasonic Purifier Lonizer',\n 'Cuisinart DCC 3000 Coffee on Demand 12 Cup Programmable Coffeemaker',\n 'Stand Ride Sit Double Baby Infant Toddler Child Walk Outdoor Stroller Maternity',\n 'Whitening Cream100g Face & Body Lightening Moisturizers +[Free Gift] Facial Mask',\n 'Shark SV1106 Navigator Cordless Upright Vacuum Dirt Cleaner Bagless Canister Pet']",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This is more like it! By combining with traditional search - we are able to get the bost of both worlds.
Now - while items are great, sometimes, we want to be able to also search on the content of the actual product - we will take a look into how we do that next.

[block:api-header]
{
  "title": "Combining with product descriptions"
}
[/block]
While we can search titles just fine, we may want to also search for content inside the product description. So let us build this.

We begin by defining how we want to display the results as such:
[block:code]
{
  "codes": [
    {
      "code": "def show_results(results, fields_to_show=[\"title\", \"content\"]):\n    return pd.DataFrame(results['results'])[fields_to_show]",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
This is a helpful function to allow us to visualise the results.

[block:api-header]
{
  "title": "Clean and encode product descriptions"
}
[/block]
Here, we encode content - here we show you how to combine both searches and the easiest way to clean and encode your dataset. In this section, we will:

1) Clean the HTML from product descriptions.
2) Encode the documents
3) Get our documents, edit them locally and push them back via the pull_update_push functionality.
[block:code]
{
  "codes": [
    {
      "code": "# The easiest way to encode content\nfrom io import StringIO\nimport unicodedata\nfrom html.parser import HTMLParser\n\nclass MLStripper(HTMLParser):\n    \"\"\"Remove HTML from the code and retrieves data.\n    \"\"\"\n    def __init__(self):\n        super().__init__()\n        self.reset()\n        self.strict = False\n        self.convert_charrefs= True\n        self.text = StringIO()\n\n    def handle_data(self, d):\n        self.text.write(d)\n\n    def get_data(self):\n        return self.text.getvalue()\n\ndef clean_html(html):\n    \"\"\"Cleans HTML from text.\"\"\"\n    s = MLStripper()\n    html = unicodedata.normalize(\"NFKD\", html).replace(\"\\r\", \"\").replace(\"\\t\", \" \").replace(\"\\n\", \" \")\n    s.feed(html)\n    return s.get_data()\n\n\ndef encode_content(docs: list): \n  \"\"\"\nencode_content takes in a list of documents\n  \"\"\"\n  for d in docs:\n    d['product_description_clean'] = clean_html(d['product_description'])\n  return use.encode_documents([\"product_description_clean\"], docs)\n\n# Pull update push takes in a Python callable and automatically \n# loops through your dataset with automatic logging and progress bar!\nclient.pull_update_push(\"ecommerce-experiments\", encode_content)",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Under the hood, pull_update_push retrieves a set of documents, runs the function that you stored against it and then updates them accordingly - allowing us to focus on writing good functionality and logs the errors.",
  "title": "pull_update_push is a very useful function built to accelerate idea testing"
}
[/block]

Now let us see what these results look like when we include description with them.
[block:code]
{
  "codes": [
    {
      "code": "query = \"gifts for my daughter\"\nresults = client.services.search.hybrid(\n        \"ecommerce-experiments\", \n        multivector_query=[{\n        \"vector\": use.encode(query),\n        \"fields\": [\n        \t\"product_title_use_vector_\", \n          \"product_description_clean_use_vector_\" # UPDATED to include descriptions\n        ], \n        }],\n        text=query,\n        fields=[\"product_title\"],\n        traditional_weight=0.025,\n        edit_distance=-1,\n)\n\npd.DataFrame(results['results'])[['product_title', \"product_description_clean\"]]",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Attached below is a screenshot of what the results look like below.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/39d8648-Capture.PNG",
        "Capture.PNG",
        1436,
        424,
        "#474747"
      ]
    }
  ]
}
[/block]
These results look better! Looking at the content, we can start testing some interesting queries to see what they return. For example, we may want to test `gifts for my son with cashback` using the code below. It is useful to note that only rarely does the title ever mention "cashback" but this can occur quite often in the actual product description. A code snippet is shown below:
[block:code]
{
  "codes": [
    {
      "code": "query = \"gifts for my son with cashback\"\nresults = client.services.search.hybrid(\n        \"ecommerce-experiments\", \n        multivector_query=[{\n          \"vector\": use.encode(query),\n          \"fields\": {\n              \"product_title_use_vector_\": 0.5, \n              \"product_description_clean_use_vector_\": 0.5 # UPDATED: Included product descriptions\n              }\n        }],\n        text=query,\n        fields=[\"product_title\",],  \n        traditional_weight=0.025,\n        edit_distance=-1,\n        page_size=5\n)\npd.set_option('display.max_colwidth', 20000)\npd.DataFrame(results['results'])[['product_title', \"product_description_clean\"]]",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
The results should look something like this:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4556670-Capture.PNG",
        "Capture.PNG",
        1466,
        598,
        "#525252"
      ]
    }
  ]
}
[/block]
From the above we can see that while there are gifts for sons (playstations, clocks, games), the results can definitely still be better. However - none of them seem to offer cashback. However, there were still results floated up mentioning cashback was an option if users wanted them.

We may now want to improve our vector search through 2 main ways.
- **Improve via chunking.** The content has a lot of sentences. We might want to break down each content section into smaller sentences and perform search on each of them (thus allowing more specific stuff like cashback to come up earlier). This can be really useful if we want more fine-grained control over our search results.
- **Improve via asymmetric search models** We may want to rely on these models that support searching with short queries against longer paragraphs (not something that Universal Sentence Encoder is known to do well!). This is known as "asymmetric search".

We can further explore these 2 ideas testing either:
* a new encoder
* chunk Search by breaking down content into different sentences.

We will leave testing chunk search for another tutorial but we will test a new encoder to compare its performance with Universal Sentence Encoder.

[block:api-header]
{
  "title": "Comparing Against SentenceTransformer Vectorizer"
}
[/block]
We begin by instantiating a new encoder. This encoder has been built on distilroberta as a backbone and finetuned on MSMarco data.
[block:code]
{
  "codes": [
    {
      "code": "from vectorhub.encoders.text.sentence_transformers import SentenceTransformer2Vec\nsent_enc = SentenceTransformer2Vec('distilroberta-base-msmarco-v1')",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Now, we use the same `pull_update_push` function before to easily update our documents with the new sentence encoder.
[block:code]
{
  "codes": [
    {
      "code": "def encode_sentences(docs):\n    \"\"\"Encodes documents\n    \"\"\"\n    return sent_enc.encode_documents([\"product_title\", \"product_description_clean\"], docs)\n\nclient.pull_update_push(\"ecommerce-experiments\", encode_sentences)\n\n# After running the above, we want to delete the logs. \nclient.delete_all_logs(\"ecommerce-experiments\")",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
We can take a quick look at the schema to identify what it has been encoded with. Under the hood, VectorHub actually separates out the field with the \_\_name\_\_ attribute of the model so that it does not overwrite the original `use` vector field ("title_use_vector_") - allowing us to quickly test the model.
[block:code]
{
  "codes": [
    {
      "code": "client.datasets.schema('ecommerce-experiments')\n",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{'_unit_id': 'numeric',\n 'insert_date_': 'date',\n 'product_description': 'text',\n 'product_description_clean': 'text',\n 'product_description_clean_sentence_transformers_vector_': {'vector': 768},\n 'product_description_clean_use_vector_': {'vector': 512},\n 'product_description_use_vector_': {'vector': 512},\n 'product_image': 'text',\n 'product_link': 'text',\n 'product_price': 'text',\n 'product_title': 'text',\n 'product_title_sentence_transformers_vector_': {'vector': 768},\n 'product_title_use_vector_': {'vector': 512},\n 'query': 'text',\n 'rank': 'numeric',\n 'relevance': 'numeric',\n 'relevance:variance': 'numeric',\n 'source': 'text',\n 'url': 'text'}",
      "language": "json",
      "name": null
    }
  ]
}
[/block]
Now, let us quickly loop through the same queries but switch them with the sentence transformer.


[block:code]
{
  "codes": [
    {
      "code": "from IPython.display import display, HTML\nqueries = [\n    \"2.4GHz PC mouse\",\n    \"gifts for my son\",\n    \"gifts for my son with cashback\"\n]\n\nfor query in queries:\n    results = client.services.search.hybrid(\n        \"ecommerce-experiments\",\n        [\n         {\n          \"vector\": sent_enc.encode(query), \n          \"fields\": [\n            \"product_title_sentence_transformers_vector_\",  # UPDATED: we now use sentence transformers encoder\n            \"product_description_clean_sentence_transformers_vector_\", # UPDATED: We now use sentence transformers\n          ]\n          }\n        ],\n        text=query, \n        fields=[\"product_title\"],\n        traditional_weight=0.025,\n        page_size=5)\n    display(HTML(\"<h2>\" + query + \"</h2>\"))\n    display(show_results(results, [\"product_title\", \"product_description_clean\"]))   ",
      "language": "python",
      "name": "Python (SDK)"
    }
  ]
}
[/block]
Re-evaluating the results, we notice that the model itself does not seem to perform as well as Universal Sentence Encoder on this dataset. As the initial results do not seem promising, we may decide to end our experimentation here to go either with another encoder or to try out chunking because this approach does not seem to be working.

[block:api-header]
{
  "title": "Conclusion"
}
[/block]
This notebook shows us a simple experimentation workflow with just a few simple queries. Often in practice, we may try to examine way 30+ queries in order to get a sense of the model's performance. We may want to test against our most popular searches, whether specific scenarios work and then identify how to improve these edge-cases. For these situations, we have built a search comparator to help users test out their searches en masse. Until then!