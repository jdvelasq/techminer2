# pylint: disable=unused-argument

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore

from tm2p._intern import Params
from tm2p._intern.packag_data.mappings.load_builtin_mapping import load_builtin_mapping
from tm2p.enum import ThField

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
VARIANT = ThField.VARIANT.value


def apply_british_to_american_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(lambda x: f" {x} ")

    british_to_american = load_builtin_mapping("british_to_american.json")
    for british, american in british_to_american.items():

        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            rf" {british} ",
            f" {american} ",
            regex=True,
        )

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()

    return thesaurus_df
