from ......thesaurus.descriptors import SortByExactMatch


def execute_exact_command():

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
    SortByExactMatch().where_root_directory_is("./").having_pattern(patterns).run()
