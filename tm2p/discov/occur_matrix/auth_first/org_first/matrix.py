"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p import ItemsOrderBy
    >>> from tm2p.discov.occur_matrix.auth_first.org_first import Matrix
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
    columns                                     Jagtiani J. 003:00682  ...  Nenavath S. 002:00256
    rows                                                               ...
    SOUTHWEST UNIV FINANC ECON [CHN] 005:01236                      0  ...                      0
    UNIV ZÜR [CHE] 005:00659                                        0  ...                      0
    [N/A] 004:00192                                                 0  ...                      0
    XI'AN JIAOTONG UNIV [CHN] 003:00689                             0  ...                      0
    FED RESERV BANK PHILA [USA] 003:00682                           3  ...                      0
    GOETHE-UNIVERSITÄT FRANKF [DEU] 002:02579                       0  ...                      0
    SOAS UNIV LOND [GBR] 002:01022                                  0  ...                      0
    SHANGHAI UNIV [CHN] 002:00656                                   0  ...                      0
    PACE UNIV [USA] 002:00511                                       0  ...                      0
    IMP COLL LOND [GBR] 002:00474                                   0  ...                      0
    <BLANKLINE>
    [10 rows x 10 columns]


"""

from tm2p._intern import ParamsMixin

from ..._intern import Matrix as BaseMatrix
from .._column import COLUMN_FIELD
from ._index import INDEX_FIELD

# how to read the name of the folder where is the current file


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseMatrix()
            .with_params(self.params)
            .with_column_field(COLUMN_FIELD)
            .with_index_field(INDEX_FIELD)
            .run()
        )
