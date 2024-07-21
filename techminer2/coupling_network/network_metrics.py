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

>>> # authors, countries, organizations, sources:
>>> from techminer2.coupling_network import network_metrics
>>> network_metrics(
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
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                    Degree  Betweenness  Closeness  PageRank
Gomber P. 2:1065         3          0.0   0.333333  0.075911
Hornuf L. 2:0358         3          0.0   0.333333  0.065572
Jagtiani J. 3:0317       3          0.0   0.333333  0.129258
Lemieux C. 2:0253        3          0.0   0.333333  0.129258
Dolata M. 2:0181         2          0.0   0.222222  0.100000


>>> # article:
>>> from techminer2.coupling_network import network_metrics
>>> network_metrics(
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
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                                            Degree  ...  PageRank
Anagnostopoulos I., 2018, J ECON BUS 1:202       7  ...  0.108354
Gomber P., 2017, J BUS ECON 1:489                7  ...  0.172423
Gomber P., 2018, J MANAGE INF SYST 1:576         5  ...  0.102747
Hu Z., 2019, SYMMETRY 1:176                      4  ...  0.101092
Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161       4  ...  0.089072
<BLANKLINE>
[5 rows x 4 columns]


"""
from ._core.docs.network_metrics import _network_metrics as docs_network_metrics
from ._core.others.network_metrics import _network_metrics as others_network_metrics


def network_metrics(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # NOT VALID FOR 'article' UNIT OF ANALYSIS:
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

        return docs_network_metrics(
            #
            # FILTER PARAMS:
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

    return others_network_metrics(
        unit_of_analysis=unit_of_analysis,
        #
        # FILTER PARAMS:
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
