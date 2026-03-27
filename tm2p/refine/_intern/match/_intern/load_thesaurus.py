from tm2p import ThField
from tm2p.refine._intern.data_access import load_thesaurus_as_dataframe
from tm2p.refine._intern.oper import sort_thesaurus_df_by_occ

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value


def load_thesaurus(params):

    thesaurus_df = load_thesaurus_as_dataframe(params=params)

    thesaurus_df = sort_thesaurus_df_by_occ(
        params=params,
        thesaurus_df=thesaurus_df,
    )
    thesaurus_df = thesaurus_df[~thesaurus_df[PREFERRED].str.startswith("#")].copy()

    thesaurus_df[SIGNATURE] = thesaurus_df[PREFERRED].str.lower()

    return thesaurus_df
