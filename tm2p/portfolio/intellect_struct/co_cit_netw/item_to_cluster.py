"""
ItemToCluster
===============================================================================

* **CITED_REF** / **CITED_AUTH** / **CITED_SRC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw import ItemToCluster  # type: ignore
    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Ahmad S, 2000, J COMPUT CIVIL ENG 9:0': 0,
     'Allen R. G., 1998, FAO Irrigation and Drainage Paper 8:0': 0,
     'BARLAS Y, 1989, EUR J OPER RES 8:0': 0,
     'Barlas Y, 1996, SYST DYNAM REV 27:0': 2,
     'Chaerul M, 2008, WASTE MANAGE 7:0': 1,
    ...


    >>> mapping = (
    ...     ItemToCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(50)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'Ahmad S, 2000, J COMPUT CIVIL ENG': 0,
     'Allen R. G., 1998, FAO Irrigation and Drainage Paper': 0,
     'BARLAS Y, 1989, EUR J OPER RES': 0,
     'Barlas Y, 1996, SYST DYNAM REV': 2,
     'Chaerul M, 2008, WASTE MANAGE': 1,
     'Ding ZK, 2016, WASTE MANAGE': 1,
     'Ding ZK, 2018, J CLEAN PROD': 1,
     'Dyson B, 2005, WASTE MANAGE': 1,
    ...

"""

from tm2p._intern.netw.item_to_clust import BaseItemToCluster

from .dir_matrix import DirectMatrix


class ItemToCluster(
    BaseItemToCluster,
):
    """:meta private:"""

    def get_similarity_matrix(self):
        """:meta private:"""

        return DirectMatrix()
