# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import os
import textwrap

import openai
from colorama import Fore
from openai import OpenAI

from techminer2._internals.package_data.templates.load_builtin_template import (
    load_builtin_template,
)
from techminer2.analyze.concordances import ConcordanceSentences
from techminer2.refine.thesaurus_old.descriptors import GetValues, MergeKeys
from techminer2.shell.colorized_input import colorized_input


# -----------------------------------------------------------------------------
def internal__user_input(core_area, n_contexts):

    # -------------------------------------------------------------------------
    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None, None, None, None
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
    lead_term = colorized_input(". Enter the lead term > ").strip()
    if lead_term == "":
        return None, None, None, None

    # -------------------------------------------------------------------------
    candidate_term = colorized_input(". Enter the candidate term > ").strip()
    if candidate_term == "":
        return None, None, None, None

    return core_area, lead_term, candidate_term, n_contexts


# -----------------------------------------------------------------------------
def internal__filter_contexts(
    n_contexts,
    contexts_lead_term,
    contexts_candidate_term,
):
    if contexts_lead_term:
        contexts_lead_term = contexts_lead_term[:n_contexts]
    if contexts_candidate_term:
        contexts_candidate_term = contexts_candidate_term[:n_contexts]

    return contexts_lead_term, contexts_candidate_term


# -----------------------------------------------------------------------------
def internal__get_contexts(pattern, n_contexts):

    terms = (
        GetValues().having_patterns_matching([pattern]).where_root_directory("./").run()
    )
    terms = [term for term in terms if pattern in term]

    complete_contexts = []

    for term in terms:

        contexts = (
            ConcordanceSentences()
            #
            .having_text_matching(term)
            .where_root_directory("./")
            .where_database("main")
            .where_record_years_range(None, None)
            .where_record_citations_range(None, None)
            #
            .run()
        )

        contexts = [c for c in contexts if len(c) > 80]
        contexts = [f"- {c} ." for c in contexts]
        contexts = [c.lower().replace("_", " ") for c in contexts]
        contexts = [c for c in contexts if pattern in c]

        complete_contexts.extend(contexts)

        if len(complete_contexts) >= n_contexts:
            break

    pattern = pattern.lower().replace("_", " ")
    complete_contexts = [c for c in complete_contexts if pattern in c]

    if len(complete_contexts) < 5:
        return None

    return complete_contexts[:n_contexts]


# -----------------------------------------------------------------------------
def internal__execute_query_with_contexts(
    core_area,
    lead_term,
    candidate_term,
    contexts_lead,
    contexts_candidate,
):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    if isinstance(contexts_lead, list):
        contexts_lead = "\n".join(contexts_lead)
    if isinstance(contexts_candidate, list):
        contexts_candidate = "\n".join(contexts_candidate)

    template = "shell.thesaurus.descriptors.clean.synonyms.with_contexts.txt"
    prompt = load_builtin_template(template)
    query = prompt.format(
        lead_term=lead_term,
        candidate_term=candidate_term,
        contexts_lead=contexts_lead,
        contexts_candidate=contexts_candidate,
        core_area=core_area,
    )

    answer = []

    try:

        for _ in range(3):
            response = client.responses.create(
                model="gpt-4o",
                input=query,
                temperature=0,
            )

            response = response.output_text
            response = response.strip().lower()
            answer.append(response)

        yes_count = answer.count("yes")

        if yes_count < 3:
            return "no"
        return "yes"

    except openai.OpenAIError as e:
        print()
        print(f"Error processing the query: {e}")
        print()
        return None


# -----------------------------------------------------------------------------
def internal__execute_query_without_contexts(
    core_area,
    lead_term,
    candidate_term,
):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    template = "shell.thesaurus.descriptors.clean.synonyms.without_contexts.txt"
    prompt = load_builtin_template(template)
    query = prompt.format(
        lead_term=lead_term,
        candidate_term=candidate_term,
        core_area=core_area,
    )

    answer = []

    try:

        for _ in range(3):
            response = client.responses.create(
                model="gpt-4o",
                input=query,
                temperature=0,
            )

            response = response.output_text
            response = response.strip().lower()
            answer.append(response)

        yes_count = answer.count("yes")

        if yes_count < 3:
            return "no"
        return "yes"

    except openai.OpenAIError as e:
        print(f"Error processing the query: {e}")
        return None


