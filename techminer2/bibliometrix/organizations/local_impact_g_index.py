# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Local Impact --- G-Index
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> items = bibliometrix.organizations.local_impact_g_index(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> print(items.df_.to_markdown())
| organizations                                                      |   h_index |   g_index |   m_index |
|:-------------------------------------------------------------------|----------:|----------:|----------:|
| Univ of Hong Kong (HKG)                                            |         3 |         3 |      0.43 |
| Univ Coll Cork (IRL)                                               |         2 |         2 |      0.33 |
| Ahlia Univ (BHR)                                                   |         2 |         2 |      0.5  |
| Kingston Bus Sch (GBR)                                             |         1 |         1 |      0.17 |
| FinTech HK, Hong Kong (HKG)                                        |         1 |         1 |      0.14 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         1 |         1 |      0.14 |
| Duke Univ Sch of Law (USA)                                         |         1 |         1 |      0.12 |
| Heinrich-Heine-Univ (DEU)                                          |         1 |         1 |      0.25 |
| UNSW Sydney, Kensington, Australia (AUS)                           |         1 |         1 |      0.25 |
| Univ of Luxembourg (LUX)                                           |         1 |         1 |      0.25 |


>>> items.fig_.write_html("sphinx/_static/bibliometrix/organizations/g_index_chart.html")

.. raw:: html

    <iframe src="../../../../../_static/bibliometrix/organizations/g_index_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'organizations' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'g_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| organizations                                                      |   h_index |   g_index |   m_index |
|:-------------------------------------------------------------------|----------:|----------:|----------:|
| Univ of Hong Kong (HKG)                                            |         3 |         3 |      0.43 |
| Univ Coll Cork (IRL)                                               |         2 |         2 |      0.33 |
| Ahlia Univ (BHR)                                                   |         2 |         2 |      0.5  |
| Kingston Bus Sch (GBR)                                             |         1 |         1 |      0.17 |
| FinTech HK, Hong Kong (HKG)                                        |         1 |         1 |      0.14 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         1 |         1 |      0.14 |
| Duke Univ Sch of Law (USA)                                         |         1 |         1 |      0.12 |
| Heinrich-Heine-Univ (DEU)                                          |         1 |         1 |      0.25 |
| UNSW Sydney, Kensington, Australia (AUS)                           |         1 |         1 |      0.25 |
| Univ of Luxembourg (LUX)                                           |         1 |         1 |      0.25 |
```
<BLANKLINE>




"""
from ...vantagepoint.discover import list_items

FIELD = "organizations"
METRIC = "g_index"


def local_impact_g_index(
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
