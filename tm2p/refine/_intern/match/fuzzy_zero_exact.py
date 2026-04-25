"""
BaseFuzzyZeroExactMatch
===============================================================================

Smoke test:
    >>> from tm2p.enum import ThFile, AnalysisUnit
    >>> from tm2p.refine._intern.match import BaseFuzzyZeroExactMatch
    >>> (
    ...     BaseFuzzyZeroExactMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
    ...     .using_similarity_cutoff(90)
    ...     .using_fuzzy_threshold(0)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )

"""

import sys

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from ._intern import (
    add_padding,
    load_thesaurus,
    remove_builtin_stopwords,
    remove_punctuation,
    remove_thesaurus_stopwords,
    report_matches,
)
from .fuzzy_one_exact import _compute_fuzzy_matches, _prepare_fuzzy_candidates


class BaseFuzzyZeroExactMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = add_padding(thesaurus_df=thesaurus_df)  # type: ignore
        thesaurus_df = remove_punctuation(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _prepare_fuzzy_candidates(thesaurus_df=thesaurus_df)
        thesaurus_df = _select_zero_exact_match_candidates(thesaurus_df=thesaurus_df)

        matches = _compute_fuzzy_matches(
            thesaurus_df=thesaurus_df,
            similarity_cutoff=self.params.similarity_cutoff,
            fuzzy_threshold=0.0,
            use_word_level=False,
            word_count_tolerance=0,
            params=self.params,
        )

        report_matches(
            params=self.params,
            mapping=matches,
        )

        sys.stderr.write(f"\n{len(matches.keys())} synonym groups found\n")
        sys.stderr.flush()


def _select_zero_exact_match_candidates(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    return thesaurus_df[thesaurus_df["word_count"] == 1].reset_index(drop=True).copy()  # type: ignore
