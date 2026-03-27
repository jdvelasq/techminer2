"""
RemoveLastWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.replace import RemoveLastWord
    >>> (
    ...     RemoveLastWord()
    ...     .having_word("States")
    ...     .having_replacement("STATES")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

    >>> from tm2p.refine.ctry.reset import Reset
    >>> (
    ...     ReplaceInitialWord()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.remove import BaseLastWord


class RemoveLastWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseLastWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .run()
        )
