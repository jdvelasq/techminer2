from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union, cast

import pandas as pd  # type: ignore
from sklearn.base import BaseEstimator  # type: ignore
from typing_extensions import Self

from tm2p._intern.valid import (  # check_required_base_estimator,
    check_optional_positive_float,
    check_optional_positive_int,
    check_optional_str,
    check_optional_str_list,
    check_plotly_color,
    check_required_analysis_unit,
    check_required_bool,
    check_required_color_list,
    check_required_corpus_field_enum,
    check_required_float,
    check_required_float_0_1,
    check_required_float_0_1_range,
    check_required_float_range,
    check_required_int,
    check_required_int_range,
    check_required_non_negative_float,
    check_required_non_negative_int,
    check_required_open_ended_int_range,
    check_required_positive_float,
    check_required_positive_float_range,
    check_required_positive_int,
    check_required_positive_int_tuple,
    check_required_positive_number_range,
    check_required_str,
    check_required_str_or_str_tuple,
    check_required_str_tuple,
    check_required_unit_order_by_enum,
    check_tuple_of_ordered_four_floats,
)
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

from .params import Params


class SortAxesMixin:

    def sort_columns(self, data_frame):
        counters = pd.DataFrame({"term": data_frame.columns.tolist()})
        counters = self._extract_term_occurrences(counters)
        counters = self._extract_citation_counts(counters)
        sorted_topics = self._rank_terms_by_count_and_citations(counters)
        data_frame = data_frame[sorted_topics]
        return data_frame

    def sort_index(self, data_frame):
        counters = pd.DataFrame({"term": data_frame.index.tolist()})
        counters = self._extract_term_occurrences(counters)
        counters = self._extract_citation_counts(counters)
        sorted_topics = self._rank_terms_by_count_and_citations(counters)
        data_frame = data_frame.loc[sorted_topics, :]
        return data_frame

    def _rank_terms_by_count_and_citations(self, counters):
        counters = counters.sort_values(
            by=["OCC", "citations", "term"], ascending=[False, False, True]
        )
        sorted_topics = counters.term.tolist()
        return sorted_topics

    def _extract_citation_counts(self, counters):
        counters["citations"] = counters.term.str.split()
        counters["citations"] = counters["citations"].map(lambda x: x[-1])
        counters["citations"] = counters["citations"].str.split(":")
        counters["citations"] = counters["citations"].map(lambda x: x[1]).astype(int)
        return counters

    def _extract_term_occurrences(self, counters):
        counters["OCC"] = counters.term.str.split()
        counters["OCC"] = counters["OCC"].map(lambda x: x[-1])
        counters["OCC"] = counters["OCC"].str.split(":")
        counters["OCC"] = counters["OCC"].map(lambda x: x[0]).astype(int)
        return counters


