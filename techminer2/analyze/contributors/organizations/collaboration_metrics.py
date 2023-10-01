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
...     field="organizations",
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
>>> metrics.fig_.write_html("sphinx/_static/analyze/contributors/organizations/collaboration_metrics.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/contributors/organizations/collaboration_metrics.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(metrics.df_.head().to_markdown())
| organizations             |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:--------------------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| Univ of Hong Kong (HKG)   |     3 |                185 |                24 |                    0 |                      3 |       1    |
| Univ Coll Cork (IRL)      |     3 |                 41 |                19 |                    2 |                      1 |       0.33 |
| Ahlia Univ (BHR)          |     3 |                 19 |                 3 |                    0 |                      3 |       1    |
| Coventry Univ (GBR)       |     2 |                 17 |                 4 |                    0 |                      2 |       1    |
| Univ of Westminster (GBR) |     2 |                 17 |                 4 |                    0 |                      2 |       1    |


>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
