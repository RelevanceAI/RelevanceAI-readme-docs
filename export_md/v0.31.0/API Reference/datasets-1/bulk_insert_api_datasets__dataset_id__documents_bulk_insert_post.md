---
title: "Inserting documents"
slug: "bulk_insert_api_datasets__dataset_id__documents_bulk_insert_post"
excerpt: "* When inserting the document you can optionally specify your own id for a document by using the field name **\"\\_id\"**, if not specified a random id is assigned. \n * When inserting or specifying vectors in a document use the suffix (ends with)  **\"\\_vector\\_\"** for the field name. e.g. \"product\\_description\\_vector\\_\".\n * When inserting or specifying chunks in a document the suffix (ends with)  **\"\\_chunk\\_\"** for the field name. e.g. \"products\\_chunk\\_\".\n * When inserting or specifying chunk vectors in a document's chunks use the suffix (ends with)  **\"\\_chunkvector\\_\"** for the field name. e.g. \"products_chunk_.product\\_description\\_chunkvector\\_\".\n\nTry to keep each batch of documents to insert under 200mb to avoid the insert timing out. For single document insert version of this request use **/datasets/{dataset_id}/documents/insert**."
hidden: false
createdAt: "2021-10-20T23:17:23.916Z"
updatedAt: "2021-10-20T23:17:23.916Z"
---
