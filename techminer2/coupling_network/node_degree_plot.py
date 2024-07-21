# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Degree Plot
===============================================================================

>>> from techminer2.coupling_network import node_degree_plot
>>> plot = node_degree_plot(
...     unit_of_analysis='authors', # article
...                                 # authors 
...                                 # countries
...                                 # organizations 
...                                 # sources
...     #
...     # FILTERS:
...     top_n=20, 
...     citations_threshold=0,
...     #
...     # FILTERS NOT VALID FOR 'article' UNIT OF ANALYSIS:
...     occurrence_threshold=2,
...     custom_terms=None,
...     #
...     # DEGREE PLOT:
...     textfont_size=10,
...     marker_size=7,
...     line_color="black",
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> plot.fig_.write_html("sphinx/_static/coupling_network/others_node_degree_plot.html")

.. raw:: html

    <iframe src="../_static/coupling_network/others_node_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


    
>>> plot.df_.head()
   Node                Name  Degree
0     0    Gomber P. 2:1065       3
1     1    Hornuf L. 2:0358       3
2     2  Jagtiani J. 3:0317       3
3     3   Lemieux C. 2:0253       3
4     4    Dolata M. 2:0181       2


>>> print(plot.prompt_) # doctest: +ELLIPSIS                                        
Your task is ...


>>> # article:
>>> from techminer2.coupling_network import node_degree_plot
>>> plot = node_degree_plot(
...     unit_of_analysis='article', # article
...                                 # authors 
...                                 # countries, 
...                                 # organizations 
...                                 # sources
...     #
...     # FILTERS:
...     top_n=20, 
...     citations_threshold=0,
...     #
...     # NOT VALID FOR 'article' UNIT OF ANALYSIS:
...     occurrence_threshold=2,
...     custom_terms=None,
...     #
...     # DEGREE PLOT:
...     textfont_size=10,
...     marker_size=7,
...     line_color="black",
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> plot.fig_.write_html("sphinx/_static/coupling_network/docs_node_degree_plot.html")

.. raw:: html

    <iframe src="../_static/coupling_network/docs_node_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


    
>>> plot.df_.head()
   Node                                        Name  Degree
0     0  Anagnostopoulos I., 2018, J ECON BUS 1:202       7
1     1           Gomber P., 2017, J BUS ECON 1:489       7
2     2    Gomber P., 2018, J MANAGE INF SYST 1:576       5
3     3                 Hu Z., 2019, SYMMETRY 1:176       4
4     4  Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161       4


>>> print(plot.prompt_) # doctest: +ELLIPSIS                                        
Your task is ...



"""
from ._core.docs.node_degree_plot import _node_degree_plot as docs_node_degree_plot
from ._core.others.node_degree_plot import _node_degree_plot as others_node_degree_plot


def node_degree_plot(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
    custom_terms=None,
    #
    # DEGREE PLOT:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
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

        return docs_node_degree_plot(
            #
            # ARTICLE PARAMS:
            top_n=top_n,
            citations_threshold=citations_threshold,
            #
            # DEGREE PLOT:
            textfont_size=textfont_size,
            marker_size=marker_size,
            line_color=line_color,
            line_width=line_width,
            yshift=yshift,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return others_node_degree_plot(
        unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
        #
        # DEGREE PLOT:
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
