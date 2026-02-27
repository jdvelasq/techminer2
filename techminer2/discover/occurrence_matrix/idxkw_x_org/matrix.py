"""
Matrix
===============================================================================

Smoke tests:
    >>> from techminer2 import ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.idxkw_x_org import Matrix
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
    columns                                       finance 028:07080  ...  commerce 006:02013
    rows                                                             ...
    SOUTHWEST UNIV FINANC ECON [CHN] 008:02269                    0  ...                   0
    UNIV ZÜR [CHE] 007:00971                                      1  ...                   1
    FED RESERV BANK PHILA [USA] 005:01156                         0  ...                   0
    UNIV HONG KONG [HKG] 004:00760                                0  ...                   0
    PEKING UNIV [CHN] 004:00576                                   0  ...                   0
    LATV UNIV [LVA] 004:00456                                     0  ...                   0
    [N/A] 004:00192                                               0  ...                   1
    SHANGHAI UNIV [CHN] 003:00911                                 1  ...                   0
    MAX PLANCK INST INNOV COMPET [DEU] 003:00904                  0  ...                   0
    XI'AN JIAOTONG UNIV [CHN] 003:00689                           0  ...                   0
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
            .with_column_field(CorpusField.IDXKW_NORM)
            .with_index_field(CorpusField.ORG)
            .run()
        )
