from techminer2.refine.thesaurus_old.descriptors import SortByExactMatch
from techminer2.shell.colorized_input import colorized_input


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
    SortByExactMatch().where_root_directory("./").having_text_matching(patterns).run()


#
#
