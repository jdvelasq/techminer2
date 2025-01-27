# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
"""Functions to sort the axes of a DataFrame."""
import pandas as pd  # type: ignore


class SortAxesMixin:

    def sort_columns(self, data_frame):
        counters = pd.DataFrame({"term": data_frame.columns.tolist()})
        counters = self._extract_term_occurrences(counters)
        counters = self._extract_citation_counts(counters)
        sorted_topics = self._rank_terms_by_count_and_citations(counters)
        data_frame = data_frame[sorted_topics]
        return data_frame

    def sort_index(self, data_frame):
        counters = pd.DataFrame({"term": data_frame.index.tolist()})
        counters = self._extract_term_occurrences(counters)
        counters = self._extract_citation_counts(counters)
        sorted_topics = self._rank_terms_by_count_and_citations(counters)
        data_frame = data_frame.loc[sorted_topics, :]
        return data_frame

    def _rank_terms_by_count_and_citations(self, counters):
        counters = counters.sort_values(
            by=["OCC", "citations", "term"], ascending=[False, False, True]
        )
        sorted_topics = counters.term.tolist()
        return sorted_topics

    def _extract_citation_counts(self, counters):
        counters["citations"] = counters.term.str.split()
        counters["citations"] = counters["citations"].map(lambda x: x[-1])
        counters["citations"] = counters["citations"].str.split(":")
        counters["citations"] = counters["citations"].map(lambda x: x[1]).astype(int)
        return counters

    def _extract_term_occurrences(self, counters):
        counters["OCC"] = counters.term.str.split()
        counters["OCC"] = counters["OCC"].map(lambda x: x[-1])
        counters["OCC"] = counters["OCC"].str.split(":")
        counters["OCC"] = counters["OCC"].map(lambda x: x[0]).astype(int)
        return counters
