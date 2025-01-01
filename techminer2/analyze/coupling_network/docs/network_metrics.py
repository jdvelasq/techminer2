# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

## >>> from techminer2.coupling_network._core.docs.network_metrics import _network_metrics
## >>> _network_metrics(
## ...     #
## ...     # ARTICLE PARAMS:
## ...     top_n=20, 
## ...     citations_threshold=0,
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build()
## ... ).head()
                                            Degree  ...  PageRank
Anagnostopoulos I., 2018, J ECON BUS 1:202       7  ...  0.109121
Gomber P., 2017, J BUS ECON 1:489                6  ...  0.164851
Gomber P., 2018, J MANAGE INF SYST 1:576         5  ...  0.108659
Hu Z., 2019, SYMMETRY 1:176                      4  ...  0.116249
Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161       4  ...  0.100082
<BLANKLINE>
[5 rows x 4 columns]



"""
from ....internals.nx.nx_compute_metrics import nx_compute_metrics
from .internals.create_coupling_nx_graph import _create_coupling_nx_graph


def _network_metrics(
    #
    # ARTICLE PARAMS:
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

    nx_graph = _create_coupling_nx_graph(
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

    return nx_compute_metrics(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
