# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordant Processed Contexts
=========================================================================================

Example:
    >>> from techminer2.database.search import ConcordantProcessedContexts

    >>> # Create, configure, and run the finder
    >>> # order_records_by:
    >>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
    >>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
    >>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
    >>> #
    >>> finder = (
    ...     ConcordantProcessedContexts()
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
           in THIS_INTRODUCTORY_ARTICLE , we describe the recent FINTECH phenomenon and the novel editorial protocol employed for >>>
    <<<  learned from the submitted proposals about the field of FINTECH and which ones we selected to be completed and ultimatel >>>
            in this study , we unveil the drivers motivating the FINTECH phenomenon perceived by the english and german popular p >>>


"""
import pandas as pd  # type: ignore
from techminer2.database.search.concordant_raw_contexts import ConcordantRawContexts


class ConcordantProcessedContexts(
    ConcordantRawContexts,
):
    """:meta private:"""

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
        abstracts = records["abstract"]
        phrases = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
        context_phrases = phrases[phrases.map(lambda x: search_for in x)]

        return context_phrases
