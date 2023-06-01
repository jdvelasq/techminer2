# flake8: noqa
"""
Organization Impact (*)
===============================================================================



Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__organization_impact.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.organization_impact(
...     metric='h_index',
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__organization_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| organizations           |   h_index |
|:------------------------|----------:|
| University of Hong Kong |         3 |
| ---FinTech HK           |         2 |
| University College Cork |         2 |
| Ahlia University        |         2 |
| Coventry University     |         2 |



>>> print(r.prompt_)
Analyze the table below, which provides impact indicators for the field 'organizations' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                                   |   OCC |   global_citations |   first_pb_year |   age |   h_index |   g_index |   m_index |   global_citations_per_year |   avg_global_citations |
|:----------------------------------------------------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| University of Hong Kong                                         |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| ---FinTech HK                                                   |     2 |                161 |            2017 |     7 |         2 |         2 |      0.29 |                       23    |                  80.5  |
| University College Cork                                         |     3 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  13.67 |
| Ahlia University                                                |     3 |                 19 |            2020 |     4 |         2 |         2 |      0.5  |                        4.75 |                   6.33 |
| Coventry University                                             |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| University of Westminster                                       |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Dublin City University                                          |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| ---Kingston Business School                                     |     1 |                153 |            2018 |     6 |         1 |         1 |      0.17 |                       25.5  |                 153    |
| ---Centre for Law                                               |     1 |                150 |            2017 |     7 |         1 |         1 |      0.14 |                       21.43 |                 150    |
| Duke University School of Law                                   |     1 |                 30 |            2016 |     8 |         1 |         1 |      0.12 |                        3.75 |                  30    |
| ---UNSW Sydney                                                  |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| Heinrich Heine University                                       |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| University of Luxembourg                                        |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| University of Zurich                                            |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| ---KS Strategic                                                 |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| ---Panepistemio Aigaiou                                         |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| ---School of Engineering                                        |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| European Central Bank                                           |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Harvard University Weatherhead Center for International Affairs |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Hebei University of Technology                                  |     1 |                 13 |            2022 |     2 |         1 |         1 |      0.5  |                        6.5  |                  13    |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import impact_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def organization_impact(
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
    """Plots the selected impact measure by organizations."""

    if title is None:
        title = f"Organization Impact by {metric.replace('_', ' ').title()}"

    return bbx_generic_indicators_by_item(
        fnc_view=impact_view,
        field="organizations",
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
