"""
RemoveInitialWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.replace import RemoveInitialWord
    >>> (
    ...     RemoveInitialWord()
    ...     .having_word("ABFI")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

    >>> from tm2p.refine.org.reset import Reset
    >>> (
    ...     ReplaceInitialWord()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.remove import BaseRemoveInitialWord


class RemoveInitialWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseRemoveInitialWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )
