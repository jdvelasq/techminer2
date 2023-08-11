# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Map 2D
===============================================================================


>>> from techminer2.co_occurrence.factor.svd.tfidf.abstract_nlp_phrases import map_2d
>>> map_2d(
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
...     # MAP:
...     dim_x="DIM_0",
...     dim_y="DIM_1",
...     node_color="#465c6b",
...     node_size=10,
...     textfont_size=8,
...     textfont_color="#465c6b",
...     xaxes_range=None,
...     yaxes_range=None,
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
... ).write_html("sphinx/_static/co_occurrence/factor/svd/tfidf/abstract_nlp_phrases/map_2d.html")

.. raw:: html

    <iframe src="../../../../../../_static/co_occurrence/factor/svd/tfidf/abstract_nlp_phrases/map_2d.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from typing import Literal

from ......factor_analysis import FactorAnalyzer

UNIT_OF_ANALYSIS = "abstract_nlp_phrases"


def map_2d(
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
    # MAP:
    dim_x="DIM_0",
    dim_y="DIM_1",
    node_color="#465c6b",
    node_size=10,
    textfont_size=8,
    textfont_color="#465c6b",
    xaxes_range=None,
    yaxes_range=None,
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

    return analyzer.embedding_2d_chart(
        dim_x=dim_x,
        dim_y=dim_y,
        node_color=node_color,
        node_size=node_size,
        textfont_size=textfont_size,
        textfont_color=textfont_color,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )
