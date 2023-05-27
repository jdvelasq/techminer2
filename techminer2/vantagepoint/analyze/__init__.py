"""
This package provides the functions available in the Analyze menu.

The following functions are available:

- auto_corr_matrix: Computes the autocorrelation matrix of a network.
- co_occ_matrix: Computes the co-occurrence matrix of a set of terms.
- column_viewer: Generates a radial diagram of term associations from a \
    (co) occurrence matrix.
- corr_map: Generates a correlation map of a network.
- create_concept_grid: Creates a grid of concepts based on their co-occurrence.
- cross_corr_matrix: Computes the cross-correlation matrix of a set of \
    networks.
- extract_topics: Extracts topics from a set of documents.
- factor_matrix: Computes the factor matrix of a network.
- list_cells_in_matrix: Lists the cells in a matrix that meet a certain \
    criterion.
- network_degree_plot: Generates a degree plot of a network.
- network_metrics: Computes the metrics of a network.
- occ_matrix: Computes the occurrence matrix of a set of terms.
- terms_by_year: Computes the frequency of terms over time.
- tf_idf_matrix: Computes the TF-IDF matrix of a set of documents.
- tf_matrix: Computes the term frequency matrix of a set of documents.

"""

from .auto_corr_matrix import auto_corr_matrix
from .co_occ_matrix import co_occ_matrix
from .column_viewer import column_viewer
from .corr_map import corr_map
from .create_concept_grid import create_concept_grid
from .cross_corr_matrix import cross_corr_matrix
from .factor_matrix import factor_matrix
from .list_cells_in_matrix import list_cells_in_matrix
from .list_view import list_view
from .matrix_viewer import matrix_viewer
from .network_degree_plot import network_degree_plot
from .network_metrics import network_metrics
from .statistics import statistics
from .terms_by_year import terms_by_year
from .tf_idf_matrix import tf_idf_matrix
from .tf_matrix import tf_matrix

__all__ = [
    "auto_corr_matrix",
    "co_occ_matrix",
    "column_viewer",
    "corr_map",
    "create_concept_grid",
    "cross_corr_matrix",
    "factor_matrix",
    "list_cells_in_matrix",
    "list_view",
    "matrix_viewer",
    "network_degree_plot",
    "network_metrics",
    "statistics",
    "terms_by_year",
    "tf_idf_matrix",
    "tf_matrix",
]
