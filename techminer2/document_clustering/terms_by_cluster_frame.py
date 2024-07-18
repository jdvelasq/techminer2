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
>>> from techminer2.document_clustering import terms_by_cluster_frame
>>> terms_by_cluster_frame(
...     #
...     # TERMS:
...     field='descriptors',
...     retain_counters=True,
...     #
...     # FILTER PARAMS:
...     top_n=50,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # ESTIMATOR:
...     sklearn_estimator=KMeans(
...         n_clusters=4,
...         init="k-means++",
...         n_init=10,
...         max_iter=300,
...         tol=0.0001,
...         algorithm="lloyd",
...         random_state=0,
...     ),
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
...     sort_by=None,
... ).head(10)
                               0  ...                                3
0     FINANCIAL_INDUSTRY 09:2006  ...  SUSTAINABLE_DEVELOPMENT 04:0306
1        BUSINESS_MODELS 04:1441  ...             ELSEVIER_LTD 03:0474
2    INFORMATION_SYSTEMS 04:0830  ...           SUSTAINABILITY 03:0227
3                SURVEYS 03:0484  ...                                 
4           CROWDFUNDING 03:0335  ...                                 
5             STUDY_AIMS 03:0283  ...                                 
6       NEW_TECHNOLOGIES 02:0773  ...                                 
7  DISRUPTIVE_INNOVATION 02:0759  ...                                 
8      ACADEMIC_RESEARCH 02:0691  ...                                 
9          CURRENT_STATE 02:0691  ...                                 
<BLANKLINE>
[10 rows x 4 columns]


"""
import pandas as pd

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
    custom_items=None,
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
        custom_items=custom_items,
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
