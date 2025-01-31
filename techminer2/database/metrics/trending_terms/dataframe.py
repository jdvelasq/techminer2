# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Dataframe
===============================================================================


# >>> from techminer2.visualize.specialized_plots.trending_words import dataframe
# >>> dataframe(
# ...     #
# ...     # ITEMS PARAMS:
# ...     field='author_keywords',
# ...     #
# ...     # TREND ANALYSIS:
# ...     time_window=2,
# ...     #
# ...     # ITEM FILTERS:
# ...     top_n=20,
# ...     occ_range=(None, None),
# ...     gc_range=(None, None),
# ...     custom_terms=None,
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(None, None),
# ...     cited_by_filter=(None, None),
# ... ).head()
                      rank_occ  OCC  ...  average_growth_rate  average_docs_per_year
author_keywords                      ...                                            
FINTECH                      1   31  ...                 -1.0                    9.0
INNOVATION                   2    7  ...                 -1.5                    0.5
FINANCIAL_SERVICES           3    4  ...                  0.0                    1.5
FINANCIAL_INCLUSION          4    3  ...                 -1.0                    0.0
FINANCIAL_TECHNOLOGY         5    3  ...                  0.0                    1.0
<BLANKLINE>
[5 rows x 7 columns]


"""
from ..growth.data_frame import growth_metrics_frame


def dataframe(
    #
    # ITEM PARAMS:
    field,
    #
    # TREND ANALYSIS:
    time_window=2,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    #
    # Extracs only the performance metrics data frame
    data_frame = growth_metrics_frame(
        #
        # ITEMS PARAMS:
        field=field,
        time_window=time_window,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return data_frame
