---
title: "Writing aggregation queries"
slug: "writing-aggregation-queries"
excerpt: "Learn how to power your cluster app visualizations"
hidden: false
createdAt: "2022-01-05T06:28:28.695Z"
updatedAt: "2022-01-05T06:28:35.415Z"
---
When using your Cluster app in the dashboard, you'll be prompted to write aggregation queries to power visualisations for previewing your clusters. You'll have to write these queries in JSON.

The basic form of an aggregation query looks like this:
```json Python (SDK)
{
 "groupby": [],
 "metrics": []
}
```
```json
```
Your aggregation query *must* include both of these fields, even if the arrays are empty.

### Groupby

Groupby is how you split up your data in your aggregation query. You can split up (groupby) your data either categorically, or numerically.

Types of groupby aggregations: `category`, `numeric`

For example:
```json Python (SDK)
{
 "groupby": [
 {
 "name": "manufacturer",
 "field": "manufacturer_en",
 "agg": "category"
 },
 {
 "name": "rrp",
 "field": "retail_price",
 "agg": "numeric"
 }
 ],
 "metrics": []
}
```
```json
```
### Metrics

Metrics are used to calculate statistics for your aggregated groups. Every aggregation will include a "frequency" metric by default.

Types of metric aggregations: `avg`, `max`, `min`, `sum`, `cardinality`

For example:
```json Python (SDK)
{
 "metrics": [
 {
 "name": "average_retail_price",
 "field": "retail_price",
 "agg": "avg"
 },
 {
 "name": "total_retail_price",
 "field": "retail_price",
 "agg": "sum"
 }
 ],
 "groupby": []
}
```
```json
```
Combined, here is an example of an aggregation query that groups the data and then calculates relevant metrics:
```json Python (SDK)
{
 "groupby": [
 {
 "name": "manufacturer",
 "field": "manufacturer_en",
 "agg": "category"
 }
 ],
 "metrics": [
 	{
 "name": "average_retail_price",
 "field": "retail_price",
 "agg": "avg"
 },
 {
 "name": "total_retail_price",
 "field": "retail_price",
 "agg": "sum"
 }
 ]
}
```
```json
```
