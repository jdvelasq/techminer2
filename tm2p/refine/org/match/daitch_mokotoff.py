"""
DaitchMokotoffMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.match import DaitchMokotoffMatch
    >>> (
    ...     DaitchMokotoffMatch()
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseDaitchMokotoffMatch


class DaitchMokotoffMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseDaitchMokotoffMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .with_source_field(Field.ORG)
            .run()
        )
