from techminer2.database.search import ConcordantRawContexts
from techminer2.shell.colorized_input import colorized_input


def execute_contexts_command():

    print()

    pattern = colorized_input(". Enter pattern > ").strip()

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
