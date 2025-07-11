from ......thesaurus.organizations import SortByEndsWithMatch


def execute_endswith_command():

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
    SortByEndsWithMatch().where_root_directory_is("./").having_pattern(patterns).run()
