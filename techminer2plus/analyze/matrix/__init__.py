"""Matrix module"""

# Main functions:
from .auto_correlation_matrix import auto_correlation_matrix
from .co_occurrence_matrix import co_occurrence_matrix
from .cross_correlation_matrix import cross_correlation_matrix
from .factor_matrix import factor_matrix

# Auxiliar functions:
from .list_cells_in_matrix import list_cells_in_matrix

__all__ = [
    #
    # Main functions:
    #
    auto_correlation_matrix,
    co_occurrence_matrix,
    cross_correlation_matrix,
    factor_matrix,
    #
    # Auxiliar functions:
    #
    list_cells_in_matrix,
]
