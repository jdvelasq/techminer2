# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=unused-argument

import os
from operator import is_
from pprint import pprint  # type: ignore

import openai
from colorama import Fore
from openai import OpenAI
from tqdm import tqdm  # type: ignore

from techminer2._internals.load_template import internal_load_template
from techminer2.database.search import ConcordantSentences
from techminer2.database.tools import ExtendStopwords
from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import GetValues


# -----------------------------------------------------------------------------
def internal__user_input(core_area, n_contexts):

    # -------------------------------------------------------------------------
    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None, None, None
        core_area = answer.upper()

    # -------------------------------------------------------------------------
    if n_contexts is None:
        n_contexts = colorized_input(
            ". Enter the number of contexts [default: 30] > "
        ).strip()
        if n_contexts == "":
            n_contexts = 30
        else:
            n_contexts = int(n_contexts)

    # -------------------------------------------------------------------------
    pattern = colorized_input(". Enter the pattern > ").strip()
    if pattern == "":
        return None, None, None

    # -------------------------------------------------------------------------
    return core_area, pattern, n_contexts


# -----------------------------------------------------------------------------
def internal__get_contexts(pattern, n_contexts):

    terms = GetValues().with_patterns([pattern]).where_root_directory_is("./").run()
    terms = [term for term in terms if pattern in term]

    complete_contexts = []

    for term in terms:

        contexts = (
            ConcordantSentences()
            #
            .with_abstract_having_pattern(term)
            .where_root_directory_is("./")
            .where_database_is("main")
            .where_record_years_range_is(None, None)
            .where_record_citations_range_is(None, None)
            #
            .run()
        )

        contexts = [c for c in contexts if len(c) > 80]
        contexts = [f"- {c} ." for c in contexts]
        contexts = [c.lower().replace("_", " ") for c in contexts]
        contexts = [c for c in contexts if pattern.lower().replace("_", " ") in c]

        complete_contexts.extend(contexts)
        if len(complete_contexts) >= n_contexts:
            break

    if len(complete_contexts) < 5:
        return None

    return complete_contexts[:n_contexts]


# -----------------------------------------------------------------------------
def internal__execute_query(core_area, pattern, contexts):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Phase 1: Domain-specific terms
    # ----------------------------------------------------------

    if contexts is None:
        template = "shell.thesaurus.descriptors.clean.stopwords.phase_1_without_context_phrases.txt"
        query = template.format(
            pattern=pattern,
            core_area=core_area,
        )
    else:
        template = "shell.thesaurus.descriptors.clean.stopwords.phase_1_with_context_phrases.txt"
        query = template.format(
            pattern=pattern,
            core_area=core_area,
            contexts="\n".join(contexts),
        )

    try:

        response = client.responses.create(
            model="gpt-4o",
            input=query,
            temperature=0,
        )

        is_domain_specific = response.output_text
        is_domain_specific = is_domain_specific.strip().lower()

        if is_domain_specific == "yes":
            print()
            print(Fore.LIGHTBLACK_EX + "The term is domain-specific." + Fore.RESET)
        else:
            print()
            print(Fore.LIGHTBLACK_EX + "The term is no domain-specific." + Fore.RESET)

    except openai.OpenAIError as e:
        print(f"Error processing the query: {e}")
        return None

    # Phase 2: Domain-specific very generic terms
    # ----------------------------------------------------------
    if is_domain_specific == "yes":

        if contexts is None:
            template = "shell.thesaurus.descriptors.clean.stopwords.phase_2_without_context_phrases.txt"
            query = template.format(
                pattern=pattern,
                core_area=core_area,
            )
        else:
            template = "shell.thesaurus.descriptors.clean.stopwords.phase_2_with_context_phrases.txt"
            query = template.format(
                pattern=pattern,
                core_area=core_area,
                contexts="\n".join(contexts),
            )

        response = client.responses.create(
            model="gpt-4o",
            input=query,
            temperature=0,
        )

        is_stopword = response.output_text
        is_stopword = is_stopword.strip().lower()

        return is_stopword

    # Phase 3: Non-domain-specific terms
    # ----------------------------------------------------------

    if contexts is None:
        template = "shell.thesaurus.descriptors.clean.stopwords.phase_3_without_context_phrases.txt"
        query = template.format(
            pattern=pattern,
            core_area=core_area,
        )
    else:
        template = "shell.thesaurus.descriptors.clean.stopwords.phase_3_with_context_phrases.txt"
        query = template.format(
            pattern=pattern,
            core_area=core_area,
            contexts="\n".join(contexts),
        )

    try:

        response = client.responses.create(
            model="gpt-4o",
            input=query,
            temperature=0,
        )

        is_stopword = response.output_text
        is_stopword = is_stopword.strip().lower()

        return is_stopword

    except openai.OpenAIError as e:
        print(f"Error processing the query: {e}")
        return None


