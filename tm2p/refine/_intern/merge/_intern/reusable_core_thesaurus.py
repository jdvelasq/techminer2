# pylint: disable=unused-argument
import re

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore

from tm2p._intern import Params
from tm2p._intern.packag_data.mappings.load_builtin_mapping import load_builtin_mapping
from tm2p.enum import ThField

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
VARIANT = ThField.VARIANT.value


def apply_reusable_core_thesaurus_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(lambda x: f" {x} ")

    core_thesaurus = load_builtin_mapping("core_thesaurus.the.json")
    for preferred, variants in core_thesaurus.items():

        for variant in variants:
            thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
                rf"^ {re.escape(variant)} $",
                f" {preferred} ",
                regex=True,
            )

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()

    return thesaurus_df
