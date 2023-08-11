# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Local Impact --- M-Index
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='authors',
...     metric="m_index",
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
| authors   |   h_index |   g_index |   m_index |
|:----------|----------:|----------:|----------:|
| Hamdan A  |         2 |         2 |       0.5 |
| Turki M   |         2 |         2 |       0.5 |
| Lin W     |         2 |         1 |       0.5 |
| Singh C   |         2 |         1 |       0.5 |
| Brennan R |         2 |         1 |       0.5 |
| Crane M   |         2 |         1 |       0.5 |
| Ryan P    |         2 |         1 |       0.5 |
| Gong X    |         1 |         1 |       0.5 |
| Muganyi T |         1 |         1 |       0.5 |
| Sun H-P   |         1 |         1 |       0.5 |



>>> items.fig_.write_html("sphinx/_static/performance/authors/m_index_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/authors/m_index_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'm_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors   |   h_index |   g_index |   m_index |
|:----------|----------:|----------:|----------:|
| Hamdan A  |         2 |         2 |       0.5 |
| Turki M   |         2 |         2 |       0.5 |
| Lin W     |         2 |         1 |       0.5 |
| Singh C   |         2 |         1 |       0.5 |
| Brennan R |         2 |         1 |       0.5 |
| Crane M   |         2 |         1 |       0.5 |
| Ryan P    |         2 |         1 |       0.5 |
| Gong X    |         1 |         1 |       0.5 |
| Muganyi T |         1 |         1 |       0.5 |
| Sun H-P   |         1 |         1 |       0.5 |
```
<BLANKLINE>




"""
