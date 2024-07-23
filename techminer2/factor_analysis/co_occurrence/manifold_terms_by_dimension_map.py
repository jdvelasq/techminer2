# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Manifold Terms by Dimensions Map
===============================================================================

>>> from sklearn.decomposition import PCA
>>> from sklearn.manifold import TSNE
>>> from techminer2.factor_analysis.co_occurrence import manifold_terms_by_dimension_map
>>> manifold_terms_by_dimension_map(
...     #
...     # PARAMS:
...     field="author_keywords",
...     association_index=None,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DESOMPOSITION PARAMS:
...     decomposition_estimator = PCA(
...         n_components=5,
...         whiten=False,
...         svd_solver="auto",
...         tol=0.0,
...         iterated_power="auto",
...         n_oversamples=10,
...         power_iteration_normalizer="auto",
...         random_state=0, 
...     ),
...     #
...     # MANIFOLD PARAMS:
...     manifold_estimator=TSNE(
...         perplexity=10.0,
...         early_exaggeration=12.0,
...         learning_rate="auto",
...         max_iter=1000,
...         n_iter_without_progress=300,
...         min_grad_norm=1e-07,
...         metric="euclidean",
...         metric_params=None,
...         init="pca",
...         verbose=0,
...         random_state=0,
...         method="barnes_hut",
...         angle=0.5,
...         n_jobs=None,
...     ),
...     #
...     # MAP PARAMS:
...     node_color="#465c6b",
...     node_size=10,
...     textfont_size=8,
...     textfont_color="#465c6b",
...     xaxes_range=None,
...     yaxes_range=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/factor_analysis/co_occurrence/manifold_terms_by_dimension_map.html")

.. raw:: html

    <iframe src="../../_static/factor_analysis/co_occurrence/manifold_terms_by_dimension_map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from .._core.manifold_2d_map import manifold_2d_map
from .terms_by_dimension_frame import terms_by_dimension_frame


def manifold_terms_by_dimension_map(
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
    # MANIFOLD PARAMS:
    manifold_estimator=None,
    #
    # MAP PARAMS:
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

    manifold = manifold_estimator.fit_transform(embedding)

    return manifold_2d_map(
        node_x=manifold[:, 0],
        node_y=manifold[:, 1],
        node_text=embedding.index.to_list(),
        node_color=node_color,
        node_size=node_size,
        title_x="Dim 0",
        title_y="Dim 1",
        textfont_size=textfont_size,
        textfont_color=textfont_color,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )
