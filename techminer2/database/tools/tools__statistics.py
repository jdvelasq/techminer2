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
...     .with_source_field("author_keywords")
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
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
from ...internals.mixins import InputFunctionsMixin
from ..load.load__filtered_database import load__filtered_database


class Statistics(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        field = self.params.source_field

        records = load__filtered_database(
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
            database=self.params.database,
            record_years_range=self.params.record_years_range,
            record_citations_range=self.params.record_citations_range,
            records_order_by=self.params.records_order_by,
            records_match=self.params.records_match,
        )

        records = records.dropna(subset=[field])
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        summary = records.groupby(field).describe()

        return summary
