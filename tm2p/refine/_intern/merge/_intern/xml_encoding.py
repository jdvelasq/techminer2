# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p.enum import ThField
from tm2p._intern import Params
from tm2p._intern.packag_data import load_builtin_mapping

CHANGED = ThField.CHANGED.value
IS_KEYWORD = ThField.IS_KEYWORD.value
OCC = ThField.OCC.value
OLD = ThField.OLD.value
PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
VARIANT = ThField.VARIANT.value


def apply_xml_encoding_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    xml_encoding = load_builtin_mapping("xml_encoding.json")

    for xml, char in xml_encoding.items():

        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            rf" {xml} ",
            f" {char} ",
            regex=True,
        )

    return thesaurus_df
