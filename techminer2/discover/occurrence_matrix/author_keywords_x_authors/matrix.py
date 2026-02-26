"""
Matrix
===============================================================================

Smoke tests:
    >>> from techminer2 import ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.author_keywords_x_authors import Matrix
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
    columns                  fintech 117:25478  ...  financial services 007:01673
    rows                                        ...
    Jagtiani J. 005:01156                    5  ...                             0
    Arner D.W. 003:00911                     2  ...                             0
    Hornuf L. 003:00904                      3  ...                             0
    Li X. 003:00894                          3  ...                             0
    Barberis J. 003:00445                    1  ...                             0
    Dolata M. 003:00330                      3  ...                             0
    Schwabe G. 003:00330                     3  ...                             0
    Zavolokina L. 003:00330                  3  ...                             0
    Gomber P. 002:02579                      1  ...                             0
    Kauffman R.J. 002:01445                  0  ...                             0
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
            .with_column_field(CorpusField.AUTH_KEY_NORM)
            .with_index_field(CorpusField.AUTH_NORM)
            .run()
        )
