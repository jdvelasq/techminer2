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

import openai
from colorama import Fore
from openai import OpenAI

from techminer2.database.search import ConcordantRawContexts
from techminer2.database.tools import ExtendStopwords
from techminer2.shell.colorized_input import colorized_input

PROMPT = """
TASK:
Decide whether the term (keyword or noun phrase) provided should be excluded from co-word or tech-mining analysis due to being too generic, vague, or ambiguous.


INSTRUCTIONS:
1. Carefully review all provided contexts in which the term appears.
2. Consider the meaning, usage, and any differences in context.
3. Use only the provided contexts for your analysis. Do not use external information or prior knowledge.
4. If the term is too generic, vague, or ambiguous to be useful for co-word or tech-mining analysis, respond with "yes".
5. If the term is specific and suitable for analysis, respond with "no".
6. Your answer must be a single word: "yes" or "no".
7. If you are uncertain or the contexts are insufficient to decide, respond with "no".

TERM:
<<{pattern}>>

CONTEXTS:
{contexts}

"""


# -----------------------------------------------------------------------------
def internal__user_input():

    pattern = colorized_input(". Enter the pattern > ").strip()
    if pattern == "":
        return None, None

    # n_contexts:
    n_contexts = colorized_input(
        ". Enter the number of contexts [default: 20] > "
    ).strip()
    if n_contexts == "":
        n_contexts = 20
    else:
        n_contexts = int(n_contexts)

    return pattern, n_contexts


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
def internal__execute_query(pattern, contexts):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    query = PROMPT.format(
        pattern=pattern,
        contexts="\n".join(contexts),
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
def internal__print_answer(pattern, answer):

    pattern = pattern.replace(" ", "_").upper()

    text = (
        Fore.LIGHTBLACK_EX
        + f"The term '{pattern}' "
        + Fore.RESET
        + "{result}"
        + Fore.LIGHTBLACK_EX
        + " very generic, vague or ambiguous."
        + Fore.RESET
    )

    if answer.lower() == "yes":
        text = text.format(result="IS")
    else:
        text = text.format(result="IS NOT")

    print()
    print(text)
    print()


# -----------------------------------------------------------------------------
def internal__extend_stopwords(pattern):

    answer = colorized_input(". Extend stopwords with pattern (y/[n])? > ").strip()
    if answer.lower() not in ["y", "yes", ""]:
        print()
        return

    pattern = pattern.upper().replace(" ", "_")
    ExtendStopwords().with_patterns([pattern]).where_root_directory_is("./").run()
    print()


# -----------------------------------------------------------------------------
def execute_generic_command():

    print()

    while True:

        pattern, n_contexts = internal__user_input()

        if pattern is None:
            print()
            return

        pattern = pattern.lower().replace("_", " ")

        contexts = internal__get_contexts(pattern, n_contexts)
        if not contexts:
            continue

        answer = internal__execute_query(pattern, contexts)

        internal__print_answer(pattern, answer)

        internal__extend_stopwords(pattern)


#
