# CODE_REVIEW: 2026-01-26
"""
Scopus
===============================================================================

Smoke test - fintech - successful import:
    >>> from tm2p.ingest.datab.scopus import Scopus
    >>> result = (
    ...     Scopus()
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS
    Note...
    >>> result.success
    True

"""


from ._intern.base_ingest import BaseIngest

__reviewed__ = "2026-01-28"


class Scopus(BaseIngest):
    """:meta private:"""

    # ------------------------------------------------------------------------
    # Marker
    # ------------------------------------------------------------------------

    def get_marker(self) -> str:
        return "Scopus"
