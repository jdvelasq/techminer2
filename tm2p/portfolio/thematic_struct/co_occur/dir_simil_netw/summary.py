"""
Summary
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import Summary
    >>> df = (
    ...     Summary()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
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
    >>> print(df.to_string()) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
       CLUSTER  NUM_ITEMS  PERCENTAGE                                                                                                                                                                                                                                                                                                                                                                                         ITEMS
    0        0         15        30.0  microcontrollers 0316:003886; neural networks 0281:003048; microcontroller 0178:001770; energy efficiency 0170:002078; deep neural networks 0142:001568; latency 0133:001232; inference 0126:001489; energy 0125:000891; low power 0122:000923; devices 0120:001779; memory 0118:001335; energy utilization 0100:001389; mcus 0091:001326; energy consumption 0088:000981; power 0087:001424
    1        1         14        28.0                                              models 0209:001874; artificial intelligence 0193:002328; deployment 0185:001146; edge devices 0163:001441; performance 0161:001246; edge 0134:001755; quantization 0129:001440; edge ai 0118:001164; efficiency 0118:000934; ai 0117:001511; sensors 0116:001134; training 0110:001159; ml 0095:001635; resource constrained devices 0095:000888
    2        2         10        20.0                                                                                               tinyml 1175:011915; machine learning 0807:009343; tiny machine learning 0480:005025; internet of things 0354:005877; learning systems 0343:003524; deep learning 0288:004416; edge computing 0257:003298; iot 0233:003713; machine learning models 0148:001181; learning algorithms 0094:001714
    3        3          9        18.0                                                                                                                                                 accuracy 0413:003917; model 0299:002572; convolutional neural networks 0183:001476; convolutional neural network 0163:001547; real time 0153:001266; real- time 0121:000533; dataset 0110:000836; cnn 0109:000935; classification 0088:000653
    4        4          2         4.0                                                                                                                                                                                                                                                                                                                                     embedded systems 0197:002332; embedded-system 0116:001320


    >>> df = (
    ...     Summary()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
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
    >>> print(df.to_string()) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
       CLUSTER  NUM_ITEMS  PERCENTAGE                                                                                                                                                                                                     ITEMS
    0        0         15        30.0  microcontrollers; neural networks; microcontroller; energy efficiency; deep neural networks; latency; inference; energy; low power; devices; memory; energy utilization; mcus; energy consumption; power
    1        1         14        28.0                                  models; artificial intelligence; deployment; edge devices; performance; edge; quantization; edge ai; efficiency; ai; sensors; training; ml; resource constrained devices
    2        2         10        20.0                                   tinyml; machine learning; tiny machine learning; internet of things; learning systems; deep learning; edge computing; iot; machine learning models; learning algorithms
    3        3          9        18.0                                                                         accuracy; model; convolutional neural networks; convolutional neural network; real time; real- time; dataset; cnn; classification
    4        4          2         4.0                                                                                                                                                                         embedded systems; embedded-system


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .cluster_to_items import ClusterToItems

CLUSTER = "CLUSTER"
NUM_ITEMS = "NUM_ITEMS"
PERCENTAGE = "PERCENTAGE"
ITEMS = "ITEMS"


class Summary(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        communities = ClusterToItems().update(**self.params.__dict__).run()
        communities_len = {}
        communities_perc = {}
        communities_dict = {}

        total = float(sum(len(communities[key]) for key in communities))

        for key, values in communities.items():
            communities_len[key] = len(values)
            communities_perc[key] = round(communities_len[key] / total * 100, 1)
            communities_dict[key] = "; ".join(values)

        summary = pd.DataFrame(
            {
                CLUSTER: list(communities_dict.keys()),
                NUM_ITEMS: communities_len.values(),
                PERCENTAGE: communities_perc.values(),
                ITEMS: communities_dict.values(),
            }
        )

        summary = summary.sort_values(CLUSTER, ascending=True)
        summary = summary.reset_index(drop=True)

        return summary
