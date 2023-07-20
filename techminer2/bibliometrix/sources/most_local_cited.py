# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Most Local Cited
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> items = bibliometrix.sources.most_local_cited(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(items.df_.to_markdown())
| source_abbr                   |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:------------------------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| J ECON BUS                    |         1 |                153 |                17 |                           153   |                           17   |                       25.5  |
| PALGRAVE STUD DIGIT BUS ENABL |         4 |                 33 |                14 |                            33   |                           14   |                        6.6  |
| J BANK REGUL                  |         3 |                 35 |                 9 |                            17.5 |                            4.5 |                        8.75 |
| J RISK FINANC                 |         6 |                 21 |                 8 |                            21   |                            8   |                        3.5  |
| J RISK MANG FINANCIAL INST    |        13 |                  8 |                 5 |                             8   |                            5   |                        1.33 |
| J FINANC CRIME                |         8 |                 13 |                 4 |                             6.5 |                            2   |                        3.25 |
| HELIYON                       |        11 |                 11 |                 4 |                            11   |                            4   |                        2.75 |
| J MONEY LAUND CONTROL         |         7 |                 14 |                 3 |                            14   |                            3   |                        3.5  |
| ICEIS - PROC INT CONF ENTERP  |        10 |                 12 |                 3 |                            12   |                            3   |                        3    |
| HANDBBLOCKCHAIN, DIGIT FINANC |        12 |                 11 |                 3 |                            11   |                            3   |                        1.57 |


>>> items.fig_.write_html("sphinx/_static/bibliometrix/sources/most_local_cited_chart.html")

.. raw:: html

    <iframe src="../../../../_static/bibliometrix/sources/most_local_cited_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'local_citations' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   rank_gc |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   global_citations_per_year |
|:------------------------------|----------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------------:|
| J ECON BUS                    |         1 |                153 |                17 |                           153   |                           17   |                       25.5  |
| PALGRAVE STUD DIGIT BUS ENABL |         4 |                 33 |                14 |                            33   |                           14   |                        6.6  |
| J BANK REGUL                  |         3 |                 35 |                 9 |                            17.5 |                            4.5 |                        8.75 |
| J RISK FINANC                 |         6 |                 21 |                 8 |                            21   |                            8   |                        3.5  |
| J RISK MANG FINANCIAL INST    |        13 |                  8 |                 5 |                             8   |                            5   |                        1.33 |
| J FINANC CRIME                |         8 |                 13 |                 4 |                             6.5 |                            2   |                        3.25 |
| HELIYON                       |        11 |                 11 |                 4 |                            11   |                            4   |                        2.75 |
| J MONEY LAUND CONTROL         |         7 |                 14 |                 3 |                            14   |                            3   |                        3.5  |
| ICEIS - PROC INT CONF ENTERP  |        10 |                 12 |                 3 |                            12   |                            3   |                        3    |
| HANDBBLOCKCHAIN, DIGIT FINANC |        12 |                 11 |                 3 |                            11   |                            3   |                        1.57 |
```
<BLANKLINE>

"""
from ...vantagepoint.discover import list_items

FIELD = "source_abbr"
METRIC = "local_citations"


def most_local_cited(
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