# -----------------------------------------------------------------------------
def internal__print_answer(answer):

    text = (
        Fore.LIGHTBLACK_EX
        + "The term "
        + Fore.RESET
        + "{result}"
        + Fore.LIGHTBLACK_EX
        + " a STOPWORD."
        + Fore.RESET
    )

    if answer.lower() == "yes":
        text = text.format(result="IS")
    else:
        text = text.format(result="IS NOT")

    # print()
    print(text)
    print()


# -----------------------------------------------------------------------------
def internal__extend_stopwords(pattern):

    answer = colorized_input(". Extend stopwords with pattern (y/[n])? > ").strip()
    if answer.lower() in ["n", "no", "not", ""]:
        print()
        return

    pattern = pattern.upper().replace(" ", "_")
    ExtendStopwords().with_patterns([pattern]).where_root_directory_is("./").run()
    print()


# -----------------------------------------------------------------------------
def execute_stopwords_command():

    print()
    # internal__run_diagnostics()
    # return
    core_area = None
    n_contexts = None

    while True:

        core_area, pattern, n_contexts = internal__user_input(core_area, n_contexts)

        if pattern is None:
            print()
            return

        contexts = internal__get_contexts(pattern, n_contexts)
        answer = internal__execute_query(core_area, pattern, contexts)

        internal__print_answer(answer)

        if answer == "yes":
            internal__extend_stopwords(pattern)


# -----------------------------------------------------------------------------
def internal__run_diagnostics():

    patterns = [
        "ELECTRIC_UTILITIES",
        "ENERGY_GENERATION",
        "ENERGY_PRODUCTION",
        "FARMS",
        "INDUSTRY",
        "INSTALLED_CAPACITY",
        "PERFORMANCE",
        "POWER_PLANTS",
        "POWER",
        "TURBINE",
        "WIND_FARMS",
        "WIND_POWER_INDUSTRY",
        "WIND_POWER",
        "WIND_TURBINE",
        #
        "ACCOUNT",
        "AMOUNTS",
        "ANALYZES",
        "APPROACH",
        "BALANCE",
        "BASIS",
        "BENEFIT",
        "COMPARISONS",
        "CONDITION",
        "CONFIGURATION",
        "CONSIDERATIONS",
        "EFFICIENCY",
        "FORMS",
        "GOALS",
        "LOSS",
        "METHOD",
        "MODEL",
        "MODELING",
        "NUMBERS",
        "OBJECTIVES",
        "RESULTS",
        "SCENARIO",
        "SITUATION",
        "SIZES",
        "STUDY_CASE",
        "TRADE_OFF",
        "TYPE",
        "VALUE",
        "YEAR",
    ]

    summary = {}

    for pattern in tqdm(patterns, total=len(patterns), ncols=80):

        contexts = internal__get_contexts(pattern, 30)

        results = []

        for _ in range(5):

            answer = internal__execute_query(
                "economics of wind energy", pattern, contexts
            )
            results.append(answer)

        summary[pattern] = results

    print()
    print("Summary: ")
    print()
    pprint(summary)
    print()
