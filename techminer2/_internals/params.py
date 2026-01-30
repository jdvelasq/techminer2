from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from sklearn.base import BaseEstimator  # type: ignore

from techminer2 import RecordsOrderBy


@dataclass
class Params:

    #
    # A
    #
    axes_visible: bool = False
    association_index: Optional[str] = None

    #
    # B
    #
    baseline_periods: int = 3
    binary_term_frequencies: bool = False

    #
    # C
    #
    case_sensitive: bool = False
    citation_threshold: int = 0
    cluster_coverages: Optional[list[str]] = None
    cluster_names: Optional[list[str]] = None
    clustering_algorithm_or_dict: Optional[Union[str, dict]] = None
    color: Optional[str] = None
    colored_output: bool = True
    colored_stderr: bool = True
    colormap: str = "Blues"
    column: Optional[str] = None
    contour_opacity: float = 0.6
    core_area: Optional[str] = None
    correlation_method: str = "pearson"
    cumulative_sum: bool = False
    cutoff_threshold: float = 85.0

    #
    # D
    #
    draw_arrows: bool = False
    decomposition_algorithm: Optional[BaseEstimator] = None

    #
    # E
    #
    edge_colors: Optional[list[Any]] = None
    edge_top_n: Optional[int] = None
    edge_width_range: Tuple[float, float] = (0.5, 0.8)
    edge_widths: Tuple[float, float, float, float] = (0.5, 0.8, 1.0, 1.2)
    edge_similarity_threshold: float = 0.0
    edge_opacity_range: Tuple[float, float] = (0.1, 0.9)

    #
    # F
    #
    field: Optional[str] = None

    #
    # I
    #
    initial_newline: bool = False

    #
    # K
    #
    kernel_bandwidth: float = 0.1
    keys_order_by: str = "alphabetical"

    #
    # L
    #
    line_color: Union[str, float, Sequence[float]] = "black"
    line_width: float = 1.5

    #
    # M
    #
    manifold_algorithm: Optional[BaseEstimator] = None
    marker_size: float = 7
    match_threshold: float = 95.0
    minimum_terms_in_cluster: int = 5
    minimum_number_of_clusters: int = 10
    maximum_occurrence: int = 10

    #
    # N
    #
    node_colors: Optional[List[Union[str, float, Sequence[float]]]] = None
    node_size: int = 10
    node_size_range: Tuple[int, int] = (5, 20)
    novelty_threshold: float = 0.15
    n_chars: int = 100
    n_contexts: int = 10

    #
    # O
    #
    occurrence_threshold: int = 2
    other_field: Optional[str] = None
    other_term_citations_range: Tuple[Optional[int], Optional[int]] = (None, None)
    other_term_occurrences_range: Tuple[Optional[int], Optional[int]] = (None, None)
    other_terms_in: Optional[list[str]] = None
    other_terms_order_by: Optional[str] = None
    other_top_n: Optional[int] = None

    #
    # P
    #
    pattern: Optional[str] = None
    periods_with_at_least_one_record: int = 3
    pie_hole: float = 0.4
    plot_dimensions: Tuple[int, int] = (0, 1)

    #
    # Q
    #
    query_expression: Optional[str] = None
    quiet: bool = False

    #
    # R
    #
    ratio_threshold: float = 0.5
    recent_periods: int = 3
    record_citations_range: Tuple[Optional[int], Optional[int]] = (None, None)
    record_years_range: Tuple[Optional[int], Optional[int]] = (None, None)
    records_match: Optional[Dict[str, List[str]]] = None
    records_order_by: RecordsOrderBy = RecordsOrderBy.DATE_NEWEST
    regex_flags: int = 0
    regex_search: bool = False
    replacement: Optional[str] = None
    root_directory: str = "./"

    #
    # S
    #
    source_field: Optional[str] = None
    source_fields: Optional[list[str]] = None
    spring_layout_iterations: int = 50
    spring_layout_k: Optional[float] = 0.1
    spring_layout_seed: int = 42
    stemming_fn: Optional[Callable] = None

    #
    # T
    #
    target_field: Optional[str] = None
    term_citations_range: Tuple[Optional[int], Optional[int]] = (None, None)
    term_counters: bool = True
    term_occurrences_range: Tuple[Optional[int], Optional[int]] = (None, None)
    terms_in: Optional[list[str]] = None
    terms_order_by: Optional[str] = None
    terms_per_year: int = 5
    textfont_color: Union[str, float, Sequence[float]] = "#465c6b"
    textfont_opacity_range: Tuple[float, float] = (0.5, 1)
    textfont_opacity: float = 1.0
    textfont_size_range: Tuple[int, int] = (8, 16)
    textfont_size: float = 10
    tfidf_norm: Optional[str] = None
    tfidf_smooth_idf: bool = False
    tfidf_sublinear_tf: bool = False  # sublinear_tf
    tfidf_use_idf: bool = False  # using_idf_reweighting
    thesaurus_file: str = "no_name.the.txt"
    time_window: int = 2
    title_text: Optional[str] = None
    top_n: Optional[int] = None
    top_terms_by_theme: int = 5
    total_records_threshold: int = 7
    tqdm_disable: bool = False
    transformation_function: Optional[Callable[[Any], Any]] = None

    #
    # U
    #
    unit_of_analysis: Optional[str] = None

    #
    # V
    #

    #
    # X
    #
    xaxes_range: Optional[Tuple[float, float]] = None
    xaxes_title_text: Optional[str] = None

    #
    # Y
    #
    yaxes_range: Optional[Tuple[float, float]] = None
    yaxes_title_text: Optional[str] = None
    yshift: float = 4

    #
    # W
    #
    word: Optional[str] = None
    word_length: int = 50

    #
    # Z
    #
    zotero_api_key: Optional[str] = None
    zotero_library_id: Optional[str] = None
    zotero_library_type: Optional[str] = None

    # -------------------------------------------------------------------------
    # PLOT PROPERTIES:
    # -------------------------------------------------------------------------

    #
    fig_width: float = 400
    fig_height: float = 400
    #

    # -------------------------------------------------------------------------
    def __init__(self, **kwargs):
        self.update(**kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self.__annotations__:
                raise ValueError(f"Unknown parameter: {key}")
            setattr(self, key, value)
        return self
