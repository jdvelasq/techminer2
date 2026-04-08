# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p.enum import ThField
from tm2p._intern import Params
from tm2p._intern.packag_data import load_builtin_word_list

PREFERRED = ThField.PREFERRED.value


def apply_scientific_and_academic_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    scientific_and_academic = load_builtin_word_list("scientific_and_academic.txt")

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: x if x not in scientific_and_academic else "#scientific_and_academic"
    )

    return thesaurus_df
