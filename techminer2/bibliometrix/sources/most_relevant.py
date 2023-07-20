# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Relevant
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> items = bibliometrix.sources.most_relevant(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(items.df_.to_markdown())
| source_abbr                   |   rank_occ |   rank_gc |   OCC |   global_citations |
|:------------------------------|-----------:|----------:|------:|-------------------:|
| J BANK REGUL                  |          1 |         3 |     2 |                 35 |
| J FINANC CRIME                |          2 |         8 |     2 |                 13 |
| FOSTER INNOVCOMPET WITH FINTE |          3 |        28 |     2 |                  1 |
| STUD COMPUT INTELL            |          4 |        29 |     2 |                  1 |
| INT CONF INF TECHNOL SYST INN |          5 |        36 |     2 |                  0 |
| ROUTLEDGE HANDBFINANCIAL TECH |          6 |        37 |     2 |                  0 |
| J ECON BUS                    |          7 |         1 |     1 |                153 |
| NORTHWEST J INTL LAW BUS      |          8 |         2 |     1 |                150 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |         4 |     1 |                 33 |
| DUKE LAW J                    |         10 |         5 |     1 |                 30 |
| J RISK FINANC                 |         11 |         6 |     1 |                 21 |
| J MONEY LAUND CONTROL         |         12 |         7 |     1 |                 14 |
| FINANCIAL INNOV               |         13 |         9 |     1 |                 13 |
| ICEIS - PROC INT CONF ENTERP  |         14 |        10 |     1 |                 12 |

>>> items.fig_.write_html("sphinx/_static/bibliometrix/sources/most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../_static/bibliometrix/sources/most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   rank_occ |   rank_gc |   OCC |   global_citations |
|:------------------------------|-----------:|----------:|------:|-------------------:|
| J BANK REGUL                  |          1 |         3 |     2 |                 35 |
| J FINANC CRIME                |          2 |         8 |     2 |                 13 |
| FOSTER INNOVCOMPET WITH FINTE |          3 |        28 |     2 |                  1 |
| STUD COMPUT INTELL            |          4 |        29 |     2 |                  1 |
| INT CONF INF TECHNOL SYST INN |          5 |        36 |     2 |                  0 |
| ROUTLEDGE HANDBFINANCIAL TECH |          6 |        37 |     2 |                  0 |
| J ECON BUS                    |          7 |         1 |     1 |                153 |
| NORTHWEST J INTL LAW BUS      |          8 |         2 |     1 |                150 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |         4 |     1 |                 33 |
| DUKE LAW J                    |         10 |         5 |     1 |                 30 |
| J RISK FINANC                 |         11 |         6 |     1 |                 21 |
| J MONEY LAUND CONTROL         |         12 |         7 |     1 |                 14 |
| FINANCIAL INNOV               |         13 |         9 |     1 |                 13 |
| ICEIS - PROC INT CONF ENTERP  |         14 |        10 |     1 |                 12 |
```
<BLANKLINE>



"""
from ...vantagepoint.discover import list_items

FIELD = "source_abbr"
METRIC = "OCCGC"


def most_relevant(
    #
    # ITEMS PARAMS:
    field=FIELD,
    metric=METRIC,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a rank chart."""

    return list_items(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
        #
        # CHART PARAMS:
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
