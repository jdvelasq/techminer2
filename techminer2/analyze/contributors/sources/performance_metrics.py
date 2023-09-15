# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Performance metrics
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> root_dir = "data/regtech/"
>>> items = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='source_abbr',
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
>>> print(items.df_.head().to_markdown())
| source_abbr                   |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:------------------------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| J BANK REGUL                  |          1 |          3 |          4 |     2 |                 35 |                 9 |         2 |         2 |      0.5  |
| J FINANC CRIME                |          2 |          8 |          8 |     2 |                 13 |                 4 |         2 |         1 |      0.5  |
| STUD COMPUT INTELL            |          3 |         28 |         23 |     2 |                  1 |                 1 |         1 |         1 |      0.33 |
| FOSTER INNOVCOMPET WITH FINTE |          4 |         30 |         31 |     2 |                  1 |                 0 |         1 |         1 |      0.25 |
| INT CONF INF TECHNOL SYST INN |          5 |         37 |         37 |     2 |                  0 |                 0 |         0 |         0 |      0    |



>>> items.fig_.write_html("sphinx/_static/analyze/contributors/sources/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/sources/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
