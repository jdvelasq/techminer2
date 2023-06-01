# flake8: noqa
"""
Country Impact (*)
===============================================================================



Example
-------------------------------------------------------------------------------


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_impact.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.country_impact(
...     metric='h_index',
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| countries      |   h_index |
|:---------------|----------:|
| Australia      |         4 |
| United Kingdom |         4 |
| Hong Kong      |         3 |
| United States  |         3 |
| Ireland        |         3 |



>>> print(r.prompt_)
Analyze the table below, which provides impact indicators for the field 'countries' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries            |   OCC |   global_citations |   first_pb_year |   age |   h_index |   g_index |   m_index |   global_citations_per_year |   avg_global_citations |
|:---------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| Australia            |     7 |                199 |            2017 |     7 |         4 |         3 |      0.57 |                       28.43 |                  28.43 |
| United Kingdom       |     7 |                199 |            2018 |     6 |         4 |         3 |      0.67 |                       33.17 |                  28.43 |
| Hong Kong            |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| United States        |     6 |                 59 |            2016 |     8 |         3 |         2 |      0.38 |                        7.38 |                   9.83 |
| Ireland              |     5 |                 55 |            2018 |     6 |         3 |         2 |      0.5  |                        9.17 |                  11    |
| Germany              |     4 |                 51 |            2018 |     6 |         3 |         2 |      0.5  |                        8.5  |                  12.75 |
| China                |     5 |                 27 |            2017 |     7 |         3 |         2 |      0.43 |                        3.86 |                   5.4  |
| Switzerland          |     4 |                 45 |            2017 |     7 |         2 |         2 |      0.29 |                        6.43 |                  11.25 |
| Luxembourg           |     2 |                 34 |            2020 |     4 |         2 |         2 |      0.5  |                        8.5  |                  17    |
| Bahrain              |     4 |                 19 |            2020 |     4 |         2 |         2 |      0.5  |                        4.75 |                   4.75 |
| United Arab Emirates |     2 |                 13 |            2020 |     4 |         2 |         1 |      0.5  |                        3.25 |                   6.5  |
| Greece               |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Japan                |     1 |                 13 |            2022 |     2 |         1 |         1 |      0.5  |                        6.5  |                  13    |
| Jordan               |     1 |                 11 |            2020 |     4 |         1 |         1 |      0.25 |                        2.75 |                  11    |
| South Africa         |     1 |                 11 |            2021 |     3 |         1 |         1 |      0.33 |                        3.67 |                  11    |
| Italy                |     5 |                  5 |            2019 |     5 |         1 |         1 |      0.2  |                        1    |                   1    |
| Spain                |     2 |                  4 |            2021 |     3 |         1 |         1 |      0.33 |                        1.33 |                   2    |
| Ukraine              |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                   4    |
| Malaysia             |     1 |                  3 |            2019 |     5 |         1 |         1 |      0.2  |                        0.6  |                   3    |
| India                |     1 |                  1 |            2020 |     4 |         1 |         1 |      0.25 |                        0.25 |                   1    |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import impact_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def country_impact(
    metric="h_index",
    root_dir="./",
    database="documents",
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
    """Plots the selected impact measure by country.


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
        title = f"Country Impact by {metric.replace('_', ' ').title()}"

    return bbx_generic_indicators_by_item(
        fnc_view=impact_view,
        field="countries",
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
