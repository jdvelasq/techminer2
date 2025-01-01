# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Degree Frame
===============================================================================

## >>> from techminer2.coupling_network import node_degree_frame
## >>> node_degree_frame(
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
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... ).head()
   Node                Name  Degree
0     0    Gomber P. 2:1065       3
1     1    Hornuf L. 2:0358       3
2     2  Jagtiani J. 3:0317       3
3     3   Lemieux C. 2:0253       3
4     4    Dolata M. 2:0181       2



## >>> # article:
## >>> from techminer2.coupling_network import node_degree_frame
## >>> node_degree_frame(
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
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... ).head()
   Node                                        Name  Degree
0     0  Anagnostopoulos I., 2018, J ECON BUS 1:202       7
1     1           Gomber P., 2017, J BUS ECON 1:489       6
2     2    Gomber P., 2018, J MANAGE INF SYST 1:576       5
3     3                 Hu Z., 2019, SYMMETRY 1:176       4
4     4  Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161       4



"""
from ._core.docs.node_degree_frame import _node_degree_frame as docs_node_degree_frame
from ._core.others.node_degree_frame import _node_degree_frame as others_node_degree_frame


def node_degree_frame(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
    custom_terms=None,
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

        return docs_node_degree_frame(
            #
            # ARTICLE PARAMS:
            top_n=top_n,
            citations_threshold=citations_threshold,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return others_node_degree_frame(
        unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
