# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Find records
===============================================================================

>>> from techminer2.database.search import FindRecords
>>> docs = (
...     FindRecords() 
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     #
...     # SEARCH:
...     .with_field_pattern('REGTECH')
...     .with_regex_search(False)
...     .with_case_sensitive(False)
...     .with_regex_flags(0)
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     .where_records_ordered_by("date_newest")   
...     #
...     .build()
... )
>>> print(docs[0])
UT 1251
AR Haddad C., 2019, SMALL BUS ECON, V53, P81
TI The emergence of the global fintech market: economic and technological
   determinants
AU Haddad C.; Hornuf L.
TC 258
SO Small Business Economics
PY 2019
AB we investigate THE_ECONOMIC_AND_TECHNOLOGICAL_DETERMINANTS inducing
   ENTREPRENEURS to establish VENTURES with THE_PURPOSE of reinventing
   FINANCIAL_TECHNOLOGY ( FINTECH ) . we find that COUNTRIES witness
   MORE_FINTECH startup FORMATIONS when THE_ECONOMY is
   WELL_DEVELOPED_AND_VENTURE_CAPITAL is readily available . furthermore ,
   THE_NUMBER of SECURE_INTERNET_SERVERS , MOBILE_TELEPHONE_SUBSCRIPTIONS , and
   THE_AVAILABLE_LABOR_FORCE has A_POSITIVE_IMPACT on THE_DEVELOPMENT of
   THIS_NEW_MARKET_SEGMENT . finally , the more difficult it is for COMPANIES
   to ACCESS_LOANS , the higher is THE_NUMBER of FINTECH_STARTUPS in A_COUNTRY
   . overall , THE_EVIDENCE suggests that FINTECH_STARTUP_FORMATION_NEED not be
   left to CHANCE , but ACTIVE_POLICIES can INFLUENCE THE_EMERGENCE of
   THIS_NEW_SECTOR . 2018 , the author ( s ) .
DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
<BLANKLINE>





"""
from ...internals.mixins import (
    InputFunctionsMixin,
    RecordMappingMixin,
    RecordViewerMixin,
)
from ..load.load__database import DatabaseLoader


class FindRecords(
    InputFunctionsMixin,
    RecordMappingMixin,
    RecordViewerMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_load_the_database(self):
        return DatabaseLoader().update_params(**self.params.__dict__).build()

    # -------------------------------------------------------------------------
    def _step_02_filter_the_records(self, records):

        records = records.copy()
        records = records.dropna(subset=[self.params.field])

        contains = records[self.params.field].str.contains(
            pat=self.params.pattern,
            case=self.params.case_sensitive,
            flags=self.params.regex_flags,
            regex=self.params.regex_search,
        )

        records = records.loc[contains.index, :]

        return records

    # -------------------------------------------------------------------------
    def build(self):

        records = self._step_01_load_the_database()
        records = self._step_02_filter_the_records(records)
        mapping = self.build_record_mapping(records)
        documents = self.build_record_viewer(mapping)

        return documents
