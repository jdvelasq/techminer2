# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordant Mapping
=========================================================================================

>>> # order_records_by:
>>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
>>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
>>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
>>> # 
>>> from techminer2.database.search import ConcordantMapping
>>> mapping = (
...     ConcordantMapping() 
...     #
...     .with_abstract_having_pattern("FINTECH")
...     #
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     .where_records_ordered_by("date_newest")   
...     #
...     .run()
... )
>>> from pprint import pprint
>>> pprint(mapping[0])
{'AB': 'we investigate THE_ECONOMIC_AND_TECHNOLOGICAL_DETERMINANTS inducing '
       'ENTREPRENEURS to establish VENTURES with THE_PURPOSE of reinventing '
       'FINANCIAL_TECHNOLOGY ( FINTECH )',
 'AR': 'Haddad C., 2019, SMALL BUS ECON, V53, P81',
 'AU': 'Haddad C.; Hornuf L.',
 'DE': 'ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS',
 'ID': nan,
 'PY': 2019,
 'SO': 'Small Business Economics',
 'TC': 258,
 'TI': 'The emergence of the global fintech market: economic and technological '
       'determinants',
 'UT': 1251}

    
"""
import re

from textblob import TextBlob  # type: ignore

from ..._internals.mixins import ParamsMixin, RecordMappingMixin, RecordViewerMixin
from .._internals.io.load_filtered_database import internal__load_filtered_database


class ConcordantMapping(
    ParamsMixin,
    RecordMappingMixin,
    RecordViewerMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_load_the_database(self):
        return internal__load_filtered_database(params=self.params)

    # -------------------------------------------------------------------------
    def _step_02__filter_by_concordance(self, records):
        search_for = self.params.pattern
        found = (
            records["abstract"]
            .astype(str)
            .str.contains(r"\b" + search_for + r"\b", regex=True)
        )
        records = records[found]
        return records

    # -------------------------------------------------------------------------
    def _step_03_process_abstracts(self, records):
        search_for = self.params.pattern
        #
        # extract phrases.
        records["abstract"] = records["abstract"].map(lambda x: TextBlob(x).sentences)
        records["abstract"] = records["abstract"].map(lambda x: [str(y) for y in x])
        records["abstract"] = records["abstract"].map(
            lambda x: [y[:-2] if y[-2:] == " ." else y for y in x]
        )
        #
        regex = r"\b" + search_for + r"\b"
        #
        records["abstract"] = records["abstract"].map(
            lambda x: [y for y in x if re.search(regex, y)]
        )
        records["abstract"] = records["abstract"].map(" . ".join)

        return records

    # -------------------------------------------------------------------------
    def run(self):

        records = self._step_01_load_the_database()
        records = self._step_02__filter_by_concordance(records)
        records = self._step_03_process_abstracts(records)
        mapping = self.build_record_mapping(records)

        return mapping
