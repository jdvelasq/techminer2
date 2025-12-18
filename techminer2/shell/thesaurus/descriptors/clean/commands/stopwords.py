# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=unused-argument

import os
from pprint import pprint  # type: ignore

import openai
from colorama import Fore
from openai import OpenAI
from tqdm import tqdm  # type: ignore

from techminer2._internals.load_template import internal_load_template
from techminer2.database.search import ConcordantSentences
from techminer2.database.tools import ExtendStopwords
from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import IsStopword


# -----------------------------------------------------------------------------
def internal__user_input(core_area, n_contexts, occ):

    # -------------------------------------------------------------------------
    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None, None
        core_area = answer.upper()

    # -------------------------------------------------------------------------
    user_n_contexts = colorized_input(
        f". Enter the number of contexts [{n_contexts}] > "
    ).strip()

    if user_n_contexts != "":
        n_contexts = int(n_contexts)

    # -------------------------------------------------------------------------
    user_occ = colorized_input(f". Enter the mininum occ [{occ}] > ").strip()

    if user_occ != "":
        occ = int(user_occ)

    # -------------------------------------------------------------------------
    return core_area, n_contexts, occ


# -----------------------------------------------------------------------------
def execute_stopwords_command():

    print()
    core_area = None
    n_contexts = 30
    occ = 7

    core_area, n_contexts, occ = internal__user_input(core_area, n_contexts, occ)

    if core_area is None:
        print()
        return

    df = (
        IsStopword(quiet=False)
        .with_core_area(core_area)
        .having_n_contexts(n_contexts)
        .having_terms_in_top(None)
        .having_terms_ordered_by("OCC")
        .having_term_occurrences_between(occ, None)
        .having_term_citations_between(None, None)
        .having_terms_in(None)
        .where_root_directory_is("./")
    ).run()

    with open("./outputs/tables/stopwords.txt", "w") as f:
        f.write(df.to_string(index=False))

    print("INFO: The report has been saved in: ./outputs/tables/stopwords.txt")
    print()
