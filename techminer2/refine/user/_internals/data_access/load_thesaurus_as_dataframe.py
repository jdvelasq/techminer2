import pandas as pd

from techminer2 import ThesaurusField
from techminer2._internals import Params

from .get_thesaurus_path import get_thesaurus_path

INDENT = " " * 4


def load_thesaurus_as_dataframe(
    params: Params,
) -> pd.DataFrame:

    filepath = get_thesaurus_path(
        root_directory=params.root_directory,
        file=params.thesaurus_file,
    )

    variants: list[str] = []
    preferred_terms: list[str] = []
    occ_variants: list[int] = []
    preferred: str = ""

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:

            line = line.replace("\t", INDENT)

            if not line.startswith(" "):
                preferred = line.strip()
            else:
                variant, occ = line.split("# occ:")
                variant = variant.strip()
                occ = occ.strip()
                variants.append(variant)
                occ_variants.append(int(occ))
                preferred_terms.append(preferred)

    dataframe = pd.DataFrame(
        {
            ThesaurusField.PREFERRED.value: preferred_terms,
            ThesaurusField.VARIANT.value: variants,
            ThesaurusField.OCC.value: occ_variants,
        }
    )

    dataframe = dataframe.sort_values(
        [
            ThesaurusField.OCC.value,
            ThesaurusField.PREFERRED.value,
            ThesaurusField.VARIANT.value,
        ],
        ascending=[False, True, True],
    ).reset_index(drop=True)

    return dataframe
