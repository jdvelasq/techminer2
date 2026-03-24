"""
ReplaceLastWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.replace import ReplaceLastWord
    >>> (
    ...     ReplaceLastWord()
    ...     .having_word("States")
    ...     .having_replacement("STATES")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

    >>> (
    ...     ReplaceLastWord()
    ...     .having_word("STATES")
    ...     .having_replacement("States")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.replace import BaseReplaceLastWord


class ReplaceLastWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseReplaceLastWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .run()
        )
