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


## >>> # authors, countries, organizations, sources:
## >>> from techminer2.analyze.coupling_network import NetworkPlot
## >>> plot = (
## ...     NetworkPlot()
## ...     .set_analysis_params(
## ...         unit_of_analysis='authors', # article
## ...                                     # authors 
## ...                                     # countries
## ...                                     # organizations 
## ...                                     # sources
## ...         top_n=20, 
## ...         citations_threshold=0,
## ...         occurrence_threshold=2,
## ...         custom_terms=None,
## ...         algorithm_or_dict="louvain",
## ...     #
## ...     ).set_nx_params(
## ...         nx_k=None,
## ...         nx_iterations=30,
## ...         nx_random_state=0,
## ...     #
## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_size_range(10, 20)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## ...         edge_color="#7793a5",
## ...         edge_width_range=(0.8, 3.0),
## ...     #
## ...     .using_xaxes_range(None, None)
## ...     .using_yaxes_range(None, None)
## ...     .using_axes_visible(False)

## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> plot.write_html("sphinx/_static/coupling_network/others_network_plot.html")

.. raw:: html

    <iframe src="../_static/coupling_network/others_network_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
## >>> # article:
## >>> from techminer2.analyze.coupling_network import NetworkPlot
## >>> plot = (
## ...     NetworkPlot()
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
## ...     ).set_nx_params(
## ...         nx_k=None,
## ...         nx_iterations=30,
## ...         nx_random_state=0,
## ...     ).set_plot_params(
## ...         node_size_range=(30, 70),
## ...         textfont_size_range=(10, 20),
## ...         textfont_opacity_range=(0.35, 1.00),
## ...         edge_color="#7793a5",
## ...         edge_width_range=(0.8, 3.0),
## ...     ).set_axes_params(
## ...         xaxes_range=None,
## ...         yaxes_range=None,
## ...         show_axes=False,
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build()
## ... )
## >>> # plot.write_html("sphinx/_static/coupling_network/docs_network_plot.html")

.. raw:: html

    <iframe src="../_static/coupling_network/docs_network_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>
    
    
                                             
"""
from .docs.network_plot import _network_plot as docs_network_plot
from .others.network_plot import _network_plot as others_network_plot


def network_plot(
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

        return docs_network_plot(
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

    return others_network_plot(
        unit_of_analysis=unit_of_analysis,
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
