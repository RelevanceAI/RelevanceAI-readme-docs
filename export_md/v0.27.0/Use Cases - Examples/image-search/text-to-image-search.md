---
title: "Text To Image Search"
slug: "text-to-image-search"
hidden: true
createdAt: "2021-10-28T09:03:03.102Z"
updatedAt: "2021-11-02T00:38:50.718Z"
---
TODO:
[ ] Complete commentary and examples
[ ] Show exploration
[ ] Add notebook


[block:code]
{
  "codes": [
    {
      "code": "!pip install -U -q vecdb vectorhub[clip]\n\n## Setting up\nfrom vecdb import VecDBClient\nfrom vecdb.datasets import get_ecommerce_dataset\nfrom vectorhub.bi_encoders.text_image.torch import Clip2Vec\nclip = Clip2Vec()\n\nproject = <API-USERNAME>  # Project name\napi_key = <API-KEY>       # API Key\ndataset_id = 'ecommerce-demo'\n\nclient = VecDBClient(project, api_key)\n\n## 1. Prepare your data\ndocs = get_ecommerce_dataset(number_of_documents=1000)\n\n## 2. Encode or vectorise your data with VectorHub\nencoded_data = clip.encode_documents([\n  \t\t\t\t\t\t\t\t\t\"product_title\", \n  \t\t\t\t\t\t\t\t\t\"product_description\", \n  \t\t\t\t\t\t\t\t\t\"product_image\"], \n  \t\t\t\t\t\t\t\tdata)\n\n## 3. Index and upload your data to VecDB\nfor d in encoded_data:\n    d['_id'] = str(d['_unit_id'])\nclient.insert_documents(dataset_id = dataset_id, \n                    docs = encoded_data,\n                    max_workers = None    ## Setting max_workers to None will use all available cores \n                    )\n\n## 4. Perform text to image search on your data with VecDB\nquery = 'Playstation 4'\nresults = client.services.search.vector(\n    dataset_id,\n    [{\n      \"vector\": clip.encode_text(query), \n      \"fields\": [\n          \"product_image_clip_vector_\",\n      ]\n      }])\n\n## TODO: Display images\n",
      "language": "python",
      "name": "Python (VecDB SDK)"
    }
  ]
}
[/block]