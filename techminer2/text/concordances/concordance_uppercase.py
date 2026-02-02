"""
Concordance Uppercase
=========================================================================================

Smoke test:
    >>> from techminer2 import RecordsOrderBy
    >>> from techminer2.text.concordances import ConcordanceUppercase
    >>> contexts = (
    ...     ConcordanceUppercase()
    ...     #
    ...     # PATTERN:
    ...     .having_text_matching("FINTECH")
    ...     #
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordsOrderBy.DATE_NEWEST)
    ...     #
    ...     .run()
    ... )
    >>> assert isinstance(contexts, list)
    >>> assert len(contexts) > 0
    >>> assert all(isinstance(c, str) for c in contexts)
    >>> for t in contexts[:10]: print(t)  # doctest: +SKIP
                           this paper explores THE_COMPLEXITY of FINTECH , and attempts A_DEFINITION , drawn from A_PROCESS of rev…
      …NITION concentrates on extracting out THE_QUINTESSENCE of FINTECH using BOTH_SPHERES
      …erreviewed DEFINITIONS of THE_TERM , it is concluded that FINTECH is A_NEW_FINANCIAL_INDUSTRY that APPLIES_TECHNOLOGY to im…
      …nts A_STEPPING_STONE in exploring THE_INTERACTION between FINTECH and its yet unfolding SOCIAL_AND_POLITICAL_CONTEXT
      …N in THE_PAST_FEW_YEARS reflected by THE_EMERGENCE of ' ' FINTECH , ' ' which represents THE_MARRIAGE of ' ' FINANCE ' ' an…
                                                             ' ' FINTECH provides OPPORTUNITIES for THE_CREATION of NEW_SERVICES a…
                                                     therefore , FINTECH has become A_SUBJECT of DEBATE among PRACTITIONERS , INVE…
       …press including THE_SUBJECTS discussed in the context of FINTECH
                in doing so , we extend THE_GROWING_KNOWLEDGE on FINTECH and contribute to A_COMMON_UNDERSTANDING in THE_FINANCIAL…
                                    ) , who explore THE_FIELD of FINTECH


"""

from techminer2 import Field
from techminer2._internals import ParamsMixin

__reviewed__ = "2026-01-29"


class ConcordanceUppercase(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        from techminer2.text.concordances import ConcordanceUser

        return (
            ConcordanceUser()
            .update(**self.params.__dict__)
            .with_field(Field.ABS_UPPER_NP)
            .run()
        )
