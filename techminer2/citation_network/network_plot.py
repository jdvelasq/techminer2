# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Plot
===============================================================================

## >>> # article:
## >>> from techminer2.citation_network import network_plot
## >>> plot = network_plot(
## ...     #
## ...     # COLUMN PARAMS:
## ...     unit_of_analysis='article',
## ...     top_n=30, 
## ...     citations_threshold=0,
## ...     #
## ...     # NETWORK CLUSTERING:
## ...     algorithm_or_dict="louvain",
## ...     #
## ...     # LAYOUT:
## ...     nx_k=None,
## ...     nx_iterations=30,
## ...     nx_random_state=0,
## ...     #
## ...     # NODES:
## ...     node_size_range=(30, 70),
## ...     textfont_size_range=(10, 20),
## ...     textfont_opacity_range=(0.35, 1.00),
## ...     #
## ...     # EDGES:
## ...     edge_color="#7793a5",
## ...     edge_width_range=(0.8, 3.0),
## ...     #
## ...     # AXES:
## ...     xaxes_range=None,
## ...     yaxes_range=None,
## ...     show_axes=False,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # plot.write_html("sphinx/_static/citation_network/documents_network_plot.html")

.. raw:: html

    <iframe src="../_static/citation_network/documents_network_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
## >>> # abbr_source_title, authors, organizations, countries:
## >>> from techminer2.citation_network import network_plot
## >>> plot = network_plot(
## ...     #
## ...     # COLUMN PARAMS:
## ...     unit_of_analysis='abbr_source_title',
## ...     top_n=30,
## ...     citations_threshold=0,
## ...     #
## ...     # ONLY FOR OTHERS:
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     #
## ...     # NETWORK CLUSTERING:
## ...     algorithm_or_dict="louvain",
## ...     #
## ...     # LAYOUT:
## ...     nx_k=None,
## ...     nx_iterations=30,
## ...     nx_random_state=0,
## ...     #
## ...     # NODES:
## ...     node_size_range=(30, 70),
## ...     textfont_size_range=(10, 20),
## ...     textfont_opacity_range=(0.35, 1.00),
## ...     #
## ...     # EDGES:
## ...     edge_color="#7793a5",
## ...     edge_width_range=(0.8, 3.0),
## ...     #
## ...     # AXES:
## ...     xaxes_range=None,
## ...     yaxes_range=None,
## ...     show_axes=False,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # plot.write_html("sphinx/_static/citation_network/others_network_plot.html")

.. raw:: html

    <iframe src="../_static/citation_network/others_network_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from ._core.docs.network_plot import _network_plot as _network_plot_from_docs
from ._core.others.network_plot import _network_plot as _network_plot_from_others


def network_plot(
    #
    # COLUMN PARAMS:
    unit_of_analysis,
    top_n=None,
    citations_threshold=0,
    #
    # ONLY FOR OTHERS:
    occurrence_threshold=None,
    custom_terms=None,
    #
    # NETWORK CLUSTERING:
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_range=(0.8, 3.0),
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    if unit_of_analysis == "article":

        return _network_plot_from_docs(
            #
            # COLUMN PARAMS:
            top_n=top_n,
            citations_threshold=citations_threshold,
            #
            # NETWORK CLUSTERING:
            algorithm_or_dict=algorithm_or_dict,
            #
            # LAYOUT:
            nx_k=nx_k,
            nx_iterations=nx_iterations,
            nx_random_state=nx_random_state,
            #
            # NODES:
            node_size_range=node_size_range,
            textfont_size_range=textfont_size_range,
            textfont_opacity_range=textfont_opacity_range,
            #
            # EDGES:
            edge_color=edge_color,
            edge_width_range=edge_width_range,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return _network_plot_from_others(
        #
        # FIELD PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # ONLY FOR OTHERS:
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        textfont_opacity_range=textfont_opacity_range,
        #
        # EDGES:
        edge_color=edge_color,
        edge_width_range=edge_width_range,
        #
        # AXES:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
