"""
Smoke test:
    >>> from tm2p.refine._intern.data_access import load_thesaurus_as_dataframe
    >>> load_thesaurus_as_dataframe(params=Params(
    ...         root_directory="examples/fintech-with-references/",
    ...         thesaurus_file="concepts.the.txt",
    ...     )
    ... ).head()
                   PREFERRED_TERM                     VARIANT
    0        a business ecozystem        a business ecozystem
    1                a case study                a case study
    2  a case study investigation  a case study investigation
    3          a cashless society          a cashless society
    4                 a challenge                 a challenge



"""

import pandas as pd  # type: ignore

from tm2p import ThField
from tm2p._intern import Params

from .get_thesaurus_path import get_thesaurus_path

INDENT = " " * 4


def load_thesaurus_as_dataframe(
    params: Params,
) -> pd.DataFrame:

    filepath = get_thesaurus_path(
        root_directory=params.root_directory,
        file=params.thesaurus_file,
    )

    records = []
    preferred = None
    values: list[str] = []

    with open(filepath, "r", encoding="utf-8") as file:

        for line in file:

            line = line.replace("\t", INDENT)

            if not line.startswith(" "):
                if preferred:
                    records.append(
                        {
                            ThField.PREFERRED.value: preferred,
                            ThField.VARIANT.value: "; ".join(values),
                        }
                    )
                preferred = line.strip()
                values = []
            else:
                if preferred is None:
                    raise ValueError(
                        "The thesaurus file is not well formatted. The first line must be a preferred term."
                    )
                values.append(line.strip())

    if preferred is not None and values:
        records.append(
            {
                ThField.PREFERRED.value: preferred,
                ThField.VARIANT.value: "; ".join(values),
            }
        )

    df = pd.DataFrame(records)

    return df
