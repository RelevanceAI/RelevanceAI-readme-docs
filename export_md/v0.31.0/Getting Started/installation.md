---
title: "Installation"
slug: "installation"
excerpt: "Installing RelevanceAI"
hidden: false
createdAt: "2021-10-26T04:06:08.694Z"
updatedAt: "2022-02-06T23:09:08.172Z"
---
**Relevance AI is tested on Python 3.6+ on Windows, Linux and MacOS.**

### Installation

The easiest way to install our Python SDK is to run:

```bash Bash
!pip install -U RelevanceAI[notebook]==0.31.0
```
```bash
```

This installation provides you with what you need to connect to RelevanceAI's API, read/write data, make different searches, etc.

**The SDK Reference** can be found at https://relevanceai.readthedocs.io/en/0.31.0/

### Installation from source

This will install the latest version of our Python SDK:


```bash Bash
!pip install git+https://github.com/RelevanceAI/RelevanceAI@0.31.0
```
```bash
```


For editable installation:


```bash Bash
git clone -b 0.31.0 https://github.com/RelevanceAI/RelevanceAI
pip install -e .
```
```bash
```

### Setting Up Client

> 👍 Free for individual use. 100K free requests for commercial use.
>
> Sign up for your free at https://cloud.relevance.ai/sdk/api, no credit card required! You can view our pricing here at https://relevance.ai/pricing.

After installation is complete, we need to instantiate a Relevance AI client object which requires you to sign up at https://cloud.relevance.ai/


@@@client_instantiation


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/0.31.0/docs_template/getting-started/_assets/RelevanceAI_auth_token_details.png?raw=true" alt="Get your Auth Details" />
<figcaption>Get your Auth Details</figcaption>
<figure>