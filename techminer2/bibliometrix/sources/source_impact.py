# flake8: noqa
"""
Source Impact
===============================================================================



Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__source_impact.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.source_impact(
...     metric='h_index',
...     top_n=20, 
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__source_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| source_abbr                   |   h_index |
|:------------------------------|----------:|
| J BANK REGUL                  |         2 |
| J FINANC CRIME                |         2 |
| J ECON BUS                    |         1 |
| NORTHWEST J INTL LAW BUS      |         1 |
| PALGRAVE STUD DIGIT BUS ENABL |         1 |


>>> print(r.prompt_)
Analyze the table below, which provides impact indicators for the field 'source_abbr' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                   |   OCC |   global_citations |   first_pb_year |   age |   h_index |   g_index |   m_index |   global_citations_per_year |   avg_global_citations |
|:------------------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| J BANK REGUL                  |     2 |                 35 |            2020 |     4 |         2 |         2 |      0.5  |                        8.75 |                   17.5 |
| J FINANC CRIME                |     2 |                 13 |            2020 |     4 |         2 |         1 |      0.5  |                        3.25 |                    6.5 |
| J ECON BUS                    |     1 |                153 |            2018 |     6 |         1 |         1 |      0.17 |                       25.5  |                  153   |
| NORTHWEST J INTL LAW BUS      |     1 |                150 |            2017 |     7 |         1 |         1 |      0.14 |                       21.43 |                  150   |
| PALGRAVE STUD DIGIT BUS ENABL |     1 |                 33 |            2019 |     5 |         1 |         1 |      0.2  |                        6.6  |                   33   |
| DUKE LAW J                    |     1 |                 30 |            2016 |     8 |         1 |         1 |      0.12 |                        3.75 |                   30   |
| J RISK FINANC                 |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                   21   |
| J MONEY LAUND CONTROL         |     1 |                 14 |            2020 |     4 |         1 |         1 |      0.25 |                        3.5  |                   14   |
| FINANCIAL INNOV               |     1 |                 13 |            2022 |     2 |         1 |         1 |      0.5  |                        6.5  |                   13   |
| ICEIS - PROC INT CONF ENTERP  |     1 |                 12 |            2020 |     4 |         1 |         1 |      0.25 |                        3    |                   12   |
| HANDBBLOCKCHAIN, DIGIT FINANC |     1 |                 11 |            2017 |     7 |         1 |         1 |      0.14 |                        1.57 |                   11   |
| HELIYON                       |     1 |                 11 |            2020 |     4 |         1 |         1 |      0.25 |                        2.75 |                   11   |
| J RISK MANG FINANCIAL INST    |     1 |                  8 |            2018 |     6 |         1 |         1 |      0.17 |                        1.33 |                    8   |
| ADV INTELL SYS COMPUT         |     1 |                  7 |            2021 |     3 |         1 |         1 |      0.33 |                        2.33 |                    7   |
| ADELAIDE LAW REV              |     1 |                  5 |            2020 |     4 |         1 |         1 |      0.25 |                        1.25 |                    5   |
| INTELL SYST ACCOUNT FINANCE M |     1 |                  5 |            2020 |     4 |         1 |         1 |      0.25 |                        1.25 |                    5   |
| J FINANCIAL DATA SCI          |     1 |                  5 |            2019 |     5 |         1 |         1 |      0.2  |                        1    |                    5   |
| LECTURE NOTES DATA ENG COMMUN |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                    4   |
| UNIV NEW SOUTH WALES LAW J    |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                    4   |
| EUR J RISK REGUL              |     1 |                  3 |            2022 |     2 |         1 |         1 |      0.5  |                        1.5  |                    3   |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import impact_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def source_impact(
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
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the selected impact measure by source.

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
        title = f"Source Impact by {metric.replace('_', ' ').title()}"

    return bbx_generic_indicators_by_item(
        fnc_view=impact_view,
        field="source_abbr",
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
