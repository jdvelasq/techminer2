# CODE_REVIEW: 2026-01-26
"""
OpenAlex
===============================================================================

Smoke test - fintech - successful import:
    >>> from tm2p.ingest.datab import OpenAlex
    >>> result = (
    ...     OpenAlex()
    ...     .where_root_directory("examples/openalex/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS
    Note...
    >>> result.success
    True

"""


from ._intern.base_ingest import BaseIngest

__reviewed__ = "2026-01-28"


class OpenAlex(BaseIngest):
    """:meta private:"""

    # ------------------------------------------------------------------------
    # Marker
    # ------------------------------------------------------------------------

    def get_marker(self) -> str:
        return "OpenAlex"
