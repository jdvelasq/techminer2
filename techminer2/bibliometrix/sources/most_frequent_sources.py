# flake8: noqa
"""
Most Frequent Sources
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_sources.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.most_frequent_sources(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_frequent_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
source_abbr
J BANK REGUL                     2
J FINANC CRIME                   2
FOSTER INNOV AND COMPET WITH     2
STUD COMPUT INTELL               2
INT CONF INF TECHNOL SYST INN    2
Name: OCC, dtype: int64


>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'source_abbr' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                   |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| J BANK REGUL                  |     2 |                 35 |                 9 |                            17.5 |                            4.5 |
| J FINANC CRIME                |     2 |                 13 |                 4 |                             6.5 |                            2   |
| FOSTER INNOV AND COMPET WITH  |     2 |                  1 |                 1 |                             0.5 |                            0.5 |
| STUD COMPUT INTELL            |     2 |                  1 |                 1 |                             0.5 |                            0.5 |
| INT CONF INF TECHNOL SYST INN |     2 |                  0 |                 0 |                             0   |                            0   |
| ROUTLEDGE HANDB OF FIN TECHNO |     2 |                  0 |                 0 |                             0   |                            0   |
| J ECON BUS                    |     1 |                153 |                17 |                           153   |                           17   |
| NORTHWEST J INTL LAW BUS      |     1 |                150 |                 0 |                           150   |                            0   |
| PALGRAVE STUD DIGIT BUS ENABL |     1 |                 33 |                14 |                            33   |                           14   |
| DUKE LAW J                    |     1 |                 30 |                 0 |                            30   |                            0   |
| J RISK FINANC                 |     1 |                 21 |                 8 |                            21   |                            8   |
| J MONEY LAUND CTRL            |     1 |                 14 |                 3 |                            14   |                            3   |
| FIN INNOV                     |     1 |                 13 |                 1 |                            13   |                            1   |
| ICEIS - PROC INT CONF ENTERP  |     1 |                 12 |                 3 |                            12   |                            3   |
| HELIYON                       |     1 |                 11 |                 4 |                            11   |                            4   |
| HANDB OF BLOCKCHAIN, DIGIT FI |     1 |                 11 |                 3 |                            11   |                            3   |
| J RISK MANG FIN INST          |     1 |                  8 |                 5 |                             8   |                            5   |
| ADV INTELL SYS COMPUT         |     1 |                  7 |                 1 |                             7   |                            1   |
| INTELL SYST ACCOUNT FIN MANAG |     1 |                  5 |                 3 |                             5   |                            3   |
| ADELAIDE LAW REV              |     1 |                  5 |                 1 |                             5   |                            1   |
<BLANKLINE>
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ..utils import bbx_indicators_by_item


def most_frequent_sources(
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
    """Most Relevant Sources.

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


    """

    if title is None:
        title = "Most Frequent Sources"

    return bbx_indicators_by_item(
        field="source_abbr",
        root_dir=root_dir,
        database=database,
        metric="OCC",
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
