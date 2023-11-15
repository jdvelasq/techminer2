# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Annual Scientific Production
===============================================================================


>>> from techminer2.analyze.overview import trend_metrics
>>> metrics = trend_metrics(
...     #
...     # TABLE PARAMS:
...     selected_columns=[
...         "OCC",
...     ],
...     #
...     # CHART PARAMS:
...     metric_to_plot="OCC",
...     auxiliary_metric_to_plot=None,
...     title="Annual Scientific Production",
...     year_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> metrics.fig_.write_html("sphinx/_static/analyze/overview/annual_scientific_production.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/overview/annual_scientific_production.html"  
    height="600px" width="100%" frameBorder="0"></iframe>



>>> print(metrics.df_.to_markdown())
|   year |   OCC |
|-------:|------:|
|   2015 |     1 |
|   2016 |     7 |
|   2017 |    10 |
|   2018 |    17 |
|   2019 |    15 |



>>> print(metrics.df_.T.to_markdown())
|     |   2015 |   2016 |   2017 |   2018 |   2019 |
|:----|-------:|-------:|-------:|-------:|-------:|
| OCC |      1 |      7 |     10 |     17 |     15 |



>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
