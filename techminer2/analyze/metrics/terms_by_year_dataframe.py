# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Year Frame
===============================================================================

>>> from techminer2.analyze.metrics import terms_by_year_frame
>>> terms_by_year_frame(

...     cumulative=False,
...     metric='OCC',
...     #
...     # FILTER PARAMS:
...     .set_item_params(
...         field="author_keywords",
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... ).head(10)
year                          2015  2016  2017  2018  2019
author_keywords                                           
FINTECH 31:5168                  0     5     8    12     6
INNOVATION 07:0911               0     3     3     1     0
FINANCIAL_SERVICES 04:0667       0     1     0     3     0
FINANCIAL_INCLUSION 03:0590      0     1     2     0     0
FINANCIAL_TECHNOLOGY 03:0461     0     0     1     1     1
CROWDFUNDING 03:0335             0     0     1     1     1
MARKETPLACE_LENDING 03:0317      0     0     0     2     1
BUSINESS_MODELS 02:0759          0     0     0     2     0
CYBER_SECURITY 02:0342           0     0     0     2     0
CASE_STUDY 02:0340               0     0     1     0     1



>>> from techminer2.analyze.metrics import terms_by_year_frame
>>> terms_by_year_frame(
...     field="author_keywords",
...     cumulative=True,
...     #
...     # FILTER PARAMS:
...     metric='OCC',
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head(10)
year                          2015  2016  2017  2018  2019
author_keywords                                           
FINTECH 31:5168                  0     5    13    25    31
INNOVATION 07:0911               0     3     6     7     7
FINANCIAL_SERVICES 04:0667       0     1     1     4     4
FINANCIAL_INCLUSION 03:0590      0     1     3     3     3
FINANCIAL_TECHNOLOGY 03:0461     0     0     1     2     3
CROWDFUNDING 03:0335             0     0     1     2     3
MARKETPLACE_LENDING 03:0317      0     0     0     2     3
BUSINESS_MODELS 02:0759          0     0     0     2     2
CYBER_SECURITY 02:0342           0     0     0     2     2
CASE_STUDY 02:0340               0     0     1     1     2



"""
from ...internals.mt.mt_calculate_global_performance_metrics import (
    _mt_calculate_global_performance_metrics,
)
from ...internals.mt.mt_extract_top_n_terms_by_metric import (
    _mt_extract_top_n_terms_by_metric,
)
from ...internals.mt.mt_term_occurrences_by_year import _mt_term_occurrences_by_year
from ...internals.utils.utils_append_occurrences_and_citations_to_axis import (
    _utils_append_occurrences_and_citations_to_axis,
)


def terms_by_year_frame(
    field,
    cumulative,
    #
    # FILTER PARAMS:
    metric="OCC",
    top_n=20,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """:meta private:"""

    data_frame = _mt_term_occurrences_by_year(
        field=field,
        cumulative=cumulative,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if custom_terms is None:
        indicators = _mt_calculate_global_performance_metrics(
            field=field,
            #
            # DATABASE PARAMS
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        custom_terms = _mt_extract_top_n_terms_by_metric(
            indicators,
            metric=metric,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    data_frame = data_frame[data_frame.index.isin(custom_terms)]
    data_frame = data_frame.loc[custom_terms, :]
    data_frame = _utils_append_occurrences_and_citations_to_axis(
        data_frame,
        axis=0,
        field=field,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return data_frame
