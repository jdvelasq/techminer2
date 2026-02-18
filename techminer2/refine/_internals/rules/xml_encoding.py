import pandas as pd  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import Params
from techminer2._internals.package_data import load_builtin_mapping

from ._post_process import _post_process
from ._pre_process import _pre_process

CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value


def apply_xml_encoding_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.lower()
    xml_encoding = load_builtin_mapping("xml_encoding.json")
    for xml, char in xml_encoding.items():
        thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].str.replace(
            rf" {xml} ", f" {char} ", regex=True
        )
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df
