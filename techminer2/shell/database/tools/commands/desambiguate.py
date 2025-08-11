import os

from colorama import Fore
from colorama import init
from openai import OpenAI
from techminer2.database.search import ConcordantProcessedContexts
from techminer2.shell.colorized_input import colorized_input

PROMPT = """
Using the contexts presented below, determine if the terms <<{pattern_1}>> and <<{pattern_2}>> are synonyms or not,
and can be merged into a single term. 

Your answer should be a single word: "yes" or "no".

Contexts for term <<{pattern_1}>>:
{contexts_1}

Contexts for term <<{pattern_2}>>:
{contexts_2}

"""


def execute_desambiguate_command():

    print()

    # PARAMETERS:

    pattern_1 = colorized_input(". Enter pattern 1 > ").strip()
    pattern_2 = colorized_input(". Enter pattern 2 > ").strip()

    # n_contexts:
    n_contexts = colorized_input(
        ". Enter the number of contexts [default: 20] > "
    ).strip()
    if n_contexts == "":
        n_contexts = 20
    else:
        n_contexts = int(n_contexts)

    # RUN:

    contexts_1 = (
        ConcordantProcessedContexts()
        #
        .with_abstract_having_pattern(pattern_1)
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        #
        .run()
    )
    contexts_1 = contexts_1[:n_contexts]

    contexts_2 = (
        ConcordantProcessedContexts()
        #
        .with_abstract_having_pattern(pattern_2)
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        #
        .run()
    )
    contexts_2 = contexts_2[:n_contexts]

    ###
    client = os.getenv("OPENAI_API_KEY")

    query = PROMPT.format(
        pattern_1=pattern_1,
        pattern_2=pattern_2,
        contexts_1="\n".join(contexts_1),
        contexts_2="\n".join(contexts_2),
    )

    try:
        response = client.responses.create(
            model="o4-mini",
            input=query,
        )
        answer = response.output_text

        text = (
            Fore.LIGHTBLACK_EX
            + f"The terms '{pattern_1}' and '{pattern_2}' "
            + Fore.RESET
            + "{result}"
            + Fore.LIGHTBLACK_EX
            + " SYNONYMOUS."
            + Fore.RESET
        )

        if answer.lower() == "yes":
            text = text.format(result="ARE")
        elif answer.lower() == "no":
            text = text.format(result="ARE NOT")

        print()
        print(text)
        print()

    except Exception as e:
        print()
        print(f"Error processing the query!")
        print()
        print()
        print()
        print()
