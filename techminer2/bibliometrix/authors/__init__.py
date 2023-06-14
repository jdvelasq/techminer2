"""
This module contains functions for computing author-level bibliometric indicators.

"""

from .author_g_index import author_g_index
from .author_h_index import author_h_index
from .author_m_index import author_m_index
from .authors_production_over_time import authors_production_over_time
from .lotka_law import lotka_law
from .most_frequent_authors import most_frequent_authors
from .most_global_cited_authors import most_global_cited_authors
from .most_local_cited_authors import most_local_cited_authors

__all__ = [
    "author_g_index",
    "author_h_index",
    "author_m_index",
    "authors_production_over_time",
    "lotka_law",
    "most_frequent_authors",
    "most_global_cited_authors",
    "most_local_cited_authors",
]
