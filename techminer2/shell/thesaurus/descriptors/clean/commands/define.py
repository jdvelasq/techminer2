# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


import textwrap

from techminer2.refine.thesaurus_old.descriptors import DefineTerm
from techminer2.shell.colorized_input import colorized_input


# -----------------------------------------------------------------------------
def internal__get_core_area(core_area):
    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None
        return answer.upper()

    answer = colorized_input(f". Enter the core area [{core_area}] > ").strip()
    return core_area if answer == "" else answer.upper()


# -----------------------------------------------------------------------------
def internal__get_term():
    term = colorized_input(". Enter the term > ").strip()
    if term == "":
        return None
    return term


# -----------------------------------------------------------------------------
def internal__get_n_contexts(n_contexts):
    answer = colorized_input(
        f". Enter the number of contexts [{n_contexts}] > "
    ).strip()
    if answer == "":
        return n_contexts
    return int(answer)


# -----------------------------------------------------------------------------
def internal__generate_definition(core_area, term, n_contexts):
    return (
        DefineTerm()
        #
        # FIELD:
        .with_core_area(core_area)
        .having_patterns_matching([term])
        .having_n_contexts(n_contexts)
        #
        # DATABASE:
        .where_root_directory("./")
        .where_database("main")
        .where_record_years_range(None, None)
        .where_record_citations_range(None, None)
        .where_records_match(None)
        #
        .run()
    )[0]


# -----------------------------------------------------------------------------
def internal__format_definition(definition):
    return textwrap.fill(definition, width=70)


# -----------------------------------------------------------------------------
def execute_define_command():

    core_area = None
    n_contexts = 30

    print()
    while True:

        core_area = internal__get_core_area(core_area)
        if core_area is None:
            return

        term = internal__get_term()
        if term is None:
            return

        n_contexts = internal__get_n_contexts(n_contexts)

        definition = internal__generate_definition(
            core_area,
            term,
            n_contexts,
        )

        definition = internal__format_definition(definition)
        print(definition)
        print()


#
