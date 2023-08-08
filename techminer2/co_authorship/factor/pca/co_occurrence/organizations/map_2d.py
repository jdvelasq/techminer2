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


>>> from techminer2.co_authorship.factor.pca.co_occurrence.organizations import map_2d
>>> map_2d(
...     #
...     # PARAMS:
...     association_index=None,
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
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # PCA PARAMS:
...     n_components=6,
...     whiten=False,
...     svd_solver="auto",
...     tol=0.0,
...     iterated_power="auto",
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/co_authorship/factor/pca/co_occurrence/organizations/map_2d.html")

.. raw:: html

    <iframe src="../../../../../../_static/co_authorship/factor/pca/co_occurrence/organizations/map_2d.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ......factor_analysis.co_occurrence.pca.factor_matrix import factor_matrix

UNIT_OF_ANALYSIS = "organizations"


def map_2d(
    #
    # PARAMS:
    association_index=None,
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
    # PCA PARAMS:
    n_components=None,
    whiten=False,
    svd_solver="auto",
    tol=0.0,
    iterated_power="auto",
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
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

    return factor_matrix(
        #
        # COOC PARAMS:
        rows_and_columns=UNIT_OF_ANALYSIS,
        association_index=association_index,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # PCA PARAMS:
        n_components=n_components,
        whiten=whiten,
        svd_solver=svd_solver,
        tol=tol,
        iterated_power=iterated_power,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).fig_(
        dim_x=dim_x,
        dim_y=dim_y,
        node_color=node_color,
        node_size=node_size,
        textfont_size=textfont_size,
        textfont_color=textfont_color,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )
