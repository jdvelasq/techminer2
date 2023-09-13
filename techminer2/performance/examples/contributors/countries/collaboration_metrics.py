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


>>> from techminer2.performance import collaboration_metrics
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> metrics.fig_.write_html("sphinx/_static/performance/contributors/countries/collaboration_metrics.html")

.. raw:: html

    <iframe src="../../../../_static/performance/contributors/countries/collaboration_metrics.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(metrics.df_.head().to_markdown())
| countries      |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:---------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| United Kingdom |     7 |                199 |                35 |                    4 |                      3 |       0.43 |
| Australia      |     7 |                199 |                31 |                    4 |                      3 |       0.43 |
| United States  |     6 |                 59 |                19 |                    4 |                      2 |       0.33 |
| Ireland        |     5 |                 55 |                22 |                    4 |                      1 |       0.2  |
| China          |     5 |                 27 |                 5 |                    2 |                      3 |       0.6  |


>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
