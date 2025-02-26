# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordant Contexts
=========================================================================================

>>> # order_records_by:
>>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
>>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
>>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
>>> # 
>>> from techminer2.database.search import ConcordantContexts
>>> contexts = (
...     ConcordantContexts() 
...     #
...     .with_abstract_having_pattern("FINTECH")
...     #
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     .where_records_ordered_by("date_newest")   
...     #
...     .build()
... )
>>> for t in contexts[:10]: print(t)
<<< S with THE_PURPOSE of reinventing FINANCIAL_TECHNOLOGY ( FINTECH )
<<< ARTIFICIAL_INTELLIGENCE ( AI ) on FINANCIAL_TECHNOLOGY ( FINTECH ) , THE_PURPOSE of THIS_PAPER is to propose A_RESEARCH_F >>>
<<< ONSUMERS_PERCEPTIONS regarding THE_INTRODUCTION of AI in FINTECH 
                                                             FINTECH is about THE_INTRODUCTION of NEW_TECHNOLOGIES into THE_F >>>
<<< _ACADEMIC_FINANCE_COMMUNITY was not actively researching FINTECH , THE_EDITORIAL_TEAM of THE_REVIEW of FINANCIAL_STUDIES  >>>
<<<  learned from THE_SUBMITTED_PROPOSALS about THE_FIELD of FINTECH and WHICH_ONES we selected to be completed and ultimatel >>>
<<< NS to help guide FUTURE_RESEARCH in THE_EMERGING_AREA of FINTECH 
                               along_with THE_DEVELOPMENT of FINTECH , MANY_SCHOLARS have studied how INFORMATION_TECHNOLOGY  >>>
<<< DERLYING_BITCOIN , is AN_EMERGING_FINANCIAL_TECHNOLOGY ( FINTECH ) that_is poised to have STRATEGIC_IMPACTS on ORGANIZATIONS
                                      FINANCIAL_TECHNOLOGY ( FINTECH ) SERVICES using EMERGING_TECHNOLOGY such_as THE_INTERNE >>>


"""
import pandas as pd  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals.io import internal__load_filtered_database


class ConcordantContexts(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_1_load_the_database(self):
        return internal__load_filtered_database(params=self.params)

    # -------------------------------------------------------------------------
    def _step_2_extract_context_phrases(self, records):

        search_for = self.params.pattern

        records = records.set_index(
            pd.Index(records.record_id + " / " + records.raw_document_title)
        )

        # sorted_records = records.sort_values(
        #     ["global_citations", "local_citations", "year"],
        #     ascending=[False, False, True],
        # )

        records["_found_"] = (
            records["abstract"]
            .astype(str)
            .str.contains(r"\b" + search_for + r"\b", regex=True)
        )

        records = records[records["_found_"]]
        abstracts = records["abstract"]
        phrases = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
        context_phrases = phrases[phrases.map(lambda x: search_for in x)]

        return context_phrases

    # -------------------------------------------------------------------------
    def _step_3_create_contexts_dataframe(self, context_phrases):

        search_for = self.params.pattern

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

    # -------------------------------------------------------------------------
    def _step_4_transform_context_dataframe_to_texts(self, contexts):

        search_for = self.params.pattern
        contexts = contexts.copy()
        contexts["left_r"] = contexts["left_context"].str[::-1]

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

    # -------------------------------------------------------------------------
    def build(self):

        records = self._step_1_load_the_database()
        context_phrases = self._step_2_extract_context_phrases(records=records)
        contexts_dataframe = self._step_3_create_contexts_dataframe(context_phrases)
        texts = self._step_4_transform_context_dataframe_to_texts(contexts_dataframe)
        return texts
