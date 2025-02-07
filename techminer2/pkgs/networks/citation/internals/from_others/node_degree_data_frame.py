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

## >>> # abbr_source_title, authors, organizations, countries:
## >>> from techminer2.pkgs.citation_network  import NodeDegreeDataFrame
## >>> node_degree_frame(
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .unit_of_analysis('source_title')
## ...     .having_terms_in_top(30)
## ...     .having_citation_threshold(0)
## ...     .having_occurrence_threshold(2)
## ...     .having_terms_in(None)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... ).head()
   Node                       Name  Degree
0     0    J Manage Inf Syst 2:696       3
1     1        J. Econ. Bus. 3:422       3
2     2      Electron. Mark. 2:287       1
3     3      Financ. Manage. 2:161       1
4     4  Ind Manage Data Sys 2:386       1






"""
from ......internals.mixins import InputFunctionsMixin

# from ....internals.nx.nx_degree_frame import nx_degree_frame
from .create_nx_graph import internal__create_nx_graph


class NodeDegreeDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(
            #
            # FUNCTION PARAMS:
            unit_of_analysis=self.params.unit_of_analysis,
            #
            # COLUMN PARAMS:
            top_n=top_n,
            citations_threshold=self.params.citations_threshold,
            occurrence_threshold=self.params.occurrence_threshold,
            custom_terms=self.params.custom_terms,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        return nx_degree_frame(
            #
            # FUNCTION PARAMS:
            nx_graph=nx_graph,
        )
