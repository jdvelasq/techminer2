# CODE_REVIEW: 2026-01-26
"""
PubMed
===============================================================================

Smoke test - fintech - successful import:
    >>> from tm2p.ingest.datab.pubmed import PubMed
    >>> result = (
    ...     PubMed()
    ...     .where_root_directory("tests/pubmed/")
    ...     .run()
    ... )
    >>> result.success
    True


"""


from ._intern.base_ingest import BaseIngest

__reviewed__ = "2026-01-28"


class PubMed(BaseIngest):
    """:meta private:"""

    # ------------------------------------------------------------------------
    # Marker
    # ------------------------------------------------------------------------

    def get_marker(self) -> str:
        return "PubMed"
