---
title: "Writing aggregation queries"
slug: "writing-aggregation-queries"
excerpt: "Learn how to power your cluster app visualizations"
hidden: true
createdAt: "2022-01-05T06:28:28.695Z"
updatedAt: "2022-01-05T06:28:35.415Z"
---
When using your Cluster app in the dashboard, you'll be prompted to write aggregation queries to power visualisations for previewing your clusters. You'll have to write these queries in JSON.

The basic form of an aggregation query looks like this:
[block:code]
{
  "codes": [
    {
      "code": "{\n \"groupby\": [],\n \"metrics\": []\n}",
      "language": "json"
    }
  ]
}
[/block]
Your aggregation query *must* include both of these fields, even if the arrays are empty.

### Groupby

Groupby is how you split up your data in your aggregation query. You can split up (groupby) your data either categorically, or numerically.

Types of groupby aggregations: `category`, `numeric`

For example:
[block:code]
{
  "codes": [
    {
      "code": "{\n \"groupby\": [\n   {\n     \"name\": \"manufacturer\",\n     \"field\": \"manufacturer_en\",\n     \"agg\": \"category\"\n   }, \n   {\n     \"name\": \"rrp\",\n     \"field\": \"retail_price\",\n     \"agg\": \"numeric\"\n   }\n  ],\n  \"metrics\": []\n}",
      "language": "json"
    }
  ]
}
[/block]
### Metrics

Metrics are used to calculate statistics for your aggregated groups. Every aggregation will include a "frequency" metric by default.

Types of metric aggregations: `avg`, `max`, `min`, `sum`, `cardinality`

For example:
[block:code]
{
  "codes": [
    {
      "code": "{\n \"metrics\": [\n   {\n     \"name\": \"average_retail_price\",\n     \"field\": \"retail_price\",\n     \"agg\": \"avg\"\n   }, \n   {\n     \"name\": \"total_retail_price\",\n     \"field\": \"retail_price\",\n     \"agg\": \"sum\"\n   }\n  ],\n  \"groupby\": []\n}",
      "language": "json"
    }
  ]
}
[/block]
Combined, here is an example of an aggregation query that groups the data and then calculates relevant metrics:
[block:code]
{
  "codes": [
    {
      "code": "{\n \"groupby\": [\n   {\n     \"name\": \"manufacturer\",\n     \"field\": \"manufacturer_en\",\n     \"agg\": \"category\"\n   }\n  ],\n  \"metrics\": [\n  \t{\n      \"name\": \"average_retail_price\",\n      \"field\": \"retail_price\",\n      \"agg\": \"avg\"\n    }, \n    {\n      \"name\": \"total_retail_price\",\n      \"field\": \"retail_price\",\n      \"agg\": \"sum\"\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]