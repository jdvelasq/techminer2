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
>>> items = bibliometrix.organizations.most_relevant(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(items.df_.to_markdown())
| organizations                                                      |   rank_occ |   rank_gc |   OCC |   global_citations |
|:-------------------------------------------------------------------|-----------:|----------:|------:|-------------------:|
| Univ of Hong Kong (HKG)                                            |          1 |         1 |     3 |                185 |
| Univ Coll Cork (IRL)                                               |          2 |         5 |     3 |                 41 |
| Ahlia Univ (BHR)                                                   |          3 |        16 |     3 |                 19 |
| Coventry Univ (GBR)                                                |          4 |        17 |     2 |                 17 |
| Univ of Westminster (GBR)                                          |          5 |        18 |     2 |                 17 |
| Dublin City Univ (IRL)                                             |          6 |        19 |     2 |                 14 |
| Politec di Milano (ITA)                                            |          7 |        50 |     2 |                  2 |
| Kingston Bus Sch (GBR)                                             |          8 |         2 |     1 |                153 |
| FinTech HK, Hong Kong (HKG)                                        |          9 |         3 |     1 |                150 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         10 |         4 |     1 |                150 |
| Duke Univ Sch of Law (USA)                                         |         11 |         6 |     1 |                 30 |
| Heinrich-Heine-Univ (DEU)                                          |         12 |         7 |     1 |                 24 |
| UNSW Sydney, Kensington, Australia (AUS)                           |         13 |         8 |     1 |                 24 |
| Univ of Luxembourg (LUX)                                           |         14 |         9 |     1 |                 24 |
| Univ of Zurich (CHE)                                               |         15 |        10 |     1 |                 24 |



>>> items.fig_.write_html("sphinx/_static/organizations_most_relevant_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/organizations_most_relevant_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'organizations' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| organizations                                                      |   rank_occ |   rank_gc |   OCC |   global_citations |
|:-------------------------------------------------------------------|-----------:|----------:|------:|-------------------:|
| Univ of Hong Kong (HKG)                                            |          1 |         1 |     3 |                185 |
| Univ Coll Cork (IRL)                                               |          2 |         5 |     3 |                 41 |
| Ahlia Univ (BHR)                                                   |          3 |        16 |     3 |                 19 |
| Coventry Univ (GBR)                                                |          4 |        17 |     2 |                 17 |
| Univ of Westminster (GBR)                                          |          5 |        18 |     2 |                 17 |
| Dublin City Univ (IRL)                                             |          6 |        19 |     2 |                 14 |
| Politec di Milano (ITA)                                            |          7 |        50 |     2 |                  2 |
| Kingston Bus Sch (GBR)                                             |          8 |         2 |     1 |                153 |
| FinTech HK, Hong Kong (HKG)                                        |          9 |         3 |     1 |                150 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         10 |         4 |     1 |                150 |
| Duke Univ Sch of Law (USA)                                         |         11 |         6 |     1 |                 30 |
| Heinrich-Heine-Univ (DEU)                                          |         12 |         7 |     1 |                 24 |
| UNSW Sydney, Kensington, Australia (AUS)                           |         13 |         8 |     1 |                 24 |
| Univ of Luxembourg (LUX)                                           |         14 |         9 |     1 |                 24 |
| Univ of Zurich (CHE)                                               |         15 |        10 |     1 |                 24 |
```
<BLANKLINE>


"""
from ...vantagepoint.discover import list_items

FIELD = "organizations"
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
