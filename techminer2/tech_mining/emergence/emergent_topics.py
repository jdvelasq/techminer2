# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Emergent Topics
===============================================================================


>>> from techminer2.tech_mining.emergence import emergent_topics
>>> emergent_topics(
...     #
...     # FUNCTION PARAMS:
...     field='descriptors',
...     #
...     # EMERGENCE:
...     baseline_periods=3,
...     recent_periods=3,
...     novelty_threshold=0.15,
...     total_records_threshold=7,
...     periods_with_at_least_one_record=3,
...     ratio_threshold=2.0,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head(5)
                        OCC  OCC_baseline  OCC_recent  nonzero_years  selected
descriptors                                                                   
AUTHOR                    9             2           8              4      True
DATA                      8             2           8              3      True
IMPACT                    7             2           7              3      True
INFORMATION_TECHNOLOGY    7             2           6              4      True
PURPOSE                   7             2           6              4      True

"""

from ...metrics._compute_trend_metrics import compute_trend_metrics
from ...metrics.globals import items_occurrences_by_year


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
    ratio_threshold=2.0,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    occurrences_by_year = items_occurrences_by_year(
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
    data_frame["OCC_baseline"] = occurrences_by_year.iloc[:, :baseline_periods].sum(
        axis=1
    )
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

    # Threshold: The term  appear in 15% or less of the base period records
    data_frame["selected"] = data_frame["selected"] & (
        data_frame["OCC_baseline"] / records_by_base_period <= novelty_threshold
    )

    # Threshold: The term appears in at least 'total_records_threshold' records
    data_frame["selected"] = data_frame["selected"] & (
        data_frame["OCC"] >= total_records_threshold
    )

    # Threshold: The term appears in at leat 'periods_with_at_least_one_record' periods
    data_frame["selected"] = data_frame["selected"] & (
        data_frame["nonzero_years"] >= periods_with_at_least_one_record
    )

    # Threshold: The ratio of records containing the term in the active period to
    # those in the base period must be at least 'ratio_threshold':1
    data_frame["selected"] = data_frame["selected"] & (
        data_frame["OCC_recent"] / data_frame["OCC_baseline"] >= ratio_threshold
    )

    return data_frame[data_frame.selected]
