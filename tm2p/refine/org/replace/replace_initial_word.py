"""
ReplaceInitialWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.replace import ReplaceInitialWord
    >>> (
    ...     ReplaceInitialWord()
    ...     .having_word("ABFI")
    ...     .having_replacement("abfi")
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
from tm2p.refine._intern.replace import BaseInitialWord


class ReplaceInitialWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseInitialWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )
