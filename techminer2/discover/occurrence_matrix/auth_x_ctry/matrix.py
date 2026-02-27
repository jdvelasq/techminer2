"""
Matrix
===============================================================================

Smoke tests:
    >>> from techminer2 import ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.auth_x_ctry import Matrix
    >>> df = (
    ...     Matrix()
    ...     #
    ...     # COLUMNS:
    ...     .having_column_items_in_top(10)
    ...     .having_column_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_column_item_occurrences_between(None, None)
    ...     .having_column_item_citations_between(None, None)
    ...     .having_column_items_in(None)
    ...     #
    ...     # ROWS:
    ...     .having_index_items_in_top(None)
    ...     .having_index_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_index_item_occurrences_between(2, None)
    ...     .having_index_item_citations_between(None, None)
    ...     .having_index_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_item_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
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
    >>> df.head(10)
    columns        Jagtiani J. 005:01156  ...  Kauffman R.J. 002:01445
    rows                                  ...
    CHN 045:09715                      0  ...                        0
    GBR 033:06802                      2  ...                        0
    USA 031:09562                      5  ...                        1
    AUS 014:03468                      0  ...                        0
    DEU 013:05295                      0  ...                        1
    IND 012:01818                      0  ...                        0
    FRA 011:02475                      0  ...                        0
    KOR 011:02378                      0  ...                        0
    CHE 008:01458                      0  ...                        0
    ITA 008:01041                      0  ...                        0
    <BLANKLINE>
    [10 rows x 10 columns]


"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin

from .._internals import Matrix as BaseMatrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseMatrix()
            .with_params(self.params)
            .with_column_field(CorpusField.AUTH_NORM)
            .with_index_field(CorpusField.CTRY_ISO3)
            .run()
        )
