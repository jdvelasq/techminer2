"""
UnitsByCluster
===============================================================================

* **AnalysisUnit.DOC**

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.coupling.direct import UnitsByCluster  # type: ignore
    >>> df = (
    ...     UnitsByCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)     
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER                                             0   ...                                         10
    UNIT                                                    ...                                           
    0                 Wei SK, 2012, EUR J OPER RES 1:00105  ...  Song YG, 2015, J KOREAN ACAD NURS 1:00004
    1                      He L, 2022, WASTE MANAG 1:00091  ...   You MJ, 2019, J KOREAN ACAD NURS 1:00000
    2                Khan S, 2009, ENV MODEL SOFTW 1:00084  ...                                           
    3                    Liu W, 2023, RESOUR POLIC 1:00077  ...                                           
    4        Purwanto A, 2021, SUSTAIN PROD CONSUM 1:00061  ...                                           
    <BLANKLINE>
    [5 rows x 11 columns]



* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

Smoke tests:
    >>> df = (
    ...     UnitsByCluster()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CTRY)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)        
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    CLUSTER    0    1    2    3
    UNIT                       
    0        AUS  CHN  IRN  USA
    1        BRA  GBR  IDN  COL
    2        KOR  TWN  IND  MEX
    3        ESP  CAN  MYS  NLD
    4        DEU  HRV  GRC  NGA




"""

from tm2p._intern.netw.unit_by_clust import BaseUnitByCluster

from ....._intern.helpers.check_db import check_database
from .cluster_to_units import ClusterToUnits


class UnitsByCluster(
    BaseUnitByCluster,
):
    """:meta private:"""

    def cluster_to_units(self):
        check_database(self.params.root_directory)
        return ClusterToUnits()
