"""
TriGramMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.country.match import TrigramMatch
    >>> (
    ...     TrigramMatch()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.enum import Field, ThFile
from tm2p.refine._intern.match import BaseTrigramMatch


class TrigramMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseTrigramMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .with_source_field(Field.CTRY)
            .run()
        )
