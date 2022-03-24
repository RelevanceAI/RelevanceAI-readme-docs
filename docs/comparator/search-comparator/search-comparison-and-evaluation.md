---
title: "Model comparison via the search comparator"
slug: "search-comparison-and-evaluation"
hidden: true
createdAt: "2021-10-26T02:57:56.828Z"
updatedAt: "2021-10-27T22:30:04.698Z"
---
## Providing the queries
Queries on which the models are compared against each other must be presented to the search comparator through a list using the `add_queries` function.
[block:code]
{
  "codes": [
    {
      "code": "queries = [\n     'How to chose the best gift?',\n     'Which are sport outfit brands?',\n     'Features of handmade pottery?',\n     'What is the best dress size for me?',\n     'options to match colors?',\n     'What is so good about stainless steel?',\n     'product to avoid dust',\n     'Golden necklace',\n     'Swarovski necklace',\n     'best gift for kids',\n     'gift for female boss']\ncomparator.add_queries(queries)",
      "language": "python"
    }
  ]
}
[/block]
##  Running the evaluator
The next step, after the queries are added, is running the evaluator function. It calls the defined searches and stores the results for further comparison(s)analysis.
[block:code]
{
  "codes": [
    {
      "code": "comparator.evaluate()",
      "language": "python"
    }
  ]
}
[/block]
## What are the responses to the queries?
The built-in function `compare_results` returns all the search results from the defined searches. Here, we present a screenshot on a table view (side note: the table headers are modified for this guide and this table is not representative of the quality of vector or hybrid search or the underlying models.).
[block:code]
{
  "codes": [
    {
      "code": "present_field_in_result=\"product_name\"    # product name is a field in the database\ndisplay(comparator.compare_results(query, present_field_in_result))",
      "language": "python"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f2c285a-compare_results1.png",
        "compare_results1.png",
        1549,
        379,
        "#ededed"
      ],
      "caption": "compare_results output"
    }
  ]
}
[/block]
## How do models score compared to one another?
### On a single query
As was mentioned earlier search comparator relies on ranking and statistical comparison of the Top-K results. Pairwise comparisons for **a single query** are accessible via `plot_comparisons_by_query`. This function plots a table view of the pairwise comparison scores. Scores are bounded between 0 and 1, with color-coding of white to dark blue respectively. This is helpful to identify what the different queries are to which two different models respond similarly or vice-versa.
[block:code]
{
  "codes": [
    {
      "code": "query = \"product to avoid dust\"\ncomparator.plot_comparisons_by_query(query)",
      "language": "python"
    }
  ]
}
[/block]
For instance, running the code above results in the following table. As expected the scores on the main diagonal of the matrix (i.e. comparing a model with itself) are all 1. We can see the first model (vec-search-original) shows almost zero similarity with the rest of the models [0.000, 0.034, 0.000]. This indicates the fine-tunning that was performed on the original model has had a big effect. We can see more similarities (0.459) between the other pair of original and fine-tuned models (hyb-search-original, hyb-search-finetuned).
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fa4f30c-plot_comparisons_by_query5.png",
        "plot_comparisons_by_query5.png",
        660,
        120,
        "#d4dce3"
      ],
      "caption": "plot_comparisons_by_query for the query \"product to avoid dust\""
    }
  ]
}
[/block]
Another example of such a plot in which the scores are larger indicating more similarities in the result lists:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/94cb5aa-plot_comparisons_by_query1.png",
        "plot_comparisons_by_query1.png",
        653,
        110,
        "#cad6de"
      ],
      "caption": "plot_comparisons_by_query for the query \"What is so good about stainless steel?\""
    }
  ]
}
[/block]
### Across all queries
The `compare_two_searches` function is designed to provide scores that are the result of comparing two models on the whole query set. Unlike the previous function, which focuses on a single query, `compare_two_searches` provides a general overview of the two models which is more informative. Since, here, and under a general overview, some queries that are tricky or edge-case for the model(s) can be identified more easily. For instance, the first screenshot below shows the comparison between  `vec-search-original`, `vec-search-finetuned`, we can see the query "options to match colors?" has the lowest score!
[block:code]
{
  "codes": [
    {
      "code": "comparator.compare_two_searches(\"vec-search-original\", \"vec-search-finetuned\")",
      "language": "python"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6a9279e-compare_two_searches24.png",
        "compare_two_searches(2,4).png",
        1541,
        295,
        "#dee4e9"
      ],
      "caption": "compare_two_searches sample 1"
    }
  ]
}
[/block]
Having a similar comparison between `vec-search-original` and `vec-search-finetuned`, we can see results are similar for only a few queries. At the same time, these models seem to have more similarities in the results for the two conceptually related queries "How to choose the best gift?" and "best gift for kids".
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6cf301f-compare_two_searches13.png",
        "compare_two_searches(1,3).png",
        1547,
        298,
        "#e2e6eb"
      ],
      "caption": "compare_two_searches sample 2"
    }
  ]
}
[/block]
## Final words
As was explained in the guide, working with the search comparator is very easy and straightforward. Some of the benefits are:
1. Easy to install and use
2. Flexible on model types
3. Flexible on the search approach
4. No need to start from scratch when there is a new model; simply add it via `add_search`
5. Various comparison functions
6. Comprehendable and easy to follow result presentation
