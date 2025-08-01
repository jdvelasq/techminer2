from ......thesaurus.organizations import SortByExactMatch
from .....colorized_input import colorized_input


def execute_exact_command():

    print()

    patterns = []
    while True:
        pattern = colorized_input(". having pattern > ").strip()
        if pattern == "":
            break
        patterns.append(pattern)

    print()
    if not patterns:
        return

    SortByExactMatch().where_root_directory_is("./").having_pattern(patterns).run()
