---
title: "Experimentation workflow"
slug: "experimentation-workflow"
excerpt: "A guide to a vector search experimentation workflow"
hidden: true
createdAt: "2021-10-26T21:27:26.490Z"
updatedAt: "2021-11-05T22:13:48.526Z"
---
Our goal is to ensure we maximize the success of vector-based applications. Our vector-based experimentation platform provides data scientists/machine learning engineers/vector enthusiasts an important way to experiment with their vectors.
[block:callout]
{
  "type": "success",
  "title": "Our experimentation workflows are designed to accelerate success in vector-based applications.",
  "body": "While vectors have a lot of potential across a range of applications - there is an enormous amount of focus required on ensuring that the correct vectors are being built."
}
[/block]
This means that you can encode, index and start searching your results in seconds!

Below, we show a flowchart demonstrating the higher-level overview of this process.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1fd1864-b55fbeb9-ea54-4270-81fa-5ee6eb1d20c6.png",
        "b55fbeb9-ea54-4270-81fa-5ee6eb1d20c6.png",
        1516,
        502,
        "#5074cd"
      ],
      "caption": "End to end vector application workflow"
    }
  ]
}
[/block]

In the flowchart above, the data is vectorised locally and then inserted into VecDB. Once these are inserted into VecDB, we will be interested in testing out the initial performance via vector searches, or traditional searches with different weightings. If we find that the embedding is bad, we may choose to finetune instead and re-insert them into a separate vector database to re-try all of our queries with different configurations.

Below, we show an example flowchart of a testing scenario for a vector-based application. While it is just a high-level overview, it does not include adjustments in numerical weightings or tweaks we made to our vectorizers (which can exponentially increase the number of experiments we run.

In our [Better Text Search](doc:better-text-search), we go into more detail into how to use all of our different endpoints. You can take a quick glance at all of our different search endpoints below in this decision-making flowchart. Our guides come with sample use cases and in-depth concept explanations about how to use each one and when to use/experiment with each endpoint.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/eac4401-different-search-endpoints-only_1.png",
        "different-search-endpoints-only (1).png",
        2026,
        1416,
        "#d7a5e1"
      ],
      "caption": "A sample workflow on endpoint testing with VecDB"
    }
  ]
}
[/block]
