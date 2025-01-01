# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Statistics
===============================================================================


## >>> from techminer2.prepare.database import Statistics
## >>> (
## ...     Statistics()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build(field="authors")
## ... ).head()
                    year                              ... local_citations                    
                   count    mean std     min     25%  ...             min  25%  50%  75%  max
authors                                               ...                                    
Almunawar M.N.       1.0  2019.0 NaN  2019.0  2019.0  ...             0.0  0.0  0.0  0.0  0.0
Alt R.               1.0  2018.0 NaN  2018.0  2018.0  ...             1.0  1.0  1.0  1.0  1.0
Anagnostopoulos I.   1.0  2018.0 NaN  2018.0  2018.0  ...             1.0  1.0  1.0  1.0  1.0
Anshari M.           1.0  2019.0 NaN  2019.0  2019.0  ...             0.0  0.0  0.0  0.0  0.0
Arner D.W.           1.0  2017.0 NaN  2017.0  2017.0  ...             1.0  1.0  1.0  1.0  1.0
<BLANKLINE>
[5 rows x 56 columns]



"""
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.read_filtered_database import read_filtered_database


class Statistics(
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.database_params = DatabaseParams()

    def build(self, field):

        records = read_filtered_database(**self.database_params.__dict__)
        records = records.dropna(subset=[field])
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        summary = records.groupby(field).describe()

        return summary
