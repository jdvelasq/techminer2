"""
DoubleMetaphoneMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.country.match import DoubleMetaphoneMatch
    >>> (
    ...     DoubleMetaphoneMatch()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseDoubleMetaphoneMatch


class DoubleMetaphoneMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseDoubleMetaphoneMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .with_source_field(Field.CTRY)
            .run()
        )
