"""
Co-citation Matrix List
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> bibliometrix.intellectual_structure.co_citation_matrix_list(directory=directory).head()
                                                    row  ... OCC
2365  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...  19
2373  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...   3
2374  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...   4
2386  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...  35
2396  Anagnostopoulos I, 2018, J ECON BUS, V100, P7 ...  ...   3
<BLANKLINE>
[5 rows x 3 columns]

"""
from ..._read_records import read_records
from ...vantagepoint.analyze.matrix.co_occ_matrix_list import (
    _add_counters_to_items,
    _create_matrix_list,
)


def co_citation_matrix_list(
    topics_length=50,
    directory="./",
    start_year=None,
    end_year=None,
    **filters,
):

    """Co-citation matrix"""

    matrix_list = _create_matrix_list(
        criterion="local_references",
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    # select most local cited references
    references = read_records(
        directory=directory,
        database="references",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    references = references.sort_values(
        ["local_citations", "global_citations"], ascending=[False, False]
    )
    references = references.head(topics_length)
    references = references.article

    # filter matrix list
    matrix_list = matrix_list[matrix_list.row.isin(references)]
    matrix_list = matrix_list[matrix_list.column.isin(references)]

    # add counters to items
    for column_name in ["row", "column"]:
        matrix_list = _add_counters_to_items(
            matrix_list=matrix_list,
            column_name=column_name,
            criterion="local_references",
            directory=directory,
            database="documents",
            start_year=start_year,
            end_year=end_year,
        )

    return matrix_list
