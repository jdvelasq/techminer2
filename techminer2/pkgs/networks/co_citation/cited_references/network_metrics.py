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


>>> from techminer2.pkgs.networks.co_citation.cited_references import NetworkMetrics
>>> (
...     NetworkMetrics()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_terms_in(None)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... ).head()
                                            Degree  ...  PageRank
Burtch G., Ghose A., Wattal S. 1:13             15  ...  0.059712
Lin M., Prabhala N.R., Viswanathan S. 1:08      15  ...  0.059586
Zavolokina L., Dolata M., Schwabe G. 1:06       14  ...  0.058428
Duarte J., Siegel S., Young L. 1:06             13  ...  0.052165
Skan J., Dickerson J., Masood S. 1:05           13  ...  0.053263
<BLANKLINE>
[5 rows x 4 columns]


"""
from ....._internals.mixins import ParamsMixin
from .._internals.network_metrics import NetworkMetrics as InternalNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNetworkMetrics()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_references")
            .run()
        )
