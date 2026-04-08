"""
RecordMapping
===============================================================================

Smoke Test:
    >>> from pprint import pprint
    >>> from tm2p.enum import Field, RecordOrderBy
    >>> from tm2p.ingest.records import RecordMapping
    >>> mapping = (
    ...     RecordMapping()
    ...     #
    ...     .with_source_field(Field.ABSTR_RAW)
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.GCS_HIGHEST)
    ...     .run()
    ... )
    >>> pprint(mapping[0])



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access.load_filtered_main_csv_zip import (
    load_filtered_main_csv_zip,
)
from tm2p._intern.rec_build import records_to_dicts


class RecordMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        records = load_filtered_main_csv_zip(params=self.params)
        mapping = records_to_dicts(records, field=self.params.source_field)
        return mapping
