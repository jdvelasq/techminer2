# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_frequent_sources_recipe:

Most Frequent
===============================================================================

>>> from techminer2.performance_analysis import performance_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='source_abbr',
...     metric="OCC",
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
| source_abbr                   |   rank_occ |   OCC |
|:------------------------------|-----------:|------:|
| J BANK REGUL                  |          1 |     2 |
| J FINANC CRIME                |          2 |     2 |
| STUD COMPUT INTELL            |          3 |     2 |
| FOSTER INNOVCOMPET WITH FINTE |          4 |     2 |
| INT CONF INF TECHNOL SYST INN |          5 |     2 |
| ROUTLEDGE HANDBFINANCIAL TECH |          6 |     2 |
| J ECON BUS                    |          7 |     1 |
| NORTHWEST J INTL LAW BUS      |          8 |     1 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |     1 |
| DUKE LAW J                    |         10 |     1 |


>>> items.fig_.write_html("sphinx/_static/performance/sources/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/sources/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   rank_occ |   OCC |
|:------------------------------|-----------:|------:|
| J BANK REGUL                  |          1 |     2 |
| J FINANC CRIME                |          2 |     2 |
| STUD COMPUT INTELL            |          3 |     2 |
| FOSTER INNOVCOMPET WITH FINTE |          4 |     2 |
| INT CONF INF TECHNOL SYST INN |          5 |     2 |
| ROUTLEDGE HANDBFINANCIAL TECH |          6 |     2 |
| J ECON BUS                    |          7 |     1 |
| NORTHWEST J INTL LAW BUS      |          8 |     1 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |     1 |
| DUKE LAW J                    |         10 |     1 |
```
<BLANKLINE>


"""