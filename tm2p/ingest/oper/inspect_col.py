"""
InspectColumn
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, UnitOrderBy
    >>> from tm2p.ingest.oper import InspectColumn
    >>> items = (
    ...     InspectColumn()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.DOCTYPE)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(items[:10])
    DOCTYPE
    Conference paper    897
    Article             503
    Review               37
    Book chapter         32
    Editorial             3
    Short survey          3
    Note                  3
    Book                  2
    Letter                1
    Name: count, dtype: int64



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip


class InspectColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = load_filtered_main_csv_zip(params=self.params)
        series = df[self.params.source_field.value].copy()
        series = series.dropna()
        series = series.str.split(";")
        series = series.explode()
        series = series.str.strip()
        values = series.value_counts()

        return values
