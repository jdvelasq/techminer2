"""
Co-occurrence Matrix List
===============================================================================


>>> directory = "data/regtech/"

**Item selection by occurrence.**

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.matrix.co_occ_matrix_list(
...    criterion='author_keywords',
...    topic_min_occ=5,
...    directory=directory,
... )
>>> r.matrix_list_
                             row                        column  OCC
0                 regtech 28:329                regtech 28:329   28
1                 regtech 28:329                fintech 12:249   12
2                 regtech 28:329  regulatory technology 07:037    2
3                 regtech 28:329             compliance 07:030    7
4                 regtech 28:329             regulation 05:164    4
5                 fintech 12:249                regtech 28:329   12
6                 fintech 12:249                fintech 12:249   12
7                 fintech 12:249  regulatory technology 07:037    1
8                 fintech 12:249             compliance 07:030    2
9                 fintech 12:249             regulation 05:164    4
10  regulatory technology 07:037                regtech 28:329    2
11  regulatory technology 07:037                fintech 12:249    1
12  regulatory technology 07:037  regulatory technology 07:037    7
13  regulatory technology 07:037             compliance 07:030    1
14  regulatory technology 07:037             regulation 05:164    1
15             compliance 07:030                regtech 28:329    7
16             compliance 07:030                fintech 12:249    2
17             compliance 07:030  regulatory technology 07:037    1
18             compliance 07:030             compliance 07:030    7
19             compliance 07:030             regulation 05:164    1
20             regulation 05:164                regtech 28:329    4
21             regulation 05:164                fintech 12:249    4
22             regulation 05:164  regulatory technology 07:037    1
23             regulation 05:164             compliance 07:030    1
24             regulation 05:164             regulation 05:164    5


>>> print(r.prompt_)
Analyze the table below, which contains the the metric OCC for author_keywords and author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row                          | column                       |   OCC |
|---:|:-----------------------------|:-----------------------------|------:|
|  0 | regtech 28:329               | regtech 28:329               |    28 |
|  1 | regtech 28:329               | fintech 12:249               |    12 |
|  2 | regtech 28:329               | regulatory technology 07:037 |     2 |
|  3 | regtech 28:329               | compliance 07:030            |     7 |
|  4 | regtech 28:329               | regulation 05:164            |     4 |
|  5 | fintech 12:249               | regtech 28:329               |    12 |
|  6 | fintech 12:249               | fintech 12:249               |    12 |
|  7 | fintech 12:249               | regulatory technology 07:037 |     1 |
|  8 | fintech 12:249               | compliance 07:030            |     2 |
|  9 | fintech 12:249               | regulation 05:164            |     4 |
| 10 | regulatory technology 07:037 | regtech 28:329               |     2 |
| 11 | regulatory technology 07:037 | fintech 12:249               |     1 |
| 12 | regulatory technology 07:037 | regulatory technology 07:037 |     7 |
| 13 | regulatory technology 07:037 | compliance 07:030            |     1 |
| 14 | regulatory technology 07:037 | regulation 05:164            |     1 |
| 15 | compliance 07:030            | regtech 28:329               |     7 |
| 16 | compliance 07:030            | fintech 12:249               |     2 |
| 17 | compliance 07:030            | regulatory technology 07:037 |     1 |
| 18 | compliance 07:030            | compliance 07:030            |     7 |
| 19 | compliance 07:030            | regulation 05:164            |     1 |
| 20 | regulation 05:164            | regtech 28:329               |     4 |
| 21 | regulation 05:164            | fintech 12:249               |     4 |
| 22 | regulation 05:164            | regulatory technology 07:037 |     1 |
| 23 | regulation 05:164            | compliance 07:030            |     1 |
| 24 | regulation 05:164            | regulation 05:164            |     5 |
<BLANKLINE>
<BLANKLINE>


**Seleccition of top terms.**

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.matrix.co_occ_matrix_list(
...    criterion='author_keywords',
...    topics_length=5,
...    directory=directory,
... )
>>> r.matrix_list_
                             row                        column  OCC
0                 regtech 28:329                regtech 28:329   28
1                 regtech 28:329                fintech 12:249   12
2                 regtech 28:329  regulatory technology 07:037    2
3                 regtech 28:329             compliance 07:030    7
4                 regtech 28:329             regulation 05:164    4
5                 fintech 12:249                regtech 28:329   12
6                 fintech 12:249                fintech 12:249   12
7                 fintech 12:249  regulatory technology 07:037    1
8                 fintech 12:249             compliance 07:030    2
9                 fintech 12:249             regulation 05:164    4
10  regulatory technology 07:037                regtech 28:329    2
11  regulatory technology 07:037                fintech 12:249    1
12  regulatory technology 07:037  regulatory technology 07:037    7
13  regulatory technology 07:037             compliance 07:030    1
14  regulatory technology 07:037             regulation 05:164    1
15             compliance 07:030                regtech 28:329    7
16             compliance 07:030                fintech 12:249    2
17             compliance 07:030  regulatory technology 07:037    1
18             compliance 07:030             compliance 07:030    7
19             compliance 07:030             regulation 05:164    1
20             regulation 05:164                regtech 28:329    4
21             regulation 05:164                fintech 12:249    4
22             regulation 05:164  regulatory technology 07:037    1
23             regulation 05:164             compliance 07:030    1
24             regulation 05:164             regulation 05:164    5


"""
from .occ_matrix_list import occ_matrix_list


def co_occ_matrix_list(
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
    return occ_matrix_list(
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
