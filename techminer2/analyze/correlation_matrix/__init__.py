"""
This module provides various functions for correlation matrix analysis, including
auto-correlation and cross-correlation maps and matrices.
"""

from .auto_correlation_map import auto_correlation_map
from .auto_correlation_matrix import auto_correlation_matrix
from .cross_correlation_map import cross_correlation_map
from .cross_correlation_matrix import cross_correlation_matrix

__all__ = [
    "auto_correlation_map",
    "auto_correlation_matrix",
    "cross_correlation_map",
    "cross_correlation_matrix",
]
