# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Components by Term Frame
===============================================================================


>>> from techminer2.topic_modeling import components_by_term_frame
>>> from sklearn.decomposition import LatentDirichletAllocation
>>> components_by_term_frame(
...     field="author_keywords",
...     #
...     # TF PARAMS:
...     is_binary=True,
...     cooc_within=2,
...     #
...     # TF-IDF PARAMS:
...     norm=None,
...     use_idf=False,
...     smooth_idf=False,
...     sublinear_tf=False,
...     #
...     # TOP TERMS:
...     n_top_terms=5,
...     #
...     # ITEM FILTERS:
...     top_n=None,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # ESTIMATOR:
...     sklearn_estimator=LatentDirichletAllocation(
...         n_components=10,
...         learning_decay=0.7,
...         learning_offset=50.0,
...         max_iter=10,
...         batch_size=128,
...         evaluate_every=-1,
...         perp_tol=0.1,
...         mean_change_tol=0.001,
...         max_doc_update_iter=100,
...         random_state=0,
...     ),
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
term       FINTECH 31:5168  ...  TRADING 01:0064
component                   ...                 
0                10.099987  ...              0.1
1                 4.100046  ...              0.1
2                 3.100012  ...              1.1
3                 4.100041  ...              0.1
4                 0.100000  ...              0.1
5                 1.099938  ...              0.1
6                 2.100033  ...              0.1
7                 0.100000  ...              0.1
8                 3.099955  ...              0.1
9                 4.099988  ...              0.1
<BLANKLINE>
[10 rows x 148 columns]



"""
import pandas as pd  #  type: ignore

from ..metrics import tfidf


def components_by_term_frame(
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
    # TOP TERMS:
    n_top_terms=5,
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

    tf_matrix = tfidf(
        #
        # TF PARAMS:
        field=field,
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
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    sklearn_estimator.fit(tf_matrix)

    frame = pd.DataFrame(
        sklearn_estimator.components_,
        index=range(sklearn_estimator.n_components),
        columns=tf_matrix.columns,
    )

    frame.columns.name = "term"
    frame.index.name = "component"

    return frame
