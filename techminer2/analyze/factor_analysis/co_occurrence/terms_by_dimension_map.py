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
## >>> from techminer2.analyze.factor_analysis.co_occurrence import terms_by_dimension_map
## >>> plot = (
## ...     TermsByDimensionMap(
## ...     .set_analysis_params(
## ...         association_index=None,
## ...         decomposition_estimator = PCA(
## ...             n_components=5,
## ...             whiten=False,
## ...             svd_solver="auto",
## ...             tol=0.0,
## ...             iterated_power="auto",
## ...             n_oversamples=10,
## ...             power_iteration_normalizer="auto",
## ...             random_state=0, 
## ...         ),
## ...     #
## ...     ).set_item_params(
## ...         field="author_keywords",
## ...         top_n=20,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_plot_params(
## ...         dim_x=0,
## ...         dim_y=1,
## ...         node_color="#465c6b",
## ...         node_size=10,
## ...         textfont_size=8,
## ...         textfont_color="#465c6b",
## ...         xaxes_range=None,
## ...         yaxes_range=None,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
>>> # plot.write_html("sphinx/_static/factor_analysis/co_occurrence/terms_by_dimension_map.html")

.. raw:: html

    <iframe src="../../_static/factor_analysis/co_occurrence/terms_by_dimension_map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ..internals.manifold_2d_map import manifold_2d_map
from .terms_by_dimension_dataframe import terms_by_dimension_frame


def terms_by_dimension_map(
    #
    # PARAMS:
    field,
    association_index=None,
    #
    # TERM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
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
        association_index=association_index,
        #
        # TERM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
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
