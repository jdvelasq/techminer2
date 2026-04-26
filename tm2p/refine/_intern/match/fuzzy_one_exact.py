"""
BaseFuzzyOneExactMatch
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field, ThFile, AnalysisUnit
    >>> from tm2p.refine._intern.match import BaseFuzzyOneExactMatch
    >>> (
    ...     BaseFuzzyOneExactMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_NORM)
    ...     .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )

"""

import sys

import pandas as pd  # type: ignore
from fuzzywuzzy import fuzz  # type: ignore
from tqdm import tqdm  # type: ignore

from tm2p._intern import Params, ParamsMixin
from tm2p.enum import ThField, UnitOrderBy

from ._intern import (
    add_padding,
    load_thesaurus,
    remove_builtin_stopwords,
    remove_punctuation,
    remove_thesaurus_stopwords,
    report_matches,
)

OCC = ThField.OCC.value
PREFERRED = ThField.PREFERRED.value


class BaseFuzzyOneExactMatch(
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
        thesaurus_df = _select_one_exact_match_candidates(thesaurus_df=thesaurus_df)

        matches = _compute_fuzzy_matches(
            thesaurus_df=thesaurus_df,
            similarity_cutoff=self.params.similarity_cutoff,
            fuzzy_threshold=self.params.fuzzy_threshold,
            use_word_level=True,
            word_count_tolerance=1,
            params=self.params,
        )

        report_matches(
            params=self.params,
            mapping=matches,
        )

        sys.stderr.write(f"\n{len(matches.keys())} synonym groups found\n")
        sys.stderr.flush()


def _prepare_fuzzy_candidates(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()

    thesaurus_df["char_length"] = thesaurus_df[PREFERRED].str.len()
    thesaurus_df["word_count"] = thesaurus_df[PREFERRED].str.split().str.len()
    thesaurus_df[OCC] = list(range(len(thesaurus_df)))
    thesaurus_df = thesaurus_df.sort_values(
        by=["word_count", "char_length", OCC, PREFERRED],
        ascending=[True, True, False, True],
    )
    thesaurus_df = thesaurus_df.reset_index(drop=True)

    return thesaurus_df


def _select_one_exact_match_candidates(thesaurus_df: pd.DataFrame) -> pd.DataFrame:
    return thesaurus_df[thesaurus_df["word_count"] > 1].reset_index(drop=True).copy()  # type: ignore


def _compute_fuzzy_matches(
    thesaurus_df: pd.DataFrame,
    similarity_cutoff: float,
    fuzzy_threshold: float,
    use_word_level: bool,
    word_count_tolerance: int,
    params: Params,
) -> dict[str, list[str]]:

    #

    from tm2p.portfolio.perform_metr.unit import Metrics

    metrics = (
        Metrics()
        .update(**params.__dict__)
        #
        .having_top_n_units(None)
        .having_units_ordered_by(UnitOrderBy.OCC)
        .having_unit_occurrence_between(None, None)
        .having_unit_global_citation_between(None, None)
        .having_units_in(None)
        #
        .where_record_years_range(None, None)
        .where_record_global_citations_range(None, None)
        .where_records_match(None)
        .run()
    )
    counters = dict(zip(metrics.index, metrics.COUNTERS))

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df["matched"] = False

    thesaurus_df["WITH_COUNTERS"] = thesaurus_df[PREFERRED].apply(counters.get)

    #
    thesaurus_df.loc[thesaurus_df["WITH_COUNTERS"].isna(), "WITH_COUNTERS"] = (
        thesaurus_df.loc[thesaurus_df["WITH_COUNTERS"].isna(), "PREFERRED"]
        + " "
        + thesaurus_df.loc[thesaurus_df["WITH_COUNTERS"].isna(), "OCC"].astype(str)
        + ":0"
    )
    #

    thesaurus_df["METRICS"] = thesaurus_df["WITH_COUNTERS"].apply(
        lambda x: x.split(" ")[-1].strip()
    )
    thesaurus_df["LENGTH"] = thesaurus_df["WITH_COUNTERS"].apply(
        lambda x: len(x.split(" "))
    )
    thesaurus_df = thesaurus_df.sort_values(
        ["METRICS", "LENGTH"], ascending=[False, True]
    )  #  type: ignore
    thesaurus_df = thesaurus_df.reset_index(drop=True)
    thesaurus_df.pop("METRICS")
    thesaurus_df.pop("LENGTH")
    thesaurus_df.pop("WITH_COUNTERS")

    #

    keys = thesaurus_df[PREFERRED].tolist()
    mergings: dict[str, list[str]] = {}

    for index, key in tqdm(
        enumerate(keys),
        total=len(keys),
        desc="  Progress",
        ncols=80,
    ):
        if thesaurus_df.loc[index, "matched"]:
            continue

        candidates = thesaurus_df[
            (thesaurus_df.index > index) & (~thesaurus_df["matched"])
        ].copy()

        if candidates.empty:
            continue

        key_word_count = len(key.split())
        candidates = candidates[
            candidates["word_count"].between(
                key_word_count - word_count_tolerance,
                key_word_count + word_count_tolerance,
            )
        ]

        if candidates.empty:
            continue

        candidates = _char_length_preselect(key, candidates, similarity_cutoff)

        if candidates.empty:
            continue

        candidates = _apply_cutoff(key, candidates, similarity_cutoff)

        if candidates.empty:
            continue

        if use_word_level:
            candidates = _apply_word_level_match(key, candidates, fuzzy_threshold)

        if candidates.empty:
            continue

        thesaurus_df.loc[candidates.index, "matched"] = True

        key_with_counters = counters.get(key.strip(), key.strip() + " 0:0")
        candidates_with_counters = candidates[PREFERRED].apply(counters.get).tolist()
        mergings[key_with_counters] = candidates_with_counters

    return mergings


def _char_length_preselect(
    key: str,
    candidates: pd.DataFrame,
    similarity_cutoff: float,
) -> pd.DataFrame:

    key_len = len(key)
    diff = int((1 - similarity_cutoff / 100.0) * key_len) + 1
    min_len = max(key_len - diff, 1)
    max_len = key_len + diff
    return candidates[  # type: ignore
        (candidates["char_length"] >= min_len) & (candidates["char_length"] <= max_len)
    ]


def _apply_cutoff(
    key: str,
    candidates: pd.DataFrame,
    similarity_cutoff: float,
) -> pd.DataFrame:

    candidates = candidates.copy()
    candidates["cutoff_score"] = candidates[PREFERRED].apply(
        lambda x: fuzz.ratio(key, x)
    )
    return candidates[candidates["cutoff_score"] >= similarity_cutoff]  # type: ignore


def _apply_word_level_match(
    key: str,
    candidates: pd.DataFrame,
    fuzzy_threshold: float,
) -> pd.DataFrame:

    def _score(string1: str, string2: str) -> float:
        words1 = string1.split()
        words2 = string2.split()
        shorter, longer = (
            (words1, words2) if len(words1) <= len(words2) else (words2, words1)
        )
        remaining = list(longer)
        scores = []
        for base_word in shorter:
            best_score, best_idx = 0, -1
            for i, candidate_word in enumerate(remaining):
                s = fuzz.ratio(base_word, candidate_word)
                if s > best_score:
                    best_score, best_idx = s, i
            scores.append(best_score)
            if best_idx >= 0:
                remaining.pop(best_idx)
        return sum(scores) / len(scores) if scores else 0.0

    candidates = candidates.copy()
    candidates["word_score"] = candidates[PREFERRED].apply(lambda x: _score(key, x))
    return candidates[candidates["word_score"] >= fuzzy_threshold]  # type: ignore
