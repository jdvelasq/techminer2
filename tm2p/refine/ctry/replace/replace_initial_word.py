"""
ReplaceInitialWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.replace import ReplaceInitialWord
    >>> (
    ...     ReplaceInitialWord()
    ...     .having_word("United")
    ...     .having_replacement("UNITED")
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
            .with_thesaurus_file(ThFile.CTRY)
            .run()
        )
