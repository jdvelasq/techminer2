# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _statistics:

Statistics
===============================================================================


>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> vantagepoint.calculate.statistics(
...     field='authors',
...     root_dir=root_dir,
... ).head()
                   year                       ... local_citations                  
                  count    mean  std     min  ...             25%   50%   75%   max
authors                                       ...                                  
Abdullah Y          1.0  2022.0  NaN  2022.0  ...             0.0   0.0   0.0   0.0
Ajmi JA             1.0  2021.0  NaN  2021.0  ...             1.0   1.0   1.0   1.0
Anagnostopoulos I   1.0  2018.0  NaN  2018.0  ...            17.0  17.0  17.0  17.0
Anasweh M           1.0  2020.0  NaN  2020.0  ...             4.0   4.0   4.0   4.0
Arman AA            2.0  2022.0  0.0  2022.0  ...             0.0   0.0   0.0   0.0
<BLANKLINE>
[5 rows x 56 columns]



"""
from .._read_records import read_records


def statistics(
    field,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Returns the statistics of the records."""

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records = records.dropna(subset=[field])
    records[field] = records[field].str.split("; ")
    records = records.explode(field)
    records[field] = records[field].str.strip()
    summary = records.groupby(field).describe()

    return summary
