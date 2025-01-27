# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes
"""Define a mixin class for input functions."""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class Params:

    # -------------------------------------------------------------------------
    # DATABASE PARAMS:
    # -------------------------------------------------------------------------
    database: str = "main"
    root_dir: str = "./"
    record_citations_range: Tuple[Optional[int], Optional[int]] = (None, None)
    record_years_range: Tuple[Optional[int], Optional[int]] = (None, None)
    record_filters: Optional[dict] = None
    records_order_by: Optional[str] = None
    records_match: Optional[Dict[str, List[str]]] = None

    # -------------------------------------------------------------------------
    # FIELD SELECTORS:
    # -------------------------------------------------------------------------
    dest_field: Optional[str] = None
    fill_field: Optional[str] = None
    from_field: Optional[str] = None
    source_field: Optional[str] = None
    with_field: Optional[str] = None

    # -------------------------------------------------------------------------
    # TERM SEARCH:
    # -------------------------------------------------------------------------
    case_sensitive: bool = False
    regex_flags: int = 0
    term_pattern: Optional[str] = None

    # -------------------------------------------------------------------------
    # TERM SEARCH:
    # -------------------------------------------------------------------------
    selected_terms: Optional[list] = None
    term_citations_range: Tuple[Optional[int], Optional[int]] = (None, None)
    term_occurrences_range: Tuple[Optional[int], Optional[int]] = (None, None)
    terms_in: Optional[list] = None
    terms_order_by: Optional[str] = None
    top_n_terms: Optional[int] = None

    # -------------------------------------------------------------------------
    # FIELD TRANSFORM:
    # -------------------------------------------------------------------------
    func = None

    # -------------------------------------------------------------------------
    # QUERY:
    # -------------------------------------------------------------------------
    query_expr: Optional[str] = None

    # -------------------------------------------------------------------------
    # TFIDF MATRIX:
    # -------------------------------------------------------------------------
    binary_term_frequencies: bool = False
    row_normalization: Optional[str] = None
    use_idf: bool = False  # using_idf_reweighting
    smooth_idf_weights: bool = False
    sublinear_tf_scaling: bool = False  # sublinear_tf

    # -------------------------------------------------------------------------
    # COUNTERS IN AXES:
    # -------------------------------------------------------------------------
    counters_in_axes: bool = True

    # -------------------------------------------------------------------------
    # PLOT TITLES:
    # -------------------------------------------------------------------------
    title_text: Optional[str] = None
    xaxes_title_text: Optional[str] = None
    yaxes_title_text: Optional[str] = None

    # -------------------------------------------------------------------------
    # PLOT PROPERTIES:
    # -------------------------------------------------------------------------
    line_width: float = 1.5
    marker_size: float = 7
    textfont_size: float = 10
    yshift: float = 4
    #
    width: float = 400
    height: float = 400
    #
    colormap: str = "Blues"
    #
    pie_hole: float = 0.4


class InputFunctionsMixin:

    def __init__(self):
        self.params = Params()

    def update_params(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self.params, key, value)
        return self

    # -------------------------------------------------------------------------
    # COUNTERS IN AXES::
    # -------------------------------------------------------------------------
    def using_counters_in_axes(self, counters_in_axes):
        self.params.counters_in_axes = counters_in_axes
        return self

    # -------------------------------------------------------------------------
    # FIELD SELECTORS:
    # -------------------------------------------------------------------------
    def as_field(self, field):
        self.params.dest_field = field
        return self

    def compare_field(self, field):
        self.params.source_field = field
        return self

    def fill_na_in_field(self, field):
        self.params.fill_field = field
        return self

    def to_field(self, field):
        self.params.dest_field = field
        return self

    def with_source_field(self, field):
        self.params.source_field = field
        return self

    def with_dest_field(self, field):
        self.params.dest_field = field
        return self

    def using_values_from_field(self, field):
        self.params.with_field = field
        return self

    # -------------------------------------------------------------------------
    # FIELD TRANSFORM:
    # -------------------------------------------------------------------------
    def transform_with(self, func):
        self.params.func = func
        return self

    # -------------------------------------------------------------------------
    # TERM EXTRACTORS:
    # -------------------------------------------------------------------------
    def having_terms_in(self, term_list):
        self.params.terms_in = term_list
        return self

    def matching_terms_with(self, terms):
        self.params.selected_terms = terms
        return self

    def order_terms_by(self, criteria):
        self.params.terms_order_by = criteria
        return self

    def select_top_n_terms(self, n):
        self.params.top_n_terms = n
        return self

    def with_case_sensitive(self, case_sensitive):
        self.params.case_sensitive = case_sensitive
        return self

    def with_regex_flags(self, flags):
        self.params.regex_flags = flags
        return self

    def having_term_citations_between(self, start, end):
        self.params.term_citations_range = (start, end)
        return self

    def with_terms_having_pattern(self, pattern):
        self.params.term_pattern = pattern
        return self

    def having_term_occurrences_between(self, start, end):
        self.params.term_occurrences_range = (start, end)
        return self

    # -------------------------------------------------------------------------
    # QUERY:
    # -------------------------------------------------------------------------
    def with_query_expression(self, expr):
        self.params.query_expr = expr
        return self

    # -------------------------------------------------------------------------
    # DATABASE PARAMS:
    # -------------------------------------------------------------------------
    def where_directory_is(self, directory):
        self.params.root_dir = directory
        return self

    def where_database_is(self, database):
        self.params.database = database
        return self

    def where_record_years_between(self, start, end):
        self.params.record_years_range = (start, end)
        return self

    def where_record_citations_between(self, start, end):
        self.params.record_citations_range = (start, end)
        return self

    def order_records_by(self, records_order_by):
        self.params.records_order_by = records_order_by
        return self

    def where_records_match(self, records_match):
        self.params.records_match = records_match
        return self

    # -------------------------------------------------------------------------
    # PLOTS:
    # -------------------------------------------------------------------------
    def using_colormap(self, colormap):
        self.params.colormap = colormap
        return self

    def using_line_width(self, width):
        self.params.line_width = width
        return self

    def using_marker_size(self, size):
        self.params.marker_size = size
        return self

    def using_pie_hole(self, pie_hole):
        self.params.pie_hole = pie_hole
        return self

    def using_plot_width(self, width):
        self.params.width = width
        return self

    def using_plot_height(self, height):
        self.params.height = height
        return self

    def using_textfont_size(self, size):
        self.params.textfont_size = size
        return self

    def using_title_text(self, text):
        self.params.title_text = text
        return self

    def using_xaxes_title_text(self, text):
        self.params.xaxes_title_text = text
        return self

    def using_yaxes_title_text(self, text):
        self.params.yaxes_title_text = text
        return self

    def using_yshift(self, yshift):
        self.params.yshift = yshift
        return self

    # -------------------------------------------------------------------------
    # TFIDF MATRIX:
    # -------------------------------------------------------------------------
    def using_binary_term_frequencies(self, binary):
        self.params.binary_term_frequencies = binary
        return self

    def using_row_normalization(self, normalization):  # nowm: L1, L2, None
        self.params.row_normalization = normalization
        return self

    def using_idf_reweighting(self, smooth):  # use_idf
        self.params.use_idf = smooth
        return self

    def using_idf_weights_smoothing(self, smooth):  # smooth_idf
        self.params.smooth_idf_weights = smooth
        return self

    def using_sublinear_tf_scaling(self, scaling):  # sublinear_tf
        self.params.sublinear_tf_scaling = scaling
        return self
