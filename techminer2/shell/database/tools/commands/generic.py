import os

from colorama import Fore
from colorama import init
from openai import OpenAI
from techminer2.database.search import ConcordantRawContexts
from techminer2.shell.colorized_input import colorized_input

PROMPT = """
Using the contexts presented below, determine if the term <<{pattern}>> is to generic, vague or ambiguous
to be used for co-word analysis or not.

Your answer should be a single word: "yes" or "no".

Contexts for the term <<{pattern}>>:

{contexts}

"""


def execute_generic_command():

    print()

    # PARAMETERS:

    pattern = colorized_input(". Enter the pattern > ").strip()

    # n_contexts:
    n_contexts = colorized_input(
        ". Enter the number of contexts [default: 20] > "
    ).strip()
    if n_contexts == "":
        n_contexts = 20
    else:
        n_contexts = int(n_contexts)

    # RUN:

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
    contexts = contexts[:n_contexts]

    ###
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    query = PROMPT.format(
        pattern=pattern,
        contexts="\n".join(contexts),
    )

    ##
    # print(query)
    ##

    query = "say hello!"

    try:

        response = client.responses.create(
            model="gpt-5-nano",
            input=query,
        )
        answer = response.output_text
        answer = answer.strip().lower()

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

    except Exception as e:
        print()
        print(f"Error processing the query: {e}")
        print()
