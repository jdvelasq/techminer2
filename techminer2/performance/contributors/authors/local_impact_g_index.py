# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- G-Index
===============================================================================

>>> from techminer2.performance import performance_metrics
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='authors',
...     metric="g_index",
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
...     top_n=20,
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
| authors           |   h_index |   g_index |   m_index |
|:------------------|----------:|----------:|----------:|
| Arner DW          |         3 |         3 |      0.43 |
| Buckley RP        |         3 |         3 |      0.43 |
| Barberis JN       |         2 |         2 |      0.29 |
| Butler T          |         2 |         2 |      0.33 |
| Hamdan A          |         2 |         2 |      0.5  |
| Turki M           |         2 |         2 |      0.5  |
| Anagnostopoulos I |         1 |         1 |      0.17 |
| OBrien L          |         1 |         1 |      0.2  |
| Baxter LG         |         1 |         1 |      0.12 |
| Weber RH          |         1 |         1 |      0.25 |
| Zetzsche DA       |         1 |         1 |      0.25 |
| Breymann W        |         1 |         1 |      0.17 |
| Gross FJ          |         1 |         1 |      0.17 |
| Kavassalis P      |         1 |         1 |      0.17 |
| Saxton K          |         1 |         1 |      0.17 |
| Stieber H         |         1 |         1 |      0.17 |
| Lin W             |         2 |         1 |      0.5  |
| Singh C           |         2 |         1 |      0.5  |
| Brennan R         |         2 |         1 |      0.5  |
| Crane M           |         2 |         1 |      0.5  |


>>> items.fig_.write_html("sphinx/_static/performance/contributors/authors/g_index_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/authors/g_index_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'g_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors           |   h_index |   g_index |   m_index |
|:------------------|----------:|----------:|----------:|
| Arner DW          |         3 |         3 |      0.43 |
| Buckley RP        |         3 |         3 |      0.43 |
| Barberis JN       |         2 |         2 |      0.29 |
| Butler T          |         2 |         2 |      0.33 |
| Hamdan A          |         2 |         2 |      0.5  |
| Turki M           |         2 |         2 |      0.5  |
| Anagnostopoulos I |         1 |         1 |      0.17 |
| OBrien L          |         1 |         1 |      0.2  |
| Baxter LG         |         1 |         1 |      0.12 |
| Weber RH          |         1 |         1 |      0.25 |
| Zetzsche DA       |         1 |         1 |      0.25 |
| Breymann W        |         1 |         1 |      0.17 |
| Gross FJ          |         1 |         1 |      0.17 |
| Kavassalis P      |         1 |         1 |      0.17 |
| Saxton K          |         1 |         1 |      0.17 |
| Stieber H         |         1 |         1 |      0.17 |
| Lin W             |         2 |         1 |      0.5  |
| Singh C           |         2 |         1 |      0.5  |
| Brennan R         |         2 |         1 |      0.5  |
| Crane M           |         2 |         1 |      0.5  |
```
<BLANKLINE>

"""
