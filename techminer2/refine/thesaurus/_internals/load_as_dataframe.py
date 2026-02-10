import pandas as pd

from techminer2 import CorpusField, ThesaurusField
from techminer2._internals import Params
from techminer2._internals.data_access import (
    get_thesaurus_path,
    load_main_data,
    load_thesaurus_as_dataframe,
)


def _compute_occurrences(params: Params, dataframe: pd.DataFrame) -> pd.DataFrame:

    dataframe = dataframe.copy()

    item_to_occ = _get_item_to_occ_mapping(
        root_directory=params.root_directory,
        column=params.field,
    )
    dataframe[ThesaurusField.OCC.value] = dataframe[ThesaurusField.PREFERRED.value].map(
        lambda x: item_to_occ.get(x, 0)
    )

    return dataframe


def _get_item_to_occ_mapping(
    root_directory: str,
    column: CorpusField,
) -> dict[str, int]:

    data = load_main_data(root_directory=root_directory, usecols=[column.value])
    data = data.dropna()
    data = data.rename(columns={column.value: ThesaurusField.PREFERRED.value})
    data[ThesaurusField.PREFERRED.value] = data[
        ThesaurusField.PREFERRED.value
    ].str.split("; ")
    data = data.explode(ThesaurusField.PREFERRED.value)
    data[ThesaurusField.PREFERRED.value] = data[
        ThesaurusField.PREFERRED.value
    ].str.strip()
    data[ThesaurusField.OCC.value] = 1
    groupby_df = data.groupby(ThesaurusField.PREFERRED.value, as_index=True).agg(
        {ThesaurusField.OCC.value: "sum"}
    )
    mapping = dict(
        zip(groupby_df.index.to_list(), groupby_df[ThesaurusField.OCC.value].to_list())
    )

    return mapping


def _load_thesaurus(
    params: Params,
) -> pd.DataFrame:

    filepath = get_thesaurus_path(
        root_directory=params.root_directory,
        file=params.thesaurus_file,
    )
    dataframe = load_thesaurus_as_dataframe(filepath=str(filepath))
    dataframe = dataframe[
        [
            ThesaurusField.PREFERRED.value,
            ThesaurusField.VARIANT.value,
        ]
    ]

    return dataframe


def load_as_dataframe(params: Params) -> pd.DataFrame:

    dataframe = _load_thesaurus(params=params)
    dataframe = _compute_occurrences(params=params, dataframe=dataframe)

    dataframe[ThesaurusField.PREFERRED_TEMP.value] = dataframe[
        ThesaurusField.PREFERRED.value
    ]

    return dataframe
