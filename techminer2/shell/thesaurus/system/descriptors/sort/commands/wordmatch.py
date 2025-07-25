from .......thesaurus.system.descriptors import SortByWordMatch
from ......colorized_input import colorized_input


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
    SortByWordMatch().having_pattern(patterns).run()
