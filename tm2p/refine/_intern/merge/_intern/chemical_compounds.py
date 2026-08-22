# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p.enum import ThField

PREFERRED = ThField.PREFERRED.value


_CHEMICAL_COMPOUNDS = {
    "co 2": "carbon dioxide",
    #
    "chlorobenzene": "chlorobenzene",
    "co-2": "carbon dioxide",
    # "co": "carbon monoxide",
    "co2": "carbon dioxide",
    "co3o4": "cobalt oxide",
    "h2o": "water",
    "h2so4": "sulfuric acid",
    "koh": "potassium hydroxide",
    "li2o2": "lithium peroxide",
    "li2s": "lithium sulfide",
    "licoo2": "lithium cobalt oxide",
    "lifepo4": "lithium iron phosphate",
    "mno2": "manganese dioxide",
    "mos2": "molybdenum disulfide",
    "o2": "oxygen",
    "tio2": "titanium dioxide",
    "toluene": "toluene",
    "v2o5": "vanadium pentoxide",
}


def apply_chemical_compounds_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(lambda x: f" {x} ")

    for compound, name in _CHEMICAL_COMPOUNDS.items():

        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            rf" {compound} ",
            f" {name} ",
            regex=True,
        )

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()

    return thesaurus_df
