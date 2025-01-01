# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Density Plot
===============================================================================

## >>> from techminer2.coupling_network import node_density_plot
## >>> plot = node_density_plot(
## ...     unit_of_analysis='authors', # article
## ...                                 # authors 
## ...                                 # countries
## ...                                 # organizations 
## ...                                 # sources
## ...     #
## ...     # FILTERS:
## ...     top_n=20, 
## ...     citations_threshold=0,
## ...     #
## ...     # FILTERS NOT VALID FOR 'article' UNIT OF ANALYSIS:
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     #
## ...     # NETWORK PARAMS:
## ...     algorithm_or_dict="louvain",
## ...     #
## ...     # LAYOUT:
## ...     nx_k=None,
## ...     nx_iterations=30,
## ...     nx_random_state=0,
## ...     #
## ...     # DENSITY VISUALIZATION:
## ...     bandwidth=0.1,
## ...     colorscale="Aggrnyl",
## ...     opacity=0.6,
## ...     #
## ...     # AXES:
## ...     # xaxes_range=None,
## ...     # yaxes_range=None,
## ...     # show_axes=False,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # plot.write_html("sphinx/_static/coupling_network/others_node_density_plot.html")

.. raw:: html

    <iframe src="../_static/coupling_network/others_node_density_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
## >>> # article:    
## >>> from techminer2.coupling_network import node_density_plot
## >>> plot = node_density_plot(
## ...     unit_of_analysis='article', # article
## ...                                 # authors 
## ...                                 # countries, 
## ...                                 # organizations 
## ...                                 # sources
## ...     #
## ...     # FILTERS:
## ...     top_n=20, 
## ...     citations_threshold=0,
## ...     #
## ...     # NOT VALID FOR 'article' UNIT OF ANALYSIS:
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     #
## ...     # NETWORK PARAMS:
## ...     algorithm_or_dict="louvain",
## ...     #
## ...     # LAYOUT:
## ...     nx_k=None,
## ...     nx_iterations=30,
## ...     nx_random_state=0,
## ...     #
## ...     # DENSITY VISUALIZATION:
## ...     bandwidth=0.1,
## ...     colorscale="Aggrnyl",
## ...     opacity=0.6,
## ...     #
## ...     # AXES:
## ...     # xaxes_range=None,
## ...     # yaxes_range=None,
## ...     # show_axes=False,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> # plot.write_html("sphinx/_static/coupling_network/docs_node_density_plot.html")

.. raw:: html

    <iframe src="../_static/coupling_network/docs_node_density_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

                                                 
"""
from ._core.docs.node_density_plot import _node_density_plot as docs_node_density_plot
from ._core.others.node_density_plot import _node_density_plot as others_node_density_plot


def node_density_plot(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
    custom_terms=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # DENSITY VISUALIZATION:
    bandwidth="silverman",
    colorscale="Aggrnyl",
    opacity=0.6,
    textfont_size_range=(10, 20),
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

        return docs_node_density_plot(
            #
            # ARTICLE PARAMS:
            top_n=top_n,
            citations_threshold=citations_threshold,
            #
            # NETWORK PARAMS:
            algorithm_or_dict=algorithm_or_dict,
            #
            # LAYOUT:
            nx_k=nx_k,
            nx_iterations=nx_iterations,
            nx_random_state=nx_random_state,
            #
            # DENSITY VISUALIZATION:
            bandwidth=bandwidth,
            colorscale=colorscale,
            opacity=opacity,
            textfont_size_range=textfont_size_range,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return others_node_density_plot(
        unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
        #
        # NETWORK PARAMS:
        algorithm_or_dict=algorithm_or_dict,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # DENSITY VISUALIZATION:
        bandwidth=bandwidth,
        colorscale=colorscale,
        opacity=opacity,
        textfont_size_range=textfont_size_range,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
