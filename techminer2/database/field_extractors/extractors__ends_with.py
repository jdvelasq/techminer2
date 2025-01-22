# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Ends With
===============================================================================

>>> from techminer2.database.field_extractors import EndsWithExtractor
>>> terms = (
...     EndsWithExtractor() 
...     #
...     .with_source_field("author_keywords")
...     .with_terms_having_pattern("ING")
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> from pprint import pprint
>>> pprint(terms[:10])
['BANKING',
 'CLOUD_COMPUTING',
 'CROWDFUNDING',
 'DATA_MINING',
 'DIGITAL_BANKING',
 'ECONOMIC_FORECASTING',
 'FINANCIAL_COMPUTING',
 'FUTURE_OF_BANKING',
 'LENDING',
 'MARKETPLACE_LENDING']
 
"""
from ...internals.mixins import InputFunctionsMixin
from ..internals.field_extractors.internal__ends_with import internal__ends_with


class EndsWithExtractor(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__ends_with(
            source_field=self.params.source_field,
            term_pattern=self.params.term_pattern,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
            database=self.params.database,
            record_years_range=self.params.record_years_range,
            record_citations_range=self.params.record_citations_range,
            records_order_by=None,
            records_match=self.params.records_match,
        )
