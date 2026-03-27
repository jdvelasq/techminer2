"""
ReplaceLastWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.replace import ReplaceLastWord
    >>> (
    ...     ReplaceLastWord()
    ...     .having_word("UNIV")
    ...     .having_replacement("univ")
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
from tm2p.refine._intern.replace import BaseLastWord


class ReplaceLastWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseLastWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )
