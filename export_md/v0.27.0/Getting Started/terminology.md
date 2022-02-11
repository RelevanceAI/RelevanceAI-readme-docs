---
title: "Terminology"
slug: "terminology"
excerpt: "Guide to the terminology used in Relevance AI"
hidden: false
createdAt: "2021-10-20T03:08:30.714Z"
updatedAt: "2022-01-10T12:30:15.221Z"
---
**Terminology**|**Definition**
:-----:|:-----:
Vectors| AKA embeddings, 1D arrays, latent space vectors
Vectorizers/models/Encoders|Turns data into vectors (e.g. Word2Vec turns words into vectors)
Vector Similarity Search|Nearest neighbor search, distance search
Dataset|Index, Table (a dataset is made up of multiple documents)
Documents|(AKA JSON, item, dictionary, data row) - a document can contain vectors and other important information (e.g. the shown example above)
Field|A field is a key in a Python dictionary (e.g. `product_title` or `product_description_vector_` in the example document above)
Value|A value is a value in a Python dictionary (e.g. `711158459` or `[0.01, 0.23, 0.45, 0.67, 0.89, 0.1, 0.12]` in the example document above)
Upload| (AKA index a dataset) is the process of uploading a dataset to Relevance AI platform