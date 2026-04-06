# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.enum import ThField

PREFERRED = ThField.PREFERRED.value


def apply_exact_match_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
        r"\r\n|\r", "", regex=True
    )
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()

    return thesaurus_df
