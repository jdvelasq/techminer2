from techminer2.thesaurus.countries import SortByExactMatch

from .....colorized_input import colorized_input


def execute_exact_command():

    print()

    patterns = []
    while True:
        pattern = colorized_input(". having pattern > ")
        if pattern == "":
            break
        patterns.append(pattern)

    if not patterns:
        print()
        return

    print()
    SortByExactMatch().where_root_directory_is("./").having_pattern(patterns).run()
