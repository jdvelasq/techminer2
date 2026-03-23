"""
SortByKeyLength
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.sort import SortByKeyLength
    >>> (
    ...     SortByKeyLength()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    53


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.sort import BaseSortByCharacterLength


class SortByKeyLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseSortByCharacterLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .run()
        )
