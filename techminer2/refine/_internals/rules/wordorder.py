import pandas as pd  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import Params
from techminer2._internals.package_data import load_builtin_word_list

from ._pre_process import _pre_process
from .fuzzy_cutoff_0_word import _report_mergings

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


def apply_wordorder_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    thesaurus_df[SIGNATURE] = thesaurus_df[PREFERRED]
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.strip()
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(lambda x: f" {x} ")
    stopwords = set(load_builtin_word_list("stopwords.txt"))
    for stopword in stopwords:
        thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.replace(
            f" {stopword} ", " "
        )
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.split(" ")
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(set)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].apply(sorted)
    thesaurus_df[SIGNATURE] = thesaurus_df[SIGNATURE].str.join(" ")
    #
    mapping_df = thesaurus_df[[SIGNATURE, PREFERRED]].copy()
    mapping_df = mapping_df.drop_duplicates()
    mapping = {
        signature: preferred
        for signature, preferred in zip(
            mapping_df[SIGNATURE].values, mapping_df[PREFERRED].values
        )
    }
    thesaurus_df[PREFERRED] = thesaurus_df[SIGNATURE].apply(lambda x: mapping.get(x, x))
    thesaurus_df[CHANGED] = thesaurus_df[PREFERRED] != thesaurus_df[OLD]

    thesaurus_df = thesaurus_df[thesaurus_df[CHANGED]].copy()

    mergings: dict[str, list[str]] = {}
    for _, row in thesaurus_df.iterrows():
        old = row[OLD]
        new = row[PREFERRED]

        if new not in mergings:
            mergings[new] = []
        if new != old:
            mergings[new].append(old)

    _report_mergings(
        params=params,
        mapping=mergings,
        filename="candidate_mergings.txt",
    )

    return thesaurus_df
