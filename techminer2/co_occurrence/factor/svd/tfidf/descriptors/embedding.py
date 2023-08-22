# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Embedding
===============================================================================


>>> from techminer2.co_occurrence.factor.svd.tfidf.descriptors import embedding
>>> embedding(
...     #
...     # TF PARAMS:
...     is_binary=True,
...     cooc_within=1,
...     #
...     # TF-IDF parameters:
...     norm=None,
...     use_idf=False,
...     smooth_idf=False,
...     sublinear_tf=False,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # SVD PARAMS:
...     n_components=5,
...     algorithm="randomized",
...     n_iter=5,
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0,
...     tol=0.0,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                                  DIM_0     DIM_1     DIM_2     DIM_3     DIM_4
descriptors                                                                    
REGTECH 29:330                 4.840162 -1.504959 -0.647841 -0.717280  0.111734
REGULATORY_TECHNOLOGY 20:274   3.399170  1.717279  0.119110 -1.630514 -0.923145
FINANCIAL_INSTITUTIONS 16:198  2.315542 -0.660764  2.269319  1.720972  0.185582
REGULATORY_COMPLIANCE 15:232   2.891051 -0.841229 -1.221029  0.013479  0.815675
FINANCIAL_REGULATION 12:395    1.889480  1.848076  0.155380  1.544229  0.879284


"""
from typing import Literal

from ......factor_analysis import FactorAnalyzer

UNIT_OF_ANALYSIS = "descriptors"


def embedding(
    #
    # TF PARAMS:
    is_binary: bool = True,
    cooc_within: int = 1,
    #
    # TF-IDF parameters:
    norm: Literal["l1", "l2", None] = None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # SVD PARAMS:
    n_components=None,
    algorithm="randomized",
    n_iter=5,
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    tol=0.0,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """
    :meta private:
    """

    analyzer = FactorAnalyzer(field=UNIT_OF_ANALYSIS)

    analyzer.tfidf(
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
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    analyzer.svd(
        #
        # SVD PARAMS:
        n_components=n_components,
        algorithm=algorithm,
        n_iter=n_iter,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
    )

    analyzer.compute_embedding()

    return analyzer.embedding()
