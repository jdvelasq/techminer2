"""
ColumnToItems
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.cross_occurrence.matrix import ColumnToItems
    >>> mapping = (
    ...     ColumnToItems()
    ...     #
    ...     # COLUMNS:
    ...     .with_column_field(Field.AUTHKW_TOK)
    ...     .having_column_items_in_top(10)
    ...     .having_column_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_column_item_occurrences_between(None, None)
    ...     .having_column_item_citations_between(None, None)
    ...     .having_column_items_in(None)
    ...     #
    ...     # ROWS:
    ...     .with_index_field(Field.AUTH_NORM)
    ...     .having_index_items_in_top(None)
    ...     .having_index_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_index_item_occurrences_between(2, None)
    ...     .having_index_item_citations_between(None, None)
    ...     .having_index_items_in(None)
    ...     #
    ...     .using_minimum_item_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(mapping).__name__
    'dict'
    >>> len(mapping) > 1
    True
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS

    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.cross_occurrence.matrix import ColumnToItems
    >>> mapping = (
    ...     ColumnToItems()
    ...     #
    ...     # COLUMNS:
    ...     .with_column_field(Field.AUTHKW_TOK)
    ...     .having_column_items_in_top(10)
    ...     .having_column_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_column_item_occurrences_between(None, None)
    ...     .having_column_item_citations_between(None, None)
    ...     .having_column_items_in(None)
    ...     #
    ...     # ROWS:
    ...     .with_index_field(Field.AUTH_NORM)
    ...     .having_index_items_in_top(10)
    ...     .having_index_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_index_item_occurrences_between(None, None)
    ...     .having_index_item_citations_between(None, None)
    ...     .having_index_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(
    ...         {
    ...             Field.AUTHKW_RAW: ["fintech", "innovation", "financial services"],
    ...         },
    ...     )
    ...     #
    ...     .run()
    ... )
    >>> type(mapping).__name__
    'dict'
    >>> len(mapping) > 1
    True
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS



"""

from tm2p._intern import ParamsMixin

from .matrix import Matrix


class ColumnToItems(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> dict[str, list[str]]:

        matrix = Matrix().update(**self.params.__dict__).run()

        mapping = {}
        for column in matrix.columns:
            column_items = [
                index for index, item in zip(matrix.index, matrix[column]) if item > 0
            ]
            mapping[column] = column_items

        return mapping
