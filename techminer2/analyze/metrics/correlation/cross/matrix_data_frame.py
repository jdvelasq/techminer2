"""
Cross-correlation Matrix
===============================================================================


Smoke tests:
    >>> from techminer2.packages.correlation.cross import MatrixDataFrame
    >>> (
    ...     MatrixDataFrame()
    ...     #
    ...     # FIELD:
    ...     .with_field("authors")
    ...     .having_terms_in_top(10)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # CROSS WITH:
    ...     .with_other_field('countries')
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method("pearson")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).round(3)
                          Jagtiani J. 3:0317  ...  Zavolokina L. 2:0181
    Jagtiani J. 3:0317                 1.000  ...                   0.0
    Gomber P. 2:1065                   0.369  ...                   0.0
    Hornuf L. 2:0358                   0.000  ...                   0.0
    Gai K. 2:0323                      0.692  ...                   0.0
    Qiu M. 2:0323                      0.692  ...                   0.0
    Sun X. 2:0323                      0.692  ...                   0.0
    Lemieux C. 2:0253                  1.000  ...                   0.0
    Dolata M. 2:0181                   0.000  ...                   1.0
    Schwabe G. 2:0181                  0.000  ...                   1.0
    Zavolokina L. 2:0181               0.000  ...                   1.0
    <BLANKLINE>
    [10 rows x 10 columns]



"""

from techminer2._internals import ParamsMixin
from techminer2.analyze.metrics.co_occurrence_matrix import (
    MatrixDataFrame as CoOccurrenceMatrixDataFrame,
)
from techminer2.analyze.metrics.correlation._internals.internal__compute_corr_matrix import (
    internal__compute_corr_matrix,
)


class MatrixDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_matrix = (
            CoOccurrenceMatrixDataFrame()
            .update(**self.params.__dict__)
            .having_other_items_ordered_by("OCC")
            .run()
        )

        corr_matrix = internal__compute_corr_matrix(
            params=self.params,
            data_matrix=data_matrix,
        )

        return corr_matrix
