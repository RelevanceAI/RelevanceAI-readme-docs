---
title: "Installation"
excerpt: "Installing RelevanceAI"
slug: "installation"
hidden: false

---

**Relevance AI is tested on Python 3.6+ on Windows, Linux and MacOS.**

### Installation

The easiest way to install our Python SDK is to run:

[block:code]
{
  "codes": [
    {
      "code": "# remove `!` if running the line in a terminal\n!pip install -U RelevanceAI[notebook]==2.0.0",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]

This installation provides you with what you need to connect to RelevanceAI's API, read/write data, make different searches, etc.

**The SDK Reference** can be found at https://relevanceai.readthedocs.io/en/v2.0.0

### Installation from source

This will install the latest version of our Python SDK:

[block:code]
{
  "codes": [
    {
      "code": "!pip install git+https://github.com/RelevanceAI/RelevanceAI@v2.0.0",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]


For editable installation:

[block:code]
{
  "codes": [
    {
      "code": "git clone -b v2.0.0 https://github.com/RelevanceAI/RelevanceAI\npip install -e .",
      "name": "Bash",
      "language": "shell"
    }
  ]
}
[/block]

### Setting Up Client

> 👍 Free for individual use. 100K free requests for commercial use.
>
> Sign up for your free at https://cloud.relevance.ai/sdk/api, no credit card required! You can view our pricing here at https://relevance.ai/pricing.

After installation is complete, we need to instantiate a Relevance AI client object which requires you to sign up at https://cloud.relevance.ai/


[block:code]
{
  "codes": [
    {
      "code": "from relevanceai import Client\n\n\"\"\"\nYou can sign up/login and find your credentials here: https://cloud.relevance.ai/sdk/api\nOnce you have signed up, click on the value under `Activation token` and paste it here\n\"\"\"\nclient = Client()",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]


<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/docs_template/_assets/RelevanceAI_auth_token_details.png?raw=true" alt="Get your Auth Details" />
<figcaption>Get your Auth Details</figcaption>
<figure>

