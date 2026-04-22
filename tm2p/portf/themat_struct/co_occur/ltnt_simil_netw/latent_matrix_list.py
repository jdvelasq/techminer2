"""
LatentMatrixList
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.latent_similarity_network import LatentMatrixList
    >>> df = (
    ...     LatentMatrixList()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
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
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> df.head(10).round(3)
                                    ROWS                            COLUMNS  SIM
    0                  finance 029:07137                  finance 029:07137  1.0
    1                    china 018:03596                    china 018:03596  1.0
    2           sustainability 013:02308           sustainability 013:02308  1.0
    3               blockchain 012:03450               blockchain 012:03450  1.0
    4          economic growth 009:01654          economic growth 009:01654  1.0
    5  artificial intelligence 008:01915  artificial intelligence 008:01915  1.0
    6        financial service 007:02627        financial service 007:02627  1.0
    7                  banking 013:03043                  banking 013:03043  1.0
    8            green finance 011:02844            green finance 011:02844  1.0
    9       financial services 011:02399       financial services 011:02399  1.0


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
