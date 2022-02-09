---
title: "Limitations of vectors"
slug: "_limitations-of-vectors"
excerpt: "An outline of the limitations of what vectors are capable of"
hidden: true
createdAt: "2021-10-24T23:26:42.495Z"
updatedAt: "2021-12-03T01:07:01.121Z"
---
**Assumed Knowledge**: Vectors
**Target Audience**: General audience
**Reading Time**: 2 minutes

Vectors are largely dependent on the models being used.

There are two main challenges associated with using vectors in production engineering systems:

- The difficulty of obtaining the right type of vectors
- The difficulty of productionisation of vectors

Let us go over each challenge.

## The Right Vectors

Choosing the right vectors for your use case can be difficult. When choosing a model for vectors, you need to ask yourself the following questions:

- Which out-of-the-box model works best for this use case?
- Is an out-of-the-box model good enough? If not, how do I fine-tune my vectors for my particular use case?
- What is the model trained on?
- If the model's vectors do not perform well - is it because it was not trained on the right data or was the training method not suitable?

**Why do some models need to be fine-tuned and how does that help?**

Firstly - what is fine-tuning? In the context of vectors, fine-tuning refers to the process of altering the position of our vectors by changing the weights in our model. We can change the weights in your model by training the model further on your dataset so that similarities between certain images and items can be improved by updating the model.

To better understand the importance of fine-tuning, let us consider an example scenario of how Image2Vec can fail in identifying the same faces and why we may need to finetune a new model to produce Face2Vec.
Image2Vec has been trained to identify similar images and this can be based on color, the orientation of the image, features of the image.

## Productionisation difficulty

Putting vectors into production can be a difficult task. One has to build out an API for the index, the encoder, provide options for advanced search functions with vectors, and then figure out ways to then store search. There is a lot of work that has been done simply to get it running but more work needs to be done to get it to a useful state for productionisation.