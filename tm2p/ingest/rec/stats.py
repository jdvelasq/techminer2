"""
Statistics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.rec import Statistics
    >>> df = (
    ...     Statistics()
    ...     .with_source_field(Field.AUTHKW_RAW)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )
    >>> assert df.shape[0] > 0
    >>> df.head() # doctest: +SKIP
                                             CONF_CODE            ...    YEAR
                                                 count      mean  ...     75%     max
    AUTHKW_RAW                                                    ...
    1-bit quantization                             0.0       NaN  ...  2025.0  2025.0
    130-nm process design kit (pdk)                0.0       NaN  ...  2023.0  2023.0
    1d cnn                                         0.0       NaN  ...  2024.0  2024.0
    1d convolutional neural network                1.0  214104.0  ...  2025.0  2025.0
    1d convolutional neural network (1d-cnn)       1.0  212711.0  ...  2025.0  2025.0
    <BLANKLINE>
    [5 rows x 104 columns]



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip


class Statistics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        field = self.params.source_field.value

        records = load_filtered_main_csv_zip(params=self.params)
        records = records.dropna(subset=[field])
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        summary = records.groupby(field).describe()

        return summary


#
