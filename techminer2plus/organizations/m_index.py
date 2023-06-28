# flake8: noqa
"""
M-Index
===============================================================================



>>> FILE_NAME = "sphinx/_static/use_cases/organizations/m_index.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.organizations.m_index(
...     top_n=20,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/organizations/m_index.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> items.df_.head()
                             rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
organizations                                        ...                           
Ahlia Univ (BHR)                    3       16    3  ...      2.0      2.0      0.5
Coventry Univ (GBR)                 4       17    2  ...      2.0      1.0      0.5
Univ of Westminster (GBR)           5       18    2  ...      2.0      1.0      0.5
Dublin City Univ (IRL)              6       19    2  ...      2.0      1.0      0.5
Hebei Univ of Technol (CHN)        21       20    1  ...      1.0      1.0      0.5
<BLANKLINE>
[5 rows x 18 columns]

>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'organizations' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'm_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| organizations                                 |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:----------------------------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Ahlia Univ (BHR)                              |          3 |        16 |     3 |             2 |                   1 |                 19 |                 5 |                            6.33 |                           1.67 |                  -0.5 |                     0.5 |                    0.166667 |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Coventry Univ (GBR)                           |          4 |        17 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Univ of Westminster (GBR)                     |          5 |        18 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Dublin City Univ (IRL)                        |          6 |        19 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Hebei Univ of Technol (CHN)                   |         21 |        20 |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Jiangsu Univ (CHN)                            |         22 |        21 |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Shanghai Univ (CHN)                           |         23 |        22 |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Tokai Univ (JPN)                              |         24 |        23 |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Tongji Univ (CHN)                             |         25 |        24 |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| 3PB, London, United Kingdom (GBR)             |         46 |        45 |     1 |             0 |                   1 |                  3 |                 1 |                            3    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
| Univ de Almeria (ESP)                         |         49 |        48 |     1 |             0 |                   1 |                  3 |                 0 |                            3    |                           0    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
| Univ of Chinese Acad of Social Sciences (CHN) |         47 |        46 |     1 |             0 |                   1 |                  3 |                 1 |                            3    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
| Goethe Univ Frankfurt (DEU)                   |         53 |        53 |     1 |             0 |                   1 |                  1 |                 1 |                            1    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| Univ Coll of Bahrain (BHR)                    |         57 |        57 |     1 |             0 |                   1 |                  1 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| Univ of Bahrain (BHR)                         |         58 |        58 |     1 |             0 |                   1 |                  1 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| Univ of Hong Kong (HKG)                       |          1 |         1 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                    0        |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Univ Coll Cork (IRL)                          |          2 |         5 |     3 |             2 |                   1 |                 41 |                19 |                           13.67 |                           6.33 |                   0   |                     0.5 |                    0.166667 |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| Univ of Johannesburg (ZAF)                    |         27 |        26 |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| Conventional Wholesale B (BHR)                |         33 |        32 |     1 |             1 |                   0 |                  7 |                 1 |                            7    |                           1    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        2.33 |         1 |         1 |      0.33 |
| Sch of Taxation and Bus Law (AUS)             |         42 |        41 |     1 |             1 |                   0 |                  3 |                 3 |                            3    |                           3    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        1    |         1 |         1 |      0.33 |
```
<BLANKLINE>





# pylint: disable=line-too-long
"""
# from ... import list_items
# from ...graphing_lib import ranking_chart

FIELD = "organizations"
METRIC = "m_index"
TITLE = "Organizations M-Index"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def m_index(
    #
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    metric_label=None,
    field_label=None,
    title=None,
    #
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most Relevant Source Items."""

    if title is None:
        title = TITLE

    itemslist = list_items(
        field=FIELD,
        metric=METRIC,
        #
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # Database filters:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return ranking_chart(
        itemslist=itemslist,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
