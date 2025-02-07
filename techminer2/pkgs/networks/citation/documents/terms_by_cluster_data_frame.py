# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================

>>> from techminer2.pkgs.networks.citation.documents import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .using_term_counters(True)
...     #
...     # CLUSTERING:
...     .using_clustering_algorithm_or_dict("louvain")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                                                   0  ...                                                  3
0  Ryu H.-S., 2018, IND MANAGE DATA SYS, V118, P5...  ...  Anagnostopoulos I., 2018, J ECON BUS, V100, P7...
1  Gracia D.B., 2019, IND MANAGE DATA SYS, V119, ...  ...     Zavolokina L., 2016, FINANCIAL INNOV, V2 1:106
2                   Hu Z., 2019, SYMMETRY, V11 1:176  ...                                                   
3    Gabor D., 2017, NEW POLIT ECON, V22, P423 1:314  ...                                                   
4  Gai K., 2018, J NETWORK COMPUT APPL, V103, P26...  ...                                                   
<BLANKLINE>
[5 rows x 4 columns]



"""
from .....internals.mixins import InputFunctionsMixin
from .....internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from ..internals.from_documents.create_nx_graph import internal__create_nx_graph


class TermsByClusterDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)
