"""
Synonym
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field, ThFile, AnalysisUnit
    >>> from tm2p.refine._intern.mmerge import BaseSynonym
    >>> (
    ...     BaseSynonym()
    ...     #
    ...     # THESAURUS:
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_NORM)
    ...     #
    ...     # ANALYSIS UNIT:    
    ...     .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)
    ...     #
    ...     # DATABASE:    
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )

"""

import sys
from collections import Counter

import pandas as pd  # type: ignore

from tm2p._intern import Params, ParamsMixin
from tm2p._intern.packag_data import update_core_thesaurus
from tm2p.enum import ThField
from tm2p.portfolio.thematic_struct.co_occur.direct import UnitToCluster

from ..match._intern import load_thesaurus
from .manual import BaseManual

OCC = ThField.OCC.value
PREFERRED = ThField.PREFERRED.value
WORDS = "WORDS"
MATCHED = "matched"
N_WORDS = "N_WORDS"
CANDIDATE = "CANDIDATE"
CLUSTER = "CLUSTER"


class BaseSynonym(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> int:

        thesaurus_df = load_thesaurus(params=self.params)
        thesaurus_df = _prepare_thesaurus(
            thesaurus_df=thesaurus_df,
            params=self.params,
        )

        n_synonyms = _merge_synonyms(
            thesaurus_df=thesaurus_df,
            params=self.params,
        )

        sys.stderr.write(f"\n{n_synonyms} synonyms merged\n")
        sys.stderr.flush()

        return n_synonyms


def _prepare_thesaurus(thesaurus_df: pd.DataFrame, params: Params) -> pd.DataFrame:

    thesaurus_df = thesaurus_df.copy()
    thesaurus_df[OCC] = list(range(len(thesaurus_df)))
    thesaurus_df = thesaurus_df.sort_values(
        by=[OCC, PREFERRED],
        ascending=[False, True],
    )
    thesaurus_df = thesaurus_df.reset_index(drop=True)
    thesaurus_df[MATCHED] = False

    mapping = UnitToCluster().update(**params.__dict__).run()

    # print(mapping, flush=True)

    n_groups = len(set(mapping.values()))
    counts = Counter(mapping.values())
    max_cluster_size = max(counts.values())
    min_cluster_size = min(counts.values())

    sys.stderr.write(f"\n{n_groups} clusters found\n")
    sys.stderr.write(f"Max cluster size: {max_cluster_size}\n")
    sys.stderr.write(f"Min cluster size: {min_cluster_size}\n")
    sys.stderr.flush()

    thesaurus_df[CLUSTER] = thesaurus_df[PREFERRED].apply(lambda x: mapping.get(x, -1))

    return thesaurus_df


def _merge_synonyms(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> int:

    df = thesaurus_df[thesaurus_df[CLUSTER] != -1]
    manual = BaseManual().update(**params.__dict__)
    n_lines = len(df)

    n_synonyms = 0

    for index, row in df.iterrows():

        if thesaurus_df.loc[index, "matched"]:  # type: ignore #  type: ignore
            continue

        key = row[PREFERRED].replace("-", " ")
        cluster = row[CLUSTER]
        words = key.split()
        n_words = len(words)

        if n_words > 5:
            continue

        candidates = thesaurus_df[
            (thesaurus_df.index > index)
            & (~thesaurus_df["matched"])
            & (thesaurus_df[CLUSTER] > -1)
        ].copy()

        if candidates.empty:
            continue

        # candidates = candidates[candidates[CLUSTER] == cluster]

        candidates[CANDIDATE] = False
        candidates[PREFERRED] = candidates[PREFERRED].str.replace("-", " ")
        candidates[WORDS] = candidates[PREFERRED].str.split()

        if n_words >= 2:

            pairs = [(words[i], words[i + 1]) for i in range(n_words - 1)]
            pairs = [" ".join(pair) for pair in pairs]

            for pair in pairs:
                candidates.loc[
                    candidates[PREFERRED].apply(lambda x: pair in x),
                    CANDIDATE,
                ] = True

            if candidates[CANDIDATE].sum() > 20:
                candidates[CANDIDATE] = False

        candidates.loc[
            candidates[WORDS].apply(lambda x: x[0] == words[0] and len(x) == n_words),
            CANDIDATE,
        ] = True

        candidates.loc[
            candidates[WORDS].apply(lambda x: x[-1] == words[-1] and len(x) == n_words),
            CANDIDATE,
        ] = True

        #

        CONNECTORS = ["of", "the", "and", "for", "in", "on", "with"]

        words = sorted(set(word for word in words if word not in CONNECTORS))

        candidates[WORDS] = candidates[WORDS].apply(
            lambda x: sorted(set(y for y in x if y not in CONNECTORS))
        )

        candidates.loc[
            candidates[WORDS].apply(lambda x: x == words),
            CANDIDATE,
        ] = True

        candidates = candidates[candidates[CANDIDATE]]

        if candidates.empty:
            continue

        for _, row in candidates.iterrows():

            variant = row[PREFERRED]

            print(f"{index}/{n_lines}  '{key}' <---- '{variant}'", flush=True)

            choice = update_core_thesaurus(preferred=key, variant=variant)

            if choice is True:
                n_synonyms += 1
                manual.having_text_matching((key, variant)).run()
                thesaurus_df.loc[thesaurus_df[PREFERRED] == variant, "matched"] = True
                print("✓ Synonym.\n")
            else:
                print("✗ Not a synonym.\n")

    return n_synonyms
