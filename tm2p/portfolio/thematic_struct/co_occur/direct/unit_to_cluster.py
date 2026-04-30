"""
UnitToCluster
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import Field  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import UnitToCluster
    >>> mapping = (
    ...     UnitToCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
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
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 0129:001262': 0,
     'convolutional neural network 0144:001310': 1,
     'convolutional neural networks 0173:001295': 1,
     'deep learning 0269:004143': 0,
     'deep neural networks 0137:001533': 1,
     'edge ai 0104:001085': 0,
     'edge computing 0228:002411': 0,
     'embedded systems 0186:002145': 2,
     'embedded-system 0116:001320': 2,
     'energy efficiency 0153:002034': 0,
     'internet of things 0346:005415': 0,
     'iot 0118:001423': 0,
     'learning systems 0343:003524': 0,
     'machine learning 0766:008244': 0,
     'machine learning models 0104:000937': 0,
     'microcontrollers 0247:003364': 1,
     'neural networks 0266:002432': 1,
     'real- time 0121:000533': 1,
     'tiny machine learning 0388:003654': 0,
     'tinyml 1031:010091': 0}

"""

from tm2p._intern.netw.unit_to_clust import BaseUnitToCluster

from .dir_matrix import DirectMatrix


class UnitToCluster(
    BaseUnitToCluster,
):
    """:meta private:"""

    def get_similarity_matrix(self):
        """:meta private:"""

        return DirectMatrix()
