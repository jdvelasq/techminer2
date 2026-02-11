# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Statistics
===============================================================================


Smoke tests:
    >>> from techminer2.database.tools import Statistics
    >>> df = (
    ...     Statistics()
    ...     #
    ...     .with_field("author_keywords_raw")
    ...     #
    ...     .where_root_directory("examples/small/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> df.head() # doctest: +SKIP
                         conference_code                ...    year
                                   count      mean std  ...     50%     75%     max
    author_keywords_raw                                 ...
    ACTOR_NETWORK_THEORY             0.0       NaN NaN  ...  2016.0  2016.0  2016.0
    ACTUALIZATION                    0.0       NaN NaN  ...  2019.0  2019.0  2019.0
    ADOPTION                         0.0       NaN NaN  ...  2019.0  2019.0  2019.0
    AGRICULTURE                      1.0  144694.0 NaN  ...  2019.0  2019.0  2019.0
    AGROPAY                          1.0  144694.0 NaN  ...  2019.0  2019.0  2019.0
    <BLANKLINE>
    [5 rows x 88 columns]



"""
from techminer2._internals import ParamsMixin
from techminer2._internals.data_access import load_filtered_main_data


class Statistics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        field = self.params.field

        records = load_filtered_main_data(params=self.params)
        records = records.dropna(subset=[field])
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        summary = records.groupby(field).describe()

        return summary


#
