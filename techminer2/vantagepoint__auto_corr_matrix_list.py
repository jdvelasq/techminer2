"""
Auto-correlation Matrix List (TODO)
===============================================================================

Returns an auto-correlation matrix.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__auto_corr_matrix_list
>>> vantagepoint__auto_corr_matrix_list(
...     criterion='authors',
...     topics_length=10,
...     directory=directory,
... )
                  row             column      CORR
0      Arner DW 7:220     Arner DW 7:220  1.000000
1   Barberis JN 4:146  Barberis JN 4:146  1.000000
2     Brennan R 3:008    Brennan R 3:008  1.000000
3    Buckley RP 6:217   Buckley RP 6:217  1.000000
4      Hamdan A 2:011     Hamdan A 2:011  1.000000
5       Mayer N 2:002      Mayer N 2:002  1.000000
6        Ryan P 3:008       Ryan P 3:008  1.000000
7       Sarea A 2:006      Sarea A 2:006  1.000000
8       Singh C 2:007      Singh C 2:007  1.000000
9   Zetzsche DA 4:092  Zetzsche DA 4:092  1.000000
10    Brennan R 3:008       Ryan P 3:008  1.000000
11       Ryan P 3:008    Brennan R 3:008  1.000000
12     Arner DW 7:220   Buckley RP 6:217  0.882735
13   Buckley RP 6:217     Arner DW 7:220  0.882735
14   Buckley RP 6:217  Zetzsche DA 4:092  0.751068
15  Zetzsche DA 4:092   Buckley RP 6:217  0.751068
16     Arner DW 7:220  Barberis JN 4:146  0.662994
17  Barberis JN 4:146     Arner DW 7:220  0.662994
18     Arner DW 7:220  Zetzsche DA 4:092  0.662994
19  Zetzsche DA 4:092     Arner DW 7:220  0.662994
20  Barberis JN 4:146   Buckley RP 6:217  0.460882
21   Buckley RP 6:217  Barberis JN 4:146  0.460882
22     Hamdan A 2:011      Sarea A 2:006  0.433333
23      Sarea A 2:006     Hamdan A 2:011  0.433333
24  Barberis JN 4:146  Zetzsche DA 4:092  0.019231
25  Zetzsche DA 4:092  Barberis JN 4:146  0.019231


"""
from .vantagepoint__auto_corr_matrix import vantagepoint__auto_corr_matrix


def vantagepoint__auto_corr_matrix_list(
    criterion,
    method="pearson",
    topics_length=50,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Returns an auto-correlation matrix list."""

    matrix = vantagepoint__auto_corr_matrix(
        criterion=criterion,
        method=method,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix = _transform_to_matrix_list(criterion, matrix)

    return matrix


def _transform_to_matrix_list(criterion, matrix):
    matrix = matrix.melt(value_name="CORR", var_name="column", ignore_index=False)
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={"index": "row"})
    matrix = matrix.sort_values(
        by=["CORR", "row", "column"], ascending=[False, True, True]
    )
    matrix = matrix[matrix.CORR != 0.0]
    matrix = matrix.reset_index(drop=True)
    return matrix
