# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=attribute-defined-outside-init
"""
Concordant Sentences
=========================================================================================

Example:
    >>> from techminer2.concordances import ConcordantSentences

    >>> # Create, configure, and run the finder
    >>> # order_records_by:
    >>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
    >>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
    >>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
    >>> #
    >>> sentences = (
    ...     ConcordantSentences()
    ...     #
    ...     # PATTERN:
    ...     .with_abstract_having_pattern("FINTECH")
    ...     #
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("date_newest")
    ...     #
    ...     .run()
    ... )
    >>> for t in sentences[:10]: print(t) # doctest: +NORMALIZE_WHITESPACE
    we investigate the economic and technological determinants inducing entrepreneurs to establish ventures with the purpose of reinventing financial technology ( fintech )
    we find that countries witness more fintech startup formations when the economy is well developed and venture capital is readily available
    finally , the more difficult it is for companies to access loans , the higher is the number of fintech startups in a country
    overall , the evidence suggests that fintech startup formation need not be left to chance , but active policies can influence the emergence of this new sector
    we provide large scale evidence on the occurrence and value of fintech innovation
    we find that most fintech innovations yield substantial value to innovators , with blockchain being particularly valuable
    purpose : considering the increasing impact of artificial intelligence ( ai ) on financial technology ( fintech ) , the purpose of this paper is to propose a research framework to better understand robo advisor adoption by a wide range of potential customers
    it contributes to understanding consumers ' perceptions regarding the introduction of ai in fintech
    fintech is about the introduction of new technologies into the financial sector , and it is now revolutionizing the financial industry
    in 2017 , when the academic finance community was not actively researching fintech , the editorial team of the review of financial studies launched a competition to develop research proposals focused on this topic


"""
import re

import pandas as pd  # type: ignore

from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.user_data import (
    internal__load_filtered_records_from_database,
)


class ConcordantSentences(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_the_database(self):
        self.records = internal__load_filtered_records_from_database(params=self.params)

    # -------------------------------------------------------------------------
    def internal__extract_raw_context_phrases(self):

        search_for = self.params.pattern.lower().replace("_", " ")

        records = self.records.set_index(
            pd.Index(self.records.record_id + " / " + self.records.raw_document_title)
        )

        records["_found_"] = (
            records["tokenized_abstract"]
            .astype(str)
            .str.contains(r"\b" + search_for + r"\b", regex=True)
        )

        records = records[records["_found_"]]
        abstracts = records["tokenized_abstract"]
        phrases = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
        self.context_phrases = phrases[phrases.map(lambda x: search_for in x)].to_list()

    # -------------------------------------------------------------------------
    def internal__extract_processed_context_phrases(self):

        search_for = self.params.pattern

        records = self.records.set_index(
            pd.Index(self.records.record_id + " / " + self.records.raw_document_title)
        )

        records["_found_"] = (
            records["abstract"]
            .astype(str)
            .str.contains(r"\b" + re.escape(search_for) + r"\b", regex=True)
        )

        records = records[records["_found_"]]
        abstracts = records["abstract"]
        phrases = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
        self.context_phrases = phrases[phrases.map(lambda x: search_for in x)].to_list()

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__load_the_database()
        self.internal__extract_processed_context_phrases()
        return self.context_phrases
