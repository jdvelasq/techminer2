"""
SortByCharacterLength
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.sort import SortByCharacterLength
    >>> (
    ...     SortByCharacterLength()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    317


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.sort import BaseSortByCharacterLength


class SortByCharacterLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseSortByCharacterLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )
