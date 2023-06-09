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
| organizations             |   h_index |
|:--------------------------|----------:|
| Univ of Hong Kong (HKG)   |         3 |
| Univ Coll Cork (IRL)      |         2 |
| Ahlia Univ (BHR)          |         2 |
| Coventry Univ (GBR)       |         2 |
| Univ of Westminster (GBR) |         2 |




>>> print(r.prompt_)
Analyze the table below, which provides impact indicators for the field 'organizations' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                                      |   OCC |   global_citations |   first_pb_year |   age |   h_index |   g_index |   m_index |   global_citations_per_year |   avg_global_citations |
|:-------------------------------------------------------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| Univ of Hong Kong (HKG)                                            |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Univ Coll Cork (IRL)                                               |     3 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  13.67 |
| Ahlia Univ (BHR)                                                   |     3 |                 19 |            2020 |     4 |         2 |         2 |      0.5  |                        4.75 |                   6.33 |
| Coventry Univ (GBR)                                                |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Univ of Westminster (GBR)                                          |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Dublin City Univ (IRL)                                             |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| Kingston Bus Sch (GBR)                                             |     1 |                153 |            2018 |     6 |         1 |         1 |      0.17 |                       25.5  |                 153    |
| FinTech HK, Hong Kong (HKG)                                        |     1 |                150 |            2017 |     7 |         1 |         1 |      0.14 |                       21.43 |                 150    |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |     1 |                150 |            2017 |     7 |         1 |         1 |      0.14 |                       21.43 |                 150    |
| Duke Univ Sch of Law (USA)                                         |     1 |                 30 |            2016 |     8 |         1 |         1 |      0.12 |                        3.75 |                  30    |
| Heinrich-Heine-Univ (DEU)                                          |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| UNSW Sydney, Kensington, Australia (AUS)                           |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| Univ of Luxembourg (LUX)                                           |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| Univ of Zurich (CHE)                                               |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| European Central B (DEU)                                           |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Harvard Univ Weatherhead ctr for International Affairs (USA)       |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| KS Strategic, London, United Kingdom (GBR)                         |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Panepistemio Aigaiou, Chios, Greece (GRC)                          |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Sch of Eng (CHE)                                                   |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Hebei Univ of Technol (CHN)                                        |     1 |                 13 |            2022 |     2 |         1 |         1 |      0.5  |                        6.5  |                  13    |
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
    database="main",
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
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
    """Plots the selected impact measure by organizations.


    Args:
        metric (str, optional): Impact metric. Defaults to "h_index".
        root_dir (str): path to the database directory.
        database (str): name of the database.
        textfont_size (int, optional): Font size. Defaults to 10.
        marker_size (int, optional): Marker size. Defaults to 6.
        line_color (str, optional): Line color. Defaults to "black".
        line_width (int, optional): Line width. Defaults to 1.
        yshift (int, optional): Y shift. Defaults to 4.
        metric_label (str): metric label.
        field_label (str): field label.
        title (str): plot title.
        top_n (int): number of items to be plotted.
        occ_range (tuple): range of occurrences.
        gc_range (tuple): range of global citations.
        custom_items (list): list of items to be plotted.
        year_filter (tuple): range of years.
        cited_by_filter (tuple): range of citations.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        BasicChart: A basic chart object.

    # pylint: disable=line-too-long
    """

    if title is None:
        title = f"Organization Impact by {metric.replace('_', ' ').title()}"

    return bbx_generic_indicators_by_item(
        fnc_view=impact_view,
        field="organizations",
        root_dir=root_dir,
        database=database,
        metric=metric,
        # Plot options:
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
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
