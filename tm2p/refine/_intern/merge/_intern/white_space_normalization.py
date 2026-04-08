# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p.enum import ThField
from tm2p._intern import Params

PREFERRED = ThField.PREFERRED.value


def apply_white_space_normalization_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.lower()
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
        r"\s+",
        " ",
        regex=True,
    )

    return thesaurus_df
