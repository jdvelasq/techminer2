# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Populate Stopwords
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, PopulateStopwords

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Populate stopwords
    >>> (
    ...     PopulateStopwords(use_colorama=False)
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


class PopulateStopwords(
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
    def internal__check_if_term_is_domain_specific(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        core_area = self.params.core_area

        self.descriptors["is_domain_specific"] = False

        for idx, row in tqdm(
            self.descriptors.iterrows(),
            total=len(self.descriptors),
            desc=f"  Checking domain-specific terms",
            ncols=80,
        ):

            pattern = row.descriptor
            contexts = row["contexts"]

            if contexts is None:
                system_prompt = internal_load_template(
                    "shell.thesaurus.descriptors.clean.stopwords.phase_1_without_context_phrases.system.txt"
                )
                user_template = internal_load_template(
                    "shell.thesaurus.descriptors.clean.stopwords.phase_1_without_context_phrases.user.txt"
                )
                user_prompt = user_template.format(
                    pattern=pattern,
                    core_area=core_area,
                )
            else:
                system_prompt = internal_load_template(
                    "shell.thesaurus.descriptors.clean.stopwords.phase_1_with_context_phrases.system.txt"
                )
                user_template = internal_load_template(
                    "shell.thesaurus.descriptors.clean.stopwords.phase_1_with_context_phrases.user.txt"
                )
                user_prompt = user_template.format(
                    pattern=pattern,
                    core_area=core_area,
                    contexts=contexts,
                )

            try:

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
                            "cache_control": {"type": "ephemeral"},
                        },
                        {
                            "role": "user",
                            "content": user_prompt,
                        },
                    ],
                    temperature=0,
                    response_format={"type": "json_object"},
                )

            except openai.OpenAIError as e:
                print(f"Error processing the query: {e}")
                response = None
                raise ValueError("API error")

            if response is not None:

                answer = response.choices[0].message.content
                answer = answer.strip()
                answer = json.loads(answer)
                answer = answer["answer"]
                answer = answer.lower().strip()

                if answer == "yes":
                    answer = True
                else:
                    answer = False

                self.descriptors.loc[idx, "is_domain_specific"] = answer

    # -------------------------------------------------------------------------
    def internal__check_if_term_is_domain_specific_stopword(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        self.descriptors["is_stopword"] = False

        df = self.descriptors[self.descriptors["is_domain_specific"]]
        core_area = self.params.core_area

        for idx, row in tqdm(
            df.iterrows(),
            total=len(df),
            desc=f"  Identifying domain-specific stopwords",
            ncols=80,
        ):
            contexts = row["contexts"]
            pattern = row.index

            if contexts is None:
                system_prompt = internal_load_template(
                    "shell.thesaurus.descriptors.clean.stopwords.phase_2_without_context_phrases.system.txt"
                )
                user_template = internal_load_template(
                    "shell.thesaurus.descriptors.clean.stopwords.phase_2_without_context_phrases.user.txt"
                )
                user_prompt = user_template.format(
                    pattern=pattern,
                    core_area=core_area,
                )
            else:
                system_prompt = internal_load_template(
                    "shell.thesaurus.descriptors.clean.stopwords.phase_2_with_context_phrases.system.txt"
                )
                user_template = internal_load_template(
                    "shell.thesaurus.descriptors.clean.stopwords.phase_2_with_context_phrases.user.txt"
                )
                user_prompt = user_template.format(
                    pattern=pattern,
                    core_area=core_area,
                    contexts=contexts,
                )

            try:

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
                            "cache_control": {"type": "ephemeral"},
                        },
                        {
                            "role": "user",
                            "content": user_prompt,
                        },
                    ],
                    temperature=0,
                    response_format={"type": "json_object"},
                )

            except openai.OpenAIError as e:
                print(f"Error processing the query: {e}")
                response = None
                raise ValueError("API error")

            if response is not None:

                answer = response.choices[0].message.content
                answer = answer.strip()
                answer = json.loads(answer)
                answer = answer["answer"]
                answer = answer.lower().strip()

                if answer == "yes":
                    answer = True
                else:
                    answer = False

                self.descriptors.loc[idx, "is_stopword"] = answer

    # -------------------------------------------------------------------------
    def internal__check_if_term_in_non_domain_stopwords(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        self.descriptors["is_stopword"] = False

        df = self.descriptors[~self.descriptors["is_domain_specific"]]
        core_area = self.params.core_area

        for idx, row in tqdm(
            df.iterrows(),
            total=len(df),
            desc=f"  Identifying domain-specific stopwords",
            ncols=80,
        ):

            contexts = row["contexts"]
            pattern = row.index

        if contexts is None:
            system_prompt = internal_load_template(
                "shell.thesaurus.descriptors.clean.stopwords.phase_3_without_context_phrases.system.txt"
            )
            user_template = internal_load_template(
                "shell.thesaurus.descriptors.clean.stopwords.phase_3_without_context_phrases.user.txt"
            )
            user_prompt = user_template.format(
                pattern=pattern,
                core_area=core_area,
            )
        else:
            system_prompt = internal_load_template(
                "shell.thesaurus.descriptors.clean.stopwords.phase_3_with_context_phrases.system.txt"
            )
            user_template = internal_load_template(
                "shell.thesaurus.descriptors.clean.stopwords.phase_3_with_context_phrases.user.txt"
            )
            user_prompt = user_template.format(
                pattern=pattern,
                core_area=core_area,
                contexts=contexts,
            )

        try:

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                        "cache_control": {"type": "ephemeral"},
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                temperature=0,
                response_format={"type": "json_object"},
            )

        except openai.OpenAIError as e:
            print(f"Error processing the query: {e}")
            response = None
            raise ValueError("API error")

        if response is not None:

            answer = response.choices[0].message.content
            answer = answer.strip()
            answer = json.loads(answer)
            answer = answer["answer"]
            answer = answer.lower().strip()

            if answer == "yes":
                answer = True
            else:
                answer = False

            self.descriptors.loc[idx, "is_stopword"] = answer

    # -------------------------------------------------------------------------
    def internal__update_stopwords_file(self):

        new_stopwords = self.descriptors[
            self.descriptors["is_stopword"]
        ].descriptor.tolist()

        stopwords = internal__load_user_stopwords(params=self.params)
        stopwords = sorted(set(stopwords).union(set(new_stopwords)))
        internal__save_user_stopwords(self.params, stopwords)

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__get_descriptors()
        self.internal__get_contexts()
        self.internal__check_if_term_is_domain_specific()
        self.internal__check_if_term_is_domain_specific_stopword()
        self.internal__check_if_term_in_non_domain_stopwords()
        self.internal__update_stopwords_file()


# =============================================================================
