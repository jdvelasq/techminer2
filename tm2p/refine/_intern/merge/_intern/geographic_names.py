# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params
from tm2p._intern.packag_data import load_builtin_word_list

PREFERRED = ThField.PREFERRED.value


def apply_geographic_names_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    geographic_names = set(load_builtin_word_list("geographic_names.txt"))

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: x if x not in geographic_names else "#geographic_names"
    )

    return thesaurus_df
