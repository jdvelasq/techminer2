# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordant Raw Contexts
=========================================================================================

Example:
    >>> from techminer2.database.search import ConcordantRawContexts

    >>> # Create, configure, and run the finder
    >>> # order_records_by:
    >>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
    >>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
    >>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
    >>> #
    >>> finder = (
    ...     ConcordantRawContexts()
    ...     #
    ...     # PATTERN:
    ...     .with_abstract_having_pattern("FINTECH")
    ...     #
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("date_newest")
    ... )
    >>> contexts = finder.run()
    >>> for t in contexts[:10]: print(t) # doctest: +NORMALIZE_WHITESPACE
    <<< s with the purpose of reinventing financial technology ( FINTECH )
                             we find that countries witness more FINTECH startup formations when the economy is well developed an >>>
    <<<  companies to access loans , the higher is the number of FINTECH startups in a country
                            overall , the evidence suggests that FINTECH startup formation need not be left to chance , but activ >>>
    <<< vide large scale evidence on the occurrence and value of FINTECH innovation
                                               we find that most FINTECH innovations yield substantial value to innovators , with >>>
    <<< artificial intelligence ( ai ) on financial technology ( FINTECH ) , the purpose of this paper is to propose a research f >>>
    <<< sumers ' perceptions regarding the introduction of ai in FINTECH
                                                                 FINTECH is about the introduction of new technologies into the f >>>
    <<<  academic finance community was not actively researching FINTECH , the editorial team of the review of financial studies  >>>


"""
import pandas as pd  # type: ignore
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_filtered_records_from_database,
)


class ConcordantRawContexts(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_1_load_the_database(self):
        return internal__load_filtered_records_from_database(params=self.params)

    # -------------------------------------------------------------------------
    def _step_2_extract_context_phrases(self, records):

        search_for = self.params.pattern.lower().replace("_", " ")

        records = records.set_index(
            pd.Index(records.record_id + " / " + records.raw_document_title)
        )

        records["_found_"] = (
            records["tokenized_abstract"]
            .astype(str)
            .str.contains(r"\b" + search_for + r"\b", regex=True)
        )

        records = records[records["_found_"]]
        abstracts = records["tokenized_abstract"]
        phrases = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
        context_phrases = phrases[phrases.map(lambda x: search_for in x)]

        return context_phrases

    # -------------------------------------------------------------------------
    def _step_3_create_contexts_dataframe(self, context_phrases):

        search_for = self.params.pattern.lower().replace("_", " ")

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
    def run(self):

        records = self._step_1_load_the_database()
        context_phrases = self._step_2_extract_context_phrases(records=records)
        contexts_dataframe = self._step_3_create_contexts_dataframe(context_phrases)
        texts = self._step_4_transform_context_dataframe_to_texts(contexts_dataframe)
        return texts
