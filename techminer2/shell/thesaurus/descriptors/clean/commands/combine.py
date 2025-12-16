# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=unused-argument

from techminer2.thesaurus.descriptors import CombineKeys


def execute_combine_command():

    print()

    df = (
        CombineKeys()
        .where_root_directory_is("./")
        .having_terms_ordered_by("OCC")
        .having_term_occurrences_between(5, None)
        .run()
    )

    if df.empty:
        print("No combinations found.")
        print()
        return

    print(df.to_string())
    print()
