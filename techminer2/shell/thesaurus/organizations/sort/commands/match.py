from ......thesaurus.organizations import SortByMatch


def execute_match_command():

    print()

    # Pattern input
    pattern = input(". having pattern > ").strip()
    if pattern == "":
        return

    # Case sensitivity
    case_sensitive = input(". case sensitive? (y/[n]) > ").strip().lower()
    if case_sensitive == "":
        case_sensitive = "n"
    if case_sensitive not in ["y", "n"]:
        return
    case_sensitive = case_sensitive == "y"

    # Regex flags
    regex_flags = input(". regex flags (default: 0) > ").strip()
    if regex_flags == "":
        regex_flags = 0
    else:
        if regex_flags.isdigit():
            regex_flags = int(regex_flags)
        else:
            regex_flags = 0

    # Regex search
    regex_search = input(". regex search? (y/[n]) > ").strip().lower()
    if regex_search == "":
        regex_search = "n"
    if regex_search not in ["y", "n"]:
        return
    regex_search = regex_search == "y"

    # Execute the sort command
    (
        SortByMatch()
        .where_root_directory_is("./")
        .having_pattern(pattern)
        .having_case_sensitive(case_sensitive)
        .having_regex_flags(regex_flags)
        .having_regex_search(regex_search)
        .run()
    )
