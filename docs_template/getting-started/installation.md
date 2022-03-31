---
title: "Installation"
excerpt: "Installing RelevanceAI"
slug: "installation"
hidden: false

---

**Relevance AI is tested on Python 3.6+ on Windows, Linux and MacOS.**

### Installation

The easiest way to install our Python SDK is to run:

@@@ relevanceai_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

This installation provides you with what you need to connect to RelevanceAI's API, read/write data, make different searches, etc.

**The SDK Reference** can be found at https://relevanceai.readthedocs.io/en/v2.0.0/

### Installation from source

This will install the latest version of our Python SDK:

@@@ relevanceai_git_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@


For editable installation:

@@@ relevanceai_editable_installation, RELEVANCEAI_SDK_VERSION=RELEVANCEAI_SDK_VERSION @@@

### Setting Up Client

> 👍 Free for individual use. 100K free requests for commercial use.
>
> Sign up for your free at https://cloud.relevance.ai/sdk/api, no credit card required! You can view our pricing here at https://relevance.ai/pricing.

After installation is complete, we need to instantiate a Relevance AI client object which requires you to sign up at https://cloud.relevance.ai/


@@@ client_instantiation @@@


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/_assets/RelevanceAI_auth_token_details.png?raw=true" alt="Get your Auth Details" />
<figcaption>Get your Auth Details</figcaption>
<figure>
