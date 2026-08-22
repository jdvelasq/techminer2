# pylint: disable=unused-argument

import re

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore

from tm2p._intern import Params
from tm2p.enum import ThField

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value


def apply_hyphen_space_plural_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df[SIGNATURE] = thesaurus_df[PREFERRED]

    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace("-", "", regex=False)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(" ", "", regex=False)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(" ", "", regex=False)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(
        lambda x: x[:-3] + "y" if x.endswith("ies") else x
    )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(
        lambda x: x[:-2] if re.search(r"(s|x|z|ch|sh)es$", x) else x
    )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(
        lambda x: x[:-1] if x.endswith("s") and not x.endswith("ss") else x
    )

    mapping_df = thesaurus_df[[SIGNATURE, PREFERRED]].copy()
    mapping_df = mapping_df.drop_duplicates(subset=[SIGNATURE], keep="first")  # type: ignore
    mapping = dict(zip(mapping_df[SIGNATURE].values, mapping_df[PREFERRED].values))

    thesaurus_df[PREFERRED] = thesaurus_df[SIGNATURE].apply(lambda x: mapping.get(x, x))

    thesaurus_df.pop(SIGNATURE)

    return thesaurus_df
