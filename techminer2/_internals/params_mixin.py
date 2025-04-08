# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes
"""Define a mixin class for input functions."""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


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
    clustering_algorithm_or_dict: Optional[str] = None
    color: Optional[str] = None
    colormap: str = "Blues"
    contour_opacity: float = 0.6
    correlation_method: str = "pearson"
    cumulative_sum: bool = False

    #
    # D
    #
    database: str = "main"
    draw_arrows: bool = False
    decomposition_algorithm = None

    #
    # E
    #
    edge_colors: Optional[List] = None
    edge_top_n: Optional[int] = None
    edge_width_range: Tuple[float, float] = (0.5, 0.8)
    edge_widths: Tuple[float, float, float, float] = (0.5, 0.8, 1.0, 1.2)
    edge_similarity_threshold: float = 0.0
    edge_opacity_range: Tuple[float, float] = (0.1, 0.9)

    #
    # F
    #
    field: Optional[str] = None  # with_selected_field
    transformation_function = None

    #
    # K
    #
    kernel_bandwidth: float = 0.1
    keys_order_by: str = "alphabetical"

    #
    # L
    #
    line_color: str = "black"
    line_width: float = 1.5

    #
    # M
    #
    manifold_algorithm = None
    marker_size: float = 7
    match_threshold: float = 80.0
    maximum_occurrence: int = 10

    #
    # N
    #
    initial_newline: bool = False
    node_colors: Optional[List] = None
    node_size: int = 10
    node_size_range: Tuple[int, int] = (5, 20)
    novelty_threshold: float = 0.15
    n_chars: int = 100

    #
    # O
    #
    occurrence_threshold: int = 2
    other_field: Optional[str] = None
    other_term_citations_range: Tuple[Optional[int], Optional[int]] = (None, None)
    other_term_occurrences_range: Tuple[Optional[int], Optional[int]] = (None, None)
    other_terms_in: Optional[list] = None
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
    record_filters: Optional[dict] = None
    record_years_range: Tuple[Optional[int], Optional[int]] = (None, None)
    records_match: Optional[Dict[str, List[str]]] = None
    records_order_by: Optional[str] = None  # order_records_by
    regex_flags: int = 0  # with_regex_flags
    regex_search: bool = False
    replacement: Optional[str] = None
    root_directory: str = "./"  # root_dir
    row_normalization: Optional[str] = None

    #
    # S
    #
    # show_progress: bool = True
    smooth_idf_weights: bool = False
    spring_layout_iterations: int = 50
    spring_layout_k: float = 0.1
    spring_layout_seed: int = 42
    stemming_fn: Optional[callable] = None
    sublinear_tf_scaling: bool = False  # sublinear_tf

    #
    # T
    #
    term_citations_range: Tuple[Optional[int], Optional[int]] = (None, None)
    term_counters: bool = True
    term_occurrences_range: Tuple[Optional[int], Optional[int]] = (None, None)
    terms_in: Optional[list] = None
    terms_order_by: Optional[str] = None
    terms_per_year: int = 5
    textfont_color: str = "#465c6b"
    textfont_opacity_range: Tuple[float, float] = (0.5, 1)
    textfont_opacity: float = 1.0
    textfont_size_range: Tuple[int, int] = (8, 16)
    textfont_size: float = 10
    thesaurus_file: str = "no_name.the.txt"
    time_window: int = 2
    title_text: Optional[str] = None
    top_n: Optional[int] = None
    top_terms_by_theme: int = 5
    total_records_threshold: int = 7
    tqdm_disable: bool = False

    #
    # U
    #
    unit_of_analysis: Optional[str] = None
    use_idf: bool = False  # using_idf_reweighting

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

    ##########
    ##########
    ##########
    ##########

    # -------------------------------------------------------------------------
    # PLOT PROPERTIES:
    # -------------------------------------------------------------------------

    #
    width: float = 400
    height: float = 400
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


