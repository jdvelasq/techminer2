"""
Auto
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.merge import Auto
    >>> (
    ...     Auto()
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.merge import BaseAuto


class Auto(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        from ..apply import Apply

        (
            BaseAuto()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.DESCRIPTOR_NORM)
            .run()
        )

        return Apply().where_root_directory(self.params.root_directory).run()
