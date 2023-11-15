# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Collaboration Metrics
===============================================================================


>>> from techminer2.analyze import collaboration_metrics
>>> metrics = collaboration_metrics(
...     # 
...     # PARAMS:
...     field='countries',
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> metrics.fig_.write_html("sphinx/_static/analyze/contributors/countries/collaboration_metrics.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/countries/collaboration_metrics.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(metrics.df_.head().to_markdown())
| countries     |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:--------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| United States |    16 |               3189 |                 8 |                    8 |                      8 |       0.5  |
| China         |     8 |               1085 |                 4 |                    3 |                      5 |       0.62 |
| Germany       |     7 |               1814 |                11 |                    4 |                      3 |       0.43 |
| South Korea   |     6 |               1192 |                 8 |                    4 |                      2 |       0.33 |
| Australia     |     5 |                783 |                 3 |                    1 |                      4 |       0.8  |


>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
