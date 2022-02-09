---
title: "Image Similarity Search"
slug: "image-similarity-search"
hidden: true
createdAt: "2021-10-28T08:55:01.732Z"
updatedAt: "2021-12-11T14:24:57.292Z"
---
TODO:
[ ] Complete commentary and examples
[ ] Show exploration
[ ] Add notebook

[block:code]
{
  "codes": [
    {
      "code": "!pip install -U -q relevanceai[notebook] vectorhub[encoders-image-tfhub]\n\n## Setting up\nfrom relevanceai import Client\nfrom relevanceai.datasets import get_ecommerce_dataset\nfrom vectorhub.encoders.image.tfhub import BitMedium2Vec\nbit = BitMedium2Vec()\n\nproject = <API-USERNAME>  # Project name\napi_key = <API-KEY>       # API Key\ndataset_id = 'ecommerce-demo'\n\nclient = Client(project, api_key)\n\n## 1. Prepare your data\ndocs = get_ecommerce_dataset(number_of_documents=1000)\n\n## 2. Encode or vectorise your data with VectorHub\nencoded_data = bit.encode_documents([\"product_image\"], data)\n\n## 3. Index and upload your data to VecDB\nfor d in encoded_data:\n    d['_id'] = str(d['_unit_id'])\nclient.insert_documents(dataset_id = dataset_id, \n                    docs = encoded_data,\n                    max_workers = None    ## Setting max_workers to None will use all available cores \n                    )\n\n## 4. Perform vector search on your data with RelevanceAI\nquery = 'Playstation 4'\nresults = client.services.search.vector(\n    dataset_id,\n    [{\n      \"vector\": bit.encode(query), \n      \"fields\": [\n          \"product_image_bit_vector_\",\n      ]\n      }])\n\n## TODO: Display similar images\n\nr = [res for res in results['product_description']]",
      "language": "python",
      "name": "Python (VecDB SDK)"
    }
  ]
}
[/block]