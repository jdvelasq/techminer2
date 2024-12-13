# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Frame
===============================================================================

>>> # article:
>>> from techminer2.citation_network import node_degree_frame
>>> node_degree_frame(
...     unit_of_analysis="article",
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_threshold=0,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
   Node                                               Name  Degree
0     0                   Hu Z., 2019, SYMMETRY, V11 1:176       7
1     1       Gomber P., 2017, J BUS ECON, V87, P537 1:489       4
2     2  Gomber P., 2018, J MANAGE INF SYST, V35, P220 ...       4
3     3       Alt R., 2018, ELECTRON MARK, V28, P235 1:150       4
4     4  Gozman D., 2018, J MANAGE INF SYST, V35, P145 ...       2



>>> # abbr_source_title, authors, organizations, countries:
>>> from techminer2.citation_network import node_degree_frame
>>> node_degree_frame(
...     unit_of_analysis="abbr_source_title",
...     #
...     # COLUMN PARAMS:
...     top_n=30,
...     citations_threshold=0,
...     occurrence_threshold=2,
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
   Node                       Name  Degree
0     0    J Manage Inf Syst 2:696       3
1     1        J. Econ. Bus. 3:422       3
2     2      Electron. Mark. 2:287       1
3     3      Financ. Manage. 2:161       1
4     4  Ind Manage Data Sys 2:386       1



"""
from ._core.docs.node_degree_frame import (
    _node_degree_frame as _node_degree_frame_from_docs,
)
from ._core.others.node_degree_frame import (
    _node_degree_frame as _node_degree_frame_from_others,
)


def node_degree_frame(
    #
    # COLUMN PARAMS:
    unit_of_analysis,
    top_n=None,
    citations_threshold=0,
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

        return _node_degree_frame_from_docs(
            #
            # COLUMN PARAMS:
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

    return _node_degree_frame_from_others(
        #
        # FIELD PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
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
