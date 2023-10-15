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
| organizations                                         |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:------------------------------------------------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| Univ. of Zurich (CHE)                                 |     3 |                434 |                 4 |                    3 |                      0 |          0 |
| Federal Reserve Bank of Philadelphia (USA)            |     3 |                317 |                 2 |                    0 |                      3 |          1 |
| Baylor Univ. (USA)                                    |     2 |                395 |                 0 |                    0 |                      2 |          1 |
| Max Planck Inst. for Innovation and Competition (DEU) |     2 |                358 |                 2 |                    0 |                      2 |          1 |
| Univ. of New South Wales (AUS)                        |     2 |                340 |                 2 |                    0 |                      2 |          1 |


>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
