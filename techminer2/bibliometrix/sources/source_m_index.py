# flake8: noqa
"""
Source M-Index
===============================================================================




>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__source_m_index.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.source_m_index(
...     top_n=20, 
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__source_m_index.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| source_abbr        |   m_index |
|:-------------------|----------:|
| J BANK REGUL       |       0.5 |
| J FINANC CRIME     |       0.5 |
| FINANCIAL INNOV    |       0.5 |
| EUR J RISK REGUL   |       0.5 |
| DECIS SUPPORT SYST |       0.5 |

>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of the \\
'source_abbr' field in a scientific bibliography database. Summarize the table below, \\
delimited by triple backticks, identify any notable patterns, trends, or outliers in \\
the data, and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| J BANK REGUL                  |     2 |             2 |                   0 |                 35 |                 9 |                            17.5 |                            4.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        8.75 |         2 |         2 |      0.5  |
| J FINANC CRIME                |     2 |             1 |                   1 |                 13 |                 4 |                             6.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        3.25 |         2 |         1 |      0.5  |
| FINANCIAL INNOV               |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| EUR J RISK REGUL              |     1 |             0 |                   1 |                  3 |                 0 |                             3   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
| DECIS SUPPORT SYST            |     1 |             0 |                   1 |                  1 |                 1 |                             1   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| J IND BUS ECON                |     1 |             0 |                   1 |                  1 |                 0 |                             1   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| LECT NOTES NETWORKS SYST      |     1 |             0 |                   1 |                  1 |                 0 |                             1   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| ADV INTELL SYS COMPUT         |     1 |             1 |                   0 |                  7 |                 1 |                             7   |                            1   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        2.33 |         1 |         1 |      0.33 |
| J ANTITRUST ENFORC            |     1 |             1 |                   0 |                  3 |                 3 |                             3   |                            3   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        1    |         1 |         1 |      0.33 |
| ACM INT CONF PROC SER         |     1 |             1 |                   0 |                  2 |                 0 |                             2   |                            0   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        0.67 |         1 |         1 |      0.33 |
| LECT NOTES BUS INF PROCESS    |     1 |             1 |                   0 |                  2 |                 0 |                             2   |                            0   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        0.67 |         1 |         1 |      0.33 |
| STUD COMPUT INTELL            |     2 |             2 |                   0 |                  1 |                 1 |                             0.5 |                            0.5 |                  -1   |                     0   |                        0    |                     2021 |     3 |                        0.33 |         1 |         1 |      0.33 |
| EAI/SPRINGER INNO COMM COMP   |     1 |             1 |                   0 |                  1 |                 0 |                             1   |                            0   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        0.33 |         1 |         1 |      0.33 |
| J MONEY LAUND CONTROL         |     1 |             1 |                   0 |                 14 |                 3 |                            14   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        3.5  |         1 |         1 |      0.25 |
| ICEIS - PROC INT CONF ENTERP  |     1 |             1 |                   0 |                 12 |                 3 |                            12   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| HELIYON                       |     1 |             1 |                   0 |                 11 |                 4 |                            11   |                            4   |                   0   |                     0   |                        0    |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| ADELAIDE LAW REV              |     1 |             1 |                   0 |                  5 |                 1 |                             5   |                            1   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| INTELL SYST ACCOUNT FINANCE M |     1 |             1 |                   0 |                  5 |                 3 |                             5   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| LECTURE NOTES DATA ENG COMMUN |     1 |             1 |                   0 |                  4 |                 0 |                             4   |                            0   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| UNIV NEW SOUTH WALES LAW J    |     1 |             1 |                   0 |                  4 |                 3 |                             4   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_items
from ...vantagepoint.report import ranking_chart


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def source_m_index(
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
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the selected impact measure by source.

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

    if title is None:
        title = "Source Impact by M-Index"

    item_list = list_items(
        field="source_abbr",
        metric="m_index",
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
