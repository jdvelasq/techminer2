"""
BaseCombineMatch
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, ThFile
    >>> from tm2p.refine._intern.match import BaseCombineMatch
    >>> (
    ...     BaseCombineMatch()
    ...     #
    ...     # FIELD:
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_NORM)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

import sys

import pandas as pd  # type: ignore

from tm2p._intern import Params, ParamsMixin
from tm2p.enum import ThField
from tm2p.portf.themat_struct.co_occur.mtx import MatrixList

from ._intern.report_matches import report_matches

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value


class BaseCombineMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        matrix_list = compute_cooc_matrix(self.params)
        matrix_list = compute_probabilities(matrix_list)
        matches = compute_matches(matrix_list)

        report_matches(
            params=self.params,
            mapping=matches,
        )

        sys.stderr.write(f"\n{len(matches.keys())} synonym groups found\n")
        sys.stderr.flush()


def compute_cooc_matrix(params: Params) -> pd.DataFrame:

    matrix_list = (
        MatrixList()
        .update(**params.__dict__)
        .having_unit_occurrence_between(5, None)
        .using_counters(True)
        .run()
    )

    matrix_list["rows_occ"] = matrix_list["rows"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[0]) if isinstance(x, str) else 0
    )

    matrix_list["rows_gc"] = matrix_list["rows"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[1]) if isinstance(x, str) else 0
    )

    matrix_list["columns_occ"] = matrix_list["columns"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[0]) if isinstance(x, str) else 0
    )

    matrix_list["columns_gc"] = matrix_list["columns"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[1]) if isinstance(x, str) else 0
    )

    matrix_list = matrix_list.loc[matrix_list.rows_occ > matrix_list.columns_occ, :]

    return matrix_list


def compute_probabilities(matrix_list: pd.DataFrame) -> pd.DataFrame:

    matrix_list["probability"] = matrix_list.OCC / matrix_list.rows_occ

    matrix_list["probability"] = matrix_list["probability"].round(3)

    matrix_list["combine?"] = matrix_list["probability"].apply(
        lambda x: "yes" if x >= 0.5 else "no"
    )

    matrix_list = matrix_list[matrix_list["combine?"] == "yes"]  #  type: ignore

    matrix_list = matrix_list.sort_values(
        by=["rows_occ", "rows_gc", "probability", "rows"], ascending=False
    )

    matrix_list = matrix_list.reset_index(drop=True)

    return matrix_list


def compute_matches(matrix_list: pd.DataFrame) -> dict[str, list[str]]:

    mapping: dict[str, list[str]] = {}

    for _, row in matrix_list.iterrows():

        row_key = row["rows"]
        column_key = row["columns"]

        if row_key not in mapping:
            mapping[row_key] = []

        mapping[row_key].append(column_key)

    return mapping
