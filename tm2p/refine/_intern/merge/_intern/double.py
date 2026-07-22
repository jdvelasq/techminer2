# pylint: disable=unused-argument

import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.packag_data import load_builtin_word_list
from tm2p.enum import ThField

CHANGED = ThField.CHANGED.value
IS_KEYWORD = ThField.IS_KEYWORD.value
OCC = ThField.OCC.value
OLD = ThField.OLD.value
PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value
VARIANT = ThField.VARIANT.value


def apply_double_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    def deduplicate_signature(signature: str) -> str:

        if not signature:
            return signature

        words = signature.split()

        if len(words) % 2 == 0:
            return signature

        mid = len(words) // 2
        first_half = words[:mid]
        second_half = words[mid + 1 :]

        if first_half == second_half:
            return " ".join(first_half)

        return signature

    thesaurus_df[SIGNATURE] = thesaurus_df[PREFERRED]
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(deduplicate_signature)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()

    mapping_df = thesaurus_df[[SIGNATURE, PREFERRED]].copy()
    mapping_df = mapping_df.drop_duplicates(subset=[SIGNATURE], keep="first")  # type: ignore
    mapping = dict(zip(mapping_df[SIGNATURE].values, mapping_df[PREFERRED].values))

    thesaurus_df[PREFERRED] = thesaurus_df[SIGNATURE].apply(lambda x: mapping.get(x, x))

    thesaurus_df.pop(SIGNATURE)

    return thesaurus_df
