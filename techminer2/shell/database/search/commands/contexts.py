from techminer2.database.search import ConcordantRawContexts
from techminer2.shell.colorized_input import colorized_input


def execute_contexts_command():

    print()

    # PARAMETERS:

    pattern = colorized_input(". Enter pattern > ").strip()

    # database:
    # database = colorized_input(". Enter database [default: main] > ").strip()
    # if not database:
    #     database = "main"

    # initial year range:
    # initial_year = colorized_input(
    #     ". Enter the initial year [default: None] > "
    # ).strip()
    # if initial_year == "":
    #     initial_year = None
    # else:
    #     initial_year = int(initial_year)

    # final year range:
    # final_year = colorized_input(". Enter the final year [default: None] > ").strip()
    # if final_year == "":
    #     final_year = None
    # else:
    #     final_year = int(final_year)

    # initial citations range:
    # initial_citations = colorized_input(
    #     ". Enter the lower limit of citations [default: None] > "
    # ).strip()
    # if initial_citations == "":
    #     initial_citations = None
    # else:
    #     initial_citations = int(initial_citations)

    # final citations range:
    # final_citations = colorized_input(
    #     ". Enter the upper limit of citations (None) > "
    # ).strip()
    # if final_citations == "":
    #     final_citations = None
    # else:
    #     final_citations = int(final_citations)

    # n_contexts:
    n_contexts = colorized_input(
        ". Enter the number of contexts [default: 10] > "
    ).strip()
    if n_contexts == "":
        n_contexts = 10
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

    print()
    for t in contexts[:n_contexts]:
        print(t)
    print()
