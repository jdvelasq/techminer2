from ......thesaurus.organizations import SortByFuzzyMatch
from .....colorized_input import colorized_input


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
        .where_root_directory_is("./")
        .having_pattern(pattern)
        .having_match_threshold(threshold)
        .run()
    )
