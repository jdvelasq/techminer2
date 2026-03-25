"""
ReplaceLastWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.replace import ReplaceLastWord
    >>> (
    ...     ReplaceLastWord()
    ...     .having_word("business")
    ...     .having_replacement("BUSINESS")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     ReplaceInitialWord()
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
            .with_thesaurus_file(ThFile.CONCEPT)
            .run()
        )
