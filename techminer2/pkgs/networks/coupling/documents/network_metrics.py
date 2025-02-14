# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Metrics
===============================================================================

>>> from techminer2.pkgs.networks.coupling.documents import NetworkMetrics
>>> (
...     NetworkMetrics()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(20)
...     .having_citation_threshold(0)
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
                                            Degree  ...  PageRank
Anagnostopoulos I., 2018, J ECON BUS 1:202       7  ...  0.109121
Gomber P., 2017, J BUS ECON 1:489                6  ...  0.164851
Gomber P., 2018, J MANAGE INF SYST 1:576         5  ...  0.108659
Hu Z., 2019, SYMMETRY 1:176                      4  ...  0.116249
Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161       4  ...  0.100082
<BLANKLINE>
[5 rows x 4 columns]



"""
from .....internals.mixins import ParamsMixin
from .....internals.nx import internal__compute_network_metrics
from ..internals.from_documents.create_nx_graph import internal__create_nx_graph


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(params=self.params)
        return internal__compute_network_metrics(nx_graph=nx_graph)
