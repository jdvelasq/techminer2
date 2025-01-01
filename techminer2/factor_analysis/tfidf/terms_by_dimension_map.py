# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Dimensions Map
===============================================================================

## >>> from sklearn.decomposition import PCA
## >>> from techminer2.factor_analysis.tfidf import terms_by_dimension_map
## >>> plot = terms_by_dimension_map(
## ...     #
## ...     # PARAMS:
## ...     field="author_keywords",
## ...     #
## ...     # TF PARAMS:
## ...     is_binary=True,
## ...     cooc_within=1,
## ...     #
## ...     # TF-IDF PARAMS:
## ...     norm=None,
## ...     use_idf=False,
## ...     smooth_idf=False,
## ...     sublinear_tf=False,
## ...     #
## ...     # TERM PARAMS:
## ...     top_n=20,
## ...     occ_range=(None, None),
## ...     gc_range=(None, None),
## ...     custom_terms=None,
## ...     #
## ...     # DESOMPOSITION PARAMS:
## ...     decomposition_estimator = PCA(
## ...         n_components=5,
## ...         whiten=False,
## ...         svd_solver="auto",
## ...         tol=0.0,
## ...         iterated_power="auto",
## ...         n_oversamples=10,
## ...         power_iteration_normalizer="auto",
## ...         random_state=0, 
## ...     ),
## ...     #
## ...     # MAP PARAMS:
## ...     dim_x=0,
## ...     dim_y=1,
## ...     node_color="#465c6b",
## ...     node_size=10,
## ...     textfont_size=8,
## ...     textfont_color="#465c6b",
## ...     xaxes_range=None,
## ...     yaxes_range=None,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # plot.write_html("sphinx/_static/factor_analysis/tfidf/terms_by_dimension_map.html")

.. raw:: html

    <iframe src="../../_static/factor_analysis/tfidf/terms_by_dimension_map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from .._core.manifold_2d_map import manifold_2d_map
from .terms_by_dimension_frame import terms_by_dimension_frame


def terms_by_dimension_map(
    #
    # PARAMS:
    field,
    #
    # TF PARAMS:
    is_binary: bool = True,
    cooc_within: int = 1,
    #
    # TERM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # TF-IDF parameters:
    norm=None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
    #
    # DECOMPOSITION:
    decomposition_estimator=None,
    #
    # MAP PARAMS:
    dim_x=0,
    dim_y=1,
    node_color="#465c6b",
    node_size=10,
    textfont_size=8,
    textfont_color="#465c6b",
    xaxes_range=None,
    yaxes_range=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    embedding = terms_by_dimension_frame(
        #
        # FUNCTION PARAMS:
        field=field,
        #
        # TF PARAMS:
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # TERM PARAMS:
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
        # DECOMPOSITION:
        decomposition_estimator=decomposition_estimator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return manifold_2d_map(
        node_x=embedding[dim_x],
        node_y=embedding[dim_y],
        node_text=embedding.index.to_list(),
        node_color=node_color,
        node_size=node_size,
        title_x=dim_x,
        title_y=dim_y,
        textfont_size=textfont_size,
        textfont_color=textfont_color,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )
