from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import pandas as pd  # type: ignore
from sklearn.base import BaseEstimator  # type: ignore

from tm2p.enum import (
    AnalysisUnit,
    AssociationIndex,
    Correlation,
    Field,
    GraphClusteringAlgorithm,
    NodeSizeMetric,
    RecordOrderBy,
    Scaling,
    ThFile,
    UnitOrderBy,
)


@dataclass
class Params:

    # ####################################################################### #
    #                                                                         #
    #                          DATABASE PARAMETERS                            #
    #                                                                         #
    # ####################################################################### #

    word_length: int

    #
    # Shell otuput:
    #
    quiet: bool
    tqdm_disable: bool
    use_counters: bool
    colored_output: bool
    colored_stderr: bool

    n_chars: int
    n_contexts: int

    cumulative_sum: bool

    core_area: Optional[str]

    # column: Optional[str] = None

    # initial_newline: bool = False

    #
    # Record filtering:
    #
    root_directory: str
    record_citations_range: Tuple[Optional[int], Optional[int]]
    record_years_range: Tuple[Optional[int], Optional[int]]
    records_match: Optional[Dict[Field, List[str]]]
    records_order_by: RecordOrderBy

    #
    # Database operations:
    #
    source_field: Field
    source_fields: tuple[Field, ...]
    stemming_fn: Callable
    target_field: Field
    transformation_function: Optional[Callable[[pd.Series], pd.Series]]

    query_expression: str

    # ####################################################################### #
    #                                                                         #
    #                      PORTFOLIO GENERIC PARAMETERS                       #
    #                                                                         #
    # ####################################################################### #

    # -------------------------------------------------------------------------
    # Analysis units:
    # -------------------------------------------------------------------------

    analysis_unit: AnalysisUnit
    analysis_units: Tuple[AnalysisUnit, ...]
    column_analysis_unit: AnalysisUnit
    cross_analysis_unit: AnalysisUnit
    index_analysis_unit: AnalysisUnit

    # -------------------------------------------------------------------------
    # Analysis unit filtering and ordering:
    # -------------------------------------------------------------------------

    top_n_units: Optional[int]
    unit_global_citation_range: Tuple[Optional[int], Optional[int]]
    unit_occurrence_range: Tuple[Optional[int], Optional[int]]
    unit_order_by: UnitOrderBy
    units_in: Optional[list[str]]

    # -------------------------------------------------------------------------

    column_unit_citation_range: Tuple[Optional[int], Optional[int]]
    column_unit_occurrence_range: Tuple[Optional[int], Optional[int]]
    column_unit_order_by: UnitOrderBy
    column_units_in: Optional[list[str]]
    top_n_column_units: Optional[int]

    # -------------------------------------------------------------------------

    index_unit_citation_range: Tuple[Optional[int], Optional[int]]
    index_unit_occurrence_range: Tuple[Optional[int], Optional[int]]
    index_units_in: Optional[list[str]]
    index_item_order_by: UnitOrderBy
    top_n_index_units: Optional[int]

    # -------------------------------------------------------------------------

    correlation_method: Correlation

    # ####################################################################### #
    #                                                                         #
    #                            CO-OCCURRENCE                                #
    #                                                                         #
    # ####################################################################### #

    minimum_pair_co_occurrence: int
    # maximum_occurrence: int = 10

    # ####################################################################### #
    #                                                                         #
    #                             TFIDF MATRIX                                #
    #                                                                         #
    # ####################################################################### #

    tfidf_binary_frequencies: bool
    tfidf_norm: Optional[str]
    tfidf_smooth_idf: bool
    tfidf_sublinear_tf: bool
    tfidf_use_idf: bool

    # ####################################################################### #
    #                                                                         #
    #                               EMERGENCE                                 #
    #                                                                         #
    # ####################################################################### #

    emergence_baseline_periods: int
    emergence_min_active_periods: int
    emergence_min_total_records: int
    emergence_novelty_threshold: float
    emergence_ratio_threshold: float
    emergence_recent_periods: int

    # ####################################################################### #
    #                                                                         #
    #                            TOPIC DYNAMICS                               #
    #                                                                         #
    # ####################################################################### #

    kleinberg_burst_rate: float
    kleinberg_burst_gamma: float
    time_window: int
    top_n_units_per_year: int

    # ####################################################################### #
    #                                                                         #
    #                             DECOMPOSITION                               #
    #                                                                         #
    # ####################################################################### #

    decomposition_algorithm: BaseEstimator
    # manifold_algorithm: Optional[BaseEstimator] = None

    # ####################################################################### #
    #                                                                         #
    #                            TOPIC MODELING                               #
    #                                                                         #
    # ####################################################################### #

    top_n_units_per_theme: int

    # ####################################################################### #
    #                                                                         #
    #                          NETWORK ALGORITHMS                             #
    #                                                                         #
    # ####################################################################### #

    # -------------------------------------------------------------------------
    # Normalization:
    # -------------------------------------------------------------------------

    association_index: AssociationIndex

    # -------------------------------------------------------------------------
    # Clustering:
    # -------------------------------------------------------------------------

    clustering: Union[
        BaseEstimator,
        GraphClusteringAlgorithm,
        dict,
    ]

    cluster_coverages: Optional[list[str]]
    cluster_names: Optional[list[str]]

    max_recursive_clustering_depth: int
    min_recursive_cluster_size: int

    # -------------------------------------------------------------------------
    # Coupling network:
    # -------------------------------------------------------------------------
    occurrence_threshold: int

    # -------------------------------------------------------------------------
    # Co-citation network:
    # -------------------------------------------------------------------------

    minimum_cited_unit_occurrences: int
    top_n_cited_units: int

    # ####################################################################### #
    #                                                                         #
    #                           REPORTING PLOTS                               #
    #                                                                         #
    # ####################################################################### #

    axes_visible: bool
    title_text: Optional[str]
    xaxes_range: Optional[Tuple[float, float]]
    xaxes_title_text: Optional[str]
    yaxes_range: Optional[Tuple[float, float]]
    yaxes_title_text: Optional[str]

    # -------------------------------------------------------------------------

    yshift: float

    # -------------------------------------------------------------------------

    color: Optional[str]
    colormap: str
    colorscale: List[Any]
    line_color: Union[str, float, Sequence[float]]
    line_width: float
    marker_size: float

    # -------------------------------------------------------------------------

    top_n_sankey_units: Tuple[int, ...]

    # -------------------------------------------------------------------------

    ranking_plotting_column = None

    # -------------------------------------------------------------------------

    pie_hole: float

    # -------------------------------------------------------------------------

    wordcloud_plot_height: float
    wordcloud_plot_width: float

    # -------------------------------------------------------------------------

    rpys_peaks: int

    # -------------------------------------------------------------------------

    top_n_sleeping_beauties: int

    # ####################################################################### #
    #                                                                         #
    #                     MAP (SCATTER) -BASED PLOTS                          #
    #                                                                         #
    # ####################################################################### #

    embedding_axes: Tuple[int, int]

    # ####################################################################### #
    #                                                                         #
    #                         NETWORK-BASED PLOTS                             #
    #                                                                         #
    # ####################################################################### #

    # -------------------------------------------------------------------------
    # Spring layout:
    # -------------------------------------------------------------------------
    spring_layout_iterations: int
    spring_layout_k: Optional[float]
    spring_layout_seed: int

    # -------------------------------------------------------------------------
    # Edges:
    # -------------------------------------------------------------------------

    edge_color_uniform: Any
    edge_colors_discrete: Tuple[Any, ...]

    # -------------------------------------------------------------------------

    edge_width_range: Tuple[float, float]
    edge_widths_discrete: Tuple[
        Union[float, int],
        Union[float, int],
        Union[float, int],
        Union[float, int],
    ]

    # -------------------------------------------------------------------------

    edge_opacity_range: Tuple[float, float]
    edge_scaling: Scaling
    edge_similarity_threshold: float

    # -------------------------------------------------------------------------

    global_top_edges: int
    top_edges_per_node: int

    # -------------------------------------------------------------------------
    # Nodes:
    # -------------------------------------------------------------------------

    node_color_uniform: Any
    node_colormap: str
    node_colors_discrete: Tuple[Any, ...]

    # -------------------------------------------------------------------------

    node_opacity_uniform: float
    node_scaling: Scaling

    # -------------------------------------------------------------------------

    node_size_metric: NodeSizeMetric
    node_size_range: Tuple[int, int]
    node_size_uniform: int

    # -------------------------------------------------------------------------

    max_node_labels: int
    node_label_max_length: int

    # -------------------------------------------------------------------------

    min_node_degree: int
    top_n_nodes: int

    # -------------------------------------------------------------------------
    # Textfont:
    # -------------------------------------------------------------------------

    textfont_color_uniform: Union[str, float, Sequence[float]]
    textfont_opacity_range: Tuple[float, float]
    textfont_opacity_uniform: float
    textfont_size_range: Tuple[float, float]
    textfont_size_uniform: float

    # -------------------------------------------------------------------------
    # Density plot:
    # -------------------------------------------------------------------------

    contour_opacity: float
    kernel_bandwidth: float

    # ####################################################################### #
    #                                                                         #
    #                              THESAURUS                                  #
    #                                                                         #
    # ####################################################################### #

    thesaurus_file: ThFile

    preferred_key: str
    variant_keys: tuple[str, ...]

    word: str
    pattern: Union[str, tuple[str, ...]]
    replacement: str
    regex_flags: int = 0
    regex_search: bool = False
    case_sensitive: bool = False

    similarity_cutoff: float = 85.0
    fuzzy_threshold: float = 95.0

    # ####################################################################### #
    #                                                                         #
    #                               ZOTERO                                    #
    #                                                                         #
    # ####################################################################### #

    zotero_api_key: Optional[str] = None
    zotero_library_id: Optional[str] = None
    zotero_library_type: Optional[str] = None

    # ####################################################################### #
    #                                                                         #
    #                             CLASS  METHODS                              #
    #                                                                         #
    # ####################################################################### #

    def __init__(self, **kwargs):
        self.update(**kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self.__annotations__:
                raise ValueError(f"Unknown parameter: {key}")
            setattr(self, key, value)
        return self
