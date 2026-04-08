"""
WordOrderMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.country.match import WordOrderMatch
    >>> (
    ...     WordOrderMatch()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseWordOrderMatch


class WordOrderMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseWordOrderMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .with_source_field(Field.CTRY)
            .run()
        )
