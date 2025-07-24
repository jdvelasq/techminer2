from ......colorized_input import colorized_input
from ......thesaurus.system.descriptors import SortByFuzzyMatch


def execute_fuzzy_command():

    print()

    pattern = colorized_input(". having pattern > ").strip()
    if pattern == "":
        print()
        return

    threshold = colorized_input(". having match threshold > ").strip()
    if threshold == "":
        print()
        return
    threshold = float(threshold)

    print()
    SortByFuzzyMatch().having_pattern(pattern).having_match_threshold(threshold).run()
