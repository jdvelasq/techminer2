# CODE_REVIEW: 2026-01-26
"""
WoS
===============================================================================

Smoke test - fintech - successful import:
    >>> from tm2p.ingest.datasrc import WoS
    >>> (
    ...     WoS()
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS


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


if __name__ == "__main__":

    WoS().where_root_directory("./").run()
