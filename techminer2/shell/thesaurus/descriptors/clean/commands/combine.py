from techminer2.refine.thesaurus_old.descriptors import CombineKeys


def execute_combine_command():

    print()

    df = (
        CombineKeys()
        .where_root_directory("./")
        .having_items_ordered_by("OCC")
        .having_item_occurrences_between(5, None)
        .run()
    )

    if df.empty:
        print("No combinations found.")
        print()
        return

    print(df.to_string())
    print()
