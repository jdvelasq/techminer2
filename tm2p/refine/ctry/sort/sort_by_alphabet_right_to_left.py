"""
SortByRightToLeft
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.sort import SortByRightToLeft
    >>> (
    ...     SortByRightToLeft()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    53


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.sort import BaseSortByAlphabetRightToLeft


class SortByRightToLeft(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseSortByAlphabetRightToLeft()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .run()
        )
