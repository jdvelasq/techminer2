from ......thesaurus.countries import SortByFuzzyMatch


def execute_fuzzy_command():

    print()

    pattern = input(". having pattern > ").strip()
    if pattern == "":
        return
    threshold = input(". having match threshold > ").strip()
    if threshold == "":
        return
    threshold = float(threshold)
    SortByFuzzyMatch().where_root_directory_is("./").having_pattern(
        pattern
    ).having_match_threshold(threshold).run()
