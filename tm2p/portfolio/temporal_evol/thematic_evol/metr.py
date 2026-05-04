"""
Metrics
===============================================================================

Smoke test:
    >>> from tm2p.portfolio.perform_metr.main import Metrics as MainMetrics
    >>> main_metrics = (
    ...     MainMetrics()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(main_metrics.head(10).to_string())
                                                        VALUE
    CATEGORY ITEM                                            
    GENERAL  Annual growth rate %                       21.62
             Average annual citations per document       0.26
             Average citations per document              9.53
             Average documents per source                1.54
             Average references per document            75.38
             Documents                                   1149
             Document average age                        8.25
             Number of sources                            745
             Timespan                               1991:2026
             Total cited references                     86608

    
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.direct import ClusterToUnits  # doctest: +ELLIPSIS
    Note...
    
    >>> mapping0 = (
    ...     ClusterToUnits()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .where_record_years_range(1991, 2005)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ) 
    >>> from pprint import pprint
    >>> pprint(mapping0) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS       
    {0: ['computer simulation',
         'system dynamics',
         'decision making',
         'mathematical models',
         'water supply',
         'water management',
    ...    
    
    >>> mapping1 = (
    ...     ClusterToUnits()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .where_record_years_range(2006, 2015)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )    
    >>> pprint(mapping1) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS           
    {0: ['system dynamics',
         'system theory',
         'computer simulation',
         'simulation',
         'system dynamics model',
         'computer software',
    ...


    >>> mapping2 = (
    ...     ClusterToUnits()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .where_record_years_range(2016, 2025)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )            
    >>> pprint(mapping2) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS           
    {0: ['system dynamics',
         'system theory',
         'system dynamics modeling',
         'computer software',
         'system dynamics model',
         'decision making',
         'sensitivity analysis',
    ...

    >>> from tm2p.portfolio.temporal_evol.thematic_evol import Metrics  # type: ignore
    >>> df = (
    ...     Metrics()
    ...     #
    ...     .using_tmap_minimum_shared_units(2)
    ...     .using_tmap_mininum_jaccard_similarity(0.15)
    ...     .using_tmap_minimum_inclusion_index(0.40)
    ...     .using_clusters_per_period(
    ...         (mapping0, mapping1, mapping2),
    ...     )
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(50).to_string())
        PERIOD_FROM  PERIOD_TO  CLUSTER_FROM  CLUSTER_TO                                                                                                                                                                                                                                                                                                SHARED_TERMS  N_SHARED_TERMS   JACCARD  INCLUSION  LINK_STRENGTH
    0             0          1             0           0                                                                                                                                                                          computer simulation; investments; optimization; simulation model; system dynamics; system theory; systems dynamics; transportation               8  0.097561   0.181818       0.181818
    1             0          1             0           1                                                                                                                                                                                                     computer program; decision support system; decision support systems; environmental protection; modeling               5  0.087719   0.312500       0.312500
    2             0          1             0           2                                                                                                                                                                                                                        artificial intelligence; decision making; irrigation; water management; water supply               5  0.089286   0.333333       0.333333
    3             0          1             2           1                                                                                                                                                                                                                                                                                      article; human; humans               3  0.111111   0.214286       0.214286
    4             0          1             2           4                                                                                                                                                                                                                                                                       nuclear power plants; risk assessment               2  0.086957   0.181818       0.181818
    5             1          2             0           0  causal loop diagrams; commerce; computer software; costs; dynamic models; information management; investments; manufacture; profitability; sales; sensitivity analysis; simulation model; supply chains; system dynamics; system dynamics approach; system dynamics model; system theory; systems dynamics              18  0.281250   0.473684       0.473684
    6             1          2             0           1                                                                                                                                                                                                                                                                                optimization; sustainability               2  0.029412   0.076923       0.076923
    7             1          2             0           2                                                                                                                                                                                                                                                                   computer simulation; dynamics; simulation               3  0.050847   0.166667       0.166667
    8             1          2             0           3                                                                                                                                                                                                                                                                          knowledge management; supply chain               2  0.037736   0.181818       0.181818
    9             1          2             1           1                                                                                                                                                                                                                   decision support systems; economic and social effects; environmental protection; modeling               4  0.105263   0.250000       0.250000
    10            1          2             1           2                                                                                                                                                                                                                                                                            article; human; humans; software               4  0.133333   0.250000       0.250000
    11            1          2             2           0                                                                                                                                                                                                                                                                    artificial intelligence; decision making               2  0.039216   0.133333       0.133333
    12            1          2             2           1                                                                                                                                                                          climate change; economic analysis; economics; irrigation; sustainable development; water management; water resources; water supply               8  0.242424   0.533333       0.533333
    13            1          2             2           2                                                                                                                                                                                                                                                                                      china; numerical model               2  0.064516   0.133333       0.133333
    14            1          2             4           0                                                                                                                                                                                                                                     risk assessment; risk management; simulation analysis; vensim softwares               4  0.088889   0.363636       0.363636


    


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> pd.DataFrame:

        links: list[dict] = []
        for base_period, (current_clusters, next_clusters) in enumerate(
            zip(
                self.params.tmap_clusters_per_period[:-1],
                self.params.tmap_clusters_per_period[1:],
            )
        ):
            links += self.compute_period_links(
                base_period, current_clusters, next_clusters
            )

        return pd.DataFrame(links)

    def compute_period_links(
        self, base_period, current_clusters, next_clusters
    ) -> list[dict]:

        rows = []

        for cluster_from, units_from in current_clusters.items():
            for cluster_to, units_to in next_clusters.items():

                shared = set(units_from).intersection(set(units_to))

                if not shared:
                    continue

                jaccard = len(shared) / len(set(units_from).union(set(units_to)))
                inclusion = len(shared) / min(len(units_from), len(units_to))

                keep = (
                    len(shared) >= self.params.tmap_minimum_shared_units
                    or jaccard >= self.params.tmap_minimum_jaccard_similarity
                    or inclusion >= self.params.tmap_minimum_inclusion_index
                )

                if keep:
                    rows.append(
                        {
                            "PERIOD_FROM": base_period,
                            "PERIOD_TO": base_period + 1,
                            "CLUSTER_FROM": cluster_from,
                            "CLUSTER_TO": cluster_to,
                            "SHARED_TERMS": "; ".join(sorted(shared)),
                            "N_SHARED_TERMS": len(shared),
                            "JACCARD": jaccard,
                            "INCLUSION": inclusion,
                            "LINK_STRENGTH": max(jaccard, inclusion),
                        }
                    )
        return rows
