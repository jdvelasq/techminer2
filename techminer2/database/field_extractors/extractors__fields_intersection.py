# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Fields Intersection
===============================================================================

>>> from techminer2.database.field_extractors import FieldsIntersectionExtractor
>>> terms = (
...     FieldsIntersectionExtractor() 
...     #
...     .compare_field("author_keywords")
...     .to_field("index_keywords")
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
['ACTOR_NETWORK_THEORY',
 'ACTUALIZATION',
 'AGRICULTURE',
 'AGROPAY',
 'ARTIFICIAL_INTELLIGENCE',
 'BANKING',
 'BIG_DATA',
 'BLOCKCHAIN',
 'BUSINESS_MODELS',
 'CASE_STUDY_METHODS']

"""

from ...internals.mixins import InputFunctionsMixin
from ..internals.field_extractors.internal__fields_intersection import (
    internal__fields_intersection,
)


class FieldsIntersectionExtractor(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        return internal__fields_intersection(
            compare_field=self.params.source_field,
            to_field=self.params.dest_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
            database=self.params.database,
            record_years_range=self.params.record_years_range,
            record_citations_range=self.params.record_citations_range,
            records_order_by=None,
            records_match=self.params.records_match,
        )
