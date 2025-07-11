from ......thesaurus.countries import SortByWordMatch


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
    SortByWordMatch().where_root_directory_is("./").having_pattern(patterns).run()
