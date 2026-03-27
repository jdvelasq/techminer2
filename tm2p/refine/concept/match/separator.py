"""
SeparatorMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.match import SeparatorMatch
    >>> (
    ...     SeparatorMatch()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseSeparatorMatch


class SeparatorMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseSeparatorMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.DESCRIPTOR_NORM)
            .run()
        )
