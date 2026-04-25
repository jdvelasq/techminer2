"""
CombineMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.match import CombineMatch
    >>> (
    ...     CombineMatch()
    ...     #
    ...     # FIELD:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseCombineMatch


class CombineMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseCombineMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.DESCRIPTOR_NORM)
            .run()
        )
