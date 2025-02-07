# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Dataframe
===============================================================================

## >>> from techminer2.pkgs.citation_network.articles  import NodeDegreeDataFrame
## >>> (
## ...     NodeDegreeDataFrame()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .having_terms_in_top(30)
## ...     .having_citation_threshold(0)
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




"""
from .....internals.mixins import InputFunctionsMixin

# from ....internals.nx.nx_degree_frame import nx_degree_frame
from ..internals.from_articles.create_nx_graph import internal__create_nx_graph


class NodeDegreeDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(self.params)

        return nx_degree_frame(
            #
            # FUNCTION PARAMS:
            nx_graph=nx_graph,
        )
