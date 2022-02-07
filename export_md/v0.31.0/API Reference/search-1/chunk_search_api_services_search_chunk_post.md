---
title: "Chunk search"
slug: "chunk_search_api_services_search_chunk_post"
excerpt: "Chunks are data that has been divided into different units. e.g. A paragraph is made of many sentence chunks, a sentence is made of many word chunks, an image frame in a video. By searching through chunks you can pinpoint more specifically where a match is occuring.\nWhen creating a chunk in your document use the suffix \"_chunk_\" and \"_chunkvector_\". An example of a document with chunks:\n\n    {\n        \"_id\" : \"123\",\n        \"title\" : \"Lorem Ipsum Article\",\n        \"description\" : \"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\",\n        \"description_vector_\" : [1.1, 1.2, 1.3],\n        \"description_sentence_chunk_\" : [\n            {\"sentence_id\" : 0, \"sentence_chunkvector_\" : [0.1, 0.2, 0.3], \"sentence\" : \"Lorem Ipsum is simply dummy text of the printing and typesetting industry.\"},\n            {\"sentence_id\" : 1, \"sentence_chunkvector_\" : [0.4, 0.5, 0.6], \"sentence\" : \"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\"},\n            {\"sentence_id\" : 2, \"sentence_chunkvector_\" : [0.7, 0.8, 0.9], \"sentence\" : \"It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\"},\n        ]\n    }\n\nFor combining chunk search with other search checkout **/services/search/advanced_chunk**."
hidden: false
createdAt: "2021-10-20T23:17:23.931Z"
updatedAt: "2021-10-20T23:17:23.931Z"
---