# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Emergent Topics
===============================================================================


## >>> from techminer2.emergence import emergent_topics
## >>> emergent_topics(
## ...     #
## ...     # FUNCTION PARAMS:
## ...     field='descriptors',
## ...     #
## ...     # EMERGENCE:
## ...     baseline_periods=3,
## ...     recent_periods=3,
## ...     novelty_threshold=0.15,
## ...     total_records_threshold=7,
## ...     periods_with_at_least_one_record=3,
## ...     ratio_threshold=0.5,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... ).head()
                        OCC  OCC_baseline  ...  growth_rate  growth_rate_ratio
descriptors                                ...                                
FINTECH_STARTUPS          8             1  ...   182.842712           1.540766
INFORMATION_TECHNOLOGY    7             2  ...    91.293118           0.769302
<BLANKLINE>
[2 rows x 10 columns]




"""
import numpy as np

from .._core.metrics.term_occurrences_by_year import term_occurrences_by_year
from ..metrics._compute_trend_metrics import compute_trend_metrics
from ..metrics.general_metrics_frame import general_metrics_frame


def emergent_topics(
    #
    # PARAMS:
    field,
    #
    # EMERGENCE:
    baseline_periods=3,
    recent_periods=3,
    novelty_threshold=0.15,
    total_records_threshold=7,
    periods_with_at_least_one_record=3,
    ratio_threshold=1.0,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    occurrences_by_year = term_occurrences_by_year(
        field=field,
        cumulative=False,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Compute base indicators
    data_frame = occurrences_by_year.sum(axis=1).to_frame()
    data_frame.columns = ["OCC"]
    data_frame["OCC_baseline"] = occurrences_by_year.iloc[:, :baseline_periods].sum(axis=1)
    data_frame["OCC_recent"] = occurrences_by_year.iloc[:, -recent_periods:].sum(axis=1)
    data_frame["nonzero_years"] = (occurrences_by_year > 0).sum(axis=1)

    records_by_base_period = (
        compute_trend_metrics(
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        .OCC[:baseline_periods]
        .sum()
    )

    data_frame["selected"] = True

    #
    # Threshold: The term  appear in 15% or less of the base period records
    #
    data_frame["selected"] = data_frame["selected"] & (data_frame["OCC_baseline"] / records_by_base_period <= novelty_threshold)

    #
    # Threshold: The term appears in at least 'total_records_threshold' records
    #
    data_frame["selected"] = data_frame["selected"] & (data_frame["OCC"] >= total_records_threshold)

    #
    # Threshold: The term appears in at leat 'periods_with_at_least_one_record' periods
    #
    data_frame["selected"] = data_frame["selected"] & (data_frame["nonzero_years"] >= periods_with_at_least_one_record)

    #
    # Threshold: The growth reate of the terms must be 'ratio_threshold' times
    # of the growth rate of the dataset
    #

    cum_occurrences_by_year = term_occurrences_by_year(
        field=field,
        cumulative=True,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    n_columns = cum_occurrences_by_year.columns.max()

    data_frame["po"] = cum_occurrences_by_year.where(cum_occurrences_by_year > 0, np.inf).min(axis=1)

    data_frame["pf"] = cum_occurrences_by_year.max(axis=1)

    data_frame["np"] = n_columns - cum_occurrences_by_year.where(cum_occurrences_by_year > 0, np.inf).idxmin(axis=1)

    data_frame["growth_rate"] = 100.0 * (
        np.power(
            data_frame["pf"].astype(float) / data_frame["po"].astype(float),
            1.0 / data_frame["np"].astype(float),
        )
        - 1
    )

    global_growth_rate = general_metrics_frame(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).loc[("GENERAL", "Annual growth rate %"), "Value"]

    data_frame["growth_rate_ratio"] = data_frame["growth_rate"].map(lambda x: x / global_growth_rate)

    data_frame["selected"] = data_frame["selected"] & (data_frame["growth_rate_ratio"] >= ratio_threshold)

    # n_years = max(self.records.year) - min(self.records.year) + 1
    # po_ = len(self.records.year[self.records.year == min(self.records.year)])
    # return round(100 * (np.power(self.n_records / po_, 1 / n_years) - 1), 2)

    #
    # NOTE: Used in the first versions of the package
    # Threshold: The ratio of records containing the term in the active period to
    # those in the base period must be at least 'ratio_threshold':1
    #
    # data_frame["selected"] = data_frame["selected"] & (
    #     data_frame["OCC_recent"] / data_frame["OCC_baseline"] >= ratio_threshold
    # )

    return data_frame[data_frame.selected]
