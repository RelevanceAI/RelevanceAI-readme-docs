---
title: "Group by and metrics"
slug: "aggregate_v2_api_services_aggregate_aggregate_post"
excerpt: "Aggregation/Groupby of a collection using an aggregation query.\nThe aggregation query is a json body that follows the schema of:\n\n    {\n        \"groupby\" : [\n            {\"name\": <alias>, \"field\": <field in the collection>, \"agg\": \"category\"},\n            {\"name\": <alias>, \"field\": <another groupby field in the collection>, \"agg\": \"numeric\"}\n        ],\n        \"metrics\" : [\n            {\"name\": <alias>, \"field\": <numeric field in the collection>, \"agg\": \"avg\"}\n            {\"name\": <alias>, \"field\": <another numeric field in the collection>, \"agg\": \"max\"}\n        ]\n    }\n    For example, one can use the following aggregations to group score based on region and player name.\n    {\n        \"groupby\" : [\n            {\"name\": \"region\", \"field\": \"player_region\", \"agg\": \"category\"},\n            {\"name\": \"player_name\", \"field\": \"name\", \"agg\": \"category\"}\n        ],\n        \"metrics\" : [\n            {\"name\": \"average_score\", \"field\": \"final_score\", \"agg\": \"avg\"},\n            {\"name\": \"max_score\", \"field\": \"final_score\", \"agg\": \"max\"},\n            {'name':'total_score','field':\"final_score\", 'agg':'sum'},\n            {'name':'average_deaths','field':\"final_deaths\", 'agg':'avg'},\n            {'name':'highest_deaths','field':\"final_deaths\", 'agg':'max'},\n        ]\n    }\n- \"groupby\" is the fields you want to split the data into. These are the available groupby types:\n    - category\" : groupby a field that is a category\n    - numeric: groupby a field that is a numeric\n- \"metrics\" is the fields you want to metrics you want to calculate in each of those, every aggregation includes a frequency metric. These are the available metric types:\n    - \"avg\", \"max\", \"min\", \"sum\", \"cardinality\"\n\nThe response returned has the following in descending order.\n\nIF you want to return documents, specify a \"group_size\" parameter and a \"select_fields\" parameter if you want to limit the specific fields chosen. \nThis looks as such: \n\n    {\n      'groupby':[\n        {'name':'Manufacturer','field':'manufacturer','agg':'category',\n        'group_size': 10, 'select_fields': [\"name\"]},\n      ],\n      'metrics':[\n        {'name':'Price Average','field':'price','agg':'avg'},\n      ],\n    }\n\n    {\"title\": {\"title\": \"books\", \"frequency\": 200, \"documents\": [{...}, {...}]}, {\"title\": \"books\", \"frequency\": 100, \"documents\": [{...}, {...}]}}"
hidden: false
createdAt: "2021-10-20T23:17:23.935Z"
updatedAt: "2021-10-20T23:17:23.935Z"
---