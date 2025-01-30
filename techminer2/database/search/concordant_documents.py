# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordant Documents
=========================================================================================

>>> # order_records_by:
>>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
>>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
>>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
>>> # 
>>> from techminer2.database.search import ConcordantDocuments
>>> docs = (
...     ConcordantDocuments() 
...     #
...     .with_abstract_having_pattern("FINTECH")
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
>>> print(len(docs))
35
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
   FINANCIAL_TECHNOLOGY ( FINTECH )
DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
<BLANKLINE>
    
"""
from ...internals.mixins import InputFunctionsMixin, RecordViewerMixin
from .concordant_mapping import ConcordantMapping


class ConcordantDocuments(
    InputFunctionsMixin,
    RecordViewerMixin,
):
    """:meta private:"""

    def build(self):

        mapping = ConcordantMapping().update_params(**self.params.__dict__).build()
        documents = self.build_record_viewer(mapping)
        return documents
