# CODE_REVIEW: 2026-01-26
"""
OpenAlex
===============================================================================

Smoke test - fintech - successful import:
    >>> from tm2p.ingest.datasrc import OpenAlex
    >>> (
    ...     OpenAlex()
    ...     .where_root_directory("tests/openalex/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS
    Note...


"""


from ._intern.base_ingest import BaseIngest

__reviewed__ = "2026-03-31"


class OpenAlex(BaseIngest):
    """:meta private:"""

    # ------------------------------------------------------------------------
    # Marker
    # ------------------------------------------------------------------------

    def get_marker(self) -> str:
        return "OpenAlex"


if __name__ == "__main__":

    OpenAlex().where_root_directory("./").run()
