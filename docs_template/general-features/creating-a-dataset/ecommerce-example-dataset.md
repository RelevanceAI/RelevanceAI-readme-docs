---
title: "Copying and cloning dataset"
slug: "ecommerce-example-dataset"
excerpt: "Guide on how to copy and clone datasets"
hidden: false
createdAt: "2021-11-03T00:10:39.691Z"
updatedAt: "2022-01-17T02:57:42.720Z"
---
## Copy a dataset from another project


In this section, we show you how to create a copy of a dataset from one project to another. This allows you to freely collaborate and share datasets between accounts.
First Relevance AI's Python SDK must be installed and then a client object must be instantiated as shown below:

@@@ relevanceai_installation , RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

@@@ client_instantiation @@@


- `dest_project` and `dest_api_key` refer to your destination project and api_key or where the copied version of dataset is going to be saved.

@@@ dataset_send_to @@@

## Clone the dataset

In this section, we show you how to create a copy of a dataset within the same project. This allows you to freely version and checkpoint datasets.

@@@ clone_dataset @@@
