"""
Co-citation Matrix List
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> matrix = co_citation_matrix_list(directory=directory)
>>> matrix.head()
                                              row  ... OCC
363  Adhami S, 2018, J ECON BUS, V100, P64 04:027  ...   4
375  Adhami S, 2018, J ECON BUS, V100, P64 04:027  ...   2
379  Adhami S, 2018, J ECON BUS, V100, P64 04:027  ...   2
380  Adhami S, 2018, J ECON BUS, V100, P64 04:027  ...   2
410  Adhami S, 2018, J ECON BUS, V100, P64 04:027  ...   2
<BLANKLINE>
[5 rows x 3 columns]


"""
from ._read_records import read_records
from .co_occ_matrix_list import _add_counters_to_items, _create_matrix_list


def co_citation_matrix_list(
    top_n=50,
    directory="./",
):

    """Co-citation matrix"""

    matrix_list = _create_matrix_list(
        column="local_references",
        row="local_references",
        directory=directory,
        database="documents",
    )

    # select most local cited references
    references = read_records(
        directory=directory, database="references", use_filter=False
    )
    references = references.sort_values(
        ["local_citations", "global_citations"], ascending=[False, False]
    )
    references = references.head(top_n)
    references = references.article

    # filter matrix list
    matrix_list = matrix_list[matrix_list.row.isin(references)]
    matrix_list = matrix_list[matrix_list.column.isin(references)]

    # add counters to items
    matrix_list = _add_counters_to_items(
        "local_references",
        "column",
        directory,
        "documents",
        matrix_list,
    )
    matrix_list = _add_counters_to_items(
        "local_references",
        "row",
        directory,
        "documents",
        matrix_list,
    )

    return matrix_list
