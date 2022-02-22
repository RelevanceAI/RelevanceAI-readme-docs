---
title: "Prerequisites"
slug: "prerequisites"
excerpt: "How to use embedding projection to better understand your vectors"
hidden: true
createdAt: "2021-11-12T01:22:11.406Z"
updatedAt: "2021-12-11T13:49:49.025Z"
---
## Introduction
## What are vectors and vector spaces

Let us imagine each word can be positioned in a 2 or 3-dimensional space; meaning each word can be represented with [x,y,z] coordinates, based on its meaning. This [x,y,z] coordinate is called a vector, and the whole space containing all the words is called a **vector space**. In reality, the number of dimensions is significantly bigger than two or three (for more information visit [What are vectors](doc:what-are-vectors))

## How is a vector space formed?
Vector spaces are formed via machine learning models. A good vector space is one that shows meaningful relationships between words (their vectors). For instance, in a good vector space, it is expected that the data points ([x,y,z]s) representing animals such as "tiger" and "lion" to be closer to each other and far from points representing words like "automobile", "whiteboard" or "Mars".
You can also expect to have similar forms of vector relation (distance, angle, etc.) between data points that are conceptually related. For instance vector relation between ("king", "man") and ("queen", "woman") are expected to be similar.

In order to better visualise our vectors, we can perform a dimensionality reduction process in order to condense the meaning of our vectors into a 3-dimensional space to better understand their similarity.

## Why do we need dimensionality reduction?
Our vector space
## Unsupervised Dimensionality Reduction
In order for us to reduce our vector dimensions from model output to 2 or 3 dimensions that can be visualised, we can apply unsupervised dimensionality techniques on the continuous vector output to condense it's meaning and project to a lower-dimensional space.
<figure>
<img src="https://files.readme.io/96b23d4-Dimensionality_Reduction_-_Unsupervised_and_Continuous2x1.png" width="2188" alt="Dimensionality Reduction - Unsupervised and Continuous@2x(1).png" />
<figcaption>Unsupervised Dimensionality Reduction Taxonomy</figcaption>
<figure>

## Clustering

## What I Need
* Project and API Key: Grab your Relevance AI project and API key by [signing up](https://cloud.relevance.ai/ )
* Python 3 (ideally a Jupyter Notebook/Colab environment)
* RelevanceAI Installed - Full installation guide can be found [here](https://docs.relevance.ai/docs/installation) or
simply run the following command to install the main dependencies.
```shell Shell
pip install -U RelevanceAI[notebook]
```
```shell
```