class ParamsMixin:

    def __init__(self, **kwargs):
        self.params = Params()
        self.update(**kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self.params, key, value)
        return self

    #
    # H
    #
    def having_case_sensitive(self, case_sensitive):
        self.params.case_sensitive = case_sensitive
        return self

    def having_citation_threshold(self, threshold):
        self.params.citation_threshold = threshold
        return self

    def having_keys_ordered_by(self, order):
        self.params.keys_order_by = order
        return self

    def having_match_threshold(self, threshold):
        self.params.match_threshold = threshold
        return self

    def having_maximum_occurrence(self, maximum_occurrence):
        self.params.maximum_occurrence = maximum_occurrence
        return self

    def having_n_chars(self, n_chars):
        self.params.n_chars = n_chars
        return self

    def having_occurrence_threshold(self, threshold):
        self.params.occurrence_threshold = threshold
        return self

    def having_other_term_citations_between(self, start, end):
        self.params.other_term_citations_range = (start, end)
        return self

    def having_other_term_occurrences_between(self, start, end):
        self.params.other_term_occurrences_range = (start, end)
        return self

    def having_other_terms_in(self, term_list):
        self.params.other_terms_in = term_list
        return self

    def having_other_terms_in_top(self, n):
        self.params.other_top_n = n
        return self

    def having_other_terms_ordered_by(self, criteria):
        self.params.other_terms_order_by = criteria
        return self

    def having_pattern(self, pattern):
        self.params.pattern = pattern
        return self

    def having_regex_flags(self, flags):
        self.params.regex_flags = flags
        return self

    def having_regex_search(self, regex_search):
        self.params.regex_search = regex_search
        return self

    def having_replacement(self, replacement):
        self.params.replacement = replacement
        return self

    def having_term_citations_between(self, start, end):
        self.params.term_citations_range = (start, end)
        return self

    def having_term_occurrences_between(self, start, end):
        self.params.term_occurrences_range = (start, end)
        return self

    def having_terms_associated_with(self, terms):
        self.params.terms_associated_with = terms
        return self

    def having_terms_in(self, term_list):
        self.params.terms_in = term_list
        return self

    def having_terms_in_top(self, n):
        self.params.top_n = n
        return self

    def having_terms_like(self, pattern):
        self.params.pattern = pattern
        return self

    def having_terms_ordered_by(self, criteria):
        self.params.terms_order_by = criteria
        return self

    def having_terms_per_year(self, n):
        self.params.terms_per_year = n
        return self

    def having_word(self, word):
        self.params.word = word
        return self

    #
    # S
    #
    ## def showing_progress(self, progress):
    ##     self.params.show_progress = progress
    ##     return self

    #
    # U
    #
    def unit_of_analysis(self, unit_of_analysis):
        self.params.unit_of_analysis = unit_of_analysis
        return self

    def using_association_index(self, association_index):
        self.params.association_index = association_index
        return self

    def using_clustering_algorithm_or_dict(self, clustering_algorithm_or_dict):
        self.params.clustering_algorithm_or_dict = clustering_algorithm_or_dict
        return self

    def using_decomposition_algorithm(self, algorithm):
        self.params.decomposition_algorithm = algorithm
        return self

    def using_draw_arrows(self, draw):
        self.params.draw_arrows = draw
        return self

    def using_axes_visible(self, visible):
        self.params.axes_visible = visible
        return self

    def using_baseline_periods(self, periods):
        self.params.baseline_periods = periods
        return self

    def using_binary_term_frequencies(self, binary):
        self.params.binary_term_frequencies = binary
        return self

    def using_color(self, color):
        self.params.color = color
        return self

    def using_colormap(self, colormap):
        self.params.colormap = colormap
        return self

    def using_contour_opacity(self, opacity):
        self.params.contour_opacity = opacity
        return self

    def using_edge_colors(self, colors):
        self.params.edge_colors = colors
        return self

    def using_edge_similarity_threshold(self, threshold):
        self.params.edge_similarity_threshold = threshold
        return self

    def using_edge_top_n(self, top_n):
        self.params.edge_top_n = top_n
        return self

    def using_edge_opacity_range(self, min_opacity, max_opacity):
        self.params.edge_opacity_range = (min_opacity, max_opacity)
        return self

    def using_edge_width_range(self, min_width, max_width):
        self.params.edge_width_range = (min_width, max_width)
        return self

    def using_edge_widths(self, widths):
        self.params.edge_widths = widths
        return self

    def using_idf_reweighting(self, smooth):  # use_idf
        self.params.use_idf = smooth
        return self

    def using_idf_weights_smoothing(self, smooth):  # smooth_idf
        self.params.smooth_idf_weights = smooth
        return self

    def using_kernel_bandwidth(self, bandwidth):
        self.params.kernel_bandwidth = bandwidth
        return self

    def using_line_color(self, color):
        self.params.line_color = color
        return self

    def using_line_width(self, width):
        self.params.line_width = width
        return self

    def using_manifold_algorithm(self, algorithm):
        self.params.manifold_algorithm = algorithm
        return self

    def using_marker_size(self, size):
        self.params.marker_size = size
        return self

    def using_node_colors(self, colors):
        self.params.node_colors = colors
        return self

    def using_node_size(self, size):
        self.params.node_size = size
        return self

    def using_node_size_range(self, min_size, max_size):
        self.params.node_size_range = (min_size, max_size)
        return self

    def using_novelty_threshold(self, threshold):
        self.params.novelty_threshold = threshold
        return self

    def using_periods_with_at_least_one_record(self, periods):
        self.params.periods_with_at_least_one_record = periods
        return self

    def using_pie_hole(self, pie_hole):
        self.params.pie_hole = pie_hole
        return self

    def using_plot_dimensions(self, dim_x, dim_y):
        self.params.plot_dimensions = (dim_x, dim_y)
        return self

    def using_plot_height(self, height):
        self.params.height = height
        return self

    def using_plot_width(self, width):
        self.params.width = width
        return self

    def using_ratio_threshold(self, threshold):
        self.params.ratio_threshold = threshold
        return self

    def using_recent_periods(self, periods):
        self.params.recent_periods = periods
        return self

    def using_row_normalization(self, normalization):  # nowm: L1, L2, None
        self.params.row_normalization = normalization
        return self

    def using_spring_layout_iterations(self, iterations):
        self.params.spring_layout_iterations = iterations
        return self

    def using_spring_layout_k(self, k):
        self.params.spring_layout_k = k
        return self

    def using_spring_layout_seed(self, seed):
        self.params.spring_layout_seed = seed
        return self

    def using_term_counters(self, counters):
        self.params.term_counters = counters
        return self

    def using_textfont_color(self, color):
        self.params.textfont_color = color
        return self

    def using_textfont_opacity(self, opacity):
        self.params.textfont_opacity = opacity
        return

    def using_textfont_opacity_range(self, min_opacity, max_opacity):
        self.params.textfont_opacity_range = (min_opacity, max_opacity)
        return self

    def using_textfont_size(self, size):
        self.params.textfont_size = size
        return self

    def using_textfont_size_range(self, min_size, max_size):
        self.params.textfont_size_range = (min_size, max_size)
        return self

    def using_title_text(self, text):
        self.params.title_text = text
        return self

    def using_top_terms_by_theme(self, n):
        self.params.top_terms_by_theme = n
        return self

    def using_total_records_threshold(self, threshold):
        self.params.total_records_threshold = threshold
        return self

    def using_xaxes_range(self, x_min, x_max):
        self.params.xaxes_range = (x_min, x_max)
        return self

    def using_xaxes_title_text(self, text):
        self.params.xaxes_title_text = text
        return self

    def using_yaxes_range(self, y_min, y_max):
        self.params.yaxes_range = (y_min, y_max)
        return self

    def using_yaxes_title_text(self, text):
        self.params.yaxes_title_text = text
        return self

    def using_yshift(self, yshift):
        self.params.yshift = yshift
        return self

    def using_sublinear_tf_scaling(self, scaling):
        self.params.sublinear_tf_scaling = scaling
        return self

    #
    # W
    #
    def where_database_is(self, database):
        self.params.database = database
        return self

    def where_root_directory_is(self, directory):
        self.params.root_directory = directory
        return self

    def where_record_citations_range_is(self, start, end):
        self.params.record_citations_range = (start, end)
        return self

    def where_record_years_range_is(self, start, end):
        self.params.record_years_range = (start, end)
        return self

    def where_records_match(self, records_match):
        self.params.records_match = records_match
        return self

    def where_records_ordered_by(self, records_order_by):
        self.params.records_order_by = records_order_by
        return self

    def with_abstract_having_pattern(self, pattern):
        self.params.pattern = pattern
        return self

    def with_correlation_method(self, method):
        self.params.correlation_method = method
        return self

    def with_cumulative_sum(self, cumulative_sum):
        self.params.cumulative_sum = cumulative_sum
        return self

    def with_field(self, field):
        self.params.field = field
        return self

    def with_field_pattern(self, pattern):
        self.params.pattern = pattern
        return self

    def with_initial_newline(self, initial_newline):
        self.params.initial_newline = initial_newline
        return self

    def with_other_field(self, field):
        self.params.other_field = field
        return self

    def with_query_expression(self, expr):
        self.params.query_expression = expr
        return self

    def with_terms_having_stem_match(self, stem):
        self.params.pattern = stem
        return self

    def with_thesaurus_file(self, thesaurus_file):
        self.params.thesaurus_file = thesaurus_file
        return self

    def with_time_window(self, time_window):
        self.params.time_window = time_window
        return self

    def with_transformation_function(self, transformation_function):
        self.params.transformation_function = transformation_function
        return self
