"""
TriGramMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.match import TrigramMatch
    >>> (
    ...     TrigramMatch()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... ) # doctest: +SKIP

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
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
            .with_thesaurus_file(ThFile.ORG)
            .with_source_field(Field.ORG)
            .run()
        )
