# flake8: noqa
"""
Author Impact
===============================================================================



Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__author_impact.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.author_impact(
...     metric='h_index',
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__author_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| authors     |   h_index |
|:------------|----------:|
| Arner DW    |         3 |
| Buckley RP  |         3 |
| Barberis JN |         2 |
| Butler T/1  |         2 |
| Hamdan A    |         2 |


>>> print(r.prompt_)
Analyze the table below, which provides impact indicators for the field 'authors' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| authors           |   OCC |   global_citations |   first_pb_year |   age |   h_index |   g_index |   m_index |   global_citations_per_year |   avg_global_citations |
|:------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| Arner DW          |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Buckley RP        |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Barberis JN       |     2 |                161 |            2017 |     7 |         2 |         2 |      0.29 |                       23    |                  80.5  |
| Butler T/1        |     2 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  20.5  |
| Hamdan A          |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |
| Turki M           |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |
| Lin W             |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Singh C           |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Brennan R         |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| Crane M           |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| Ryan P            |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| Anagnostopoulos I |     1 |                153 |            2018 |     6 |         1 |         1 |      0.17 |                       25.5  |                 153    |
| OBrien L          |     1 |                 33 |            2019 |     5 |         1 |         1 |      0.2  |                        6.6  |                  33    |
| Baxter LG         |     1 |                 30 |            2016 |     8 |         1 |         1 |      0.12 |                        3.75 |                  30    |
| Weber RH          |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| Zetzsche DA       |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| Breymann W        |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Gross FJ          |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Kavassalis P      |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Saxton K          |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import impact_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def author_impact(
    metric="h_index",
    root_dir="./",
    database="documents",
    # Plot options:
    plot="cleveland_dot_chart",
    title=None,
    metric_label=None,
    field_label=None,
    # Item filters:
    top_n=20,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the selected impact measure by author."""

    if title is None:
        title = f"Author Impact by {metric.replace('_', ' ').title()}"

    return bbx_generic_indicators_by_item(
        fnc_view=impact_view,
        field="authors",
        root_dir=root_dir,
        database=database,
        metric=metric,
        # Plot options:
        plot=plot,
        metric_label=metric_label,
        field_label=field_label,
        title=title,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
