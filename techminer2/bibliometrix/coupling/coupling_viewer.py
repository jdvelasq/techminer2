# flake8: noqa
"""
Coupling (Network) Viewer
===============================================================================


>>> ROOT_DIR = "data/regtech/"

>>> import techminer2plus
>>> coupling_matrix = techminer2plus.analyze.coupling.coupling_matrix(
...     field="author_keywords",
...     top_n=20,
...     root_dir=ROOT_DIR,
... )
>>> graph = techminer2plus.analyze.coupling.coupling_network(
...    coupling_matrix,
...    algorithm_or_estimator="louvain",
... )

>>> fig = techminer2plus.analyze.coupling.coupling_viewer(
...     graph,
...     n_labels=15,
...     node_size_min=8,
...     node_size_max=45,
...     textfont_size_min=8,
...     textfont_size_max=20,
... )
>>> file_name = "sphinx/_static/analyze/coupling/coupling_viewer.html"
>>> fig.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/analyze/coupling/coupling_viewer.html"
    height="600px" width="100%" frameBorder="0"></iframe>



# pylint: disable=line-too-long
"""

# from ..network import network_viewer


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def coupling_viewer(
    graph,
    n_labels=None,
    nx_k=None,
    nx_iterations=10,
    random_state=0,
    node_size_min=None,
    node_size_max=None,
    textfont_size_min=None,
    textfont_size_max=None,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    """Plots a network"""

    return network_viewer(
        graph=graph,
        n_labels=n_labels,
        is_article=True,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        random_state=random_state,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )
