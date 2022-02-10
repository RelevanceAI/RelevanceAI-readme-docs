---
title: "Or"
slug: "or"
excerpt: "How to filter when you have multiple filter requirements"
hidden: false
createdAt: "2021-12-14T02:24:01.377Z"
updatedAt: "2022-01-19T05:18:17.107Z"
---
# Or


The `or` filter helps you filter for multiple conditions. Unlike other filters, the only values used here are `filter_type` and `condition_value`.
```python Python (SDK)
from relevanceai import Client
client = Client()

filters = [{
	'filter_type' : 'or',
	"condition_value": [
 {
 'field' : 'price',
 'filter_type' : 'numeric',
 "condition":"<=", "condition_value":90
 },
 {
 'field' : 'price',
 'filter_type' : 'numeric',
 "condition":">=",
 "condition_value": 150
 }
 ]}
]

```
```python
```

@@@ filter_dataset @@@

## (A or B) and (C or D)

Below, we show an example of how to use 2 lists of filters with `or` logic.
```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{
	'filter_type' : 'or',
	"condition_value": [
 {
 'field' : 'price',
 'filter_type' : 'numeric',
 "condition":"<=",
 "condition_value":90
 },
 {
 'field' : 'price',
 'filter_type' : 'numeric',
 "condition":">=",
 "condition_value": 150
 }
 ]},
 'filter_type' : 'or',
	"condition_value": [
 {
 'field' : 'animal',
 'filter_type' : 'category',
 "condition":"==",
 "condition_value":"cat"
 },
 {
 'field' : 'animal',
 'filter_type' : 'category',
 "condition":"==",
 "condition_value": "dog"
 }
 ]},
]

```
```python
```

@@@ filter_dataset @@@


## (A or B or C) and D

Below, we show an example of how to use 2 lists of filters with `or` logic.

```python Python (SDK)
from relevanceai import Client
client = Client()

filter = [{
	'filter_type' : 'or',
	"condition_value": [
 {
 'field' : 'price',
 'filter_type' : 'numeric',
 "condition":"<=",
 "condition_value":90
 },
 {
 'field' : 'price',
 'filter_type' : 'numeric',
 "condition":">=",
 "condition_value": 150
 },
 {
 'field' : 'value',
 'filter_type' : 'numeric',
 "condition":">=",
 "condition_value": 2
 },
 ],
 {
 'field' : 'animal',
 'filter_type' : 'category',
 "condition":"==",
 "condition_value":"cat"
 },
]

```
```python
```
@@@ filter_dataset @@@