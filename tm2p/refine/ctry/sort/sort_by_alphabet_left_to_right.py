"""
SortByLeftToRight
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.sort import SortByLeftToRight
    >>> (
    ...     SortByLeftToRight()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    53

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.sort import BaseSortByAlphabetLeftToRight


class SortByLeftToRight(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseSortByAlphabetLeftToRight()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .run()
        )
