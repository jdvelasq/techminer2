from techminer2.analyze.concordances import ConcordanceRaw
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
        ConcordanceRaw()
        #
        .having_text_matching(pattern)
        .where_root_directory("./")
        .where_database("main")
        .where_record_years_range(None, None)
        .where_record_citations_range(None, None)
        #
        .run()
    )

    print()
    for t in contexts[:n_contexts]:
        print(t)
    print()
