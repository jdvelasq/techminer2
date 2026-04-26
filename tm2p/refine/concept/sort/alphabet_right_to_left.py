"""
SortByAlphabetRightToLeft
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.sort import SortByAlphabetRightToLeft
    >>> (
    ...     SortByAlphabetRightToLeft()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.sort import BaseSortByAlphabetRightToLeft


class SortByAlphabetRightToLeft(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseSortByAlphabetRightToLeft()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .run()
        )
