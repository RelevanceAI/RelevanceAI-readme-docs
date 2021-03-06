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
<figure>
<img src="https://files.readme.io/b3937c1-quickstart_datasets_view.png" width="1300" alt="quickstart_datasets_view.png" />
<figcaption>RelevanceAI Datasets</figcaption>
<figure>
## Interacting With Datasets

By storing data on our platform, you can directly invoke vectorization models, perform an optimized nearest-neighbor search, cluster data, etc.

Some basic actions to deal with datasets are:

- Create a dataset
- List the available datasets in a project/account
- Monitor a specific dataset
- Delete a dataset

You can either use the dashboard to take these actions or employ Relevance AI Python SDK. For the Python SDK, you need to install Relevance AI and initiate a client as shown in the two code snippets below:
```shell Python (SDK)
pip install -U RelevanceAI
```
```shell
```

```python Python (SDK)
from relevanceai import Client

"""
Running this cell will provide you with
the link to sign up/login page where you can find your credentials.
Once you have signed up, click on the value under `Authorization token`
in the API tab
and paste it in the Auth token box that appears below
"""

client = Client()
```
```python
```
### Creating a dataset
To create a new empty dataset pass the name under which you wish to save the dataset to the `create` function as shown below. In this example, we have used `ecommerce-sample-dataset` as the name.
```python Python (SDK)
client.datasets.create(dataset_id="ecommerce-sample-dataset")
```
```python
```
See [Inserting and updating documents](doc:inserting-data) for more details on how to insert/upload documents into a dataset.
> ???? Remember!
>
> * You cannot rename datasets or rename/edit existing field names. However, you can copy datasets and edit field names using the [`clone`](https://relevanceai.github.io/RelevanceAI/docs/html/relevanceai.api.endpoints.html?highlight=clone#relevanceai.api.endpoints.datasets.Datasets.clone) feature.
* Id field: Relevance AI platform identifies unique data entries within a dataset using a field called `_id` (i.e. every document in the dataset must include an `_id` field with a unique value per document).
* Vector fields: the name of vector fields must end in `_vector_`

### List your datasets

You can see a list of all datasets you have uploaded to your account in the dashboard.
<figure>
<img src="https://files.readme.io/fd97cbd-Screen_Shot_2022-01-17_at_12.21.57_pm.png" width="484" alt="Screen Shot 2022-01-17 at 12.21.57 pm.png" />
<figcaption>List of datasets in the dashboard</figcaption>
<figure>
Alternatively, you can use the list endpoint under Python SDK as shown below:
```python Python (SDK)
client.datasets.list()
```
```python
```
### Monitoring a specific dataset

RelevanceAI's dashboard at https://cloud.relevance.ai is the most straightforward place to monitor your data.
<figure>
<img src="https://files.readme.io/e9f331a-vector_health.png" width="1263" alt="vector_health.png" />
<figcaption>Monitor your vector health</figcaption>
<figure>
Alternatively, you can monitor the health of a dataset using the command below which returns the count of total missing and existing fields in the data points in the named dataset.
```python Python (SDK)
client.datasets.monitor.health("ecommerce-sample-dataset")

# Returns a count of total missing and existing data
```
```python
```

<figure>
<img src="https://files.readme.io/d2136ad-0aa6b74-Screen_Shot_2022-01-10_at_3.44.42_pm.png" width="607" alt="0aa6b74-Screen_Shot_2022-01-10_at_3.44.42_pm.png" />
<figcaption>Monitoring dataset health</figcaption>
<figure>
### Deleting a dataset

Deleting an existing dataset can be done on the dashboard using the Delete All Data button. Or through the following code. In this case, we are deleting the `ecommerce-dataset`:
<figure>
<img src="https://files.readme.io/8d8f670-Screen_Shot_2022-01-17_at_12.27.05_pm.png" width="1900" alt="Screen Shot 2022-01-17 at 12.27.05 pm.png" />
<figcaption>Dash board view</figcaption>
<figure>

```python Python (SDK)
client.datasets.delete(dataset_id = "ecommerce-sample-dataset")
```
```python
```
