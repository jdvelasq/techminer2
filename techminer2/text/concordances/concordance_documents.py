"""
Concordance Documents
=========================================================================================

Smoke test:
    >>> from techminer2 import RecordsOrderBy
    >>> from techminer2.text.concordances import ConcordanceDocuments
    >>> docs = (
    ...     ConcordanceDocuments()
    ...     #
    ...     .having_text_matching("FINTECH")
    ...     #
    ...     .where_root_directory("examples/small/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordsOrderBy.PUBYEAR_NEWEST)
    ...     .run()
    ... )
    >>> assert isinstance(docs, list)
    >>> assert len(docs) > 0
    >>> assert all(isinstance(d, str) for d in docs)
    >>> print(docs[0])
    UT 17
    AR Schueffel, 2016, J INNOV MANAG, V4, P32
    TI Taming the beast: A scientific definition of fintech
    AU Schueffel P.
    TC 394
    SO J. Innov.  Manag.
    PY 2016
    AB there is currently no consensus about what the term fintech means . this
       paper explores the complexity of fintech , and attempts a definition , drawn
       from a process of reviewing more than 200 scholarly articles referencing the
       term fintech and covering a period of more than 40 years .
       the_objective_of_this study is to offer a definition which is distinct
       as_well_as succinct in its communication , yet sufficiently broad in its
       range of application . as the origins of the term can neither be
       unequivocally placed in academia nor in practice , the definition
       concentrates on extracting out the quintessence of fintech using both
       spheres . applying semantic analysis and building on the commonalities of 13
       peerreviewed definitions of the term , it is concluded that fintech is a new
       financial industry that applies technology to improve financial activities .
       the implications as_well_as the shortcomings of this definition are
       diskussed . 2021 journal of innovation management . all rights reserved .
    DE Banking; Financial institution; Financial services; Innovation; Research;
       Technology; Terminology
    <BLANKLINE>



"""

from techminer2._internals import ParamsMixin
from techminer2._internals.record_builders import dicts_to_strings
from techminer2.text.concordances.concordance_records import ConcordanceRecords

__reviewed__ = "2026-01-29"


class ConcordanceDocuments(ParamsMixin):
    """:meta private:"""

    def run(self):

        mapping = ConcordanceRecords().update(**self.params.__dict__).run()
        documents = dicts_to_strings(mapping)
        return documents
