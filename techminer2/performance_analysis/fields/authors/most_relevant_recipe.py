# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Relevant (Recipe)
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='authors',
...     metric="OCCGC",
...     #
...     # CHART PARAMS:
...     title=None,
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # ITEM FILTERS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(items.df_.to_markdown())
| authors           |   rank_occ |   rank_gc |   OCC |   global_citations |
|:------------------|-----------:|----------:|------:|-------------------:|
| Arner DW          |          1 |         1 |     3 |                185 |
| Buckley RP        |          2 |         2 |     3 |                185 |
| Barberis JN       |          3 |         3 |     2 |                161 |
| Butler T          |          4 |         5 |     2 |                 41 |
| Hamdan A          |          5 |        15 |     2 |                 18 |
| Turki M           |          6 |        16 |     2 |                 18 |
| Lin W             |          7 |        17 |     2 |                 17 |
| Singh C           |          8 |        18 |     2 |                 17 |
| Brennan R         |          9 |        19 |     2 |                 14 |
| Crane M           |         10 |        20 |     2 |                 14 |
| Anagnostopoulos I |         16 |         4 |     1 |                153 |
| OBrien L          |         17 |         6 |     1 |                 33 |
| Baxter LG         |         18 |         7 |     1 |                 30 |
| Weber RH          |         19 |         8 |     1 |                 24 |
| Zetzsche DA       |         20 |         9 |     1 |                 24 |
| Breymann W        |         21 |        10 |     1 |                 21 |



>>> items.fig_.write_html("sphinx/_static/performance_analysis/fields/authors/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/authors/most_relevant_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors           |   rank_occ |   rank_gc |   OCC |   global_citations |
|:------------------|-----------:|----------:|------:|-------------------:|
| Arner DW          |          1 |         1 |     3 |                185 |
| Buckley RP        |          2 |         2 |     3 |                185 |
| Barberis JN       |          3 |         3 |     2 |                161 |
| Butler T          |          4 |         5 |     2 |                 41 |
| Hamdan A          |          5 |        15 |     2 |                 18 |
| Turki M           |          6 |        16 |     2 |                 18 |
| Lin W             |          7 |        17 |     2 |                 17 |
| Singh C           |          8 |        18 |     2 |                 17 |
| Brennan R         |          9 |        19 |     2 |                 14 |
| Crane M           |         10 |        20 |     2 |                 14 |
| Anagnostopoulos I |         16 |         4 |     1 |                153 |
| OBrien L          |         17 |         6 |     1 |                 33 |
| Baxter LG         |         18 |         7 |     1 |                 30 |
| Weber RH          |         19 |         8 |     1 |                 24 |
| Zetzsche DA       |         20 |         9 |     1 |                 24 |
| Breymann W        |         21 |        10 |     1 |                 21 |
```
<BLANKLINE>


"""
