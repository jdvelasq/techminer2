import pandas as pd

from tm2p import ThesaurusField
from tm2p._intern import Params

from .get_thesaurus_path import get_thesaurus_path

PREFERRED = ThesaurusField.PREFERRED.value
VARIANT = ThesaurusField.VARIANT.value

INDENT = " " * 4


def save_dataframe_as_thesaurus(
    params: Params,
    dataframe: pd.DataFrame,
) -> int:

    filepath = get_thesaurus_path(
        root_directory=params.root_directory,
        file=params.thesaurus_file,
    )

    with open(filepath, "w", encoding="utf-8") as file:

        for _, row in dataframe.iterrows():

            preferred = row[PREFERRED]
            variants = row[VARIANT]

            file.write(f"{preferred}\n")

            if variants:
                for variant in variants.split("; "):
                    file.write(f"{INDENT}{variant}\n")

    return len(dataframe)
