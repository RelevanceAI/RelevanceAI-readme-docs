---
title: "Installation"
excerpt: "Installing RelevanceAI"
slug: "installation"
hidden: false

---

**Relevance AI is tested on Python 0.31.0+ on Windows, Linux and MacOS.**

### Installation

The easiest way to install our Python SDK is to run: 

```bash Bash
!pip install -U -q RelevanceAI==0.31.0
```
```bash
```

This installation provides you with what you need to connect to RelevanceAI's API, read/write data, make different searches, etc.

**The SDK Reference** can be found at https://relevanceai.readthedocs.io/en/v0.31.0/

### Installation from source

This will install the latest version of our Python SDK:


```bash Bash
!pip install git+https://github.com/RelevanceAI/RelevanceAI@v0.31.0
```
```bash
```


For editable installation:


```bash Bash
git clone -b v0.31.0 https://github.com/RelevanceAI/RelevanceAI
pip install -e .
```
```bash
```

### Setting Up Client

> 👍 Free for individual use. 100K free requests for commercial use.
> 
> Sign up for your free at https://cloud.relevance.ai/sdk/api, no credit card required! You can view our pricing here at https://relevance.ai/pricing.

After we install, we want to also set up the client. If you are missing an API key, grab your API key from https://cloud.relevance.ai/ in the [Settings](https://cloud.relevance.ai/settings) area and let's get started!


```python Python (SDK)
from relevanceai import Client 

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Authorization token` and paste it here
"""
client = Client()

```
```python
```


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.31.0/docs_template/GETTING_STARTED/_assets/RelevanceAI_auth_token_details.png?raw=true" alt="Get your Auth Details" />
<figcaption>Get your Auth Details</figcaption>
<figure>

Once you've retrieved your authentication credentials, you can instantiate your client in future in the following manner.


```python Python (SDK)

from relevanceai import Client 

project = <API Project>
api_key = <API Key>

client = Client(project=project, api_key=api_key)

```
```python
```

The key can also be found here:

<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v0.31.0/docs_template/GETTING_STARTED/_assets/RelevanceAI_auth_setting_details.png?raw=true" alt="Find your API and project key here in Settings" />
<figcaption>Find your API and project key in Project Settings</figcaption>
<figure>