# -----------------------------------------------------------------------------
def internal__print_answer(answer):

    text = (
        Fore.LIGHTBLACK_EX
        + "The terms "
        + Fore.RESET
        + "{result}"
        + Fore.LIGHTBLACK_EX
        + " synonymous."
        + Fore.RESET
    )

    if answer.lower() == "yes":
        text = text.format(result="ARE")
    elif answer.lower() == "no":
        text = text.format(result="ARE NOT")
    elif answer.lower() == "na-lead":
        text = "No context available for the lead term."
    elif answer.lower() == "na-candidate":
        text = "No context available for the candidate term."
    else:
        text = f"Obtained answer: {answer}"

    print()
    print(text)
    print()


# -----------------------------------------------------------------------------
def internal__merge_keys(lead_term, candidate_term):

    answer = colorized_input(". Merge lead and candidate terms (y/[n])? > ").strip()
    if answer.lower() in ["n", "no", "not", ""]:
        print()
        return

    (
        MergeKeys()
        .having_patterns_matching([lead_term, candidate_term])
        .where_root_directory("./")
        .run()
    )

    print()


# -----------------------------------------------------------------------------
def internal__explain(
    core_area,
    lead_term,
    candidate_term,
    contexts_lead,
    contexts_candidate,
):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    if contexts_lead:
        contexts_lead = "\n".join(contexts_lead)
    else:
        contexts_lead = "N/A"

    if contexts_candidate:
        contexts_candidate = "\n".join(contexts_candidate)
    else:
        contexts_candidate = "N/A"

    template = "shell.thesaurus.descriptors.clean.synonyms.explain.txt"
    prompt = load_builtin_template(template)
    query = prompt.format(
        lead_term=lead_term,
        candidate_term=candidate_term,
        contexts_lead=contexts_lead,
        contexts_candidate=contexts_candidate,
        core_area=core_area,
    )

    try:

        response = client.responses.create(
            model="gpt-4o",
            input=query,
            temperature=0,
        )

        answer = response.output_text
        answer = answer.strip()
        return answer

    except openai.OpenAIError as e:
        print()
        print(f"Error processing the query: {e}")
        print()
        return None


# -----------------------------------------------------------------------------
def internal__print(msg):
    print(Fore.LIGHTBLACK_EX + msg + Fore.RESET)


# -----------------------------------------------------------------------------
def execute_synonyms_command():

    print()
    core_area = None
    n_contexts = None

    while True:

        core_area, lead_term, candidate_term, n_contexts = internal__user_input(
            core_area, n_contexts
        )

        print()
        internal__print("Evaluating synonyms...")

        if lead_term is None or candidate_term is None:
            print()
            return

        internal__print("  Building contexts for the lead term...")
        contexts_lead = internal__get_contexts(lead_term, n_contexts)
        if not contexts_lead:
            internal__print(
                "  No sufficient contextual information found for the lead term."
            )

        if contexts_lead:
            internal__print("  Building contexts for the candidate term...")
            contexts_candidate = internal__get_contexts(candidate_term, n_contexts)
            if not contexts_candidate:
                internal__print(
                    "  No sufficient contextual information found for the candidate term."
                )
        else:
            contexts_candidate = None

        internal__print("  Executing the query...")
        if not contexts_lead and not contexts_candidate:
            answer = internal__execute_query_without_contexts(
                core_area, lead_term, candidate_term
            )
        else:
            contexts_lead, contexts_candidate = internal__filter_contexts(
                n_contexts, contexts_lead, contexts_candidate
            )
            if not contexts_lead:
                contexts_lead = "N/A"
            if not contexts_candidate:
                contexts_candidate = "N/A"
            answer = internal__execute_query_with_contexts(
                core_area, lead_term, candidate_term, contexts_lead, contexts_candidate
            )

        internal__print("  Evaluation process completed successfully.")

        internal__print_answer(answer)

        if answer == "yes":
            internal__merge_keys(lead_term, candidate_term)
        else:
            explanation = internal__explain(
                core_area,
                lead_term,
                candidate_term,
                contexts_lead,
                contexts_candidate,
            )
            explanation = textwrap.fill(explanation, width=80)
            if explanation:
                print(explanation)
                print()


#
