# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Statistics
===============================================================================


Example:
    >>> from techminer2.database.tools import Statistics

    >>> (
    ...     Statistics()
    ...     #
    ...     .with_field("raw_author_keywords")
    ...     #
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     #
    ...     .run()
    ... ).head() # doctest: +NORMALIZE_WHITESPACE
                         conference_code                ...    year
                                   count      mean std  ...     50%     75%     max
    raw_author_keywords                                 ...
    ACTOR_NETWORK_THEORY             0.0       NaN NaN  ...  2016.0  2016.0  2016.0
    ACTUALIZATION                    0.0       NaN NaN  ...  2019.0  2019.0  2019.0
    ADOPTION                         0.0       NaN NaN  ...  2019.0  2019.0  2019.0
    AGRICULTURE                      1.0  144694.0 NaN  ...  2019.0  2019.0  2019.0
    AGROPAY                          1.0  144694.0 NaN  ...  2019.0  2019.0  2019.0
    <BLANKLINE>
    [5 rows x 96 columns]



"""
from ..._internals.mixins import ParamsMixin
from .._internals.io import internal__load_filtered_records_from_database


class Statistics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        field = self.params.field

        records = internal__load_filtered_records_from_database(params=self.params)
        records = records.dropna(subset=[field])
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        summary = records.groupby(field).describe()

        return summary
