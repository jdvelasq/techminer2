# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.performance.overview.average_citations_per_year:

Average Citations per Year
===============================================================================


>>> from techminer2.analyze.overview import trend_metrics
>>> metrics = trend_metrics(
...     #
...     # TABLE PARAMS:
...     selected_columns=[
...         "mean_global_citations",
...     ],
...     #
...     # CHART PARAMS:
...     metric_to_plot="mean_global_citations",
...     auxiliary_metric_to_plot=None,
...     title="Average Citations per Year",
...     year_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> metrics.fig_.write_html("sphinx/_static/analyze/overview/average_citations_per_year.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/overview/average_citations_per_year.html"  
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(metrics.df_.to_markdown())
|   year |   mean_global_citations |
|-------:|------------------------:|
|   2016 |                30       |
|   2017 |                40.5     |
|   2018 |                60.6667  |
|   2019 |                 7.83333 |
|   2020 |                 6.64286 |
|   2021 |                 2.7     |
|   2022 |                 1.83333 |
|   2023 |                 0       |


>>> print(metrics.df_.T.to_markdown())
|                       |   2016 |   2017 |    2018 |    2019 |    2020 |   2021 |    2022 |   2023 |
|:----------------------|-------:|-------:|--------:|--------:|--------:|-------:|--------:|-------:|
| mean_global_citations |     30 |   40.5 | 60.6667 | 7.83333 | 6.64286 |    2.7 | 1.83333 |      0 |



>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""