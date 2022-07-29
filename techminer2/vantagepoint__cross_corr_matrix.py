"""
Cross-correlation Matrix (TODO)
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__cross_corr_matrix
>>> vantagepoint__cross_corr_matrix(
...     criterion_for_columns = 'authors', 
...     criterion_for_rows='countries',
...     topics_length=10,
...     directory=directory,
... )
column             Arner DW 7:220  ...  Das SR 2:028
column                             ...              
Arner DW 7:220           1.000000  ...           0.0
Buckley RP 6:217         0.994244  ...           0.0
Barberis JN 4:146        0.921304  ...           0.0
Zetzsche DA 4:092        0.927105  ...           0.0
Brennan R 3:008          0.000000  ...           0.0
Ryan P 3:008             0.000000  ...           0.0
Crane M 2:008            0.000000  ...           0.0
Das SR 2:028             0.000000  ...           1.0
<BLANKLINE>
[8 rows x 8 columns]

"""
from .vantagepoint__auto_corr_matrix import _compute_corr_matrix
from .vantagepoint__occ_matrix import vantagepoint__occ_matrix


def vantagepoint__cross_corr_matrix(
    criterion_for_columns=None,
    criterion_for_rows=None,
    method="pearson",
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):

    data_matrix = vantagepoint__occ_matrix(
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    corr_matrix = _compute_corr_matrix(method, data_matrix)

    return corr_matrix
