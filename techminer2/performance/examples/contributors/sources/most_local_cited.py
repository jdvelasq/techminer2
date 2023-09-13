# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Local Cited
===============================================================================

>>> from techminer2.performance import performance_metrics
>>> root_dir = "data/regtech/"
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='source_abbr',
...     metric="local_citations",
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
| source_abbr                   |   rank_gcs |   rank_lcs |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:------------------------------|-----------:|-----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| J ECON BUS                    |          1 |          1 |                153 |                17 |                           153   |                           17   |                       25.5  |
| NORTHWEST J INTL LAW BUS      |          2 |          2 |                150 |                16 |                           150   |                           16   |                       21.43 |
| PALGRAVE STUD DIGIT BUS ENABL |          4 |          3 |                 33 |                14 |                            33   |                           14   |                        6.6  |
| J BANK REGUL                  |          3 |          4 |                 35 |                 9 |                            17.5 |                            4.5 |                        8.75 |
| DUKE LAW J                    |          5 |          5 |                 30 |                 8 |                            30   |                            8   |                        3.75 |
| J RISK FINANC                 |          6 |          6 |                 21 |                 8 |                            21   |                            8   |                        3.5  |
| J RISK MANG FINANCIAL INST    |         13 |          7 |                  8 |                 5 |                             8   |                            5   |                        1.33 |
| J FINANC CRIME                |          8 |          8 |                 13 |                 4 |                             6.5 |                            2   |                        3.25 |
| J MONEY LAUND CONTROL         |          7 |          9 |                 14 |                 3 |                            14   |                            3   |                        3.5  |
| ICEIS - PROC INT CONF ENTERP  |         10 |         10 |                 12 |                 3 |                            12   |                            3   |                        3    |



>>> items.fig_.write_html("sphinx/_static/performance/contributors/sources/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/sources/most_local_cited_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
