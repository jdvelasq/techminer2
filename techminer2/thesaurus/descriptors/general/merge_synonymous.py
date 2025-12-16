# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Merge Synonymous
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, MergeSynonymous

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Populate stopwords
    >>> (
    ...     MergeSynonymous(use_colorama=False)
    ...     .with_core_area("FINTECH - FINANCIAL TECHNOLOGIES")
    ...     .having_n_contexts(10)
    ...     .having_terms_in_top(40)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     .where_root_directory_is("examples/fintech/")
    ... ).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP



"""
import json
import os

import openai
import pandas as pd
from openai import OpenAI
from tqdm import tqdm  # type: ignore

from techminer2._internals.load_template import internal_load_template
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_user_stopwords,
    internal__save_user_stopwords,
)
from techminer2.database.metrics.performance import DataFrame as MetricsDataFrame
from techminer2.database.search import ConcordantSentences
from techminer2.thesaurus.descriptors import GetValues

# -----------------------------------------------------------------------------


class MergeSynonymous(
    ParamsMixin,
):
    """:meta private:"""

    def internal__get_descriptors(self):

        descriptors = (
            MetricsDataFrame()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .run()
        )

        self.descriptors = pd.DataFrame({"descriptor": descriptors.index})
        self.descriptors["merged"] = False

    # -------------------------------------------------------------------------
    def internal__build_merging_keys(self):

        self.descriptors["keys"] = [[] for _ in range(len(self.descriptors))]

        for idx, row in self.descriptors.iterrows():

            pattern = row.descriptor
            pattern = pattern.replace("_", " ")
            pattern = pattern.split()

            # first word + key length
            self.descriptors.at[idx, "keys"].append(
                (pattern[0] + "-" + str(len(pattern)))
            )

            # last word + key length
            self.descriptors.at[idx, "keys"].append(
                (pattern[-1] + "-" + str(len(pattern)))
            )

            # all bigrams separated by hyphen
            if len(pattern) >= 2:
                for i in range(len(pattern) - 1):
                    bigram = pattern[i] + "-" + pattern[i + 1]
                    self.descriptors.at[idx, "keys"].append(bigram)

        self.descriptors["keys"] = self.descriptors["keys"].apply(
            lambda x: list(set(x))
        )

    # -------------------------------------------------------------------------
    def internal__get_contexts(self):

        n_contexts = self.params.n_contexts
        get_values = GetValues().update(**self.params.__dict__)

        def internal__get_row_contexts(pattern):

            terms = get_values.with_patterns([pattern]).run()
            terms = [term for term in terms if pattern in term]

            complete_contexts = []

            for term in terms:

                contexts = (
                    ConcordantSentences()
                    .update(**self.params.__dict__)
                    #
                    .with_abstract_having_pattern(term)
                    .where_database_is("main")
                    .where_record_years_range_is(None, None)
                    .where_record_citations_range_is(None, None)
                    #
                    .run()
                )

                contexts = [c for c in contexts if len(c) > 80]
                contexts = [f"- {c} ." for c in contexts]
                contexts = [c.lower().replace("_", " ") for c in contexts]
                contexts = [
                    c for c in contexts if pattern.lower().replace("_", " ") in c
                ]

                complete_contexts.extend(contexts)
                if len(complete_contexts) >= n_contexts:
                    break

            if len(complete_contexts) < 5:
                return None

            return "\n".join(complete_contexts[:n_contexts])

        self.descriptors["contexts"] = self.descriptors["descriptor"].apply(
            internal__get_row_contexts
        )

    # -------------------------------------------------------------------------
    def internal__evaluate_merging(self):

        self.descriptors["merge_with"] = [[] for _ in range(len(self.descriptors))]

        core_area = self.params.core_area

        for idx0, row0 in self.descriptors.iterrows():

            if idx0 == self.descriptors.index[-1]:
                break

            keys0 = row0["keys"]
            pattern0 = row0.descriptor

            for idx1, row1 in self.descriptors.iterrows():

                if idx0 >= idx1:
                    continue

                keys1 = row1["keys"]
                pattern1 = row1.descriptor

                # Check if they share at least one key
                if len(set(keys0).intersection(set(keys1))) == 0:
                    continue

                # Here, we can use LLM to check if they are synonymous
                # For simplicity, we will assume they are synonymous if they share a key
                self.descriptors.at[idx0, "merge_with"].append(pattern1)

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__get_descriptors()
        self.internal__build_merging_keys()
        self.internal__get_contexts()
        self.internal__check_if_term_is_domain_specific()
        self.internal__check_if_term_is_domain_specific_stopword()
        self.internal__check_if_term_in_non_domain_stopwords()
        self.internal__update_stopwords_file()


# =============================================================================
