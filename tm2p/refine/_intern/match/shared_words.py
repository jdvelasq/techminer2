"""
BaseSharedWordsMatch
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field, ThFile, AnalysisUnit
    >>> from tm2p.refine._intern.match import BaseSharedWordsMatch
    >>> (
    ...     BaseSharedWordsMatch()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_NORM)
    ...     .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )

"""

import os
import sys

import numpy as np
import pandas as pd  # type: ignore
from fuzzywuzzy import fuzz  # type: ignore
from openai import OpenAI
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
VARIANT = ThField.VARIANT.value


class BaseSharedWordsMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = add_padding(thesaurus_df=thesaurus_df)  # type: ignore
        thesaurus_df = remove_punctuation(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_builtin_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = remove_thesaurus_stopwords(thesaurus_df=thesaurus_df)
        thesaurus_df = _prepare_candidates(thesaurus_df=thesaurus_df)

        matches = _compute_matches(
            thesaurus_df=thesaurus_df,
            params=self.params,
        )

        report_matches(
            params=self.params,
            mapping=matches,
        )

        sys.stderr.write(f"\n{len(matches.keys())} synonym groups found\n")
        sys.stderr.flush()


def _prepare_candidates(thesaurus_df: pd.DataFrame) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[OCC] = list(range(len(thesaurus_df)))
    thesaurus_df = thesaurus_df.sort_values(
        by=[OCC, PREFERRED],
        ascending=[False, True],
    )
    thesaurus_df = thesaurus_df.reset_index(drop=True)

    return thesaurus_df


def _compute_matches(
    thesaurus_df: pd.DataFrame,
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

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    keys = thesaurus_df[thesaurus_df[OCC] >= 3][PREFERRED].tolist()
    mergings: dict[str, list[str]] = {}

    for index, preferred in tqdm(
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

        preferred_words = set(preferred.lower().split())
        # print(f"Preferred: {preferred} | Words: {preferred_words}")

        candidates["variant_words"] = candidates[VARIANT].apply(
            lambda x: set(x.lower().split())
        )

        # print(f"Candidates: {candidates['variant_words'].head()}")
        candidates["has_common_words"] = candidates["variant_words"].apply(
            lambda x: len(preferred_words.intersection(x)) > 0
        )

        candidates = candidates[candidates["has_common_words"] == True]  # type: ignore

        if candidates.empty:
            continue

        candidates["SYNNOYMS"] = True

        # for index, row in candidates.iterrows():
        #     variant = row[VARIANT]
        #     candidates.loc[index, "SYNNOYMS"] = _compare_terms(
        #         client,
        #         preferred,
        #         variant,
        #         params.core_area,  #  type: ignore
        #     )

        candidates = candidates[candidates["SYNNOYMS"] == True]  # type: ignore

        if candidates.empty:
            continue

        thesaurus_df.loc[candidates.index, "matched"] = True

        key_with_counters = counters.get(preferred.strip(), preferred.strip() + " 0:0")
        candidates_with_counters = candidates[PREFERRED].apply(counters.get).tolist()
        mergings[key_with_counters] = candidates_with_counters

    return mergings


# def _compare_terms(
#     client,
#     preferred: str,
#     variant: str,
#     core_area: str,
# ) -> bool:

#     def cosine_similarity(a, b):
#         a = np.array(a, dtype=np.float32)
#         b = np.array(b, dtype=np.float32)
#         return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

#     def embed_texts(texts, model="text-embedding-3-small"):
#         resp = client.embeddings.create(model=model, input=texts)
#         return [item.embedding for item in resp.data]

#     domain = core_area.lower()
#     a = f"{domain} keyword: {preferred}."
#     b = f"{domain} keyword: {variant}."

#     emb_a, emb_b = embed_texts([a, b], model="text-embedding-3-small")
#     sim = cosine_similarity(emb_a, emb_b)

#     if sim >= 0.94:
#         return True
#     return False
