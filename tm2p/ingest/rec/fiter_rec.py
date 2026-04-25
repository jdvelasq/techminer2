"""
RecordsDataFrame
=======================================================================================

Smoke tests:
    >>> from tm2p.enum import RecordOrderBy
    >>> from tm2p.ingest.rec import FilteredRecords
    >>> df = (
    ...     FilteredRecords()
    ...     #
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     .run()
    ... )
    >>> assert df.shape[0] > 0
    >>> df.head()  # doctest: +SKIP
                                               TITLE_RAW  ...  YEAR
    0  Tiny Machine Learning and On-Device Inference:...  ...  2025
    1  A Comprehensive Survey on Tiny Machine Learnin...  ...  2025
    2  Non-invasive blood glucose monitoring using PP...  ...  2025
    3  Safeguarding IoT consumer devices: Deep learni...  ...  2025
    4  Efficient human activity recognition on edge d...  ...  2025
    <BLANKLINE>
    [5 rows x 9 columns]


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field, UnitOrderBy

AUTH_RAW = Field.AUTH_RAW.value
GCS = Field.GCS.value
LCS = Field.LCS.value
DOCTYPE = Field.DOCTYPE.value
RID = Field.REC_ID.value
TITLE_RAW = Field.TITLE_RAW.value
YEAR = Field.YEAR.value

GCS_PER_YEAR = UnitOrderBy.GCS_PER_YEAR.value
LCS_PER_YEAR = UnitOrderBy.LCS_PER_YEAR.value
RANK_GCS = "RANK_GCS"
RANK_LCS = "RANK_LCS"


class FilteredRecords(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = load_filtered_main_csv_zip(params=self.params)
        df = df.assign(_order_=range(1, len(df) + 1))
        df = df.reset_index(drop=True)

        max_year = df[YEAR].dropna().max()

        df[GCS] = df[GCS].astype(int)
        df[GCS_PER_YEAR] = df[GCS].astype(float) / (max_year - df[YEAR] + 1)
        df[GCS_PER_YEAR] = df[GCS_PER_YEAR].round(3)

        df = df.sort_values(
            [GCS, LCS, YEAR, AUTH_RAW],
            ascending=[False, False, True, True],
        )
        df[RANK_GCS] = range(1, len(df) + 1)

        df = df.sort_values(
            [LCS, GCS, YEAR, AUTH_RAW],
            ascending=[False, False, True, True],
        )
        df[RANK_LCS] = range(1, len(df) + 1)

        df[LCS] = df[LCS].astype(int)
        df[LCS_PER_YEAR] = df[LCS].astype(float) / (max_year - df[YEAR] + 1)
        df[LCS_PER_YEAR] = df[LCS_PER_YEAR].round(3)

        #
        # Order
        df = df.sort_values("_order_", ascending=True)
        df = df[
            [
                TITLE_RAW,
                AUTH_RAW,
                RID,
                DOCTYPE,
                RANK_GCS,
                GCS,
                RANK_LCS,
                LCS,
                YEAR,
            ]
        ]

        return df


#
