"""
BaseStartsWithMatch
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field, ThFile
    >>> from tm2p.refine._intern.match import BaseStartsWithMatch
    >>> (
    ...     BaseStartsWithMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_NORM)
    ...     .having_text_matching("fint")
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )

"""

import sys

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params, ParamsMixin

from ._intern import (
    add_padding,
    load_thesaurus,
    remove_builtin_stopwords,
    remove_punctuation,
    remove_thesaurus_stopwords,
    report_matches,
)
from .fuzzy_one_exact import (
    _compute_fuzzy_matches,
    _prepare_fuzzy_candidates,
    _select_one_exact_match_candidates,
)
from .fuzzy_zero_exact import _select_zero_exact_match_candidates

PREFERRED = ThField.PREFERRED.value


class BaseStartsWithMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = add_padding(thesaurus_df=thesaurus_df)  # type: ignore
        thesaurus_df = remove_punctuation(thesaurus_df=thesaurus_df)
        thesaurus_df = _startswith(thesaurus_df=thesaurus_df, params=self.params)
        thesaurus_df = remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _prepare_fuzzy_candidates(thesaurus_df=thesaurus_df)

        zero_exact_match_candidates = _select_zero_exact_match_candidates(
            thesaurus_df=thesaurus_df
        )

        one_exact_match_candidates = _select_one_exact_match_candidates(
            thesaurus_df=thesaurus_df
        )

        zero_exact_match_mapping = _compute_fuzzy_matches(
            thesaurus_df=zero_exact_match_candidates,
            similarity_cutoff=self.params.similarity_cutoff,
            fuzzy_threshold=0.0,
            use_word_level=False,
            word_count_tolerance=0,
            params=self.params,
        )

        one_exact_match_mapping = _compute_fuzzy_matches(
            thesaurus_df=one_exact_match_candidates,
            similarity_cutoff=self.params.similarity_cutoff,
            fuzzy_threshold=self.params.fuzzy_threshold,
            use_word_level=True,
            word_count_tolerance=1,
            params=self.params,
        )

        matches: dict[str, list[str]] = {
            **zero_exact_match_mapping,
            **one_exact_match_mapping,
        }

        report_matches(
            params=self.params,
            mapping=matches,
        )

        sys.stderr.write(f"\n{len(matches.keys())} synonym groups found\n")
        sys.stderr.flush()


def _startswith(thesaurus_df: pd.DataFrame, params: Params) -> pd.DataFrame:
    return thesaurus_df[  #  type: ignore
        thesaurus_df[PREFERRED].str.startswith(f"{params.pattern[0]}")
    ].copy()
