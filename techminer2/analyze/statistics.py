# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _performance_analysis.statistics:

Statistics
===============================================================================


>>> from techminer2.analyze import statistics
>>> statistics(
...     field='authors',
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                    year                              ... countries_from_affiliations                
                   count    mean std     min     25%  ...                         min 25% 50% 75% max
authors                                               ...                                            
Almunawar M.N.       1.0  2019.0 NaN  2019.0  2019.0  ...                         NaN NaN NaN NaN NaN
Alt R.               1.0  2018.0 NaN  2018.0  2018.0  ...                         NaN NaN NaN NaN NaN
Anagnostopoulos I.   1.0  2018.0 NaN  2018.0  2018.0  ...                         NaN NaN NaN NaN NaN
Anshari M.           1.0  2019.0 NaN  2019.0  2019.0  ...                         NaN NaN NaN NaN NaN
Arner D.W.           1.0  2017.0 NaN  2017.0  2017.0  ...                         NaN NaN NaN NaN NaN
<BLANKLINE>
[5 rows x 80 columns]


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
    """Returns the statistics of the records.

    :meta private:
    """

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
