"""

Smoke tests:
    >>> from techminer2._internals import Params
    >>> from techminer2.database._internals.io import internal__load_all_records_from_database
    >>> df = internal__load_all_records_from_database(
    ...         Params(root_directory="examples/fintech/")
    ... ).head()
    >>> df # doctest: +SKIP
                        source_title_abbr  ...  year
    0             Int. J. Appl. Eng. Res.  ...  2016
    1                   Telecommun Policy  ...  2016
    2                 Comput. Hum. Behav.  ...  2016
    3                      China Econ. J.  ...  2016
    4  Contemp. Stud. Econ. Financ. Anal.  ...  2016
    <BLANKLINE>
    [5 rows x 80 columns]



"""

import pandas as pd  # type: ignore

from techminer2._internals.data_access.get_main_data_path import get_main_data_path


def load_all_records_from_database(params):
    """:meta private:"""

    file_path = get_main_data_path(params)
    records = pd.read_csv(
        file_path,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    columns = sorted(records.columns)
    records = records[columns]

    return records


# =============================================================================
