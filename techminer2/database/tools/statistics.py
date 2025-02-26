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
...     #
...     .with_field("author_keywords")
...     #
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... ).head()
                      year                              ... local_citations                    
                     count    mean std     min     25%  ...             min  25%  50%  75%  max
author_keywords                                         ...                                    
ACTOR_NETWORK_THEORY   1.0  2016.0 NaN  2016.0  2016.0  ...             0.0  0.0  0.0  0.0  0.0
ACTUALIZATION          1.0  2019.0 NaN  2019.0  2019.0  ...             0.0  0.0  0.0  0.0  0.0
ADOPTION               1.0  2019.0 NaN  2019.0  2019.0  ...             0.0  0.0  0.0  0.0  0.0
AGRICULTURE            1.0  2019.0 NaN  2019.0  2019.0  ...             0.0  0.0  0.0  0.0  0.0
AGROPAY                1.0  2019.0 NaN  2019.0  2019.0  ...             0.0  0.0  0.0  0.0  0.0
<BLANKLINE>
[5 rows x 56 columns]

"""
from ..._internals.mixins import ParamsMixin
from .._internals.io import internal__load_filtered_database


class Statistics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        field = self.params.field

        records = internal__load_filtered_database(params=self.params)
        records = records.dropna(subset=[field])
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        summary = records.groupby(field).describe()

        return summary
