# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Statistics
===============================================================================


>>> from techminer2.database.tools import Statistics
>>> (
...     Statistics()
...     .set_analysis_params(
...         field="authors",
...     ).set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... ).head()
                    year                              ... test_num_authors                    
                   count    mean std     min     25%  ...              min  25%  50%  75%  max
authors                                               ...                                     
Almunawar M.N.       1.0  2019.0 NaN  2019.0  2019.0  ...              4.0  4.0  4.0  4.0  4.0
Alt R.               1.0  2018.0 NaN  2018.0  2018.0  ...              3.0  3.0  3.0  3.0  3.0
Anagnostopoulos I.   1.0  2018.0 NaN  2018.0  2018.0  ...              1.0  1.0  1.0  1.0  1.0
Anshari M.           1.0  2019.0 NaN  2019.0  2019.0  ...              4.0  4.0  4.0  4.0  4.0
Arner D.W.           1.0  2017.0 NaN  2017.0  2017.0  ...              3.0  3.0  3.0  3.0  3.0
<BLANKLINE>
[5 rows x 64 columns]


"""
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from ..load.load__filtered_database import load__filtered_database
from .internals.set_field_param_mixin import SetFieldParamMixin


class Statistics(
    SetFieldParamMixin,
    SetDatabaseFiltersMixin,
):
    """:meta private:"""

    def __init__(self):
        self.field = None
        self.database_params = DatabaseFilters()

    def build(self):

        field = self.field
        records = load__filtered_database(**self.database_params.__dict__)
        records = records.dropna(subset=[field])
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        summary = records.groupby(field).describe()

        return summary
