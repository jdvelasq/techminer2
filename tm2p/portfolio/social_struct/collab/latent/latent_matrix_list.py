"""
LatentMatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.social_struct.collab.latent import LatentMatrixList  # type: ignore
    >>> df = (
    ...     LatentMatrixList()
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
                               ROWS                       COLUMNS    SIM
    0    Marianne Silva 0020:000255    Marianne Silva 0020:000255  1.000
    1       Luca Benini 0041:000706       Luca Benini 0041:000706  1.000
    2     Michele Magno 0035:000501     Michele Magno 0035:000501  1.000
    3  Ivanovitch Silva 0027:000442  Ivanovitch Silva 0027:000442  1.000
    4   Daniel G. Costa 0016:000312   Daniel G. Costa 0016:000312  1.000
    5    Marianne Silva 0020:000255   Daniel G. Costa 0016:000312  0.656
    6   Daniel G. Costa 0016:000312    Marianne Silva 0020:000255  0.656
    7  Ivanovitch Silva 0027:000442   Daniel G. Costa 0016:000312  0.460
    8   Daniel G. Costa 0016:000312  Ivanovitch Silva 0027:000442  0.460
    9  Ivanovitch Silva 0027:000442    Marianne Silva 0020:000255  0.368

    >>> df = (
    ...     LatentMatrixList()
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

    
"""

from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.mtx_to_mtx_list import matrix_to_matrix_list

from .latent_matrix import LatentMatrix


class LatentMatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = LatentMatrix().update(**self.params.__dict__).run()
        matrix_list = matrix_to_matrix_list(matrix, value_name="SIM")

        return matrix_list
