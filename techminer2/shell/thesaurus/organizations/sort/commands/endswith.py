from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.organizations import SortByEndsWithMatch


def execute_endswith_command():

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
    SortByEndsWithMatch().where_root_directory_is("./").having_pattern(patterns).run()


##
