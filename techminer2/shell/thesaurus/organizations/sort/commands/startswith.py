from ......thesaurus.organizations import SortByStartsWithMatch


def execute_startswith_command():

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
    (
        SortByStartsWithMatch()
        .where_root_directory_is("./")
        .having_pattern(patterns)
        .run()
    )
