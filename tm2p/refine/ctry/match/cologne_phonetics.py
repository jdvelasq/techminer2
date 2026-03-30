"""
ColognePhoneticsMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.match import ColognePhoneticsMatch
    >>> (
    ...     ColognePhoneticsMatch()
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseColognePhoneticsMatch


class ColognePhoneticsMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseColognePhoneticsMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .with_source_field(Field.CTRY)
            .run()
        )
