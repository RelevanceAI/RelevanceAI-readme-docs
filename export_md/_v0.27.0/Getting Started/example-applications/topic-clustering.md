---
title: "Clustering"
slug: "topic-clustering"
hidden: true
createdAt: "2021-12-08T23:00:54.096Z"
updatedAt: "2021-12-08T23:25:39.442Z"
---
## Clustering topics
Vector-based clustering is done by employing vectors of specified fields in our data. This allows us to group our data by relying on the existing information in the vector space (i.e concept representations) and not just naive word/n-gram matching.

In this section, we will show you how to create a clustering experiment using Relevance AI platform.

**Try it out in Colab:** [![Open In Colab](https://colab.research.google.com/???)

### What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)

### Installation Requirements

Prior to starting, let's install the main dependencies. This installation provides you with what you need to connect to RelevanceAI API, read/write data, make different searches, etc. Also, the encoder needed to vectorize data.
