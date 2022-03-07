---
title: "Installation"
excerpt: "Installing RelevanceAI"
slug: "installation"
hidden: false

---

**Relevance AI is tested on Python 3.6+ on Windows, Linux and MacOS.**

### Installation

The easiest way to install our Python SDK is to run:

```bash Bash
# remove `!` if running the line in a terminal
!pip install -U RelevanceAI[notebook]==1.4.0
```
```bash
```

This installation provides you with what you need to connect to RelevanceAI's API, read/write data, make different searches, etc.

**The SDK Reference** can be found at https://relevanceai.readthedocs.io/en/v1.4.0

/

### Installation from source

This will install the latest version of our Python SDK:


```bash Bash
!pip install git+https://github.com/RelevanceAI/RelevanceAI@v1.4.0


```
```bash
```


For editable installation:


```bash Bash
git clone -b v1.4.0

 https://github.com/RelevanceAI/RelevanceAI
pip install -e .
```
```bash
```

### Setting Up Client

> 👍 Free for individual use. 100K free requests for commercial use.
>
> Sign up for your free at https://cloud.relevance.ai/sdk/api, no credit card required! You can view our pricing here at https://relevance.ai/pricing.

After installation is complete, we need to instantiate a Relevance AI client object which requires you to sign up at https://cloud.relevance.ai/


```python Python (SDK)
from relevanceai import Client

"""
You can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api
Once you have signed up, click on the value under `Activation token` and paste it here
"""
client = Client()
```
```python
```


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v1.4.0

/docs_template/_assets/RelevanceAI_auth_token_details.png?raw=true" alt="Get your Auth Details" />
<figcaption>Get your Auth Details</figcaption>
<figure>

