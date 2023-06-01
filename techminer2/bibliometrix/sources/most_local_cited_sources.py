# flake8: noqa
"""
Most Local Cited Sources (from reference lists)
===============================================================================

Example
-------------------------------------------------------------------------------



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_sources.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.most_local_cited_sources(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_local_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
source_abbr
J ECON BUS                       17
PALGRAVE STUD DIGIT BUS ENABL    14
J BANK REGUL                      9
J RISK FINANC                     8
J RISK MANG FIN INST              5
Name: local_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'source_abbr' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                   |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| J ECON BUS                    |     1 |                153 |                17 |                           153   |                           17   |
| PALGRAVE STUD DIGIT BUS ENABL |     1 |                 33 |                14 |                            33   |                           14   |
| J BANK REGUL                  |     2 |                 35 |                 9 |                            17.5 |                            4.5 |
| J RISK FINANC                 |     1 |                 21 |                 8 |                            21   |                            8   |
| J RISK MANG FIN INST          |     1 |                  8 |                 5 |                             8   |                            5   |
| J FINANC CRIME                |     2 |                 13 |                 4 |                             6.5 |                            2   |
| HELIYON                       |     1 |                 11 |                 4 |                            11   |                            4   |
| J MONEY LAUND CTRL            |     1 |                 14 |                 3 |                            14   |                            3   |
| ICEIS - PROC INT CONF ENTERP  |     1 |                 12 |                 3 |                            12   |                            3   |
| HANDB OF BLOCKCHAIN, DIGIT FI |     1 |                 11 |                 3 |                            11   |                            3   |
| INTELL SYST ACCOUNT FIN MANAG |     1 |                  5 |                 3 |                             5   |                            3   |
| UNIV NEW SOUTH WALES LAW J    |     1 |                  4 |                 3 |                             4   |                            3   |
| J ANTITRUST ENFORC            |     1 |                  3 |                 3 |                             3   |                            3   |
| CEUR WKSHP PROC               |     1 |                  2 |                 3 |                             2   |                            3   |
| FRONTIER ARTIF INTELL         |     1 |                  3 |                 2 |                             3   |                            2   |
| PROC - IEEE WORLD CONGR SERV, |     1 |                  3 |                 2 |                             3   |                            2   |
| FIN INNOV                     |     1 |                 13 |                 1 |                            13   |                            1   |
| ADV INTELL SYS COMPUT         |     1 |                  7 |                 1 |                             7   |                            1   |
| ADELAIDE LAW REV              |     1 |                  5 |                 1 |                             5   |                            1   |
| J FIN DATA SCI                |     1 |                  5 |                 1 |                             5   |                            1   |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def most_local_cited_sources(
    root_dir="./",
    database="documents",
    # Plot options:
    plot="cleveland_dot_chart",
    metric_label=None,
    field_label=None,
    title=None,
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
    """Most local cited sources.

    Args:
        root_dir (str): path to the database directory.
        database (str): name of the database.
        plot (str): plot type. Options: 'bar_chart', 'cleveland_dot_chart', 'column_chart', 'line_chart'.
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

    return bbx_generic_indicators_by_item(
        fnc_view=list_view,
        field="source_abbr",
        root_dir=root_dir,
        database=database,
        metric="local_citations",
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
