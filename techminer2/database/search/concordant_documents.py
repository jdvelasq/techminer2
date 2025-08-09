# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordant Documents
=========================================================================================


Example:
    >>> from techminer2.database.search import ConcordantDocuments

    >>> # Create, configure, and run the finder
    >>> # order_records_by:
    >>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
    >>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
    >>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
    >>> #
    >>> finder = (
    ...     ConcordantDocuments()
    ...     #
    ...     .with_abstract_having_pattern("FINTECH")
    ...     #
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("date_newest")
    ... )
    >>> docs = finder.run()

    >>> print(len(docs))
    46

    >>> print(docs[0])
    UT 26
    AR Haddad C., 2019, SMALL BUS ECON, V53, P81
    TI The emergence of the global fintech market: economic and technological
       determinants
    AU Haddad C.; Hornuf L.
    TC 258
    SO Small Business Economics
    PY 2019
    AB we investigate the economic and technological determinants inducing
       entrepreneurs to establish ventures with the purpose of reinventing
       financial technology ( fintech ) . we find that countries witness more
       fintech startup formations when the economy is well developed and venture
       capital is readily available . finally , the more difficult it is for
       companies to access loans , the higher is the number of fintech startups in
       a country . overall , the evidence suggests that fintech startup formation
       need not be left to chance , but active policies can influence the emergence
       of this new sector
    DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
    <BLANKLINE>


"""
from techminer2._internals.mixins import ParamsMixin, RecordViewerMixin

from .concordant_mapping import ConcordantMapping


class ConcordantDocuments(
    ParamsMixin,
    RecordViewerMixin,
):
    """:meta private:"""

    def run(self):

        mapping = ConcordantMapping().update(**self.params.__dict__).run()
        documents = self.build_record_viewer(mapping)
        return documents
