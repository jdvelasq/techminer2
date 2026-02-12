import pandas as pd

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


def chemical_compounds_match(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe
