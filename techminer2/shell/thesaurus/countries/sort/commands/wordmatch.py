from techminer2.refine.thesaurus_old.countries import SortByWordMatch
from techminer2.shell.colorized_input import colorized_input


def execute_wordmatch_command():

    print()

    patterns = []
    while True:
        pattern = input(". having pattern > ").strip()
        if pattern == "":
            break
        patterns.append(pattern)

    if not patterns:
        print()
        return

    print()
    SortByWordMatch().where_root_directory("./").having_text_matching(patterns).run()
