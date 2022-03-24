---
title: "Search Comparator"
slug: "search-comparator-2"
hidden: true
createdAt: "2021-12-16T00:43:43.510Z"
updatedAt: "2021-12-16T00:44:09.977Z"
---
It is much easier to evaluate or compare different models when dealing with supervised data. That is because, under supervised learning and evaluation, datasets include both input elements and their corresponding labels. For instance:
* in image processing, in an animal database a picture of a dog is labeled with "dog" or "puppy"
* in sentiment analysis, a sentence such as "the movie was great" is labeled with "positive"
* in question answering, a question text is labeled with one/some possible answers. For instance, "where is the capital city of Australia?", "Canberra is the federal capital of Australia" or "Canberra".

Therefore, by comparing the model output and the labels, we can calculate the accuracy of different models or compare them against each other. This is very different for unsupervised learning since there is no gold standard against which we can compare the results (i.e. there is only input with no specific label or target answer). Hence, in many cases, human evaluators will study the outputs and manually compare different models. This can turn into a tiresome task. The **search comparator** is a Python tool developed intended to provide a meaningful model comparison, especially under unsupervised learning.

## The idea behind Relevance AI search comparator
It relies on ranking and statistical comparison of Top-K results where Top-k refers to the top k results returned by a model. Some fundamental ideas are
* the first Top-k is more important than the last one
* changes in the first Top-k(s) are more important than the ones close to the end of the result list
* the result lists of different models can be of different lengths, or even infinite

## What do I need to use Relevance AI search comparator?
* Project
* API key
* Jupyter Notebook environment

**Project** and **API key** are the username and password to access the service
**Dataset** is the dataset over which the search is done (#TODO# link to a how-to upload data, link on how to vectorize a database)
**Models**
Models are vectorizers, also called encoders, used to turn the text data (query or data in the database) into vectors to be able to perform a search in vector space.

## How do I use Relevance AI search comparator?
This guide is organized in two steps:
1. [Setting up the search comparator](https://docs.relevance.ai/docs/set-up)
2. [Model comparison via the search comparator](https://docs.relevance.ai/docs/search-comparison-and-evaluation)
