"""
Group
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.group import Group
    >>> (
    ...     Group()
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.group import BaseGroup


class Group(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        from ..apply import Apply

        (
            BaseGroup()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )

        return Apply().where_root_directory(self.params.root_directory).run()
