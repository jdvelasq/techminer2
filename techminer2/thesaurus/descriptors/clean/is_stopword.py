# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Is Stopword?
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, IsStopword

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Is stopword?
    >>> (
    ...     IsStopword()
    ...     .with_core_area("FINTECH - FINANCIAL TECHNOLOGIES")
    ...     .having_n_contexts(10)
    ...     .having_terms_in_top(40)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     .where_root_directory_is("examples/fintech/")
    ... ).run() # doctest: +SKIP

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
                             descriptor  is_domain_specific?  is_stopword?
    0                           FINTECH                 True          True
    1                           FINANCE                 True          True
    2                      TECHNOLOGIES                False         False
    3                        INNOVATION                 True          True
    4            FINANCIAL_TECHNOLOGIES                 True          True
    5                 FINANCIAL_SERVICE                 True          True
    6            THE_FINANCIAL_INDUSTRY                 True          True
    7                   THE_DEVELOPMENT                False         False
    8                             BANKS                 True          True
    9                        REGULATORS                 True          True
    10                         SERVICES                False         False
    11                             DATA                False         False
    12                        CONSUMERS                False         False
    13                          BANKING                 True          True
    14                       INVESTMENT                 True          True
    15  THE_FINANCIAL_SERVICES_INDUSTRY                 True          True
    16                     PRACTITIONER                False         False
    17                       THE_IMPACT                False         False
    18                            CHINA                False         False
    19                   BUSINESS_MODEL                 True          True
    20                       BLOCKCHAIN                 True         False
    21             THE_FINANCIAL_SECTOR                 True          True
    22           INFORMATION_TECHNOLOGY                 True          True
    23                FINTECH_COMPANIES                 True          True
    24            FINANCIAL_INSTITUTION                 True          True
    25                     THE_RESEARCH                False         False
    26                            USERS                False         False
    27                           SURVEY                False         False
    28                            VALUE                False         False
    29                         THE_ROLE                False         False
    30        FINTECH_BASED_INNOVATIONS                 True          True
    31                          THE_USE                False         False
    32                 FINANCIAL_MARKET                 True          True
    33                      APPLICATION                False         False
    34                    ENTREPRENEURS                False         False
    35                    THE_EMERGENCE                False         False
    36                 FINANCIAL_SYSTEM                 True          True
    37                        CUSTOMERS                False         False
    38                    THE_POTENTIAL                False          True
    39          ARTIFICIAL_INTELLIGENCE                 True          True



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


class IsStopword(
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
        self.descriptors["is_domain_specific?"] = False
        self.descriptors["is_stopword?"] = False

    # -------------------------------------------------------------------------
    def internal__get_contexts(self):

        from techminer2.thesaurus.descriptors import GetContexts

        get_contexts = GetContexts().update(**self.params.__dict__)
        self.descriptors["contexts"] = self.descriptors["descriptor"].apply(
            lambda x: "\n".join(get_contexts.with_patterns([x]).run())
        )

    # -------------------------------------------------------------------------
    def internal__is_domain_specific_term(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        core_area = self.params.core_area

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

                self.descriptors.loc[idx, "is_domain_specific?"] = answer

    # -------------------------------------------------------------------------
    def internal__is_domain_specific_stopword(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        df = self.descriptors[self.descriptors["is_domain_specific?"]]
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

                self.descriptors.loc[idx, "is_stopword?"] = answer

    # -------------------------------------------------------------------------
    def internal__is_non_domain_specific_stopword(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        df = self.descriptors[~self.descriptors["is_domain_specific?"]]
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

            self.descriptors.loc[idx, "is_stopword?"] = answer

    # -------------------------------------------------------------------------
    def run(self):

        self.internal__get_descriptors()
        self.internal__get_contexts()
        self.internal__is_domain_specific_term()
        self.internal__is_domain_specific_stopword()
        self.internal__is_non_domain_specific_stopword()

        return self.descriptors[
            [
                "descriptor",
                "is_domain_specific?",
                "is_stopword?",
            ]
        ]


# =============================================================================
