# CODE_REVIEW: 2026-01-26
"""
PubMed
===============================================================================

Smoke test - fintech - successful import:
    >>> from tm2p.ingest.datasrc import PubMed
    >>> (
    ...     PubMed()
    ...     .where_root_directory("tests/health-analytics-pubmed/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS



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


if __name__ == "__main__":

    PubMed().where_root_directory("./").run()
