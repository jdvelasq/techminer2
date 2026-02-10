from techminer2.refine.thesaurus_old.organizations import SortByStartsWithMatch
from techminer2.shell.colorized_input import colorized_input


def execute_startswith_command():

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
    (SortByStartsWithMatch().where_root_directory("./").having_pattern(patterns).run())


##
