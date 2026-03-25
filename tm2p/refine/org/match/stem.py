"""
StemMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.match import StemMatch
    >>> (
    ...     StemMatch()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseStemMatch


class StemMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseStemMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .with_source_field(Field.ORG)  # type: ignore
            .run()
        )
