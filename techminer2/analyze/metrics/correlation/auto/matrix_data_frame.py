"""
Data Frame
===============================================================================


Smoke Test:
    >>> from techminer2.packages.correlation.auto import MatrixDataFrame
    >>> (
    ...     MatrixDataFrame()
    ...     #
    ...     # FIELD:
    ...     .with_field("authors")
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method("pearson")
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... ).round(3)
                          Jagtiani J. 3:0317  ...  Zavolokina L. 2:0181
    Jagtiani J. 3:0317                  1.00  ...                   0.0
    Gomber P. 2:1065                    0.00  ...                   0.0
    Hornuf L. 2:0358                    0.00  ...                   0.0
    Gai K. 2:0323                       0.00  ...                   0.0
    Qiu M. 2:0323                       0.00  ...                   0.0
    Sun X. 2:0323                       0.00  ...                   0.0
    Lemieux C. 2:0253                   0.77  ...                   0.0
    Dolata M. 2:0181                    0.00  ...                   1.0
    Schwabe G. 2:0181                   0.00  ...                   1.0
    Zavolokina L. 2:0181                0.00  ...                   1.0
    <BLANKLINE>
    [10 rows x 10 columns]


"""

from techminer2._internals import ParamsMixin
from techminer2.analyze.metrics.correlation._internals.internal__compute_corr_matrix import (
    internal__compute_corr_matrix,
)
from techminer2.analyze.tfidf import DataFrame as TfIdfDataFrame


class MatrixDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        tfidf = TfIdfDataFrame()
        tfidf = tfidf.update(**self.params.__dict__)
        # tfidf = tfidf.using_term_counters(False)
        data_matrix = tfidf.run()

        corr_matrix = internal__compute_corr_matrix(
            params=self.params,
            data_matrix=data_matrix,
        )

        return corr_matrix
