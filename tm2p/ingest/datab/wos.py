# CODE_REVIEW: 2026-01-26
"""
WoS
===============================================================================

Smoke test - fintech - successful import:
    >>> from tm2p.ingest.datab.wos import WoS
    >>> result = (
    ...     WoS()
    ...     .where_root_directory("tests/wos/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS
    Note...
    >>> result.success
    True

"""


from ._intern.base_ingest import BaseIngest

__reviewed__ = "2026-01-28"


class WoS(BaseIngest):
    """:meta private:"""

    # ------------------------------------------------------------------------
    # Marker
    # ------------------------------------------------------------------------

    def get_marker(self) -> str:
        return "WoS"
