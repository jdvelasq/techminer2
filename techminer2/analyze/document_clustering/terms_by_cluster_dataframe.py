# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Cluster Dataframe
===============================================================================

>>> from sklearn.cluster import KMeans
>>> from techminer2.analyze.document_clustering import terms_by_cluster_frame
>>> (
...     TermsByClusterDataFrame()
...     .set_analysis_params(
...         sklearn_estimator=KMeans(
...             n_clusters=4,
...             init="k-means++",
...             n_init=10,
...             max_iter=300,
...             tol=0.0001,
...             algorithm="lloyd",
...             random_state=0,
...         ),
...     #
...     ).set_output_params(
...         retain_counters=True,
...     #
...     .set_item_params(
...         field='descriptors',
...         top_n=50,
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
                                     0  ...                               3
0                   INNOVATION 08:0990  ...                 FINTECH 32:5393
1  FINANCIAL_SERVICES_INDUSTRY 06:1370  ...    FINANCIAL_TECHNOLOGY 18:2519
2              BUSINESS_MODELS 04:1441  ...      FINANCIAL_SERVICES 12:1929
3          INFORMATION_SYSTEMS 04:0830  ...                 FINANCE 11:1950
4                   BLOCKCHAIN 03:0881  ...      FINANCIAL_INDUSTRY 09:2006
5           FINTECH_REVOLUTION 03:0731  ...        FINTECH_STARTUPS 08:1913
6                      BANKING 03:0370  ...        FINANCIAL_SECTOR 07:1562
7                   STUDY_AIMS 03:0283  ...  INFORMATION_TECHNOLOGY 07:1383
8            ACADEMIC_RESEARCH 02:0691  ...           FRANCIS_GROUP 05:1227
9                CURRENT_STATE 02:0691  ...       FINTECH_COMPANIES 05:1072
<BLANKLINE>
[10 rows x 4 columns]


"""
import pandas as pd  # type: ignore

from .clusters_to_terms_mapping import clusters_to_terms_mapping


def terms_by_cluster_frame(
    #
    # TF PARAMS:
    field,
    retain_counters: bool = True,
    is_binary: bool = False,
    cooc_within: int = 1,
    #
    # FILTER PARAMS:
    top_n=20,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # ESIIMATOR:
    sklearn_estimator=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    sort_by=None,
    **filters,
):
    """:meta private:"""

    mapping = clusters_to_terms_mapping(
        #
        # TF PARAMS:
        field=field,
        retain_counters=retain_counters,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # FILTER PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # ESIIMATOR:
        sklearn_estimator=sklearn_estimator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )
    frame = pd.DataFrame.from_dict(mapping, orient="index").T
    frame = frame.fillna("")
    frame = frame.sort_index(axis=1)
    return frame
