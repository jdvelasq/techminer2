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
...     .for_field(
...         with_name="author_keywords", 
...         with_terms_having_pattern="FINTECH",
...     ).for_data(
...         in_root_dir="example/",
...         where_database="main",
...         where_record_years_between=(None, None),
...         where_record_citations_between=(None, None),
...     ).build()
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
from ..internals.field_extractors.internal__contains import internal__contains
from ..internals.mixins.for_field_having_pattern import (
    FieldSearchPatternPMixin,
    ForFieldHavingPatternMixin,
)


class ContainsExtractor(
    ForFieldHavingPatternMixin,
):
    """:meta private:"""

    def __init__(self):

        self.with_name = FieldSearchPatternPMixin()

    def build(self):

        return internal__contains(
            field=self.field,
            pattern=self.pattern,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            **self.database_filters.__dict__,
        )
