from ......thesaurus.countries import SortByStartsWithMatch
from .....colorized_input import colorized_input


def execute_startswith_command():

    print()

    patterns = []
    while True:
        pattern = input(". having pattern > ").strip()
        if pattern == "":
            break
        patterns.append(pattern)

    if not patterns:
        print()
        return

    print()
    (
        SortByStartsWithMatch()
        .where_root_directory_is("./")
        .having_pattern(patterns)
        .run()
    )
