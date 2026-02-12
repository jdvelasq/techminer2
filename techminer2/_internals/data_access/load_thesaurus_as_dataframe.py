import pandas as pd

from techminer2 import ThesaurusField


def _read_file(filepath: str):
    pass


def _transform_to_dataframe(
    variants: list[str],
    preferred_terms: list[str],
) -> pd.DataFrame:

    dataframe = pd.DataFrame(
        {
            ThesaurusField.PREFERRED.value: preferred_terms,
            ThesaurusField.VARIANT.value: variants,
        }
    )

    dataframe = (
        dataframe.groupby(ThesaurusField.PREFERRED.value, as_index=False)
        .agg({ThesaurusField.VARIANT.value: list})
        .reset_index(drop=True)
    )
    dataframe[ThesaurusField.VARIANT.value] = dataframe[
        ThesaurusField.VARIANT.value
    ].str.join("; ")
    dataframe = dataframe.sort_values(ThesaurusField.PREFERRED.value).reset_index(
        drop=True
    )

    return dataframe


def load_thesaurus_as_dataframe(filepath: str) -> pd.DataFrame:

    variants, preferred_terms = _read_file(filepath)

    return _transform_to_dataframe(variants, preferred_terms)
