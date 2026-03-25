"""
BaseFuzzyZeroExactMatch
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field, ThFile
    >>> from tm2p.refine._intern.match import BaseFuzzyZeroExactMatch
    >>> (
    ...     BaseFuzzyZeroExactMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.CONCEPT_RAW)
    ...     .using_similarity_cutoff(90)
    ...     .using_fuzzy_threshold(0)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    1


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from ._report_matches import report_matches
from .fuzzy_one_exact import _compute_fuzzy_matches, _prepare_fuzzy_candidates
from .wordorder import (
    _add_padding,
    _load_thesaurus,
    _remove_builtin_stopwords,
    _remove_thesaurus_stopwords,
)


class BaseFuzzyZeroExactMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        thesaurus_df = _load_thesaurus(params=self.params)
        thesaurus_df = _add_padding(thesaurus_df=thesaurus_df)
        thesaurus_df = _remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _prepare_fuzzy_candidates(thesaurus_df=thesaurus_df)
        thesaurus_df = _select_zero_exact_match_candidates(thesaurus_df=thesaurus_df)

        mapping = _compute_fuzzy_matches(
            thesaurus_df=thesaurus_df,
            similarity_cutoff=self.params.similarity_cutoff,
            fuzzy_threshold=0.0,
            use_word_level=False,
            word_count_tolerance=0,
        )

        report_matches(
            params=self.params,
            mapping=mapping,
        )

        return 1


def _select_zero_exact_match_candidates(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    return thesaurus_df[thesaurus_df["word_count"] == 1].reset_index(drop=True).copy()  # type: ignore
