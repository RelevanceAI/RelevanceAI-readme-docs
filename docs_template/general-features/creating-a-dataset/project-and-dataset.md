---
title: "Dataset Basics"
slug: "project-and-dataset"
excerpt: "Dedicated section to managing your RelevanceAI space"
hidden: false
createdAt: "2021-10-28T06:57:07.293Z"
updatedAt: "2022-01-18T02:31:36.905Z"
---
To be able to conduct vector experiments using Relevance AI, you need to sign up at https://cloud.relevance.ai/. Alternatively, you can follow the [guide](doc:installation) on our installation page.

## Datasets

After uploading a dataset to your account in Relevance AI, you can preview your data in the dashboard https://cloud.relevance.ai under Dataset. Note that if you just started, your account will be empty!

Open an example in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs/general-features/creating-a-dataset/_notebooks/RelevanceAI_ReadMe_Creating_A_Dataset.ipynb)


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_dataset_dashboard.png?raw=true" alt="See your dataset in the dashboard" />
<figcaption>See your dataset in the dashboard</figcaption>
<figure>

## Interacting With Datasets

By storing data on our platform, you can directly invoke vectorization models, perform an optimized nearest-neighbor search, cluster data, etc.

Some basic actions to deal with datasets are:

- Create a dataset
- List the available datasets in a project/account
- Monitor a specific dataset
- Delete a dataset

You can either use the dashboard to take these actions or employ Relevance AI Python SDK. For the Python SDK, you need to install Relevance AI and initiate a client as shown in the two code snippets below:

@@@ relevanceai_dev_installation @@@

@@@ client_instantiation @@@

### Creating a dataset
To create a new empty dataset pass the name under which you wish to save the dataset to the `create` function as shown below. In this example, we have used `ecommerce-sample-dataset` as the name.

@@@ dataset_basics, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@

See [Inserting and updating documents](doc:inserting-data) for more details on how to insert/upload documents into a dataset.

> 🚧 Remember!
>
> * You cannot rename datasets or rename/edit existing field names. However, you can copy datasets and edit field names using the [`clone`](https://relevanceai.readthedocs.io/en/v0.33.2/client.html#relevanceai.http_client.Client.clone_dataset) feature.


* Id field: Relevance AI platform identifies unique data entries within a dataset using a field called `_id` (i.e. every document in the dataset must include an `_id` field with a unique value per document).
* Vector fields: the name of vector fields must end in `_vector_`

### List your datasets

You can see a list of all datasets you have uploaded to your account in the dashboard.
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/general-features/creating-a-dataset/_assets/dataset-list-view.png?raw=true" alt="Datasets List View" />
<figcaption>List of datasets in the dashboard</figcaption>
<figure>


Alternatively, you can use the list endpoint under Python SDK as shown below:

@@@ list_datasets @@@

### Monitoring a specific dataset

RelevanceAI's dashboard at https://cloud.relevance.ai is the most straightforward place to monitor your data.
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/general-features/creating-a-dataset/_assets/monitor-dataset.png?raw=true" width="1263" alt="vector_health.png" />

<figcaption>Monitor your vector health</figcaption>
<figure>
Alternatively, you can monitor the health of a dataset using the command below which returns the count of total missing and existing fields in the data points in the named dataset.

@@@ dataset_health @@@

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/general-features/creating-a-dataset/_assets/health.png?raw=true" width="607" alt="Dataset health".png" />
<figcaption>Monitoring dataset health</figcaption>
<figure>

### Deleting a dataset

Deleting an existing dataset can be done on the dashboard using the delete option availabal for each dataset. Or through the Python SDK:

@@@ delete_dataset, DATASET_ID=ECOMMERCE_SAMPLE_DATASET_ID @@@
