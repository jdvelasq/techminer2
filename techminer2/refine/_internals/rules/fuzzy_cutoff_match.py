from pathlib import Path

import pandas as pd
from fuzzywuzzy import fuzz  # type: ignore
from tqdm import tqdm  # type: ignore

from techminer2._internals import Params
from techminer2.enums import ThesaurusField

from ._pre_process import _pre_process

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


def _compute_key_length(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df["keylength"] = thesaurus_df[PREFERRED].str.len()
    thesaurus_df = thesaurus_df.sort_values(
        by=["keylength", OCC, PREFERRED],
        ascending=[True, False, True],
    )
    return thesaurus_df


def _compute_fuzzy_match(string1, string2, fuzzy_threshold):

    string1 = string1.split(" ")
    string2 = string2.split(" ")

    if len(string1) > len(string2):
        shorten_string = string2
        lengthen_string = string1
    else:
        shorten_string = string1
        lengthen_string = string2

    scores_per_word = []
    for base_word in shorten_string:
        best_match = 0
        for candidate_word in lengthen_string:
            score = fuzz.ratio(base_word, candidate_word)
            if score > best_match:
                best_match = score
        scores_per_word.append(best_match)

    score = min(scores_per_word)
    match = all(score >= fuzzy_threshold for score in scores_per_word)

    return score, match


def _compute_matches(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> dict[str, list[str]]:

    similarity_cutoff = params.similarity_cutoff
    fuzzy_threshold = params.fuzzy_threshold

    thesaurus_df = thesaurus_df.copy().reset_index(drop=True)

    mergings: dict[str, list[str]] = {}

    thesaurus_df["selected"] = False
    thesaurus_df["cutoff"] = 0.0
    thesaurus_df["fuzzy"] = 0.0

    keys = thesaurus_df[PREFERRED].tolist()

    for index, key in tqdm(
        enumerate(keys),
        total=len(keys),
        desc="  Progress",
        ncols=80,
        # disable=self.params.tqdm_disable,
    ):

        if thesaurus_df.loc[index, "selected"] is True:
            continue

        df = thesaurus_df[thesaurus_df.index > index]

        key_length = len(key.split(" "))
        df = df[df.keylength == key_length]

        if df.empty:
            continue

        # Preselect
        diff_in_length = int((1 - similarity_cutoff / 100.0) * len(key)) + 1
        min_key_length = max(len(key) - diff_in_length, 1)
        max_key_length = len(key) + diff_in_length
        df = df[df.keylength <= max_key_length]
        df = df[df.keylength >= min_key_length]

        df["cutoff"] = df[PREFERRED].apply(lambda x: fuzz.ratio(key, x))
        df = df[df["cutoff"] >= similarity_cutoff]

        if df.empty:
            continue

        results = df[PREFERRED].apply(
            lambda x: _compute_fuzzy_match(key, x, fuzzy_threshold)
        )

        df["fuzzy"] = results.map(lambda x: x[0])
        df["fuzzy_match"] = results.map(lambda x: x[1])

        df = df[df["fuzzy_match"].apply(lambda x: x is True)]

        if df.empty:
            continue

        thesaurus_df.loc[df.index, "fuzzy"] = df.fuzzy
        thesaurus_df.loc[df.index, "cutoff"] = df.cutoff
        thesaurus_df.loc[df.index, "selected"] = True

        mergings[key] = df[PREFERRED].tolist()

    return mergings


def _report_mergings(params: Params, mapping: dict[str, list[str]]) -> None:

    filepath = Path(params.root_directory) / "refine" / "thesaurus" / "mergings.txt"

    with open(filepath, "w", encoding="utf-8") as f:
        for preferred, variants in mapping.items():
            f.write(f"{preferred}\n")
            for variant in variants:
                f.write(f"    {variant}\n")


def apply_fuzzy_cutoff_match_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)

    thesaurus_df = _compute_key_length(thesaurus_df=thesaurus_df)
    mapping = _compute_matches(thesaurus_df=thesaurus_df, params=params)
    _report_mergings(params=params, mapping=mapping)

    return thesaurus_df
