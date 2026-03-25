"""
BaseEndsWithMatch
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field, ThFile
    >>> from tm2p.refine._intern.match import BaseEndsWithMatch
    >>> (
    ...     BaseEndsWithMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.CONCEPT_RAW)
    ...     .having_text_matching("ion")
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    1


"""

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params, ParamsMixin

from ._report_matches import report_matches
from .fuzzy_one_exact import (
    _compute_fuzzy_matches,
    _prepare_fuzzy_candidates,
    _select_one_exact_match_candidates,
)
from .fuzzy_zero_exact import _select_zero_exact_match_candidates
from .wordorder import (
    _add_padding,
    _load_thesaurus,
    _remove_builtin_stopwords,
    _remove_thesaurus_stopwords,
)

PREFERRED = ThField.PREFERRED.value


class BaseEndsWithMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        thesaurus_df = _load_thesaurus(params=self.params)
        thesaurus_df = _add_padding(thesaurus_df=thesaurus_df)
        thesaurus_df = _endswith(thesaurus_df=thesaurus_df, params=self.params)
        thesaurus_df = _remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
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
        )

        one_exact_match_mapping = _compute_fuzzy_matches(
            thesaurus_df=one_exact_match_candidates,
            similarity_cutoff=self.params.similarity_cutoff,
            fuzzy_threshold=self.params.fuzzy_threshold,
            use_word_level=True,
            word_count_tolerance=1,
        )

        report_matches(
            params=self.params,
            mapping={**zero_exact_match_mapping, **one_exact_match_mapping},
        )

        return 1


def _endswith(thesaurus_df: pd.DataFrame, params: Params) -> pd.DataFrame:
    return thesaurus_df[  #  type: ignore
        thesaurus_df[PREFERRED].str.endswith(f"{params.pattern[0]}")
    ].copy()
