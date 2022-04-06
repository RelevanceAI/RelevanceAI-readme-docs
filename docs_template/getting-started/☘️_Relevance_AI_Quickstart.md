---
category: 623abf4109822f00e1da0b80
createdAt: '2022-04-06T02:34:20.910205Z'
excerpt: ''
hidden: false
slug: relevance-ai-quickstart
title: ☘️ Relevance AI Quickstart
updatedAt: '2022-04-06T02:34:20.910232Z'
---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/workflows/blob/main/workflows/quickstart_workflow/☘%EF%B8%8F_Relevance_AI_Quickstart.ipynb)







# Quickstart
Use Relevance AI to experiment, build and share the best vectors to solve similarity and relevance based problems across teams.


<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_DS_Workflow.png?raw=true"  alt="Relevance AI" />




@@@ relevanceai_installation , RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@


@@@ client_instantiation @@@

# 🚣 Inserting data

An easy way to insert your data can be seen below!




@@@ quickstart_docs_1; dataset_basics,DATASET_ID=QUICKSTART_DATASET_ID  @@@


# 🤼 Get started with clustering

Clustering can help you group which ones are relevant and better understand your vectors/embeddings. Here is an example of how to cluster which will allow you to better visualise groups in the projector!

Need more clustering? [Read more about it here](https://relevanceai.readthedocs.io/en/latest/auto_clustering.html)!





@@@ cluster, ALIAS="kmeans_3", VECTOR_FIELD="example_vector_" @@@


You can now adjust the projector settings as required in settings and choosing the respective cluster that you want. Behind the scenes, Relevance AI handles data management, schema, operations, productionisation for users so users can focus on building important applications.



# 🔎 Get started with search

You can launch a search app immediately!




@@@ launch_search_app @@@

# 🌀 Insert Your Own Data Via Dashboard!

Try out Relevance AI on your own data! You can insert your own data at https://cloud.relevance.ai/onboard/create/.





# 🚀 Launching a 3D projector

You can now view your projector here at:

https://cloud.relevance.ai/dataset/quickstart-projector/deploy/recent/projector

In the projector, you should be able to see something similar to this:







You can also share your app by now clicking the **Share** button on the top right! This now produces a public application for others to view!



# ⚡ Vectorizing

Vectorize using models that produce out of the box good results!




@@@ vectorhub_encoders_text_tfhub_installation @@@



@@@ vectorize, TEXT_FIELDS=["text"] @@@

# What's next 🚀?
This is just a quick tutorial on Relevance AI, there are many more applications that is possible such as zero-shot based labelling, recommendations, anomaly detection, projector and more:
- There are more indepth tutorials and guides at https://docs.relevance.ai
- There are detailed library references at https://relevanceai.readthedocs.io/