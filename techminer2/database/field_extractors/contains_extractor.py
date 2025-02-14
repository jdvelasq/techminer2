# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Contains
===============================================================================

>>> from techminer2.database.field_extractors import ContainsExtractor
>>> terms = (
...     ContainsExtractor() 
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     #
...     # SEARCH:
...     .having_terms_like("FINTECH")
...     .having_case_sensitive(False)
...     .having_regex_flags(0)
...     .having_regex_search(False)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['BANK_FINTECH_PARTNERSHIP',
 'FINANCIAL_TECHNOLOGY (FINTECH)',
 'FINTECH',
 'FINTECH_DISRUPTION',
 'FINTECH_INDUSTRY',
 'FINTECH_SERVICES']


"""
from ...internals.mixins import ParamsMixin
from .internals.internal__contains import internal__contains


class ContainsExtractor(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__contains(
            #
            # FIELD:
            field=self.params.field,
            #
            # SEARCH:
            term_pattern=self.params.pattern,
            case_sensitive=self.params.case_sensitive,
            regex_flags=self.params.regex_flags,
            regex_search=self.params.regex_search,
            #
            # DATABASE:
            root_dir=self.params.root_dir,
            database=self.params.database,
            record_years_range=self.params.record_years_range,
            record_citations_range=self.params.record_citations_range,
            records_order_by=None,
            records_match=self.params.record_filters,
        )
