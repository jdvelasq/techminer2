from techminer2.refine.thesaurus_old.organizations import SortByExactMatch
from techminer2.shell.colorized_input import colorized_input


def execute_exact_command():

    print()

    patterns = []
    while True:
        pattern = colorized_input(". having pattern > ").strip()
        if pattern == "":
            break
        patterns.append(pattern)

    print()
    if not patterns:
        return

    SortByExactMatch().where_root_directory("./").having_text_matching(patterns).run()


##
