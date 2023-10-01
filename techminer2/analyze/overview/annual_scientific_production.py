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
|   2016 |     1 |
|   2017 |     4 |
|   2018 |     3 |
|   2019 |     6 |
|   2020 |    14 |
|   2021 |    10 |
|   2022 |    12 |
|   2023 |     2 |



>>> print(metrics.df_.T.to_markdown())
|     |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:----|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| OCC |      1 |      4 |      3 |      6 |     14 |     10 |     12 |      2 |



>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
