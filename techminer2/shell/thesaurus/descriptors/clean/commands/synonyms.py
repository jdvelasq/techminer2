# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import AreSynonymous


# -----------------------------------------------------------------------------
def internal__user_input(core_area, occ):

    # -------------------------------------------------------------------------
    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None, None
        core_area = answer.upper()

    # -------------------------------------------------------------------------
    user_occ = colorized_input(f". Enter the mininum occ [{occ}] > ").strip()

    if user_occ != "":
        occ = int(user_occ)

    # -------------------------------------------------------------------------
    return core_area, occ


# -----------------------------------------------------------------------------
def execute_synonyms_command():

    print()
    core_area = None
    n_contexts = 30
    occ = 7

    core_area, occ = internal__user_input(core_area, occ)

    if core_area is None:
        print()
        return

    df = (
        AreSynonymous(quiet=False)
        .with_core_area(core_area)
        .having_n_contexts(n_contexts)
        .having_items_in_top(None)
        .having_items_ordered_by("OCC")
        .having_item_occurrences_between(occ, None)
        .having_item_citations_between(None, None)
        .having_items_in(None)
        .where_root_directory("./")
    ).run()

    with open("./outputs/tables/synonyms.txt", "w") as f:
        for _, row in df.iterrows():
            lead_term = row["lead_term"]
            candidate_terms = row["candidate_terms"].split("; ")
            f.write(f"{lead_term}\n")
            for candidate in candidate_terms:
                f.write(f"    {candidate}\n")

    print("INFO: The report has been saved in: ./outputs/tables/synonyms.txt")
    print()


#
