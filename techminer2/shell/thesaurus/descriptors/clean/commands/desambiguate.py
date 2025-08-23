# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import os

import openai
from colorama import Fore
from openai import OpenAI

from techminer2.database.search import ConcordantRawContexts
from techminer2.shell.colorized_input import colorized_input

PROMPT = """
TASK:
Decide whether the two provided terms (keywords or noun phrases) are conceptual synonyms in scientific or technical language, based solely on the provided contexts.

INSTRUCTIONS:
1. Carefully review all provided contexts for each term.
2. Compare the meaning, usage, and roles of each term within their respective contexts.
3. Use only the provided contexts for your analysis. Do not use external information or prior knowledge.
4. If both terms consistently refer to the same concept, idea, or entity in these contexts—and merging them would not lose any meaningful distinction—respond with "yes".
5. If the terms clearly represent different concepts, have distinct roles, or merging them would obscure important differences, respond with "no".
6. Your answer must be a single word: "yes" or "no".
7. If you are uncertain or the contexts are insufficient to decide, respond with "no".


TERMS:
Term 1: <<{pattern_1}>>
Term 2: <<{pattern_2}>>


CONTEXTS FOR TERM 1:
{contexts_1}


CONTEXTS FOR TERM 2:
{contexts_2}


"""


# -----------------------------------------------------------------------------
def internal__user_input():

    print()

    pattern_1 = colorized_input(". Enter pattern 1 > ").strip()
    if pattern_1 == "":
        return None, None, None

    pattern_2 = colorized_input(". Enter pattern 2 > ").strip()
    if pattern_2 == "":
        return None, None, None

    n_contexts = colorized_input(
        ". Enter the number of contexts [default: 20] > "
    ).strip()
    if n_contexts == "":
        n_contexts = 20
    else:
        n_contexts = int(n_contexts)

    return pattern_1, pattern_2, n_contexts


# -----------------------------------------------------------------------------
def internal__filter_contexts(pattern_1, pattern_2, n_contexts, contexts_1, contexts_2):

    if pattern_1 in pattern_2:  # pattern_1 is a substring of pattern_2
        contexts_1 = [t for t in contexts_1 if not pattern_2 in t]

    if pattern_2 in pattern_1:  # pattern_2 is a substring of pattern_1
        contexts_2 = [t for t in contexts_2 if not pattern_1 in t]

    contexts_1 = contexts_1[:n_contexts]
    contexts_2 = contexts_2[:n_contexts]

    return contexts_1, contexts_2


# -----------------------------------------------------------------------------
def internal__get_contexts(pattern, n_contexts):

    contexts = (
        ConcordantRawContexts()
        #
        .with_abstract_having_pattern(pattern)
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        #
        .run()
    )

    if len(contexts) < 5:
        print()
        print(f"Insufficient number of context for pattern {pattern}")
        print()
        return []

    return contexts[:n_contexts]


# -----------------------------------------------------------------------------
def internal__execute_query(pattern_1, pattern_2, contexts_1, contexts_2):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    query = PROMPT.format(
        pattern_1=pattern_1,
        pattern_2=pattern_2,
        contexts_1="\n".join(contexts_1),
        contexts_2="\n".join(contexts_2),
    )

    try:
        response = client.responses.create(
            model="gpt-5-nano",
            input=query,
        )

        answer = response.output_text
        answer = answer.strip().lower()
        return answer

    except openai.OpenAIError as e:
        print()
        print(f"Error processing the query: {e}")
        print()
        return None


# -----------------------------------------------------------------------------
def internal__print_answer(pattern_1, pattern_2, answer):

    pattern_1 = pattern_1.replace(" ", "_").upper()
    pattern_2 = pattern_2.replace(" ", "_").upper()

    text = (
        Fore.LIGHTBLACK_EX
        + f"The terms '{pattern_1}' and '{pattern_2}' "
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
    else:
        text = f"Obtained answer: {answer}"

    print()
    print(text)
    print()


# -----------------------------------------------------------------------------
def execute_desambiguate_command():

    while True:

        pattern_1, pattern_2, n_contexts = internal__user_input()

        if pattern_1 is None or pattern_2 is None:
            print()
            return

        pattern_1 = pattern_1.lower().replace("_", " ")
        pattern_2 = pattern_2.lower().replace("_", " ")

        contexts_1 = internal__get_contexts(pattern_1, n_contexts)
        if not contexts_1:
            continue

        contexts_2 = internal__get_contexts(pattern_2, n_contexts)
        if not contexts_2:
            continue

        contexts_1, contexts_2 = internal__filter_contexts(
            pattern_1, pattern_2, n_contexts, contexts_1, contexts_2
        )

        answer = internal__execute_query(pattern_1, pattern_2, contexts_1, contexts_2)

        internal__print_answer(pattern_1, pattern_2, answer)


#
