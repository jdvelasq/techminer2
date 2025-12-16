# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Are Synonymous?
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, AreSynonymous

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Populate stopwords
    >>> (
    ...     AreSynonymous(use_colorama=False)
    ...     .with_core_area("fintech (financial technologies)")
    ...     .having_n_contexts(10)
    ...     .having_terms_in_top(40)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     .where_root_directory_is("examples/fintech/")
    ... ).run()  # doctest: +SKIP
                            lead_term candidate_terms
    0                    TECHNOLOGIES
    1                 THE_DEVELOPMENT
    2                        SERVICES
    3                            DATA
    4                       CONSUMERS
    5                    PRACTITIONER
    6                      THE_IMPACT
    7                           CHINA
    8                      BLOCKCHAIN
    9                    THE_RESEARCH
    10                          USERS
    11                         SURVEY
    12                          VALUE
    13                       THE_ROLE
    14                        THE_USE
    15                    APPLICATION
    16                  ENTREPRENEURS
    17                  THE_EMERGENCE
    18                      CUSTOMERS
    19               FINTECH_SERVICES
    20                       BIG_DATA
    21               FINTECH_START_UP
    22                         EUROPE
    23                        LENDING
    24  FINANCIAL_SERVICES_INDUSTRIES
    25                     INDUSTRIES
    26                     DISRUPTION
    27                         CHANGE
    28                       COMMERCE
    29                       RESEARCH
    30         THE_FINTECH_REVOLUTION
    31                    CONVENIENCE
    32                 DIGITALIZATION
    33           DIGITAL_TECHNOLOGIES
    34            FINANCIAL_INCLUSION
    35                       NETWORKS
    36           FINANCIAL_INDUSTRIES
    37               THE_IMPLICATIONS
    38                       A_SURVEY
    39                 THE_HYPOTHESES


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

# -----------------------------------------------------------------------------


class AreSynonymous(
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

        self.dataframe = pd.DataFrame({"lead_term": descriptors.index})
        self.dataframe["merged"] = False
        self.dataframe["keys"] = [[] for _ in range(len(self.dataframe))]
        self.dataframe["candidate_terms"] = [[] for _ in range(len(self.dataframe))]

    # -------------------------------------------------------------------------
    def internal__build_merging_keys(self):

        for idx, row in self.dataframe.iterrows():

            pattern = row.lead_term
            pattern = pattern.replace("_", " ")
            pattern = pattern.split()

            # first word + key length
            self.dataframe.at[idx, "keys"].append(
                (pattern[0] + "-" + str(len(pattern)))
            )

            # last word + key length
            self.dataframe.at[idx, "keys"].append(
                (pattern[-1] + "-" + str(len(pattern)))
            )

            # all bigrams separated by hyphen
            if len(pattern) >= 2:
                for i in range(len(pattern) - 1):
                    bigram = pattern[i] + "-" + pattern[i + 1]
                    self.dataframe.at[idx, "keys"].append(bigram)

        self.dataframe["keys"] = self.dataframe["keys"].apply(lambda x: list(set(x)))

    # -------------------------------------------------------------------------
    def internal__get_contexts(self):

        from techminer2.thesaurus.descriptors import GetContexts

        get_contexts = GetContexts().update(**self.params.__dict__)

        def internal__get_row_contexts(pattern):

            contexts = get_contexts.with_patterns([pattern]).run()
            contexts = [c for c in contexts if len(c) > 80]
            contexts = [c.lower().replace("_", " ") for c in contexts]
            contexts = [c for c in contexts if pattern.lower().replace("_", " ") in c]

            return "\n".join(contexts)

        self.dataframe["contexts"] = self.dataframe["lead_term"].apply(
            internal__get_row_contexts
        )

    # -------------------------------------------------------------------------
    def internal__compare_terms(
        self,
        lead_term,
        lead_contexts,
        candidate_term,
        candidate_contexts,
    ):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        core_area = self.params.core_area

        system_prompt = internal_load_template(
            "shell.thesaurus.descriptors.clean.synonyms.system.txt"
        )
        user_template = internal_load_template(
            "shell.thesaurus.descriptors.clean.synonyms.user.txt"
        )
        user_prompt = user_template.format(
            core_area=core_area,
            lead_term=lead_term,
            lead_contexts=lead_contexts,
            candidate_term=candidate_term,
            candidate_contexts=candidate_contexts,
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

        return answer

    # -------------------------------------------------------------------------
    def internal__evaluate_merging(self):

        for idx0, row0 in self.dataframe.iterrows():

            if idx0 == self.dataframe.index[-1]:
                break

            if self.dataframe.at[idx0, "merged"] is True:
                continue

            lead_keys = row0["keys"]
            lead_term = row0.lead_term
            lead_contexts = row0["contexts"]

            for idx1, row1 in self.dataframe.iterrows():

                if idx0 >= idx1:
                    continue

                if self.dataframe.at[idx1, "merged"] is True:
                    continue

                candidate_keys = row1["keys"]
                candidate_term = row1.lead_term
                candidate_contexts = row1["contexts"]

                # Check if they share at least one key
                if len(set(lead_keys).intersection(set(candidate_keys))) == 0:
                    continue

                answer = self.internal__compare_terms(
                    lead_term,
                    lead_contexts,
                    candidate_term,
                    candidate_contexts,
                )

                if answer is True:
                    self.dataframe.at[idx1, "merged"] = True
                    self.dataframe.at[idx0, "candidate_terms"].append(candidate_term)

    # -------------------------------------------------------------------------
    def internal__format_output(self):

        self.dataframe["candidate_terms"] = self.dataframe["candidate_terms"].str.join(
            "; "
        )

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__get_descriptors()
        self.internal__build_merging_keys()
        self.internal__get_contexts()
        self.internal__evaluate_merging()
        self.internal__format_output()

        return self.dataframe[["lead_term", "candidate_terms"]]


# =============================================================================
