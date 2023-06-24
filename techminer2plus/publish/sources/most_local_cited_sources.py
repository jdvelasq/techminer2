# flake8: noqa
"""
Most Local Cited Sources (from reference lists)
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/sources/most_local_cited_sources.html"

>>> import techminer2plus
>>> r = techminer2plus.publish.sources.most_local_cited_sources(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/examples/sources/most_local_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
source_abbr
J ECON BUS                       17
PALGRAVE STUD DIGIT BUS ENABL    14
J BANK REGUL                      9
J RISK FINANC                     8
J RISK MANG FINANCIAL INST        5
Name: local_citations, dtype: int64

>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'local_citations' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| J ECON BUS                    |     1 |             1 |                   0 |                153 |                17 |                           153   |                           17   |                   0   |                     0   |                        0    |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| PALGRAVE STUD DIGIT BUS ENABL |     1 |             1 |                   0 |                 33 |                14 |                            33   |                           14   |                   0   |                     0   |                        0    |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| J BANK REGUL                  |     2 |             2 |                   0 |                 35 |                 9 |                            17.5 |                            4.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        8.75 |         2 |         2 |      0.5  |
| J RISK FINANC                 |     1 |             1 |                   0 |                 21 |                 8 |                            21   |                            8   |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| J RISK MANG FINANCIAL INST    |     1 |             1 |                   0 |                  8 |                 5 |                             8   |                            5   |                   0   |                     0   |                        0    |                     2018 |     6 |                        1.33 |         1 |         1 |      0.17 |
| J FINANC CRIME                |     2 |             1 |                   1 |                 13 |                 4 |                             6.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        3.25 |         2 |         1 |      0.5  |
| HELIYON                       |     1 |             1 |                   0 |                 11 |                 4 |                            11   |                            4   |                   0   |                     0   |                        0    |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| J MONEY LAUND CONTROL         |     1 |             1 |                   0 |                 14 |                 3 |                            14   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        3.5  |         1 |         1 |      0.25 |
| ICEIS - PROC INT CONF ENTERP  |     1 |             1 |                   0 |                 12 |                 3 |                            12   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| HANDBBLOCKCHAIN, DIGIT FINANC |     1 |             1 |                   0 |                 11 |                 3 |                            11   |                            3   |                   0   |                     0   |                        0    |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| INTELL SYST ACCOUNT FINANCE M |     1 |             1 |                   0 |                  5 |                 3 |                             5   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| UNIV NEW SOUTH WALES LAW J    |     1 |             1 |                   0 |                  4 |                 3 |                             4   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| J ANTITRUST ENFORC            |     1 |             1 |                   0 |                  3 |                 3 |                             3   |                            3   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        1    |         1 |         1 |      0.33 |
| CEUR WORKSHOP PROC            |     1 |             1 |                   0 |                  2 |                 3 |                             2   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        0.5  |         1 |         1 |      0.25 |
| FRONTIER ARTIF INTELL         |     1 |             1 |                   0 |                  3 |                 2 |                             3   |                            2   |                   0   |                     0   |                        0    |                     2019 |     5 |                        0.6  |         1 |         1 |      0.2  |
| PROC - IEEE WORLD CONGR SERV, |     1 |             1 |                   0 |                  3 |                 2 |                             3   |                            2   |                   0   |                     0   |                        0    |                     2019 |     5 |                        0.6  |         1 |         1 |      0.2  |
| FINANCIAL INNOV               |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| ADV INTELL SYS COMPUT         |     1 |             1 |                   0 |                  7 |                 1 |                             7   |                            1   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        2.33 |         1 |         1 |      0.33 |
| ADELAIDE LAW REV              |     1 |             1 |                   0 |                  5 |                 1 |                             5   |                            1   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| J FINANCIAL DATA SCI          |     1 |             1 |                   0 |                  5 |                 1 |                             5   |                            1   |                   0   |                     0   |                        0    |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ...analyze import list_items
from ...report import ranking_chart


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_local_cited_sources(
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
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most local cited sources.

    Args:
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

        root_dir (str): path to the database directory.
        database (str): name of the database.
        year_filter (tuple): range of years.
        cited_by_filter (tuple): range of citations.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        BasicChart: A basic chart object.

    # pylint: disable=line-too-long
    """

    item_list = list_items(
        field="source_abbr",
        metric="local_citations",
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return ranking_chart(
        obj=item_list,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
