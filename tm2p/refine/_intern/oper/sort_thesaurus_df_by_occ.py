import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import ThField

CHANGED = ThField.CHANGED.value
KEY = ThField.OLD.value
OCC = ThField.OCC.value
PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


def sort_thesaurus_df_by_occ(
    params: Params,
    thesaurus_df: pd.DataFrame,
) -> pd.DataFrame:

    data_df = load_main_csv_zip(
        root_directory=params.root_directory,
        usecols=[params.analysis_unit.value],
    )

    variant_to_preferred = _build_variant_to_preferred_mapping(thesaurus_df)

    preferred_to_occ = _build_preferred_to_occ_mapping(
        data_df=data_df,
        variant_to_preferred=variant_to_preferred,
        analysis_unit=params.analysis_unit.value,
    )

    thesaurus_df = _sort_by_occ(thesaurus_df, preferred_to_occ)

    return thesaurus_df


def _build_variant_to_preferred_mapping(dataframe):

    dataframe = dataframe.copy()
    dataframe = dataframe[[PREFERRED, VARIANT]].copy()
    dataframe[VARIANT] = dataframe[VARIANT].str.split("; ")
    dataframe = dataframe.explode(VARIANT)
    dataframe[VARIANT] = dataframe[VARIANT].str.strip()

    variant_to_preferred = dict(zip(dataframe[VARIANT], dataframe[PREFERRED]))

    return variant_to_preferred


def _build_preferred_to_occ_mapping(
    data_df,
    variant_to_preferred,
    analysis_unit,
):

    data_df = data_df.copy()
    data_df = data_df.dropna()

    data_df[analysis_unit] = data_df[analysis_unit].str.split("; ")
    data_df[analysis_unit] = data_df[analysis_unit].apply(
        lambda x: [variant_to_preferred.get(y.strip(), y.strip()) for y in x]
    )
    data_df[analysis_unit] = data_df[analysis_unit].apply(set)
    data_df = data_df.explode(analysis_unit)

    series = data_df[analysis_unit].value_counts()

    occ_mapping = dict(
        zip(
            series.index,
            series.to_list(),
        )
    )

    return occ_mapping


def _sort_by_occ(df, occ_mapping):

    df = df.copy()
    df[OCC] = df[PREFERRED].apply(lambda x: occ_mapping.get(x, 0))
    df = df.sort_values([OCC, PREFERRED], ascending=[False, True])
    df = df.drop(columns=[OCC])

    return df
