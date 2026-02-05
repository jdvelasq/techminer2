import pandas as pd

from techminer2 import ThesaurusField

INDENT = " " * 4


def _read_file(filepath: str):

    variants: list[str] = []
    preferred_terms: list[str] = []
    preferred: str = ""

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\t", INDENT)
            line = line.split(" # ")[0].rstrip()

            if not line.startswith(" "):
                preferred = line.strip()
            else:
                line = line.strip()
                variants.append(line)
                preferred_terms.append(preferred)

    return variants, preferred_terms


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
