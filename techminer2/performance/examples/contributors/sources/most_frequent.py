# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
.. _most_frequent_sources_recipe:

Performance Metrics
===============================================================================

>>> from techminer2.performance import performance_metrics
>>> items = performance_metrics(
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
| source_abbr                   |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| J BANK REGUL                  |          1 |     2 |             2 |                   0 |                   0 |
| J FINANC CRIME                |          2 |     2 |             1 |                   1 |                  50 |
| STUD COMPUT INTELL            |          3 |     2 |             2 |                   0 |                   0 |
| FOSTER INNOVCOMPET WITH FINTE |          4 |     2 |             2 |                   0 |                   0 |
| INT CONF INF TECHNOL SYST INN |          5 |     2 |             0 |                   2 |                 100 |
| ROUTLEDGE HANDBFINANCIAL TECH |          6 |     2 |             2 |                   0 |                   0 |
| J ECON BUS                    |          7 |     1 |             1 |                   0 |                   0 |
| NORTHWEST J INTL LAW BUS      |          8 |     1 |             1 |                   0 |                   0 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |     1 |             1 |                   0 |                   0 |
| DUKE LAW J                    |         10 |     1 |             1 |                   0 |                   0 |



>>> items.fig_.write_html("sphinx/_static/performance/contributors/sources/most_frequent_chart.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/sources/most_frequent_chart.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
