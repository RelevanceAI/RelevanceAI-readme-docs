---
title: "🌱 How to build image to text search using code"
slug: "how-to-build-image-to-text-search-using-code"
excerpt: "A guide on building text to image/image to text search with Relevance AI"
hidden: true
createdAt: "2021-10-20T03:08:30.713Z"
updatedAt: "2021-09-13T06:41:30.913Z"
---
**Assumed Knowledge**: Vectors, Vector Search, Python (Basic level)
**Target Audience**: General Developer, Data Scientist, Python Developer
**Reading Time**: 5 minutes
**Requirements**: Python 3.6 or Python 3.7

To build text to image search, you will need a text to image model. An example of a text to image model is OpenAI's CLIP. You can read more about CLIP as a model [here](https://hub.getvectorai.com/model/text_image%2Fclip).


[block:code]
{
  "codes": [
    {
      "code": "!pip install vectorhub[clip]\nfrom vectorhub.bi_encoders.text_image.torch import Clip2Vec\nmodel = Clip2Vec() # This will download and run the model",
      "language": "python"
    },
    {
      "code": "pub fn nth(n: u32) -> u32 {\n    if n == 0 {\n        return 2\n    }\n    let mut primes: Vec<u32> = vec![2];\n    for c in 3..u32::max_value() {\n        if primes.len() as u32 > n {\n            break;\n        } else if c % 2 == 0 {\n            continue;\n        } else {\n            for i in 0..primes.len() {\n                if c % primes[i] == 0 {\n                    break;\n                } else if i == primes.len() - 1 {\n                    primes.push(c as u32);\n                    break;\n                }\n            }\n        }\n    }\n    primes[n as usize]\n}",
      "language": "rust"
    }
  ]
}
[/block]
To encode the text, you can run the following in Python:

[block:code]
{
  "codes": [
    {
      "code": "model.encode_text(\"This is a dog.\")",
      "language": "python"
    }
  ]
}
[/block]
To encode images, you can run the following in Python (if you are curious about the encoding process for images, you can read about it here.