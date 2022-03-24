---
title: "How to vector search"
slug: "how-to-vector-search"
excerpt: "A Guide On Using Vector Search"
hidden: false
createdAt: "2021-10-20T03:08:30.713Z"
updatedAt: "2021-10-29T09:03:00.155Z"
---
**Assumed Knowledge**: Vectors
**Target Audience**: General audience
**Reading Time**: 1 minute

Vector Search is reliant largely on index libraries and open-source models. Each vector search guide follows a template of:


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5d08a29-5e40ffa9-4392-4e95-80f8-f9a998a6075e.png",
        "5e40ffa9-4392-4e95-80f8-f9a998a6075e.png",
        5000,
        1100,
        "#dde1ed"
      ],
      "caption": "Process of indexing and searching vectors"
    }
  ]
}
[/block]
The steps/materials can be summarised in the following way:

**Data**: Obtain the data in a way that can be processed into a numerical representation and fed through the necessary model.
**Encode**: Feed the data's numerical representation into a model and extract the vector which can be indexed and searched.
**Index**: Indexing the vectors (from which the data has been encoded) in an efficient way that allows for retrieval.
**Search**: Search the vectors that have been indexed by using a variety of Nearest Neighbor algorithms, filters, chunking and queries.

**The Difficulties of Vector Search**
While the above process appears simple, there are a lot of difficulties with actually using vector search for production. These difficulties include:

- Deploying your index and search for production
- Usage of vectors to optimise search results
- Optimising the way search is being done on the vectors
- Optimising the matching of user intent and products
