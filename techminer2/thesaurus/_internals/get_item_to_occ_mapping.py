"""
Smoke test:
    >>> from techminer2.thesaurus._internals import get_item_to_occ_mapping
    >>> from techminer2 import Field
    >>> mapping = get_item_to_occ_mapping(
    ...     root_directory="examples/small/",
    ...     column=Field.ALL_KEY_NP_WORD_RAW,
    ... )
    >>> len(mapping)
    1906
    >>> mapping['Conceptual frameworks']
    1


"""

from techminer2 import CorpusField, ThesaurusField
from techminer2._internals.data_access import load_main_data


def get_item_to_occ_mapping(root_directory: str, column: CorpusField) -> dict[str, int]:

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
