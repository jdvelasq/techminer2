"""
BiGramMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.organization.match import BigramMatch
    >>> (
    ...     BigramMatch()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.enum import Field, ThFile
from tm2p.refine._intern.match import BaseBigramMatch


class BigramMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseBigramMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .with_source_field(Field.ORG)
            .run()
        )
