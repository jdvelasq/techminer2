# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=unused-argument


from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus_old.descriptors import MergeKeys


# -----------------------------------------------------------------------------
def internal__user_input():

    # -------------------------------------------------------------------------
    lead_term = colorized_input(". Enter the lead term > ").strip()
    if lead_term == "":
        return None

    # -------------------------------------------------------------------------
    candidate_term = colorized_input(". Enter the candidate term > ").strip()
    if candidate_term == "":
        return None

    # -------------------------------------------------------------------------
    return [lead_term, candidate_term]


# -----------------------------------------------------------------------------
def execute_merge_command():

    print()

    while True:

        patterns = internal__user_input()

        if patterns is None:
            print()
            return

        MergeKeys().having_patterns_matching(patterns).where_root_directory("./").run()
        print()
