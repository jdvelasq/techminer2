"""
MatrixList
===============================================================================

Smoke Test:
    >>> from tm2p.enum import UnitOrderBy, Field, Correlation
    >>> from tm2p.portfolio.thematic_struct.correlation.auto import MatrixList
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method(Correlation.PEARSON)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> df.head().round(3)
                                 rows                         columns  CORR
    0               fintech 117:25478               fintech 117:25478   1.0
    1   financial inclusion 017:03823   financial inclusion 017:03823   1.0
    2  financial technology 015:02734  financial technology 015:02734   1.0
    3         green finance 011:02844         green finance 011:02844   1.0
    4            blockchain 011:02023            blockchain 011:02023   1.0


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.mtx_to_mtx_list import matrix_to_matrix_list

from .matrix import Matrix


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).run()
        matrix_list = matrix_to_matrix_list(matrix, "CORR")

        return matrix_list
