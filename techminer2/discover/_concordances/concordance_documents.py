"""
Concordance Documents
=========================================================================================

Smoke test:
    >>> from techminer2 import RecordsOrderBy
    >>> from techminer2.analyze.concordances import ConcordanceDocuments
    >>> docs = (
    ...     ConcordanceDocuments()
    ...     #
    ...     .having_text_matching("FINTECH")
    ...     #
    ...     .where_root_directory("tests/fintech/")
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
    AB there is currently NO_CONSENSUS about what THE_TERM_FINTECH means .
       this_paper_explores THE_COMPLEXITY of FINTECH , and attempts A_DEFINITION ,
       drawn from A_PROCESS of reviewing more than 200 scholarly articles
       referencing THE_TERM_FINTECH and covering A_PERIOD of more than 40 years .
       the_objective_of_this_study_is_to offer A_DEFINITION which is distinct as
       well as succinct in ITS_COMMUNICATION , yet sufficiently broad in ITS_RANGE
       of APPLICATION . as THE_ORIGINS of THE_TERM can neither be unequivocally
       placed in ACADEMIA nor in PRACTICE , THE_DEFINITION concentrates on
       extracting out THE_QUINTESSENCE of FINTECH using BOTH_SPHERES . applying
       SEMANTIC_ANALYSIS and BUILDING on THE_COMMONALITIES of 13 peerreviewed
       DEFINITIONS of THE_TERM , it_is_concluded_that FINTECH is
       A_NEW_FINANCIAL_INDUSTRY that APPLIES_TECHNOLOGY to improve
       FINANCIAL_ACTIVITIES . THE_IMPLICATIONS as well as THE_SHORTCOMINGS of
       THIS_DEFINITION are discussed . 2021 journal of innovation management . all
       rights reserved .
    DE Banking; Financial institution; Financial services; Innovation; Research;
       Technology; Terminology
    <BLANKLINE>


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.record_builders import dicts_to_strings
from techminer2.discover._concordances.concordance_records import ConcordanceRecords

__reviewed__ = "2026-01-29"


class ConcordanceDocuments(ParamsMixin):
    """:meta private:"""

    def run(self):

        mapping = ConcordanceRecords().update(**self.params.__dict__).run()
        documents = dicts_to_strings(mapping)
        return documents
