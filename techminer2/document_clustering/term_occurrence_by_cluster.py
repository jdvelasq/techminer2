# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Term Occurrence by Cluster
===============================================================================

## >>> from sklearn.cluster import KMeans
## >>> from techminer2.document_clustering import term_occurrence_by_cluster
## >>> term_occurrence_by_cluster(
## ...     #
## ...     # TERMS:
## ...     field='descriptors',
## ...     retain_counters=True,
## ...     #
## ...     # FILTER PARAMS:
## ...     top_n=50,
## ...     occ_range=(None, None),
## ...     gc_range=(None, None),
## ...     custom_terms=None,
## ...     #
## ...     # ESTIMATOR:
## ...     sklearn_estimator=KMeans(
## ...         n_clusters=8,
## ...         init="k-means++",
## ...         n_init=10,
## ...         max_iter=300,
## ...         tol=0.0001,
## ...         algorithm="lloyd",
## ...         random_state=0,
## ...     ),
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ...     sort_by=None,
## ... ).head(20)
cluster                              0   1  2  3  4  5  6  7
descriptors                                                 
FINTECH 32:5393                      3  21  0  1  0  2  5  0
FINANCIAL_TECHNOLOGY 18:2519         5   6  1  1  4  0  1  0
FINANCIAL_SERVICES 12:1929           0   3  1  1  4  0  2  1
FINANCE 11:1950                      5   0  1  0  0  2  2  1
FINANCIAL_INDUSTRY 09:2006           0   2  0  0  2  2  3  0
FINTECH_STARTUPS 08:1913             0   3  1  0  0  0  3  1
INNOVATION 08:0990                   0   2  0  0  2  0  4  0
FINANCIAL_SECTOR 07:1562             2   2  0  0  3  0  0  0
INFORMATION_TECHNOLOGY 07:1383       1   2  0  0  2  0  2  0
FINANCIAL_SERVICES_INDUSTRY 06:1370  0   2  0  1  2  0  0  1
FRANCIS_GROUP 05:1227                0   2  1  0  1  0  0  1
FINTECH_COMPANIES 05:1072            0   5  0  0  0  0  0  0
FINANCIAL_INNOVATION 05:0401         0   2  0  0  2  0  1  0
BUSINESS_MODELS 04:1441              0   0  0  1  0  0  2  1
FINANCIAL_SERVICE 04:1036            0   0  1  0  0  1  1  1
INFORMATION_SYSTEMS 04:0830          0   3  0  0  0  0  1  0
FINANCIAL_INSTITUTIONS 04:0722       1   2  0  1  0  0  0  0
FINANCIAL_SYSTEM 04:0688             0   1  0  1  2  0  0  0
ARTIFICIAL_INTELLIGENCE 04:0495      1   1  0  0  2  0  0  0
FINTECH_SERVICES 04:0468             1   1  0  0  2  0  0  0

"""
from ..metrics import tfidf_frame


def term_occurrence_by_cluster(
    #
    # TF PARAMS:
    field,
    retain_counters=True,
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

    tf_matrix = tfidf_frame(
        #
        # TF PARAMS:
        field=field,
        retain_counters=retain_counters,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # TF-IDF parameters:
        norm=None,
        use_idf=False,
        smooth_idf=False,
        sublinear_tf=False,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    sklearn_estimator.fit(tf_matrix)

    #
    # Assigns the cluster to the record
    tf_matrix["cluster"] = list(sklearn_estimator.labels_)
    data_frame = tf_matrix.groupby("cluster").sum()
    data_frame = data_frame.T

    return data_frame
