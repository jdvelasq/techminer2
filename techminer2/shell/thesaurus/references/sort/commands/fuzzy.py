from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.references import SortByFuzzyMatch


def execute_fuzzy_command():

    print()

    pattern = colorized_input(". having pattern > ").strip()
    if pattern == "":
        print()
        return

    threshold = colorized_input(". having match threshold > ").strip()
    if threshold == "":
        print()
        return
    threshold = float(threshold)

    print()
    (
        SortByFuzzyMatch()
        .where_root_directory("./")
        .having_pattern(pattern)
        .using_match_threshold(threshold)
        .run()
    )


##
