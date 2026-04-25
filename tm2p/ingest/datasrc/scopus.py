# CODE_REVIEW: 2026-01-26
"""
Scopus
===============================================================================


Smoke tests:
    >>> from tm2p.ingest.datasrc import Scopus
    >>> (
    ...     Scopus()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS +SKIP


    >>> from tm2p.ingest.datasrc import Scopus
    >>> (
    ...     Scopus()
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS +SKIP


    >>> from tm2p.ingest.datasrc import Scopus
    >>> (
    ...     Scopus()
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )  # doctest: +ELLIPSIS +SKIP


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


if __name__ == "__main__":

    Scopus().where_root_directory("./").run()
