import pandas as pd  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import Params

from ._post_process import _post_process
from ._pre_process import _pre_process

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


# Consolidate chemical terms and formulas
#
# Load CHEMICAL_COMPOUNDS_THESAURUS:
#   Structure:
#     preferred_term
#         variant1
#         variant2
#
#   Example:
#     iron oxide
#         iron oxide
#         iron oxides
#         Fe2O3
#         ferric oxide
#
# For each key in descriptor thesaurus:
#   1. Search in chemical thesaurus (check if key is a variant)
#
#   2. If found as variant:
#      a. Get preferred_term from chemical thesaurus
#      b. In descriptor thesaurus:
#         - Move key and all its variants under preferred_term
#
#   3. If not found:
#      - Keep key as-is
#
#
# Before:
#
# iron oxide
#     iron oxide
# Fe2O3
#     Fe2O3
# ferric oxide
#     ferric oxide
# titanium dioxide
#     titanium dioxide
# TiO2
#     TiO2
#
#
# Chemical compunds thesaurus:
#
# iron oxide
#     iron oxide
#     Fe2O3
#     ferric oxide
# titanium dioxide
#     titanium dioxide
#     TiO2
#     titania
#
#
# After:
#
# iron oxide
#     iron oxide
#     Fe2O3
#     ferric oxide
#
# titanium dioxide
#     titanium dioxide
#     TiO2
#


def apply_chemical_compounds_match_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    #

    #
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
