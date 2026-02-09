"""
Concordance Raw
=========================================================================================

Smoke test:
    >>> from techminer2 import RecordsOrderBy
    >>> from techminer2.text.concordances import ConcordanceRaw
    >>> contexts = (
    ...     ConcordanceRaw()
    ...     #
    ...     # PATTERN:
    ...     .having_text_matching("FINTECH")
    ...     #
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordsOrderBy.PUBYEAR_NEWEST)
    ...     #
    ...     .run()
    ... )
    >>> assert isinstance(contexts, list)
    >>> assert len(contexts) > 0
    >>> assert all(isinstance(c, str) for c in contexts)
    >>> for t in contexts[:10]: print(t)
             There is currently no consensus about what the term FINTECH means
      …ing more than 200 scholarly articles referencing the term FINTECH and covering a period of more than 40 years
      …nition concentrates on extracting out the quintessence of FINTECH using both spheres
      …eerreviewed definitions of the term, it is concluded that FINTECH is a new financial industry that applies technology to im…
       …historical development of China's financial technology ( FINTECH ) industry
      …nts a stepping stone in exploring the interaction between FINTECH and its yet unfolding social and political context
               It also discusses policy implications for China's FINTECH industry, focusing on the changing role of the state in f…
      …ion in the past few years reflected by the emergence of “ FINTECH ,” which represents the marriage of “finance” and “inform…
                                                               ” FINTECH provides opportunities for the creation of new services a…
                                                      Therefore, FINTECH has become a subject of debate among practitioners, inves…


"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin

__reviewed__ = "2026-01-29"


class ConcordanceRaw(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        from techminer2.text.concordances import ConcordanceUser

        return (
            ConcordanceUser()
            .update(**self.params.__dict__)
            .with_field(CorpusField.ABS_RAW)
            .run()
        )
