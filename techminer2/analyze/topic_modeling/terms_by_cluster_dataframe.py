# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Cluster Frame
===============================================================================


>>> from techminer2.analyze.topic_modeling import terms_by_cluster_frame
>>> from sklearn.decomposition import LatentDirichletAllocation
>>> (
...     TermsByClusterDataFrame()
...     .set_analysis_params(
...         sklearn_estimator=LatentDirichletAllocation(
...             n_components=10,
...             learning_decay=0.7,
...             learning_offset=50.0,
...             max_iter=10,
...             batch_size=128,
...             evaluate_every=-1,
...             perp_tol=0.1,
...             mean_change_tol=0.001,
...             max_doc_update_iter=100,
...             random_state=0,
...         ),
...     #
...     ).set_tf_params(
...         is_binary=True,
...         cooc_within=3,
...     #
...     ).set_tfidf_params(
...         norm=None,
...         use_idf=False,
...         smooth_idf=False,
...         sublinear_tf=False,
...     #
...     .set_item_params(
...         field="author_keywords",
...         top_n=None,
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
... ).head()
cluster                                    0  ...                            9
term                                          ...                             
0                            FINTECH 31:5168  ...              FINTECH 31:5168
1                 FINANCIAL_SERVICES 04:0667  ...           INNOVATION 07:0911
2               FINANCIAL_TECHNOLOGY 03:0461  ...  FINANCIAL_INCLUSION 03:0590
3                         INNOVATION 07:0911  ...       MOBILE_PAYMENT 02:0184
4        SERVICE_INNOVATION_STRATEGY 01:0079  ...           CASE_STUDY 02:0340
<BLANKLINE>
[5 rows x 10 columns]



"""
import pandas as pd  # type: ignore

from .cluster_to_terms_mapping import cluster_to_terms_mapping


def terms_by_cluster_frame(
    field,
    #
    # TF PARAMS:
    is_binary: bool = True,
    cooc_within: int = 1,
    #
    # TF-IDF parameters:
    norm=None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
    #
    # TERM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # ESTIMATOR:
    sklearn_estimator=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    mapping = cluster_to_terms_mapping(
        field=field,
        #
        # TF PARAMS:
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # TF-IDF parameters:
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        #
        # TOP TERMS:
        n_top_terms=None,
        #
        # TERM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # ESTIMATOR:
        sklearn_estimator=sklearn_estimator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    frame = pd.DataFrame.from_dict(mapping, orient="index").T
    frame = frame.fillna("")
    frame = frame.sort_index(axis=1)
    frame.columns.name = "cluster"
    frame.index.name = "term"
    return frame
