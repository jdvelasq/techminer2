# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
TSNE
===============================================================================


>>> from techminer2.tech_mining.svd.cooc_matrix import tsne
>>> tsne(
...     #
...     # PARAMS:
...     field="nlp_phrases",
...     association_index=None,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # TSNE PARAMS:
...     perplexity=10.0,
...     early_exaggeration=12.0,
...     learning_rate="auto",
...     n_iter_tsne=1000,
...     n_iter_without_progress=300,
...     min_grad_norm=1e-07,
...     metric="euclidean",
...     metric_params=None,
...     init="pca",
...     tsne_random_state=0,
...     method="barnes_hut",
...     angle=0.5,
...     n_jobs=None,
...     #
...     # MAP:
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
...     n_iter_svd=5,
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0,
...     tol=0.0,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/analyze/svd/cooc_matrix/tsne.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/svd/cooc_matrix/tsne.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ..._core.factor_analysis import FactorAnalyzer


def plot_tsne_map_from_co_occurrence_svd_embedding(
    #
    # PARAMS:
    field,
    association_index=None,
    #
    # TSNE PARAMS:
    perplexity=10.0,
    early_exaggeration=12.0,
    learning_rate="auto",
    n_iter_tsne=1000,
    n_iter_without_progress=300,
    min_grad_norm=1e-07,
    metric="euclidean",
    metric_params=None,
    init="pca",
    tsne_random_state=0,
    method="barnes_hut",
    angle=0.5,
    n_jobs=None,
    #
    # MAP:
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
    n_iter_svd=5,
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

    analyzer = FactorAnalyzer(field=field)

    analyzer.cooc_matrix(
        #
        # COOC PARAMS:
        association_index=association_index,
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
        n_iter=n_iter_svd,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
    )

    analyzer.compute_embedding()

    return analyzer.tsne(
        #
        # TSNE PARAMS:
        perplexity=perplexity,
        early_exaggeration=early_exaggeration,
        learning_rate=learning_rate,
        n_iter=n_iter_tsne,
        n_iter_without_progress=n_iter_without_progress,
        min_grad_norm=min_grad_norm,
        metric=metric,
        metric_params=metric_params,
        init=init,
        random_state=tsne_random_state,
        method=method,
        angle=angle,
        n_jobs=n_jobs,
        #
        # MAP:
        node_color=node_color,
        node_size=node_size,
        textfont_size=textfont_size,
        textfont_color=textfont_color,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )
