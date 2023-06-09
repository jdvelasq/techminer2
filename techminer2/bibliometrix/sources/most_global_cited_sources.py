# flake8: noqa
"""
Most Global Cited Sources
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_sources.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.most_global_cited_sources(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_global_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
source_abbr
J ECON BUS                       153
NORTHWEST J INTL LAW BUS         150
J BANK REGUL                      35
PALGRAVE STUD DIGIT BUS ENABL     33
DUKE LAW J                        30
Name: global_citations, dtype: int64


>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'source_abbr' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                   |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| J ECON BUS                    |     1 |                153 |                17 |                           153   |                           17   |
| NORTHWEST J INTL LAW BUS      |     1 |                150 |                 0 |                           150   |                            0   |
| J BANK REGUL                  |     2 |                 35 |                 9 |                            17.5 |                            4.5 |
| PALGRAVE STUD DIGIT BUS ENABL |     1 |                 33 |                14 |                            33   |                           14   |
| DUKE LAW J                    |     1 |                 30 |                 0 |                            30   |                            0   |
| J RISK FINANC                 |     1 |                 21 |                 8 |                            21   |                            8   |
| J MONEY LAUND CONTROL         |     1 |                 14 |                 3 |                            14   |                            3   |
| J FINANC CRIME                |     2 |                 13 |                 4 |                             6.5 |                            2   |
| FINANCIAL INNOV               |     1 |                 13 |                 1 |                            13   |                            1   |
| ICEIS - PROC INT CONF ENTERP  |     1 |                 12 |                 3 |                            12   |                            3   |
| HELIYON                       |     1 |                 11 |                 4 |                            11   |                            4   |
| HANDBBLOCKCHAIN, DIGIT FINANC |     1 |                 11 |                 3 |                            11   |                            3   |
| J RISK MANG FINANCIAL INST    |     1 |                  8 |                 5 |                             8   |                            5   |
| ADV INTELL SYS COMPUT         |     1 |                  7 |                 1 |                             7   |                            1   |
| INTELL SYST ACCOUNT FINANCE M |     1 |                  5 |                 3 |                             5   |                            3   |
| ADELAIDE LAW REV              |     1 |                  5 |                 1 |                             5   |                            1   |
| J FINANCIAL DATA SCI          |     1 |                  5 |                 1 |                             5   |                            1   |
| UNIV NEW SOUTH WALES LAW J    |     1 |                  4 |                 3 |                             4   |                            3   |
| LECTURE NOTES DATA ENG COMMUN |     1 |                  4 |                 0 |                             4   |                            0   |
| J ANTITRUST ENFORC            |     1 |                  3 |                 3 |                             3   |                            3   |
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def most_global_cited_sources(
    root_dir="./",
    database="main",
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    metric_label=None,
    field_label=None,
    title=None,
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
    """Most global cited sources.

    Args:
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
        title = "Most Global Cited Sources"

    return bbx_generic_indicators_by_item(
        fnc_view=list_view,
        field="source_abbr",
        root_dir=root_dir,
        database=database,
        metric="global_citations",
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
