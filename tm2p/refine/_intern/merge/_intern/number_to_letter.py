# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params
from tm2p._intern.packag_data import load_builtin_mapping

PREFERRED = ThField.PREFERRED.value


def apply_number_to_letter_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    number_to_letter = load_builtin_mapping("number_to_letter.json")

    for number, letter in number_to_letter.items():

        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            rf"^{number} ",
            f" {letter} ",
            regex=True,
        )

    return thesaurus_df
