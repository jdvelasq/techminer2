from ......thesaurus.organizations import SortByWordMatch
from .....colorized_input import colorized_input


def execute_wordmatch_command():

    print()

    patterns = []
    while True:
        pattern = colorized_input(". having pattern > ").strip()
        if pattern == "":
            break
        patterns.append(pattern)

    if not patterns:
        print()
        return

    print()
    SortByWordMatch().where_root_directory_is("./").having_pattern(patterns).run()
