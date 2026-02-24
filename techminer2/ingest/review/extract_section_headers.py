"""
Extract Colon Phrases
===============================================================================

Smoke test:
    >>> from techminer2.ingest.review import ExtractSectionHeaders
    >>> text = (
    ...     ExtractSectionHeaders()
    ...     .where_root_directory("tests/fintech/")
    ...     .run()
    ... )
    >>> assert isinstance(text, list)
    >>> assert all(isinstance(t, str) for t in text)
    >>> for t in text: print(t)
                                                    introduction  :  since 2015 is THE_YEAR of FINTECH in TAIWAN , it is worth…
                                                case description  :  this_study used A_CASE_STUDY_INVESTIGATION of a top 5 BAN…
                                       discussion and evaluation  :  this_study has SEVERAL_FINDINGS : ( 1 ) REGULATIONS_AND_P…
                                                      conclusion  :  the_findings and DISCUSSION can benefit RESEARCHERS and A…
      …RS and ASSET_MANAGERS are scrambling for MORE_INFORMATION  :  who are THE_KEY_PLAYERS ? what is driving THE_EXPLOSIVE_G…
      …HNOLOGY and TRANSACTION_ORIENTATION , OWNERSHIP_STRUCTURE  :  PARTNERSHIPS , STABILITY and INSTITUTIONAL_FRANCHISE_VALU…
                                       our_contributions include  :  1 ) this_study_is the first to unveil THE_IMPACT of UGC_M…
                                                        overview  :  A_SUCCESSION of NEW_USER_ORIENTED_SERVICES combining FINA…
      …_BANKING THE_NEXT_REVOLUTION in OUR_CREDIT_DRIVEN_ECONOMY  :  THE_ADVENT of FINANCIAL_TECHNOLOGY_INTEGRATES_MARKET_THEO…
      …_ANALYTICS for GREEN_AND_SUSTAINABLE_ECONOMIC_DEVELOPMENT  :  SUPPLY_CHAIN_MODELS and FINANCIAL_TECHNOLOGIES_FOCUSES on…

"""

from techminer2._internals import ParamsMixin
from techminer2.discover._concordances import ConcordanceUppercase

__reviewed__ = "2026-01-28"


class ExtractSectionHeaders(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> list[str]:

        return (
            ConcordanceUppercase()
            .update(**self.params.__dict__)
            .having_text_matching(" : ")
            .run()
        )
