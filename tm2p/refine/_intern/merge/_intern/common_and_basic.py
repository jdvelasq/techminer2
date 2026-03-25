# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params
from tm2p._intern.packag_data import load_builtin_word_list

CHANGED = ThField.CHANGED.value
IS_KEYWORD = ThField.IS_KEYWORD.value
OCC = ThField.OCC.value
OLD = ThField.OLD.value
PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
VARIANT = ThField.VARIANT.value


def apply_common_and_basic_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    common_and_basic = set(load_builtin_word_list("common_and_basic.txt"))

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(
        lambda x: x if x not in common_and_basic else "#common_and_basic"
    )

    return thesaurus_df
