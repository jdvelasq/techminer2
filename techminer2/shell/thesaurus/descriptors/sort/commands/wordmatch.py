from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import SortByWordMatch


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
    SortByWordMatch().where_root_directory("./").having_pattern(patterns).run()


##
