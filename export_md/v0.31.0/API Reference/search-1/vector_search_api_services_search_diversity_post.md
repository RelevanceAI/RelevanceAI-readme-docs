---
title: "Diversity search"
slug: "vector_search_api_services_search_diversity_post"
excerpt: "This will first perform an advanced search and then cluster the top X (page_size) search results.\nResults are returned as such:\nOnce you have the clusters:\n\n```\nCluster 0: [A, B, C]\nCluster 1: [D, E]\nCluster 2: [F, G]\nCluster 3: [H, I]\n```\n(Note, each cluster is ordered by highest to lowest search score.\n\nThis intermediately returns:\n\n```\nresults_batch_1: [A, H, F, D] (ordered by highest search score)\nresults_batch_2: [G, E, B, I] (ordered by highest search score)\nresults_batch_3: [C]\n```\n\nThis then returns the final results:\n\n```\nresults: [A, H, F, D, G, E, B, I, C]"
hidden: false
createdAt: "2021-10-20T23:17:23.934Z"
updatedAt: "2021-10-20T23:17:23.934Z"
---
