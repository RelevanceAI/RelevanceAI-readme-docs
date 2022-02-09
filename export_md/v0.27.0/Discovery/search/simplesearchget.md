---
title: "SimpleSearchGet"
slug: "simplesearchget"
excerpt: "All properties supported in the POST body can be set in query parameters when using GET method. \n    It returns the same response body SimpleSearchPost\n\n\n    For example: \n    \n    /latest/datasets/:dataset_id/simple_search?query=c&page=1&pageSize=1&fieldsToAggregate=[\"filter_field\"] \n    \n     \n    \n    Integer and string properies such as query, page, pageSize should be directly included as query parameters. \n    \n    Object properties such as \"fieldsToAggregate\" should be stringified as JSON, then included as parameters. \n    \n     \n    \n    For example, in javascript, use the following code to add an object query parameter: \n    \n    \"/latest/datasets/:dataset_id/simple_search?fieldsToAggregate=\"+JSON.stringify([\"filter_field\"])"
hidden: false
createdAt: "2021-10-20T23:10:36.465Z"
updatedAt: "2021-10-20T23:10:36.465Z"
---
