# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params

PREFERRED = ThField.PREFERRED.value


_TECHNOLOGY = {
    "li-ion": "lithium-ion",
    "li ion": "lithium-ion",
    "li-s": "lithium-sulfur",
    "li sulfur": "lithium-sulfur",
    "li-air": "lithium-air",
    "na-ion": "sodium-ion",
    "k-ion": "potassium-ion",
    "zn-ion": "zinc-ion",
    "al-ion": "aluminum-ion",
    "mg-ion": "magnesium-ion",
}


def apply_technology_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(lambda x: f" {x} ")

    for term, name in _TECHNOLOGY.items():

        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            rf" {term} ",
            f" {name} ",
            regex=True,
        )

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()

    return thesaurus_df
