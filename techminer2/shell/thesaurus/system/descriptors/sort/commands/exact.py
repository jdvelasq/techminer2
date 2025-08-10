from techminer2.thesaurus.system.descriptors import SortByExactMatch

from ......colorized_input import colorized_input


def execute_exact_command():

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
    SortByExactMatch().having_pattern(patterns).run()


#
#
