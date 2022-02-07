---
title: "Documents"
slug: "documents-1"
excerpt: "Introduction to documents and complex document types"
hidden: false
createdAt: "2021-10-28T08:21:14.663Z"
updatedAt: "2022-01-31T09:14:05.560Z"
---
## Document Basics

Documents can be described as Python dictionaries and are the core unit of data in RelevanceAI's DB - similar to a row in an SQL table or a document in MongoDB.

An example of a document is as such:



```json JSON

{
  "_id" : "711158459",
  "_unit_id" : 711158459,
  "product_title" : "Sony PlayStation 4 (PS4) (Latest Model)- 500 GB Jet Black Console",
  "product_title_vector_" : [0.02, 0.46, 0.9, 0.67, 0.91, 0.21, 0.12],
  "product_description": "The PlayStation 4 system opens the door to an incredible journey through immersive new gaming worlds and a deeply connected gaming community. Step into living, breathing worlds where you are hero of your epic journey. Explore gritty urban environments, vast galactic landscapes, and fantastic historical settings brought to life on an epic scale, without limits. With an astounding launch lineup and over 180 games in development the PS4 system offers more top-tier blockbusters and inventive indie hits than any other next-gen console. The PS4 system is developer inspired, gamer focused. The PS4 system learns how you play and intuitively curates the content you use most often. Fire it up, and your PS4 system points the way to new, amazing experiences you can jump into alone or with friends. Create your own legend using a sophisticated, intuitive network built for gamers. Broadcast your gameplay live and direct to the world, complete with your commentary. Or immortalize your most epic moments and share at the press of a button. Access the best in music, movies, sports and television. PS4 system doesn t require a membership fee to access your digital entertainment subscriptions. You get the full spectrum of entertainment that matters to you on the PS4 system. PlayStation 4: The Best Place to Play The PlayStation 4 system provides dynamic, connected gaming, powerful graphics and speed, intelligent personalization, deeply integrated social capabilities, and innovative second-screen features. Combining unparalleled content, immersive gaming experiences, all of your favorite digital entertainment apps, and PlayStation exclusives, the PS4 system focuses on the gamers.Gamer Focused, Developer InspiredThe PS4 system focuses on the gamer, ensuring that the very best games and the most immersive experiences are possible on the platform.<br>Read more about the PS4 on ebay guides.</br>",
  "product_description_vector_" : [0.8, 0.38, 0.85, 0.47, 0.19, 0.18, 0.4],
  "product_image" : "https://thumbs2.ebaystatic.com/d/l225/m/mzvzEUIknaQclZ801YCY1ew.jpg",
  "product_image_vector_" : [0.01, 0.23, 0.45, 0.67, 0.89, 0.1, 0.12],
  "product_link" : "https://www.ebay.com/itm/Sony-PlayStation-4-PS4-Latest-Model-500-GB-Jet-Black-Console-/321459436277?pt=LH_DefaultDomain_0&hash=item4ad879baf5",
  "product_price" : 329.98,
  "relevency_data" : {
    "rank" : 1,
    "relevance" : 3.67,
  }
  "source" : "eBay",
}

```
```json
```



### Schema Rules

Schema Rules for working with documents in RelevanceAI.


|**Schema Rule**|**Example**|
|:-----:|:-----:|
|When inserting the document you can optionally specify your own id for a document by using the field name `_id`, if not specified a random id is assigned.| ```{"_id": "j2hfio23j"}``` |
|When inserting or specifying vectors in a document use the suffix (ends with) `_vector_` for the field name.| `product_description_vector_`|



## Advanced

### Chunk Documents

Chunk documents are essentially documents with a list as one of the values. This can be useful to depict parent-child relationships in documents such as `lines` in a `page` and you want the most relevant line in a page returned.

Chunk documents have `chunks` which are denoted by the suffix `_chunk_`.

An example of a chunk document is as such:


```json JSON
{
  "page_number": 2,
  "lines_chunk_": [
  	{
    	"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
    	"text": "Tempus quam pellentesque nec nam aliquam sem et tortor consequat."
    }
  ]
},
{
  "page_number": 3,
  "lines_chunk_": [
  	{
    	"text": "Eu scelerisque felis imperdiet proin fermentum leo vel."
    },
    {
    	"text": "Leo vel orci porta non pulvinar neque laoreet. Eleifend donec pretium vulputate sapien."
    }
  ]
}


```
```json
```


Chunk documents need to be used with special chunk search endpoints and have separate vector fields that end with  `_chunkvector_`. These search endpoints are `/services/search/chunk_search`, `/services/search/advanced_chunk_search`, `/services/search/multistep_chunk_search` and `/services/search/multistep_advanced_chunk_search`. Note that when storing chunks in Relevance AI, the order within the chunk is maintained.

### Schema Rules

Schema Rules for working with chunk documents in RelevanceAI.


|**Schema Rule**|**Example**|
|:-----:|:-----:|
|When inserting or specifying chunks in a document the suffix (ends with) `_chunk_` for the field name. If you are unfamiliar with chunks, you can [read about them here Documents](doc:documents-1).| `products_chunk_`|
|When inserting or specifying chunk vectors in a document's chunks use the suffix (ends with) `_chunkvector_` for the field name.| `products_chunk_.product_description_chunkvector_`|