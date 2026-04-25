"""
Manual
===============================================================================

Smoke tests:
    >>> from tm2p.refine.organization.group import Manual
    >>> (
    ...     Manual()
    ...     .having_text_matching(
    ...         (
    ...             "fintech innovation",
    ...             "fin-tech innovation",
    ...         )
    ...     )
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.merge import BaseManual


class Manual(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        from ..apply import Apply

        (
            BaseManual()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )

        return Apply().where_root_directory(self.params.root_directory).run()
