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

from techminer2.database.search import ConcordantSentences
from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import GetValues

PROMPT = """
ROLE:
You are an expert in the core area <<{core_area}>>. 


CONTEXT:
This task is part of a process to refine the thesaurus for co-word and 
tech-mining analysis in the core area of <<{core_area}>>. The goal is to build 
a definition of the <<{term}>> based on the provided context phrases.

Important extraction assumption:
-   The corpus has been pre-processed to extract meaningful terms 
    (noun phrases / keywords).
-   Multi-word terms are indexed separately from their headwords. Therefore, 
    phrases for an isolated term do not include occurrences that belong to its 
    multi-word variants (e.g., phrases for "value" exclude "market value", 
    "net present value", etc.).


TASK:
Build a definition of the <<{term}>> in the core area of <<{core_area}>>, based 
on the provided context phrases.

CONSTRAINTS:
-   Use only the provided context phrases plus general scientific knowledge 
    of <<{core_area}>>.


OUTPUT:
A text paragraph.


LENGTH:
80 to 120 words.


CONTEXT PHRASES:
{contexts}

"""


# -----------------------------------------------------------------------------
def internal__user_input(core_area):

    #
    # Core Area
    #
    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None, None, None
    else:
        answer = colorized_input(f". Enter the core area [{core_area}] > ").strip()

    if answer != "":
        core_area = answer.upper()

    #
    # Term
    #
    term = colorized_input(". Enter the term > ").strip()
    if term == "":
        return None, None, None

    #
    # Number of Contexts
    #
    n_contexts = colorized_input(
        ". Enter the number of contexts [default: 30] > "
    ).strip()
    if n_contexts == "":
        n_contexts = 30
    else:
        n_contexts = int(n_contexts)

    return core_area, term, n_contexts


# -----------------------------------------------------------------------------
def internal__filter_contexts(
    n_contexts,
    contexts,
):
    contexts = contexts[:n_contexts]
    return contexts


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

        complete_contexts.extend(contexts)

    pattern = pattern.lower().replace("_", " ")
    complete_contexts = [c for c in complete_contexts if pattern in c]

    if len(complete_contexts) < 5:
        return None

    return complete_contexts[:n_contexts]


# -----------------------------------------------------------------------------
def internal__execute_query(
    core_area,
    term,
    contexts,
):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    query = PROMPT.format(
        term=term,
        contexts="\n".join(contexts),
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
        print(f"Error processing the query: {e}")
        return None


# -----------------------------------------------------------------------------
def internal__print(msg):
    print(Fore.LIGHTBLACK_EX + msg + Fore.RESET)


# -----------------------------------------------------------------------------
def execute_define_command():

    print()
    core_area = None

    while True:

        core_area, term, n_contexts = internal__user_input(core_area)

        print()
        internal__print("Evaluating synonyms...")

        if term is None:
            print()
            return

        internal__print("  Building contexts for the term...")
        contexts = internal__get_contexts(term, n_contexts)
        if not contexts:
            print("Insufficient contexts available for the term.")
            continue

        contexts = internal__filter_contexts(n_contexts, contexts)

        internal__print("  Executing the query...")

        definition = internal__execute_query(core_area, term, contexts)
        definition = definition.lower()
        term = term.lower().replace("_", " ")
        definition = definition.replace(term, term.upper())

        internal__print("  Evaluation process completed successfully.")
        print()
        definition = textwrap.fill(definition, width=80)
        print(definition)
        print()


#
