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

## >>> from techminer2.pkgs.networks.citation.authors  import NodeDegreeDataFrame
## >>> (
## ...     NodeDegreeDataFrame()
## ...     #
## ...     # UNIT OF ANALYSIS:
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

from .....internals.mixins import InputFunctionsMixin
from ..internals.from_others.node_degree_data_frame import (
    NodeDegreeDataFrame as OtherNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            OtherNodeDegreeDataFrame()
            .update_params(**self.params.__dict__)
            .unit_of_analysis("authors")
            .build()
        )
