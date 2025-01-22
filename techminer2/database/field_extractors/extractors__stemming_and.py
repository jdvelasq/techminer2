# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with AND
===============================================================================

>>> from techminer2.database.field_extractors import StemmingAndExtractor
>>> terms = (
...     StemmingAndExtractor() 
...     .with_source_field("author_keywords")
...     .matching_terms_with(
...             [
...                 "financial technology", 
...                 "artificial intelligence",
...             ],
...         ) 
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
['ARTIFICIAL_INTELLIGENCE',
 'FINANCIAL_TECHNOLOGY',
 'FINANCIAL_TECHNOLOGY (FINTECH)']

"""

from ...internals.mixins import InputFunctionsMixin
from ..internals.field_extractors.internal__stemming import internal__stemming_and


class StemmingAndExtractor(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__stemming_and(
            custom_items=self.params.selected_terms,
            source_field=self.params.source_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
            database=self.params.database,
            record_years_range=self.params.record_years_range,
            record_citations_range=self.params.record_citations_range,
            records_order_by=None,
            records_match=self.params.records_match,
        )
