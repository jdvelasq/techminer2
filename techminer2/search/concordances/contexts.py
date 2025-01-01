# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Contexts (MIGRATED)
=========================================================================================

## >>> from techminer2.search.concordances import Contexts
## >>> contexts = (
## ...     Contexts() 
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...         sort_by="date_newest", # date_newest, date_oldest, global_cited_by_highest, 
## ...                                # global_cited_by_lowest, local_cited_by_highest, 
## ...                                # local_cited_by_lowest, first_author_a_to_z, 
## ...                                # first_author_z_to_a, source_title_a_to_z, 
## ...                                # source_title_z_to_a
## ...     ).build(search_for='FINTECH')
## ... )
## >>> for t in contexts[:20]: print(t)
                             the INDUSTRY_OVERALL , and many FINTECH start_ups are looking for NEW_PATHWAYS to SUCCESSFUL_BUS >>>
                                                             FINTECH brings about a NEW_PARADIGM in which INFORMATION_TECHNOL >>>
                                                             FINTECH is touted as a GAME changing , DISRUPTIVE_INNOVATION cap >>>
                this ARTICLE_INTRODUCES a HISTORICAL_VIEW of FINTECH and discusses the ECOSYSTEM of the FINTECH_SECTOR
<<< ich embraces three KEY_DIMENSIONS of DIGITAL_FINANCE and FINTECH , i
<<< s with the purpose of reinventing FINANCIAL_TECHNOLOGY ( FINTECH )
                   as a NEW_TERM in the FINANCIAL_INDUSTRY , FINTECH has become a POPULAR_TERM that describes NOVEL_TECHNOLOG >>>
                     an accurate and up_to_date AWARENESS of FINTECH has an URGENT_DEMAND for both academics and professionals
<<< PORARY_ACHIEVEMENTS , by which a theoretical data_driven FINTECH framework is proposed
                       this PAPER_EXPLORES the COMPLEXITY of FINTECH , and attempts a DEFINITION , drawn from a PROCESS of re >>>
<<< ITION_CONCENTRATES on extracting out the quintessence of FINTECH using both spheres
<<< rreviewed definitions of the term , IT is concluded that FINTECH is a NEW_FINANCIAL_INDUSTRY that APPLIES_TECHNOLOGY to i >>>
<<< ARTIFICIAL_INTELLIGENCE ( AI ) on FINANCIAL_TECHNOLOGY ( FINTECH ) , the purpose of this paper is to propose a RESEARCH_F >>>
<<< ONSUMERS_PERCEPTIONS regarding the introduction of AI in FINTECH 
<<<  to aid the understanding of the DISRUPTIVE_POTENTIAL of FINTECH , and its implications for the wider FINANCIAL_ECOSYSTEM
<<< DEVELOPMENT , the CURRENT_STATE , and POSSIBLE_FUTURE of FINTECH 
        IT is also of interest to bankers who might consider FINTECH and STRATEGIC_PARTNERSHIPS as a prospective , future str >>>
                                                             FINTECH is about the introduction of NEW_TECHNOLOGIES into the F >>>
<<<  academic FINANCE COMMUNITY was not actively researching FINTECH , the EDITORIAL_TEAM of the REVIEW of FINANCIAL_STUDIES  >>>
<<<  learned from the submitted proposals about the field of FINTECH and which ones we selected to be completed and ultimatel >>>

"""
import pandas as pd  # type: ignore

from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.read_filtered_database import read_filtered_database
from .._core.get_context_phrases_from_records import _get_context_phrases_from_records


class Contexts(
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.database_params = DatabaseParams()

    def build(self, search_for: str):
        return concordance_contexts(search_for, **self.database_params.__dict__)


def concordance_contexts(
    #
    # FUNCTION PARAMS:
    search_for: str,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    sort_by: str = "date_newest",
    **filters,
):
    """:meta private:"""

    def create_contexts_table(
        context_phrases: pd.Series,
    ):
        """Extracts the contexts table."""

        regex = r"\b" + search_for + r"\b"
        contexts = context_phrases.str.extract(
            r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)"
        )

        contexts["left_context"] = contexts["left_context"].fillna("")
        contexts["left_context"] = contexts["left_context"].str.strip()

        contexts["right_context"] = contexts["right_context"].fillna("")
        contexts["right_context"] = contexts["right_context"].str.strip()

        contexts = contexts[
            contexts["left_context"].map(lambda x: x != "")
            | contexts["right_context"].map(lambda x: x != "")
        ]

        return contexts

    def transform_context_table_to_contexts(
        contexts: pd.DataFrame,
    ):
        """Transforms the contexts table to a text."""

        contexts = contexts.copy()

        contexts["left_r"] = contexts["left_context"].str[::-1]

        # contexts = contexts.sort_values(["left_r", "right_context"])

        contexts["left_context"] = contexts["left_context"].map(
            lambda x: "<<< " + x[-56:] if len(x) > 60 else x
        )
        contexts["right_context"] = contexts["right_context"].map(
            lambda x: x[:56] + " >>>" if len(x) > 60 else x
        )

        texts = []
        for _, row in contexts.iterrows():
            text = (
                f"{row['left_context']:>60} {search_for.upper()} {row['right_context']}"
            )
            texts.append(text)

        return texts

    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    context_phrases = _get_context_phrases_from_records(
        search_for=search_for,
        records=records,
    )
    context_table = create_contexts_table(context_phrases)
    contexts = transform_context_table_to_contexts(context_table)

    return contexts
