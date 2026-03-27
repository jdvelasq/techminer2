"""
BeiderMorseMatch
===============================================================================

Smoke tests:
    >>> from tm2p.enum import ThFile, Field
    >>> from tm2p.refine.concept.match import BeiderMorseMatch
    >>> (
    ...     BeiderMorseMatch()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    '892 synonym groups found'

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseBeiderMorseMatch


class BeiderMorseMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseBeiderMorseMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.DESCRIPTOR_RAW)
            .run()
        )
