"""
This module contains functions to compute indicators calculated over
the entire dataset.


"""


from .co_occ_matrix_list import co_occ_matrix_list
from .collaboration_indicators_by_topic import (
    collaboration_indicators_by_topic,
)
from .column_indicators_by_metric import column_indicators_by_metric
from .growth_indicators_by_topic import growth_indicators_by_topic
from .impact_indicators_by_item import impact_indicators_by_item
from .indicators_by_document import indicators_by_document
from .indicators_by_item import indicators_by_item
from .indicators_by_item_per_year import indicators_by_item_per_year
from .indicators_by_year import indicators_by_year
from .indicators_by_year_plot import indicators_by_year_plot
from .items_occ_by_year import items_occ_by_year

__all__ = [
    "co_occ_matrix_list",
    "collaboration_indicators_by_topic",
    "column_indicators_by_metric",
    "growth_indicators_by_topic",
    "impact_indicators_by_item",
    "indicators_by_document",
    "indicators_by_item",
    "indicators_by_item_per_year",
    "indicators_by_year",
    "indicators_by_year_plot",
    "items_occ_by_year",
]
