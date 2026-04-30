"""
DirectMatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.social_struct.collab.direct import DirectMatrixList  # type: ignore
    >>> df = (
    ...     DirectMatrixList()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> df.head(10).round(3)
                               ROWS                       COLUMNS  ASSOC
    0  Ivanovitch Silva 0027:000442    Marianne Silva 0020:000255  0.037
    1    Marianne Silva 0020:000255  Ivanovitch Silva 0027:000442  0.037
    2  Ivanovitch Silva 0027:000442   Daniel G. Costa 0016:000312  0.032
    3   Daniel G. Costa 0016:000312  Ivanovitch Silva 0027:000442  0.032
    4    Marianne Silva 0020:000255   Daniel G. Costa 0016:000312  0.025
    5   Daniel G. Costa 0016:000312    Marianne Silva 0020:000255  0.025
    6       Luca Benini 0041:000706     Michele Magno 0035:000501  0.008
    7     Michele Magno 0035:000501       Luca Benini 0041:000706  0.008
    8       Luca Benini 0041:000706       Luca Benini 0041:000706  0.000
    9       Luca Benini 0041:000706  Ivanovitch Silva 0027:000442  0.000


    >>> df = (
    ...     DirectMatrixList()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 1
    >>> assert df.shape[1] > 1
    >>> df.head(10).round(3)
                   ROWS           COLUMNS  ASSOC
    0  Ivanovitch Silva    Marianne Silva  0.037
    1    Marianne Silva  Ivanovitch Silva  0.037
    2  Ivanovitch Silva   Daniel G. Costa  0.032
    3   Daniel G. Costa  Ivanovitch Silva  0.032
    4    Marianne Silva   Daniel G. Costa  0.025
    5   Daniel G. Costa    Marianne Silva  0.025
    6       Luca Benini     Michele Magno  0.008
    7     Michele Magno       Luca Benini  0.008
    8       Luca Benini       Luca Benini  0.000
    9       Luca Benini  Ivanovitch Silva  0.000

    
"""

from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.mtx_to_mtx_list import matrix_to_matrix_list

from .direct_matrix import DirectMatrix


class DirectMatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        counters = self.params.use_counters
        matrix = (
            DirectMatrix().update(**self.params.__dict__).using_counters(True).run()
        )
        matrix_list = matrix_to_matrix_list(matrix, value_name="ASSOC")
        if counters is False:
            matrix_list["ROWS"] = matrix_list["ROWS"].apply(
                lambda x: " ".join(x.split(" ")[:-1])
            )
            matrix_list["COLUMNS"] = matrix_list["COLUMNS"].apply(
                lambda x: " ".join(x.split(" ")[:-1])
            )

        return matrix_list
