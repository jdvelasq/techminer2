# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms to Cluster Mapping
===============================================================================


## >>> from techminer2.analyze.co_occurrence_network import DocumentsByClusterMapping
## >>> documents_by_cluster = (
## ...     DocumentsByClusterMapping()
## ...     .set_analysis_params(
## ...         algorithm_or_dict="louvain",
## ...         association_index="association",
## ...     #
## ...     .set_item_params(
## ...         field="author_keywords",
## ...         top_n=20,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...        custom_terms=None,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...         sort_by="date_newest", # date_newest, date_oldest, global_cited_by_highest, 
## ...                                # global_cited_by_lowest, local_cited_by_highest, 
## ...                                # local_cited_by_lowest, first_author_a_to_z, 
## ...                                # first_author_z_to_a, source_title_a_to_z, 
## ...                                # source_title_z_to_a
## ...     ).build()
## ... )
## >>> print(len(documents_by_cluster))
## 4
## >>> print(documents_by_cluster[0][0])
Record-No: 6
AR Haddad C., 2019, SMALL BUS ECON, V53, P81
TI The emergence of the global fintech market: economic and technological
   determinants
AU Haddad C.; Hornuf L.
TC 258
SO Small Business Economics
PY 2019
AB we investigate the economic and TECHNOLOGICAL_DETERMINANTS inducing
   ENTREPRENEURS to establish ventures with the purpose of reinventing
   FINANCIAL_TECHNOLOGY ( FINTECH ) . we find that countries witness more
   FINTECH_STARTUP_FORMATIONS when the economy is well_developed and
   VENTURE_CAPITAL is readily available . furthermore , the number of secure
   INTERNET_SERVERS , MOBILE_TELEPHONE_SUBSCRIPTIONS , and the
   AVAILABLE_LABOR_FORCE has a POSITIVE_IMPACT on the DEVELOPMENT of this
   NEW_MARKET_SEGMENT . finally , the more difficult IT is for companies to
   ACCESS_LOANS , the higher is the number of FINTECH_STARTUPS in a country .
   overall , the EVIDENCE_SUGGESTS that FINTECH_STARTUP_FORMATION_NEED not be
   left to chance , but ACTIVE_POLICIES can INFLUENCE the emergence of this
   NEW_SECTOR . 2018 , the author ( s ) .
DE ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS
** ACCESS_LOANS; ACTIVE_POLICIES; AVAILABLE_LABOR_FORCE; EVIDENCE_SUGGESTS;
   FINANCIAL_TECHNOLOGY; FINTECH_STARTUPS; FINTECH_STARTUP_FORMATIONS;
   FINTECH_STARTUP_FORMATION_NEED; GLOBAL_FINTECH_MARKET; INTERNET_SERVERS;
   MOBILE_TELEPHONE_SUBSCRIPTIONS; NEW_MARKET_SEGMENT; NEW_SECTOR;
   POSITIVE_IMPACT; TECHNOLOGICAL_DETERMINANTS; VENTURE_CAPITAL
<BLANKLINE>



"""
# from ..documents import select_documents
from .clusters_to_terms_mapping import clusters_to_terms_mapping


def documents_by_cluster_mapping(
    #
    # PARAMS:
    field,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    association_index="association",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    sort_by=None,
    **filters,
):
    """:meta private:"""

    c2t_mapping = clusters_to_terms_mapping(
        #
        # PARAMS:
        field=field,
        retain_counters=False,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # NETWORK PARAMS:
        algorithm_or_dict=algorithm_or_dict,
        association_index=association_index,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    mapping = {}

    for key, values in c2t_mapping.items():

        params = {field: values}

        mapping[key] = select_documents(
            #
            # DATABASE PARAMS
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            sort_by=sort_by,
            **params,
            **filters,
        )

    return mapping
