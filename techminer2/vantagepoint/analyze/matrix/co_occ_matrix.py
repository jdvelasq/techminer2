"""
Co-occurrence Matrix (GPT)
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.matrix.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=4,
...    directory=directory,
... )
>>> r.matrix_
column                          regtech 28:329  ...  financial services 04:168
row                                             ...                           
regtech 28:329                              28  ...                          3
fintech 12:249                              12  ...                          2
compliance 07:030                            7  ...                          0
regulatory technology 07:037                 2  ...                          0
regulation 05:164                            4  ...                          1
artificial intelligence 04:023               2  ...                          0
financial regulation 04:035                  2  ...                          2
financial services 04:168                    3  ...                          4
<BLANKLINE>
[8 rows x 8 columns]

>>> print(r.prompt_)
Analyze the table below which contains values for the metric OCC. The columns of the table correspond to author_keywords, and the rows correspond to author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   fintech 12:249 |   compliance 07:030 |   regulatory technology 07:037 |   regulation 05:164 |   artificial intelligence 04:023 |   financial regulation 04:035 |   financial services 04:168 |
|:-------------------------------|-----------------:|-----------------:|--------------------:|-------------------------------:|--------------------:|---------------------------------:|------------------------------:|----------------------------:|
| regtech 28:329                 |               28 |               12 |                   7 |                              2 |                   4 |                                2 |                             2 |                           3 |
| fintech 12:249                 |               12 |               12 |                   2 |                              1 |                   4 |                                1 |                             1 |                           2 |
| compliance 07:030              |                7 |                2 |                   7 |                              1 |                   1 |                                1 |                             0 |                           0 |
| regulatory technology 07:037   |                2 |                1 |                   1 |                              7 |                   1 |                                1 |                             0 |                           0 |
| regulation 05:164              |                4 |                4 |                   1 |                              1 |                   5 |                                0 |                             0 |                           1 |
| artificial intelligence 04:023 |                2 |                1 |                   1 |                              1 |                   0 |                                4 |                             0 |                           0 |
| financial regulation 04:035    |                2 |                1 |                   0 |                              0 |                   0 |                                0 |                             4 |                           2 |
| financial services 04:168      |                3 |                2 |                   0 |                              0 |                   1 |                                0 |                             2 |                           4 |
<BLANKLINE>
<BLANKLINE>


"""
from .occ_matrix import occ_matrix


def co_occ_matrix(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    return occ_matrix(
        criterion_for_columns=criterion,
        criterion_for_rows=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    # matrix_list = co_occ_matrix_list(
    #     criterion=criterion,
    #     topics_length=topics_length,
    #     topic_min_occ=topic_min_occ,
    #     topic_max_occ=topic_max_occ,
    #     topic_min_citations=topic_min_citations,
    #     topic_max_citations=topic_max_citations,
    #     directory=directory,
    #     database=database,
    #     start_year=start_year,
    #     end_year=end_year,
    #     **filters,
    # )

    # matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    # matrix = matrix.fillna(0)
    # matrix = matrix.astype(int)

    # columns = sorted(
    #     matrix.columns.tolist(), key=lambda x: x.split()[-1].split(":")[0], reverse=True
    # )
    # indexes = sorted(
    #     matrix.index.tolist(), key=lambda x: x.split()[-1].split(":")[0], reverse=True
    # )
    # matrix = matrix.loc[indexes, columns]

    # return matrix
