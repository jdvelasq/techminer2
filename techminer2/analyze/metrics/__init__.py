"""Metrics menu options"""

from ...database.metrics.general_metrics.data_frame import general_metrics_frame
from ...database.metrics.growth_metrics.growth_metrics_dataframe import (
    growth_metrics_frame,
)
from ...database.metrics.performance_metrics.data_frame import performance_metrics_frame
from ...database.metrics.terms_by_year.data_frame import terms_by_year_frame
from ...database.metrics.terms_by_year.ranking_plot import terms_by_year_plot
from ...database.metrics.tfidf.data_frame import tfidf_frame
from ..collaboration.collaboration_metrics_dataframe import collaboration_metrics_frame
from ..collaboration.collaboration_metrics_plot import collaboration_metrics_plot
from .trend_metrics.trend_metrics_dataframe import trend_metrics_frame
from .trend_metrics.trend_metrics_plot import trend_metrics_plot

__all__ = [
    "collaboration_metrics_dataframe",
    "collaboration_metrics_plot",
    "general_metrics_dataframe",
    "growth_metrics_dataframe",
    "performance_metrics_dataframe",
    "terms_by_year_dataframe",
    "terms_by_year_plot",
    "tfidf_dataframe",
    "trend_metrics_dataframe",
    "trend_metrics_plot",
]
