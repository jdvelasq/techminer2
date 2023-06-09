"""
This module contains functions to compute indicators calculated over
the entire dataset.


"""
from .co_occ_matrix_list import co_occ_matrix_list
from .collaboration_indicators_by_field import (
    collaboration_indicators_by_field,
)
from .column_indicators_by_metric import column_indicators_by_metric
from .growth_indicators_by_field import growth_indicators_by_field
from .impact_indicators_by_field import impact_indicators_by_field
from .indicators_by_document import indicators_by_document
from .indicators_by_field import indicators_by_field
from .indicators_by_field_per_year import indicators_by_field_per_year
from .indicators_by_year import indicators_by_year
from .indicators_by_year_plot import indicators_by_year_plot
from .items_occ_by_year import items_occ_by_year

__all__ = [
    "co_occ_matrix_list",
    "collaboration_indicators_by_field",
    "column_indicators_by_metric",
    "growth_indicators_by_field",
    "impact_indicators_by_field",
    "indicators_by_document",
    "indicators_by_field",
    "indicators_by_field_per_year",
    "indicators_by_year",
    "indicators_by_year_plot",
    "items_occ_by_year",
]
