"""
SortByMaxTokenLength
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.sort import SortByMaxTokenLength
    >>> (
    ...     SortByMaxTokenLength()
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )
    7722


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.sort import BaseSortByMaxTokenLength


class SortByMaxTokenLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseSortByMaxTokenLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )
