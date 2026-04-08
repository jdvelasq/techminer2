"""
ItemsByColumn
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.cross_occurrence.matrix import ItemsByColumn
    >>> df = (
    ...     ItemsByColumn()
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
    ...     .having_index_item_occurrences_between(None, None)
    ...     .having_index_item_citations_between(None, None)
    ...     .having_index_items_in(None)
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
    >>> type(df).__name__
    'DataFrame'
    >>> len(df) > 1
    True
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
          fintech 117:25478 financial inclusion 017:03823 financial technology 015:02734 green finance 011:02844    blockchain 011:02023       banking 010:02599       china 009:01947    innovation 009:01703 artificial intelligence 008:01915 financial services 007:01673
    0  Jagtiani J 005:01156            Arner DW 003:00911             Arner DW 003:00911         Luo S 002:00670    Jagtiani J 005:01156     Murinde V 002:01022  Jagtiani J 005:01156      Dolata M 003:00330                 Ashta A 002:00372  Anagnostopoulos I 001:00436
    1    Arner DW 003:00911           Murinde V 002:01022           Barberis J 003:00445        Zhou G 002:00670      Dolata M 003:00330       Ashta A 002:00372    Arner DW 003:00911     Schwabe G 003:00330             Al-Okaily M 002:00191        Schueffel P 001:00402
    2    Hornuf L 003:00904          Buckley RP 002:00898              Afzal A 002:00280     Muganyi T 002:00656     Schwabe G 003:00330     Hassan MK 002:00228  Barberis J 003:00445  Zavolokina L 003:00330              Belanche D 001:00605           Jünger M 001:00256
    3  Barberis J 003:00445        Al-Sartawi A 002:00274          Firdousi SF 002:00280       Sun H-P 002:00656  Zavolokina L 003:00330     Thakor AV 001:00770   Muganyi T 002:00656       Afzal A 002:00280         Casaló Ariño LV 001:00605         Mietzner M 001:00256
    4    Dolata M 003:00330            Brooks S 001:00563             Jangir K 002:00183         Yan L 002:00656       Allen F 002:00474  Rizopoulos E 001:00494     Sun H-P 002:00656   Firdousi SF 002:00280               Flavián C 001:00605           Gimpel H 001:00234


    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.cross_occurrence.matrix import ItemsByColumn
    >>> df = (
    ...     ItemsByColumn()
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
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> len(df) > 1
    True
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
          fintech financial inclusion financial technology green finance    blockchain       banking       china    innovation artificial intelligence financial services
    0  Jagtiani J            Arner DW             Arner DW         Luo S    Jagtiani J     Murinde V  Jagtiani J      Dolata M                 Ashta A  Anagnostopoulos I
    1    Arner DW           Murinde V           Barberis J        Zhou G      Dolata M       Ashta A    Arner DW     Schwabe G             Al-Okaily M        Schueffel P
    2    Hornuf L          Buckley RP              Afzal A     Muganyi T     Schwabe G     Hassan MK  Barberis J  Zavolokina L              Belanche D           Jünger M
    3  Barberis J        Al-Sartawi A          Firdousi SF       Sun H-P  Zavolokina L     Thakor AV   Muganyi T       Afzal A         Casaló Ariño LV         Mietzner M
    4    Dolata M            Brooks S             Jangir K         Yan L       Allen F  Rizopoulos E     Sun H-P   Firdousi SF               Flavián C           Gimpel H


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .column_to_items import ColumnToItems


class ItemsByColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> pd.DataFrame:

        use_counters = self.params.counters

        c2i = ColumnToItems().update(**self.params.__dict__).using_counters(True).run()

        df = pd.DataFrame.from_dict(c2i, orient="index").T
        df = df.fillna("")

        if use_counters is False:
            df = df.map(lambda cell: " ".join(cell.split(" ")[:-1]) if cell else "")
            df.columns = [" ".join(col.split(" ")[:-1]) for col in df.columns]

        return df
