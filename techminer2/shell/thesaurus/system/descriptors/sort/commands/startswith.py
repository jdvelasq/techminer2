from ......colorized_input import colorized_input
from ......thesaurus.system.descriptors import SortByStartsWithMatch


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
    SortByStartsWithMatch().having_pattern(patterns).run()