class ParamsMixin:

    def __init__(self, **kwargs):
        self.params = Params()
        self.update(**kwargs)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self.params, key, value)
        return self

    # ==========================================================================
    # HAVING_* → Item filtering (WHICH items?)
    # ==========================================================================

    #
    # Generic parameters:
    #

    def using_counters(self, counters: bool) -> Self:
        counters = check_required_bool(
            value=counters,
            param_name="counters",
        )
        self.params.use_counters = counters
        return self

    def with_core_area(self, core_area: Optional[str]) -> Self:
        core_area = check_optional_str(
            value=core_area,
            param_name="core_area",
        )
        self.params.core_area = core_area
        return self

    # ####################################################################### #
    #                                                                         #
    #                          DATABASE PARAMETERS                            #
    #                                                                         #
    # ####################################################################### #

    #
    # Record filtering:
    #
    def where_root_directory(self, root_directory: str) -> Self:
        root_directory = check_required_str(
            value=root_directory,
            param_name="root_directory",
        )
        self.params.root_directory = root_directory
        return self

    def where_record_global_citations_range(
        self, start: Optional[int], end: Optional[int]
    ) -> Self:
        self.params.record_citations_range = check_required_open_ended_int_range(
            (start, end), "record_citations_range"
        )
        return self

    def where_record_years_range(
        self, start: Optional[int], end: Optional[int]
    ) -> Self:
        (start, end) = check_required_open_ended_int_range(
            (start, end), "record_years_range"
        )
        self.params.record_years_range = (start, end)
        return self

    def where_records_match(
        self, records_match: Optional[Dict[Field, List[str]]]
    ) -> Self:
        self.params.records_match = records_match
        return self

    def where_records_ordered_by(self, records_order_by: RecordOrderBy) -> Self:
        if not isinstance(records_order_by, RecordOrderBy):
            raise TypeError(
                "records_order_by must be an instance of RecordsOrderBy enum"
            )
        self.params.records_order_by = records_order_by
        return self

    #
    # Database operations:
    #
    def with_source_field(self, field: Field) -> Self:
        field = check_required_corpus_field_enum(
            value=field,
            param_name="source_field",
        )
        self.params.source_field = field
        return self

    def with_source_fields(self, fields: tuple[Field, ...]) -> Self:
        for field in fields:
            check_required_corpus_field_enum(
                value=field,
                param_name="source_fields",
            )
        self.params.source_fields = fields
        return self

    def with_target_field(self, field: Field) -> Self:
        field = check_required_corpus_field_enum(
            value=field,
            param_name="target_field",
        )
        self.params.target_field = field
        return self

    def with_query_expression(self, query_expression: str) -> Self:
        query_expression = check_required_str(
            value=query_expression,
            param_name="query_expression",
        )
        self.params.query_expression = query_expression
        return self

    # ####################################################################### #
    #                                                                         #
    #                      PORTFOLIO GENERIC PARAMETERS                       #
    #                                                                         #
    # ####################################################################### #

    # -------------------------------------------------------------------------
    # Analysis units:
    # -------------------------------------------------------------------------

    def with_analysis_unit(self, analysis_unit: AnalysisUnit) -> Self:
        if not isinstance(analysis_unit, AnalysisUnit):
            raise TypeError("analysis_unit must be an instance of AnalysisUnit enum")
        self.params.analysis_unit = analysis_unit
        return self

    def with_column_analysis_unit(self, unit: AnalysisUnit) -> Self:
        unit = check_required_analysis_unit(
            unit=unit,
            param_name="unit",
        )
        self.params.column_analysis_unit = unit
        return self

    def with_cross_analysis_unit(self, unit: AnalysisUnit) -> Self:
        unit = check_required_analysis_unit(
            unit=unit,
            param_name="unit",
        )
        self.params.cross_analysis_unit = unit
        return self

    def with_index_analysis_unit(self, unit: AnalysisUnit) -> Self:
        unit = check_required_analysis_unit(
            unit=unit,
            param_name="index_field",
        )
        self.params.index_analysis_unit = unit
        return self

    # -------------------------------------------------------------------------
    # Analysis unit filtering and ordering:
    # -------------------------------------------------------------------------

    def having_top_n_units(self, n: Optional[int]) -> Self:
        n = check_optional_positive_int(
            value=n,
            param_name="n",
        )
        self.params.top_n_units = n
        return self

    def having_unit_global_citation_between(
        self, start: Optional[int], end: Optional[int]
    ) -> Self:
        start, end = check_required_open_ended_int_range(
            (start, end), "unit_global_citation_range"
        )
        self.params.unit_global_citation_range = (start, end)
        return self

    def having_unit_occurrence_between(
        self, start: Optional[int], end: Optional[int]
    ) -> Self:
        start, end = check_required_open_ended_int_range(
            (start, end), "item_occurrences_range"
        )
        self.params.unit_occurrence_range = (start, end)
        return self

    def having_units_ordered_by(self, unit_order_by: UnitOrderBy) -> Self:
        unit_order_by = check_required_unit_order_by_enum(
            value=unit_order_by,
            param_name="unit_order_by",
        )
        self.params.unit_order_by = unit_order_by
        return self

    def having_units_in(self, units: Optional[list[str]]) -> Self:
        units = check_optional_str_list(
            value=units,
            param_name="units",
        )
        self.params.units_in = units
        return self

    # -------------------------------------------------------------------------

    def having_column_unit_citation_between(
        self, start: Optional[int], end: Optional[int]
    ) -> Self:
        start, end = check_required_open_ended_int_range(
            (start, end), "column_unit_citation_range"
        )
        self.params.column_unit_citation_range = (start, end)
        return self

    def having_column_unit_occurrence_between(
        self, start: Optional[int], end: Optional[int]
    ) -> Self:
        start, end = check_required_open_ended_int_range(
            (start, end), "having_column_unit_occurrence_between"
        )
        self.params.column_unit_occurrence_range = (start, end)
        return self

    def having_column_units_in(self, units_in: Optional[list[str]]) -> Self:
        units_in = check_optional_str_list(
            value=units_in,
            param_name="units_in",
        )
        self.params.column_units_in = units_in
        return self

    def having_column_units_ordered_by(self, column_unit_order_by: UnitOrderBy) -> Self:
        column_unit_order_by = check_required_unit_order_by_enum(
            value=column_unit_order_by,
            param_name="column_unit_order_by",
        )
        self.params.column_unit_order_by = column_unit_order_by
        return self

    def having_column_units_in_top(self, top_n_column_units: Optional[int]) -> Self:
        top_n_column_units = check_optional_positive_int(
            value=top_n_column_units,
            param_name="column_top_n",
        )
        self.params.top_n_column_units = top_n_column_units
        return self

    # -------------------------------------------------------------------------

    def having_index_unit_citation_between(
        self, start: Optional[int], end: Optional[int]
    ) -> Self:
        start, end = check_required_open_ended_int_range(
            (start, end), "index_item_citations_range"
        )
        self.params.index_unit_citation_range = (start, end)
        return self

    def having_index_unit_occurrence_between(
        self, start: Optional[int], end: Optional[int]
    ) -> Self:
        start, end = check_required_open_ended_int_range(
            (start, end), "index_unit_occurrence_range"
        )
        self.params.index_unit_occurrence_range = (start, end)
        return self

    def having_index_units_in(self, index_units_in: Optional[list[str]]) -> Self:
        index_units_in = check_optional_str_list(
            value=index_units_in,
            param_name="index_units_in",
        )
        self.params.index_units_in = index_units_in
        return self

    def having_index_units_ordered_by(self, index_units_order_by: UnitOrderBy) -> Self:
        index_units_order_by = check_required_unit_order_by_enum(
            value=index_units_order_by,
            param_name="index_items_order_by",
        )
        self.params.index_item_order_by = index_units_order_by
        return self

    def having_index_units_in_top(self, top_n_index_units: Optional[int]) -> Self:
        top_n_index_units = check_optional_positive_int(
            value=top_n_index_units,
            param_name="index_top_n",
        )
        self.params.top_n_index_units = top_n_index_units
        return self

    # -------------------------------------------------------------------------

    def with_correlation_method(self, correlation_method: Correlation) -> Self:
        if not isinstance(correlation_method, Correlation):
            raise TypeError(
                "correlation_method must be an instance of Correlation enum"
            )
        self.params.correlation_method = correlation_method
        return self

    # ####################################################################### #
    #                                                                         #
    #                            CO-OCCURRENCE                                #
    #                                                                         #
    # ####################################################################### #

    def using_minimum_pair_co_occurrence(self, minimum_pair_co_occurrence: int) -> Self:
        minimum_pair_co_occurrence = check_required_positive_int(
            value=minimum_pair_co_occurrence,
            param_name="minimum_item_co_occurrence",
        )
        self.params.minimum_pair_co_occurrence = minimum_pair_co_occurrence
        return self

    # ####################################################################### #
    #                                                                         #
    #                             TFIDF MATRIX                                #
    #                                                                         #
    # ####################################################################### #

    def using_tfidf_binary_frequencies(self, frequencies: bool) -> Self:
        frequencies = check_required_bool(
            value=frequencies,
            param_name="frequencies",
        )
        self.params.tfidf_binary_frequencies = frequencies
        return self

    def using_tfidf_norm(self, tfidf_norm: Optional[str]) -> Self:
        tfidf_norm = check_optional_str(
            value=tfidf_norm,
            param_name="tfidf_norm",
        )
        self.params.tfidf_norm = tfidf_norm
        return self

    def using_tfidf_smooth_idf(self, tfidf_smooth_idf: bool) -> Self:
        tfidf_smooth_idf = check_required_bool(
            value=tfidf_smooth_idf,
            param_name="tfidf_smooth_idf",
        )
        self.params.tfidf_smooth_idf = tfidf_smooth_idf
        return self

    def using_tfidf_sublinear_tf(self, tfidf_sublinear_tf: bool) -> Self:
        tfidf_sublinear_tf = check_required_bool(
            value=tfidf_sublinear_tf,
            param_name="tfidf_sublinear_tf",
        )
        self.params.tfidf_sublinear_tf = tfidf_sublinear_tf
        return self

    def using_tfidf_use_idf(self, tfidf_use_idf: bool) -> Self:
        tfidf_use_idf = check_required_bool(
            value=tfidf_use_idf,
            param_name="tfidf_use_idf",
        )
        self.params.tfidf_use_idf = tfidf_use_idf
        return self

    # ####################################################################### #
    #                                                                         #
    #                               EMERGENCE                                 #
    #                                                                         #
    # ####################################################################### #

    def using_emergence_baseline_periods(self, periods: int) -> Self:
        periods = check_required_positive_int(
            value=periods,
            param_name="periods",
        )
        self.params.emergence_baseline_periods = periods
        return self

    def using_emergence_min_active_periods(self, periods: int) -> Self:
        periods = check_required_positive_int(
            value=periods,
            param_name="periods",
        )
        self.params.emergence_min_active_periods = periods
        return self

    def using_emergence_min_total_records(self, total_records: int) -> Self:
        total_records = check_required_positive_int(
            value=total_records,
            param_name="total_records",
        )
        self.params.emergence_min_total_records = total_records
        return self

    def using_emergence_novelty_threshold(self, threshold: float) -> Self:
        threshold = check_required_float_0_1(
            value=threshold,
            param_name="threshold",
        )
        self.params.emergence_novelty_threshold = threshold
        return self

    def using_emergence_ratio_threshold(self, threshold: float) -> Self:
        threshold = check_required_positive_float(
            value=threshold,
            param_name="threshold",
        )
        self.params.emergence_ratio_threshold = threshold
        return self

    def using_emergence_recent_periods(self, recent_periods: int) -> Self:
        recent_periods = check_required_positive_int(
            value=recent_periods,
            param_name="recent_periods",
        )
        self.params.emergence_recent_periods = recent_periods
        return self

    # ####################################################################### #
    #                                                                         #
    #                            TOPIC DYNAMICS                               #
    #                                                                         #
    # ####################################################################### #

    def using_kleinberg_burst_rate(self, kleinberg_burst_rate: float) -> Self:
        kleinberg_burst_rate = check_required_positive_float(
            value=kleinberg_burst_rate,
            param_name="kleinberg_burst_rate",
        )
        self.params.kleinberg_burst_rate = kleinberg_burst_rate
        return self

    def using_kleinberg_burst_gamma(self, kleinberg_burst_gamma: float) -> Self:
        kleinberg_burst_gamma = check_required_positive_float(
            value=kleinberg_burst_gamma,
            param_name="kleinberg_burst_gamma",
        )
        self.params.kleinberg_burst_gamma = kleinberg_burst_gamma
        return self

    def with_time_window(self, time_window: int) -> Self:
        time_window = check_required_positive_int(
            value=time_window,
            param_name="time_window",
        )
        self.params.time_window = time_window
        return self

    def having_top_n_units_per_year(self, items_per_year: int) -> Self:
        items_per_year = check_required_positive_int(
            value=items_per_year,
            param_name="items_per_year",
        )
        self.params.top_n_units_per_year = items_per_year
        return self

    # ####################################################################### #
    #                                                                         #
    #                            TOPIC MODELING                               #
    #                                                                         #
    # ####################################################################### #

    def using_top_n_units_per_theme(self, n: int) -> Self:
        n = check_required_positive_int(
            value=n,
            param_name="n",
        )
        self.params.top_n_units_per_theme = n
        return self

    # ####################################################################### #
    #                                                                         #
    #                          NETWORK ALGORITHMS                             #
    #                                                                         #
    # ####################################################################### #

    # -------------------------------------------------------------------------
    # Normalization:
    # -------------------------------------------------------------------------
    def using_association_index(
        self,
        normalization: AssociationIndex,
    ) -> Self:
        self.params.association_index = normalization
        return self

    # -------------------------------------------------------------------------
    # Clustering:
    # -------------------------------------------------------------------------
    def using_clustering(
        self,
        clustering: Union[
            GraphClusteringAlgorithm,
            BaseEstimator,
            dict,
        ],
    ) -> Self:
        if not isinstance(clustering, (GraphClusteringAlgorithm, BaseEstimator, dict)):
            raise ValueError(
                f"Invalid clustering algorithm: expected a scikit-learn estimator or str or dict, got {type(clustering)}"
            )
        self.params.clustering = clustering
        return self

    def using_max_recursive_clustering_depth(self, depth: int) -> Self:
        depth = check_required_positive_int(
            value=depth,
            param_name="max_recursive_clustering_depth",
        )
        self.params.max_recursive_clustering_depth = depth
        return self

    def using_min_recursive_cluster_size(self, size: int) -> Self:
        size = check_required_positive_int(
            value=size,
            param_name="min_recursive_cluster_size",
        )
        self.params.min_recursive_cluster_size = size
        return self

    # -------------------------------------------------------------------------
    # Co-citation network:
    # -------------------------------------------------------------------------

    def having_top_n_cited_units(self, n: int) -> Self:
        n = check_required_positive_int(
            value=n,
            param_name="cited_top_n",
        )
        self.params.top_n_cited_units = n
        return self

    def having_minimum_cited_unit_occurrences(self, n: int) -> Self:
        n = check_required_non_negative_int(
            value=n,
            param_name="minimum_citation_count",
        )
        self.params.minimum_cited_unit_occurrences = n
        return self

    # ####################################################################### #
    #                                                                         #
    #                           REPORTING PLOTS                               #
    #                                                                         #
    # ####################################################################### #

    def using_axes_visible(self, axes_visible: bool) -> Self:
        axes_visible = check_required_bool(
            value=axes_visible,
            param_name="axes_visible",
        )
        self.params.axes_visible = axes_visible
        return self

    def using_title_text(self, title_text: Optional[str]) -> Self:
        title_text = check_optional_str(
            value=title_text,
            param_name="title_text",
        )
        self.params.title_text = title_text
        return self

    def using_xaxes_range(self, x_min: Optional[float], x_max: Optional[float]) -> Self:

        if x_min is None and x_max is None:
            self.params.xaxes_range = None
            return self
        x_min, x_max = check_required_float_range(
            min_value=cast(float, x_min),
            max_value=cast(float, x_max),
            min_param_name="x_min",
            max_param_name="x_max",
        )
        self.params.xaxes_range = (x_min, x_max)
        return self

    def using_xaxes_title_text(self, xaxes_title_text: Optional[str]) -> Self:
        xaxes_title_text = check_optional_str(
            value=xaxes_title_text,
            param_name="xaxes_title_text",
        )
        self.params.xaxes_title_text = xaxes_title_text
        return self

    def using_yaxes_range(self, y_min: Optional[float], y_max: Optional[float]) -> Self:

        if y_min is None and y_max is None:
            self.params.yaxes_range = None
            return self
        y_min, y_max = check_required_float_range(
            min_value=cast(float, y_min),
            max_value=cast(float, y_max),
            min_param_name="y_min",
            max_param_name="y_max",
        )
        self.params.yaxes_range = (y_min, y_max)
        return self

    def using_yaxes_title_text(self, yaxes_title_text: Optional[str]) -> Self:
        yaxes_title_text = check_optional_str(
            value=yaxes_title_text,
            param_name="yaxes_title_text",
        )
        self.params.yaxes_title_text = yaxes_title_text
        return self

    # -------------------------------------------------------------------------

    def using_yshift(self, yshift: float) -> Self:
        yshift = check_required_float(
            value=yshift,
            param_name="yshift",
        )
        self.params.yshift = yshift
        return self

    # -------------------------------------------------------------------------

    def using_color(self, color: str) -> Self:
        color = check_required_str(
            value=color,
            param_name="color",
        )
        self.params.color = color
        return self

    def using_colorscale(self, colorscale: List[Any]) -> Self:
        self.params.colorscale = colorscale
        return self

    def using_colormap(self, colormap: str) -> Self:
        colormap = check_required_str(
            value=colormap,
            param_name="colormap",
        )
        self.params.colormap = colormap
        return self

    def using_line_color(self, color: Union[str, float, Sequence[float]]) -> Self:
        color = check_plotly_color(
            value=color,
            param_name="color",
        )
        self.params.line_color = color
        return self

    def using_line_width(self, width) -> Self:
        width = check_required_positive_float(
            value=width,
            param_name="width",
        )
        self.params.line_width = width
        return self

    def using_marker_size(self, size: float) -> Self:
        size = check_required_positive_float(
            value=size,
            param_name="size",
        )
        self.params.marker_size = size
        return self

    # -------------------------------------------------------------------------

    def having_sankey_top_n_units(self, n: Tuple[int, ...]) -> Self:
        n = check_required_positive_int_tuple(
            tuple_values=n,
            param_name="sankey_items_in_top_n",
        )
        self.params.top_n_sankey_units = n
        return self

    # -------------------------------------------------------------------------

    def with_ranking_plotting_column(self, plotting_column: Any) -> Self:
        self.params.ranking_plotting_column = plotting_column
        return self

    # -------------------------------------------------------------------------

    def using_pie_hole(self, pie_hole: float) -> Self:
        pie_hole = check_required_float_0_1(
            value=pie_hole,
            param_name="pie_hole",
        )
        self.params.pie_hole = pie_hole
        return self

    # -------------------------------------------------------------------------
    def using_rpys_peaks(self, peaks: int) -> Self:
        peaks = check_required_positive_int(
            value=peaks,
            param_name="rpys_peaks",
        )
        self.params.rpys_peaks = peaks
        return self

    # -------------------------------------------------------------------------
    def using_top_n_sleeping_beauties(self, n: int) -> Self:
        n = check_required_positive_int(
            value=n,
            param_name="top_n_sleeping_beauties",
        )
        self.params.top_n_sleeping_beauties = n
        return self

    # ####################################################################### #
    #                                                                         #
    #                     MAP (SCATTER) -BASED PLOTS                          #
    #                                                                         #
    # ####################################################################### #

    def using_embedding_axes(self, xaxis, yaxis) -> Self:
        self.params.embedding_axes = (xaxis, yaxis)
        return self

    # ####################################################################### #
    #                                                                         #
    #                         NETWORK-BASED PLOTS                             #
    #                                                                         #
    # ####################################################################### #

    # -------------------------------------------------------------------------
    # Spring layout:
    # -------------------------------------------------------------------------

    def using_spring_layout_iterations(self, iterations: int) -> Self:
        iterations = check_required_positive_int(
            value=iterations,
            param_name="iterations",
        )
        self.params.spring_layout_iterations = iterations
        return self

    def using_spring_layout_k(self, k: Optional[float]) -> Self:
        k = check_optional_positive_float(
            value=k,
            param_name="k",
        )
        self.params.spring_layout_k = k
        return self

    def using_spring_layout_seed(self, seed: int) -> Self:
        seed = check_required_int(
            value=seed,
            param_name="seed",
        )
        self.params.spring_layout_seed = seed
        return self

    # -------------------------------------------------------------------------
    # Edges:
    # -------------------------------------------------------------------------

    def using_uniform_edge_color(self, edge_color: Any) -> Self:
        if not isinstance(edge_color, (str, int, float)):
            raise TypeError(
                f"edge color must be a string or number (valid Plotly color), got {type(edge_color).__name__}"
            )
        self.params.edge_color_uniform = edge_color
        return self

    def using_discrete_edge_colors(self, edge_colors: Tuple[Any]) -> Self:
        edge_colors = check_required_color_list(
            value=edge_colors,
            param_name="edge_colors",
        )
        self.params.edge_colors_discrete = edge_colors
        return self

    # -------------------------------------------------------------------------

    def using_edge_width_range(self, min_width: float, max_width: float) -> Self:
        min_width, max_width = check_required_positive_float_range(
            range_tuple=(min_width, max_width),
            param_name="edge_width_range",
        )
        self.params.edge_width_range = (min_width, max_width)
        return self

    def using_discrete_edge_widths(
        self,
        edge_widths: Tuple[
            Union[float, int],
            Union[float, int],
            Union[float, int],
            Union[float, int],
        ],
    ) -> Self:
        values = cast(Tuple[float, float, float, float], edge_widths)
        values = check_tuple_of_ordered_four_floats(
            value=values,
            param_name="edge_widths",
        )
        self.params.edge_widths_discrete = values
        return self

    # -------------------------------------------------------------------------

    def using_edge_opacity_range(self, min_opacity: float, max_opacity: float) -> Self:
        min_opacity, max_opacity = check_required_float_0_1_range(
            min_value=min_opacity,
            max_value=max_opacity,
            min_param_name="min_opacity",
            max_param_name="max_opacity",
        )
        self.params.edge_opacity_range = (min_opacity, max_opacity)
        return self

    def using_edge_scaling(self, edge_scaling: Scaling) -> Self:
        self.params.edge_scaling = edge_scaling
        return self

    def using_edge_similarity_threshold(self, threshold: float) -> Self:
        threshold = check_required_positive_float(
            value=threshold,
            param_name="edge_similarity_threshold",
        )
        self.params.edge_similarity_threshold = threshold
        return self

    # -------------------------------------------------------------------------

    def using_global_top_edges(self, global_top_edges: int) -> Self:
        global_top_edges = check_required_positive_int(
            value=global_top_edges,
            param_name="edge_top_n",
        )
        self.params.global_top_edges = global_top_edges
        return self

    def using_top_edges_per_node(self, top_edges_per_node: int) -> Self:
        top_edges_per_node = check_required_positive_int(
            value=top_edges_per_node,
            param_name="top_edges_per_node",
        )
        self.params.top_edges_per_node = top_edges_per_node
        return self

    # -------------------------------------------------------------------------
    # Nodes:
    # -------------------------------------------------------------------------

    def using_uniform_node_color(self, color: Any) -> Self:
        if not isinstance(color, (str, int, float)):
            raise TypeError(
                f"color must be a valid Plotly color, got {type(color).__name__}"
            )
        self.params.node_color_uniform = color
        return self

    def using_discrete_node_colors(self, colors: Tuple[Any, ...]) -> Self:
        colors = check_required_color_list(
            value=colors,
            param_name="node_colors",
        )
        self.params.node_colors_discrete = colors
        return self

    def using_node_colormap(self, colormap: str) -> Self:
        if not isinstance(colormap, str):
            raise TypeError(
                f"color must be a valid Plotly color, got {type(colormap).__name__}"
            )
        self.params.node_colormap = colormap
        return self

    # -------------------------------------------------------------------------

    def using_uniform_node_opacity(self, opacity: float) -> Self:
        opacity = check_required_float_0_1(
            value=opacity,
            param_name="opacity",
        )
        self.params.node_opacity_uniform = opacity
        return self

    def using_node_scaling(self, node_scaling: Scaling) -> Self:
        self.params.node_scaling = node_scaling
        return self

    # -------------------------------------------------------------------------

    def using_node_size_metric(self, metric: NodeSizeMetric) -> Self:
        if not isinstance(metric, NodeSizeMetric):
            raise TypeError(
                f"node_size_metric must be an instance of NodeSizeMetric enum, got {type(metric).__name__}"
            )
        self.params.node_size_metric = metric
        return self

    def using_node_size_range(self, min_size: int, max_size: int) -> Self:
        min_size, max_size = check_required_int_range(
            range_tuple=(min_size, max_size),
            param_name="node_size_range",
        )
        self.params.node_size_range = (min_size, max_size)
        return self

    def using_uniform_node_size(self, size: int) -> Self:
        size = check_required_positive_int(
            value=size,
            param_name="node_size",
        )
        self.params.node_size_uniform = size
        return self

    # -------------------------------------------------------------------------

    def using_max_node_labels(self, n: int) -> Self:
        n = check_required_positive_int(
            value=n,
            param_name="n",
        )
        self.params.max_node_labels = n
        return self

    def using_node_label_max_length(self, max_length: int) -> Self:
        max_length = check_required_positive_int(
            value=max_length,
            param_name="max_length",
        )
        self.params.node_label_max_length = max_length
        return self

    # -------------------------------------------------------------------------

    def using_min_node_degree(self, min_node_degree: int) -> Self:
        min_node_degree = check_required_positive_int(
            value=min_node_degree,
            param_name="min_node_degree",
        )
        self.params.min_node_degree = min_node_degree
        return self

    def using_top_n_nodes(self, top_n_nodes: int) -> Self:
        top_n_nodes = check_required_positive_int(
            value=top_n_nodes,
            param_name="top_n_nodes",
        )
        self.params.top_n_nodes = top_n_nodes
        return self

    # -------------------------------------------------------------------------
    # Textfont:
    # -------------------------------------------------------------------------

    def using_uniform_textfont_color(
        self, color: Union[str, float, Sequence[float]]
    ) -> Self:
        color = check_plotly_color(
            value=color,
            param_name="color",
        )
        self.params.textfont_color_uniform = color
        return self

    def using_textfont_opacity_range(
        self, min_opacity: float, max_opacity: float
    ) -> Self:
        min_opacity, max_opacity = check_required_float_0_1_range(
            min_value=min_opacity,
            max_value=max_opacity,
            min_param_name="min_opacity",
            max_param_name="max_opacity",
        )
        self.params.textfont_opacity_range = (min_opacity, max_opacity)
        return self

    def using_uniform_textfont_opacity(self, textfont_opacity: float) -> Self:
        textfont_opacity = check_required_float_0_1(
            value=textfont_opacity,
            param_name="textfont_opacity",
        )
        self.params.textfont_opacity_uniform = textfont_opacity
        return self

    def using_textfont_size_range(
        self, min_size: Union[float, int], max_size: Union[float, int]
    ) -> Self:
        min_size, max_size = check_required_positive_number_range(
            range_tuple=(min_size, max_size),
            param_name="textfont_size_range",
        )
        self.params.textfont_size_range = (min_size, max_size)
        return self

    def using_uniform_textfont_size(self, textfont_size: float) -> Self:
        textfont_size = check_required_positive_float(
            value=textfont_size,
            param_name="textfont_size",
        )
        self.params.textfont_size_uniform = textfont_size
        return self

    # -------------------------------------------------------------------------
    # Kernel density plot:
    # -------------------------------------------------------------------------

    def using_contour_opacity(self, opacity: float) -> Self:
        opacity = check_required_float_0_1(
            value=opacity,
            param_name="contour_opacity",
        )
        self.params.contour_opacity = opacity
        return self

    def using_kernel_bandwidth(self, kernel_bandwidth: float) -> Self:
        kernel_bandwidth = check_required_positive_float(
            value=kernel_bandwidth,
            param_name="kernel_bandwidth",
        )
        self.params.kernel_bandwidth = kernel_bandwidth
        return self

    # ####################################################################### #
    #                                                                         #
    #                              THESAURUS                                  #
    #                                                                         #
    # ####################################################################### #

    def having_case_sensitive(self, case_sensitive: bool) -> Self:
        case_sensitive = check_required_bool(
            value=case_sensitive,
            param_name="case_sensitive",
        )
        self.params.case_sensitive = case_sensitive
        return self

    # def having_maximum_occurrence(self, maximum_occurrence: int) -> Self:
    #     maximum_occurrence = check_required_positive_int(
    #         value=maximum_occurrence,
    #         param_name="maximum_occurrence",
    #     )
    #     self.params.maximum_occurrence = maximum_occurrence
    #     return self

    def having_n_chars(self, n_chars: int) -> Self:
        n_chars = check_required_positive_int(
            value=n_chars,
            param_name="n_chars",
        )
        self.params.n_chars = n_chars
        return self

    def having_n_contexts(self, n_contexts: int) -> Self:
        n_contexts = check_required_positive_int(
            value=n_contexts,
            param_name="n_contexts",
        )
        self.params.n_contexts = n_contexts
        return self

    def having_preferred_key(self, preferred_key: str) -> Self:
        preferred_key = check_required_str(
            value=preferred_key,
            param_name="preferred_key",
        )
        self.params.preferred_key = preferred_key
        return self

    def having_regex_flags(self, regex_flags: int) -> Self:
        regex_flags = check_required_non_negative_int(
            value=regex_flags,
            param_name="regex_flags",
        )
        self.params.regex_flags = regex_flags
        return self

    def having_regex_search(self, regex_search: bool) -> Self:
        regex_search = check_required_bool(
            value=regex_search,
            param_name="regex_search",
        )
        self.params.regex_search = regex_search
        return self

    def having_replacement(self, replacement: str) -> Self:
        replacement = check_required_str(
            value=replacement,
            param_name="replacement",
        )
        self.params.replacement = replacement
        return self

    def having_text_matching(self, pattern: Union[str, tuple[str, ...]]) -> Self:
        pattern = check_required_str_or_str_tuple(
            value=pattern,
            param_name="pattern",
        )
        self.params.pattern = pattern
        return self

    def having_variant_keys(self, variant_keys: tuple[str, ...]) -> Self:
        variant_keys = check_required_str_tuple(
            value=variant_keys,
            param_name="variant_keys",
        )
        self.params.variant_keys = variant_keys
        return self

    def having_word(self, word: str) -> Self:
        word = check_required_str(
            value=word,
            param_name="word",
        )
        self.params.word = word
        return self

    #
    # S
    #
    ## def showing_progress(self, progress):
    ##     self.params.show_progress = progress
    ##     return self

    # ==========================================================================
    # USING_* → Parameters (HOW to analyze/display?)
    # ==========================================================================

    def using_colored_output(self, colored_output: bool) -> Self:
        colored_output = check_required_bool(
            value=colored_output,
            param_name="colored_output",
        )
        self.params.colored_output = colored_output
        return self

    def using_colored_stderr(self, colored_stderr: bool) -> Self:
        colored_stderr = check_required_bool(
            value=colored_stderr,
            param_name="colored_stderr",
        )
        self.params.colored_stderr = colored_stderr
        return self

    def using_similarity_cutoff(self, similarity_cutoff: float) -> Self:
        similarity_cutoff = check_required_positive_float(
            value=similarity_cutoff,
            param_name="similarity_cutoff",
        )
        self.params.similarity_cutoff = similarity_cutoff
        return self

    def having_occurrence_threshold(self, occurrence_threshold: int) -> Self:
        occurrence_threshold = check_required_positive_int(
            value=occurrence_threshold,
            param_name="occurrence_threshold",
        )
        self.params.occurrence_threshold = occurrence_threshold
        return self

    # def using_decomposition_algorithm(self, algorithm: BaseEstimator) -> Self:
    #     algorithm = check_required_base_estimator(
    #         value=algorithm,
    #         param_name="decomposition_algorithm",
    #     )
    #     self.params.decomposition_algorithm = algorithm
    #     return self

    def using_cluster_coverages(self, cluster_coverages: Optional[list[str]]) -> Self:
        cluster_coverages = check_optional_str_list(
            value=cluster_coverages,
            param_name="cluster_coverages",
        )
        self.params.cluster_coverages = cluster_coverages
        return self

    def using_cluster_names(self, cluster_names: Optional[list[str]]) -> Self:
        cluster_names = check_optional_str_list(
            value=cluster_names,
            param_name="cluster_names",
        )
        self.params.cluster_names = cluster_names
        return self

    def using_cumulative_sum(self, cumulative_sum: bool) -> Self:
        cumulative_sum = check_required_bool(
            value=cumulative_sum,
            param_name="cumulative_sum",
        )
        self.params.cumulative_sum = cumulative_sum
        return self

    # def using_initial_newline(self, initial_newline) -> Self:
    #     initial_newline = check_required_bool(
    #         value=initial_newline,
    #         param_name="initial_newline",
    #     )
    #     self.params.initial_newline = initial_newline
    #     return self

    # def using_manifold_algorithm(
    #     self, manifold_algorithm: Optional[BaseEstimator]
    # ) -> Self:
    #     manifold_algorithm = check_optional_base_estimator(
    #         value=manifold_algorithm,
    #         param_name="manifold_algorithm",
    #     )
    #     self.params.manifold_algorithm = manifold_algorithm
    #     return self

    def using_fuzzy_threshold(self, fuzzy_threshold: float) -> Self:
        fuzzy_threshold = check_required_non_negative_float(
            value=fuzzy_threshold,
            param_name="fuzzy_threshold",
        )
        self.params.fuzzy_threshold = fuzzy_threshold
        return self

    # def using_minimum_number_of_clusters(self, minimum_number_of_clusters: int) -> Self:
    #     minimum_number_of_clusters = check_required_positive_int(
    #         value=minimum_number_of_clusters,
    #         param_name="minimum_number_of_clusters",
    #     )
    #     self.params.minimum_number_of_clusters = minimum_number_of_clusters
    #     return self

    # def using_minimum_items_in_cluster(self, minimum_items_in_cluster: int) -> Self:
    #     minimum_items_in_cluster = check_required_positive_int(
    #         value=minimum_items_in_cluster,
    #         param_name="minimum_items_in_cluster",
    #     )
    #     self.params.minimum_items_in_cluster = minimum_items_in_cluster
    #     return self

    def using_plot_height(self, height) -> Self:
        self.params.wordcloud_plot_height = height
        return self

    def using_plot_width(self, width) -> Self:
        self.params.wordcloud_plot_width = width
        return self

    def using_word_length(self, word_length: int) -> Self:
        word_length = check_required_positive_int(
            value=word_length,
            param_name="word_length",
        )
        self.params.word_length = word_length
        return self

    # ==========================================================================
    # WITH_* → Configuration (WHAT to analyze?)
    # ==========================================================================

    # def with_column(self, column: str) -> Self:
    #     column = check_required_str(
    #         value=column,
    #         param_name="column",
    #     )
    #     self.params.column = column
    #     return self

    # def with_index_and_column_field(self, index_and_column_field: Field) -> Self:
    #     index_and_column_field = check_required_corpus_field_enum(
    #         value=index_and_column_field,
    #         param_name="index_and_column_field",
    #     )
    #     self.params.index_and_column_field = index_and_column_field
    #     return self

    def with_params(self, params) -> Self:
        self.update(**params.__dict__)
        return self

    def with_thesaurus_file(self, thesaurus_file: ThFile) -> Self:
        if not isinstance(thesaurus_file, ThFile):
            raise TypeError("thesaurus_file must be an instance of ThFile enum")

        self.params.thesaurus_file = thesaurus_file
        return self

    def with_transformation_function(
        self, transformation_function: Optional[Callable[[Any], Any]]
    ) -> Self:
        self.params.transformation_function = transformation_function
        return self

    # ==========================================================================
    # WHERE_* → Data filtering (WHICH records?)
    # ==========================================================================

    # def where_database(self, database: str) -> Self:
    #     database = internal__check_required_str(
    #         value=database,
    #         param_name="database",
    #     )
    #     self.params.database = database
    #     return self

    # ####################################################################### #
    #                                                                         #
    #                               ZOTERO                                    #
    #                                                                         #
    # ####################################################################### #

    def using_zotero_api_key(self, zotero_api_key: str) -> Self:
        zotero_api_key = check_required_str(
            value=zotero_api_key,
            param_name="api_key",
        )
        self.params.zotero_api_key = zotero_api_key
        return self

    def using_zotero_library_id(self, zotero_library_id: str) -> Self:
        zotero_library_id = check_required_str(
            value=zotero_library_id,
            param_name="library_id",
        )
        self.params.zotero_library_id = zotero_library_id
        return self

    def using_zotero_library_type(self, zotero_library_type: str) -> Self:
        zotero_library_type = check_required_str(
            value=zotero_library_type,
            param_name="library_type",
        )
        self.params.zotero_library_type = zotero_library_type
        return self
