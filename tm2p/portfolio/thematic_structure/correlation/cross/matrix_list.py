"""
MatrixList
===============================================================================

Smoke tests:
    >>> from tm2p import ItemOrderBy, Field, Correlation
    >>> from tm2p.discover.correlation.cross import MatrixList
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # CROSS WITH:
    ...     .with_cross_field(Field.CTRY_ISO3)
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method(Correlation.PEARSON)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head().round(3)
                                    rows                            columns  CORR
    0  artificial intelligence 008:01915  artificial intelligence 008:01915   1.0
    1                  banking 010:02599                  banking 010:02599   1.0
    2               blockchain 011:02023               blockchain 011:02023   1.0
    3       financial services 007:01673       financial services 007:01673   1.0
    4            green finance 011:02844            green finance 011:02844   1.0




"""

from tm2p._intern import ParamsMixin

from .matrix import Matrix


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).run()
        matrix_list = matrix.stack().reset_index()
        matrix_list.columns = ["rows", "columns", "CORR"]
        matrix_list = matrix_list.sort_values(
            by=["CORR", "rows", "columns"],
            ascending=[False, True, True],
        )
        matrix_list = matrix_list.reset_index(drop=True)

        return matrix_list
