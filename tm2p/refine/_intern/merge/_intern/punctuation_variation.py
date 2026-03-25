# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params

PREFERRED = ThField.PREFERRED.value


STANDARD_PUNCTUATION = ".,;:!?\"'()"


def apply_punctuation_variation_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    for char in STANDARD_PUNCTUATION:

        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            char, "", regex=False
        )

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
        r"\s+",
        " ",
        regex=True,
    )

    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.strip()

    return thesaurus_df
