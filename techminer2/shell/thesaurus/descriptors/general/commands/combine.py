from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import CombineKeys


def execute_combine_command():

    # print()

    # pattern = colorized_input(". Enter pattern > ").strip()
    # if not pattern:
    #     print()
    #     return

    print()

    df = (
        CombineKeys()
        .where_root_directory_is("./")
        # .with_field_pattern(pattern)
        .having_terms_ordered_by("OCC")
        .having_term_occurrences_between(5, None)
        .run()
    )

    # df = df[df["combine?"] == "yes"]

    if df.empty:
        print("No combinations found.")
        print()
        return

    print(df.to_string())
    print()
