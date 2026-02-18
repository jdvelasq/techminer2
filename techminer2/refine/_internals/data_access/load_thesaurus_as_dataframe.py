"""
Smoke test:
    >>> from techminer2.refine._internals.data_access import load_thesaurus_as_dataframe
    >>> load_thesaurus_as_dataframe(params=Params(
    ...         root_directory="examples/fintech-with-references/",
    ...         thesaurus_file="descriptors.the.txt",
    ...     )
    ... ).head()
                   PREFERRED_TERM                     VARIANT
    0        a business ecozystem        a business ecozystem
    1                a case study                a case study
    2  a case study investigation  a case study investigation
    3          a cashless society          a cashless society
    4                 a challenge                 a challenge



"""

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

    mapping: dict[str, list[str]] = {}
    preferred = None

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:

            line = line.replace("\t", INDENT)

            if not line.startswith(" "):
                preferred = line.strip()
                mapping[preferred] = []
            else:
                if preferred is None:
                    raise ValueError(
                        "The thesaurus file is not well formatted. The first line must be a preferred term."
                    )
                mapping[preferred].append(line.strip())

    keys = sorted(mapping.keys())

    dataframe = pd.DataFrame(
        {
            ThesaurusField.PREFERRED.value: keys,
            ThesaurusField.VARIANT.value: [
                "; ".join(sorted(mapping[key])) for key in keys
            ],
        }
    )

    return dataframe
